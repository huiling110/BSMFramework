#!/usr/bin/python
# coding=utf-8


import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import copy
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
options = VarParsing.VarParsing('analysis')
# ===== Register new variables =====
options.register('optionlepfilt',#231
0,
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.int,
"Minimum number of leptons")

options.register('ofName',
'sentinel_output_name',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for output file."
)
# ===== Get & parse any command line arguments =====
options.parseArguments()

#####
##   Initial standard configs
#####
#process = cms.Process("Demo")
process = cms.Process("BSM")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.load("Geometry.CaloEventSetup.CaloTowerConstituents_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag.globaltag = '102X_mcRun2_asymptotic_v6'
process.GlobalTag.globaltag = '102X_mcRun2_asymptotic_v8'#102X_mcRun2_asymptotic_v8 (2016), 102X_mc2017_realistic_v8 (2017), 102X_upgrade2018_realistic_v21 (2018)

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')

#####
##   Input files
#####
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    #'/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/F61E4EE9-127E-E911-8FF5-549F3525CD78.root',
  #  don't know why the above 2 files can not be open.
   #  '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M1_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/20000/CACFB972-44F1-E811-98CF-001E67A3E8CC.root',
   '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/100000/0411821D-BBC3-E811-98BA-0CC47A57CBBC.root',
  ),
  skipEvents = cms.untracked.uint32(0)
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )

##### JEC
#update the JEC in the MiniAOD
#reverts these corrections and applies the new ones, producing as output an new collection of pat::Jets which have the same content as the input jet, but new jet energy corrections applied. 
#https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections?redirectedfrom=CMS.WorkBookJetEnergyCorrections  maybe outdated
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
updateJetCollection(
  process,
  jetSource = cms.InputTag('slimmedJets'),
  pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
  svSource = cms.InputTag('slimmedSecondaryVertices'),
  #labelName = 'UpdatedJEC',
  jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet','L2Relative','L3Absolute']), 'None'),
  btagDiscriminators = [#for The DeepFlavour discriminator, https://twiki.cern.ch/twiki/bin/view/CMS/DeepJet
     'pfDeepFlavourJetTags:probb',
     'pfDeepFlavourJetTags:probbb',
     'pfDeepFlavourJetTags:problepb',
     'pfDeepFlavourJetTags:probc',
     'pfDeepFlavourJetTags:probuds',
     'pfDeepFlavourJetTags:probg'
  ],
  postfix='NewDFTraining'# the final updated jet collection will be called updatedPatJets+labelName+postfix, with labelName and postfix 
)
jetsNameAK4="selectedUpdatedPatJetsNewDFTraining" #the name of the updated jets


##### L1 Prefire
#instruction for this?https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1ECALPrefiringWeightRecipe
#EDProducer 
from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
    DataEra = cms.string("2016BtoH"), # 2017BtoF
    UseJetEMPt = cms.bool(False),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings = False)
 

#####
##   ELECTRON ID and sclale smear SECTION
#####https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#2018_Preliminary_Energy_Correcti
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process, 
#        applyEnergyCorrections=False,
#        applyVIDOnCorrectedEgamma=False,
        runEnergyCorrections=False, # False for 2016/2018, as energy corrections are not yet availible for 2018; corrections by default are fine for 2016 so no need to re-run
        runVID=True, # if you are running on miniAOD v1 or Fall17V2 please enable it 
        # for 2017v2saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
        era='2016-Legacy') # '2018-Prompt', '2016-Legacy'


#####
##   For tt+X
#####
# Setting input particle collections to be used by the tools
#?what is this part doing?
genParticleCollection = "prunedGenParticles"
genJetCollection      = "slimmedGenJets"
jetFlavourInfos       = "genJetFlavourInfos"
jetAlgo               = "AntiKt"
rParam                = 0.4
genJetPtMin           = 20.
genJetAbsEtaMax       = 2.4
from PhysicsTools.JetMCAlgos.HadronAndPartonSelector_cfi import selectedHadronsAndPartons
from PhysicsTools.JetMCAlgos.AK4PFJetsMCFlavourInfos_cfi import ak4JetFlavourInfos
from PhysicsTools.JetMCAlgos.GenHFHadronMatcher_cff import matchGenBHadron
from PhysicsTools.JetMCAlgos.GenHFHadronMatcher_cff import matchGenCHadron
process.selectedHadronsAndPartons = selectedHadronsAndPartons.clone(particles = genParticleCollection)
process.genJetFlavourInfos = ak4JetFlavourInfos.clone(jets=genJetCollection,rParam=cms.double(rParam),jetAlgorithm = cms.string(jetAlgo))
process.matchGenBHadron = matchGenBHadron.clone(genParticles = genParticleCollection,jetFlavourInfos = jetFlavourInfos)
process.matchGenCHadron = matchGenCHadron.clone(genParticles = genParticleCollection,jetFlavourInfos = jetFlavourInfos)

#####Tau#####

#  '''
#  from BSMFramework.BSM3G_TNT_Maker.runTauIdMVA import *
#  na = TauIDEmbedder(process, cms,
        #  debug=True,
        #  toKeep = ["dR0p32017v2","deepTau2017v2"] # pick the one you need: ["2017v1", "2017v2", "newDM2017v2", "dR0p32017v2", "2016v1", "newDM2016v1"]
        #  )
#  na.runTauID()
#  '''
#re-running DeepTauv2p1 on MiniAOD https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Running_of_the_DeepTauIDs_ver_20
updatedTauName = "slimmedTausNewID" #name of pat::Tau collection with new tau-Ids
import RecoTauTag.RecoTau.tools.runTauIdMVA as tauIdConfig
tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms, debug = False,
                updatedTauName = updatedTauName,
                toKeep = ["deepTau2017v2p1",#deepTau TauIDs
                    "dR0p32017v2"]) #classic MVAIso tau-Ids # pick the one you need: ["2017v1", "2017v2", "newDM2017v2", "dR0p32017v2", "2016v1", "newDM2016v1","deepTau2017v2"]
tauIdEmbedder.runTauID()


############### MET Re-correct ##################
#https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#PF_MET
#If the JECs are updated, one would need to re-compute the type-1 MET for both PF and Puppi flavors.
#For 10_2_X, X>=7: Use CMSSW out of the box.
#?below is the instruction for 10_2_6.maybe wrong
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD (
        process,
        isData = False, # false for MC
        fixEE2017 = False,#reduce effect of high eta EE noise on the PF MET measurement in 2017 data
        fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139} ,
        postfix = "ModifiedMET"
)

############### MET filter ###############
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2
process.load('RecoMET.METFilters.ecalBadCalibFilter_cfi')
baddetEcallist = cms.vuint32(
    [872439604,872422825,872420274,872423218,
     872423215,872416066,872435036,872439336,
     872420273,872436907,872420147,872439731,
     872436657,872420397,872439732,872439339,
     872439603,872422436,872439861,872437051,
     872437052,872420649,872422436,872421950,
     872437185,872422564,872421566,872421695,
     872421955,872421567,872437184,872421951,
     872421694,872437056,872437057,872437313])


process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter(
    "EcalBadCalibFilter",
    EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
    ecalMinEt        = cms.double(50.),
    baddetEcal    = baddetEcallist, 
    taggingMode = cms.bool(True),
    debug = cms.bool(False)
    )


#####
##   Output file
#####
process.TFileService = cms.Service("TFileService",
    #  fileName = cms.string("TauOfTTTT_Toptagger_oldEID.root")
#  fileName = cms.string("test0901BSM_TTTTTau_AddHLT_Toptagger_EMetJetUpdated_oldEIDBack_v1.root")
    #  fileName = cms.string("smalltest.root")
    fileName = cms.string("v3.root")
)

#####
##   Analysis parameters
#####
process.TNT = cms.EDAnalyzer("BSM3G_TNT_Maker",#{{{
  #### Running options
  # Choose which trigger you want (do NOT need to put * as it will consider all the versions by default)
  ifevtriggers      = cms.bool(False), # True means you want to require the triggers
  maxtriggerversion = cms.double(20), # please leave it as a double
  evtriggers        = cms.vstring(
     #'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',
     'HLT_DoubleEle33_CaloIdL_MW_v',
     #'HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v',
     #'HLT_IsoMu24_v',
     #'HLT_IsoTkMu24_v',
     'HLT_Mu50_v',
     'HLT_TkMu50_v',
     'HLT_Mu30_TkMu11_v',
  ),
  # Choose which information you want to use
  fillgeninfo           = cms.bool(True),
  fillgenHFCategoryinfo = cms.bool(False),
  filleventinfo         = cms.bool(True),
  filltriggerinfo       = cms.bool(True),
  fillPVinfo            = cms.bool(True),
  fillmuoninfo          = cms.bool(True),
  fillelectronpatinfo   = cms.bool(True),
  filltauinfo           = cms.bool(True),#FF
  filljetinfo           = cms.bool(True), #T
  filltthjetinfo        = cms.bool(False), #F
  fillBoostedJetinfo    = cms.bool(False),
 # fillBoostedJetinfo    = cms.bool(True),
  fillTopSubJetinfo     = cms.bool(False), #F
#??
#  fillTauJetnessinfo    = cms.bool(True),
  fillTauJetnessinfo    = cms.bool(False),
  fillBJetnessinfo      = cms.bool(False),
  fillBJetnessFVinfo    = cms.bool(False),
  fillBTagReweight      = cms.bool(False),
#  fillBTagReweight      = cms.bool(True),
  fillPileupReweight    = cms.bool(True),
  fillMETinfo           = cms.bool(True),
  fillphotoninfo        = cms.bool(False), #F   
  # Choose format 
  MiniAODv2 = cms.bool(True),
  is_data   = cms.bool(False),
  lepfilter   = cms.int32(options.optionlepfilt), # at least #lepfilter lepton : muon: CutBaseLoose , Electron : pt/eta
  reHLT     = cms.bool(True),
  debug_    = cms.bool(False),
  super_TNT = cms.bool(False),
  AJVar     = cms.bool(False),
  tthlepVar = cms.bool(True),#FF#turn this to True to get electron miniIsolation and ele_jet and pvassocisation and IP information
  bjetnessselfilter = cms.bool(False),
  PuppiVar  = cms.bool(False),
  qglVar    = cms.bool(True),#FF
  dataEra   = cms.int32(2016),
  # Input tags 
  bits                = cms.InputTag("TriggerResults","","HLT"),
  prescales           = cms.InputTag("patTrigger"),
  objects             = cms.InputTag("selectedPatTrigger"),  
  vertices            = cms.InputTag("offlineSlimmedPrimaryVertices"),#offlineSlimmedPrimaryVertices 
  beamSpot            = cms.InputTag("offlineBeamSpot"),
  muons               = cms.InputTag("slimmedMuons"),
  patElectrons        = cms.InputTag("slimmedElectrons"),
#  electronVetoIdMap   = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto"),
#  electronLooseIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose"),
#  electronMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium"),
#  electronTightIdMap  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight"),
#  eleMVATrigIdMap        = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp80"),
#  eleMVAnonTrigIdMap     = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp80"),
#  eleMVATrigwp90IdMap    = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp90"),
#  eleMVAnonTrigwp90IdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wp90"),
#  eleMVATrigwpLooseIdMap    = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wpLoose"),
#  eleMVAnonTrigwpLooseIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Fall17-noIso-V1-wpLoose"),
#  eleHEEPIdMap                 = cms.InputTag("egmGsfElectronIDs:heepElectronID-HEEPV70"),
#  elemvaValuesMap_Trig      = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17IsoV1Values"),
#  elemvaCategoriesMap_Trig  = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
#  elemvaValuesMap_nonTrig         = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
#  elemvaCategoriesMap_nonTrig     = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
#  eleMVAHZZwpLooseIdMap = cms.InputTag("egmGsfElectronIDs:mvaEleID-Spring16-HZZ-V1-wpLoose"),
#  elemvaValuesMap_HZZ          = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16HZZV1Values"),
#  elemvaCategoriesMap_HZZ      = cms.InputTag("electronMVAValueMapProducer:ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
  ebRecHits = cms.InputTag("reducedEgamma","reducedEBRecHits"),
  taus                = cms.InputTag("slimmedTausNewID"),
  #taus                = cms.InputTag("NewTauIDsEmbedded"),
  #jets                = cms.InputTag("slimmedJets"),
  jets                = cms.InputTag(jetsNameAK4),
  #lepjets             = cms.InputTag("updatedPatJetsUpdatedJEC"),
  lepjets             = cms.InputTag(jetsNameAK4),
  jetsPUPPI           = cms.InputTag("slimmedJetsPuppi"),
  fatjets             = cms.InputTag("slimmedJetsAK8"),
  topsubjets          = cms.InputTag("slimmedJetsCMSTopTagCHSPacked", "SubJets"),
  mets                = cms.InputTag("slimmedMETsModifiedMET"),
  metsPUPPI           = cms.InputTag("slimmedMETsPuppi"),
  metFilterBits       = cms.InputTag("TriggerResults", "", "PAT"),
  photons             = cms.InputTag("slimmedPhotons"),
  packedPFCandidates  = cms.InputTag("packedPFCandidates"), 
  pruned              = cms.InputTag("prunedGenParticles"),
  #what is pruned? https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2016#MC_Truth
  # JER
  jerAK4PFchs     =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK4PFchs.txt"),
  jerAK4PFchsSF   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK4PFchs.txt"),
  jerAK4PFPuppi   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK4PFPuppi.txt"),
  jerAK4PFPuppiSF =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK4PFPuppi.txt"),
  jerAK8PFchs     =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK8PFchs.txt"),
  jerAK8PFchsSF   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK8PFchs.txt"),
  jerAK8PFPuppi   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK8PFPuppi.txt"),
  jerAK8PFPuppiSF =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK8PFPuppi.txt"),
  # JEC - CORRECTIONS ON FLY
  #apply the correction jet by jet
  jecPayloadNamesAK4PFchsMC1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsMC2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L2Relative_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsMC3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsMCUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_UncertaintySources_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsDATA1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsDATA2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsDATA3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsDATA4   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsDATAUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK4PFchs.txt"),
  jecPayloadNamesAK4PFPuppiMC1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiMC2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L2Relative_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiMC3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiMCUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_Uncertainty_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiDATA1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiDATA2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiDATA3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiDATA4   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiDATAUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK4PFPuppi.txt"),
  jecPayloadNamesAK8PFchsMC1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L1FastJet_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsMC2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L2Relative_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsMC3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L3Absolute_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsMCUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_Uncertainty_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsDATA1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsDATA2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsDATA3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsDATA4   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsDATAUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK8PFchs.txt"),
  # PILEUP REWEIGHTING
  PUReweightfile      = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/PUReweight/PileUpReweighting2016.root"),
  MinBiasUpReweightfile      = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/PUReweight/PileUpUpReweighting2016.root"),
  MinBiasDownReweightfile      = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/PUReweight/PileUpDownReweighting2016.root"),
  # PUPPI WEIGHT
  PuppiWeightFilePath = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/PUPPI/puppiCorr.root"),
  # BTAG REWEIGHTING
  BTAGReweightfile1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/BTAGReweight/csv_rwt_fit_hf_v2_final_2016_06_30test.root"),
  BTAGReweightfile2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/BTAGReweight/csv_rwt_fit_lf_v2_final_2016_06_30test.root"),
  # Object selection
  # Primary vertex cuts
  Pvtx_ndof_min   = cms.double(4.),
  Pvtx_vtx_max    = cms.double(24.),
  Pvtx_vtxdxy_max = cms.double(2.),
  # Obj primary vertex cuts
  #used in TauSelector
  vtx_ndof_min        = cms.int32(4),
  vtx_rho_max         = cms.int32(2),
  vtx_position_z_max  = cms.double(24.),
  # Muon cuts
  Muon_pt_min         = cms.double(5.),
  Muon_eta_max        = cms.double(50),
  # Electron cuts
  patElectron_pt_min  = cms.double(5.),
  patElectron_eta_max = cms.double(50),
  # Tau cuts
  Tau_pt_min          = cms.double(18.),
  Tau_eta_max         = cms.double(5.),
  # Jet cuts
  Jet_pt_min = cms.double(15.),
  # Photon cuts 
  Photon_pt_min   = cms.double(5.0),
  Photon_eta_max  = cms.double(5.0),
  # ttHFCategorization
  genJetPtMin               = cms.double(genJetPtMin),
  genJetAbsEtaMax           = cms.double(genJetAbsEtaMax),
  genJets                   = cms.InputTag(genJetCollection),
  genBHadJetIndex           = cms.InputTag("matchGenBHadron", "genBHadJetIndex"),
  genBHadFlavour            = cms.InputTag("matchGenBHadron", "genBHadFlavour"),
  genBHadFromTopWeakDecay   = cms.InputTag("matchGenBHadron", "genBHadFromTopWeakDecay"),
  genBHadPlusMothers        = cms.InputTag("matchGenBHadron", "genBHadPlusMothers"),
  genBHadPlusMothersIndices = cms.InputTag("matchGenBHadron", "genBHadPlusMothersIndices"),
  genBHadIndex              = cms.InputTag("matchGenBHadron", "genBHadIndex"),
  genBHadLeptonHadronIndex  = cms.InputTag("matchGenBHadron", "genBHadLeptonHadronIndex"),
  genBHadLeptonViaTau       = cms.InputTag("matchGenBHadron", "genBHadLeptonViaTau"),
  genCHadJetIndex           = cms.InputTag("matchGenCHadron", "genCHadJetIndex"),
  genCHadFlavour            = cms.InputTag("matchGenCHadron", "genCHadFlavour"),
  genCHadFromTopWeakDecay   = cms.InputTag("matchGenCHadron", "genCHadFromTopWeakDecay"),
  genCHadBHadronId          = cms.InputTag("matchGenCHadron", "genCHadBHadronId"),
)#}}}



#####
##   Dump gen particle list 
#####
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printGenParticleList = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(-1),
  printVertex = cms.untracked.bool(True),
  src = cms.InputTag("prunedGenParticles")
)

#QG likelihood  #Quark-gluon likelihood
## discriminate between (light) Quark and Gluon jets. https://twiki.cern.ch/twiki/bin/view/CMS/QuarkGluonLikelihood
#https://github.com/cms-nanoAOD/cmssw/pull/271#
#load db explicitly
#step0 This step can be skipped if you use the training from the GT
#  from CondCore.DBCommon.CondDBSetup_cfi import *
#  process.QGPoolDBESSource = cms.ESSource("PoolDBESSource",
      #  CondDBSetup,
      #  toGet = cms.VPSet(
         #  cms.PSet(
         #  record = cms.string('QGLikelihoodRcd'),
         #  tag    = cms.string('QGLikelihoodObject_v1_AK4'),
         #  label  = cms.untracked.string('QGL_AK4PFchs')
         #  inconsitence in AK4PFchs and AK4，which are type
         #  ),
      #  ),
      #  connect = cms.string('sqlite:QGL_AK4chs_94X.db')
     #  )
#  
#  process.es_prefer_qg = cms.ESPrefer('PoolDBESSource','QGPoolDBESSource')
#?
#step1 use training from GT #EDProducer
process.load('RecoJets.JetProducers.QGTagger_cfi')
#process.QGTagger.srcJets       = cms.InputTag('slimmedJets')
process.QGTagger.srcJets       = cms.InputTag(jetsNameAK4)#jetsNameAK4="selectedUpdatedPatJetsNewDFTraining"
process.QGTagger.jetsLabel     = cms.string('QGL_AK4PFchs')
#what does this step in python config do?
#In addition to the qgLikelihood, the QGTagger plugin will also produce the three veriables axis2, mult and ptD. 

#top tagger
from PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi import patElectrons #https://github.com/cms-sw/cmssw/blob/CMSSW_10_2_X/PhysicsTools/PatAlgos/python/producersLayer1/electronProducer_cfi.py
process.slimmedElectronsUpdated = cms.EDProducer("PATElectronUpdater",
        #?where to find this PATElectronUpdater?
#    src = cms.InputTag("slimmedElectrons","patElectrons_slimmedElectrons__PAT."),
    src = cms.InputTag("slimmedElectrons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    computeMiniIso = cms.bool(True),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    miniIsoParamsB = patElectrons.miniIsoParamsB, # so they're in sync
    miniIsoParamsE = patElectrons.miniIsoParamsE, # so they're in sync
)
process.isoForEle = cms.EDProducer("EleIsoValueMapProducer",
    src = cms.InputTag("slimmedElectronsUpdated"),
#    src = cms.InputTag("slimmedElectrons"),
    relative = cms.bool(False),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    rho_PFIso = cms.InputTag("fixedGridRhoFastjetAll"),
    EAFile_MiniIso = cms.FileInPath("RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt"),
    EAFile_PFIso = cms.FileInPath("RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt"),
)
process.ptRatioRelForEle = cms.EDProducer("ElectronJetVarProducer",
    srcJet = cms.InputTag("slimmedJets"),
    srcLep = cms.InputTag("slimmedElectronsUpdated"),
#    srcLep = cms.InputTag("slimmedElectrons"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices"),
)
process.slimmedElectronsWithUserData = cms.EDProducer("PATElectronUserDataEmbedder",
    src = cms.InputTag("slimmedElectronsUpdated"),
#    src = cms.InputTag("slimmedElectrons"),
    userFloats = cms.PSet(
        miniIsoAll = cms.InputTag("isoForEle:miniIsoAll"),
        #?what does InputTag in this form mean?
    ),
#    userInts = cms.PSet(#but we use userInt to call
#        VIDNestedWPBitmap = cms.InputTag("bitmapVIDForEle"),
#    ),
    userCands = cms.PSet(
        jetForLepJetVar = cms.InputTag("ptRatioRelForEle:jetForLepJetVar") # warning: Ptr is null if no match is found
    ),
)
###############################################################################################################################
from PhysicsTools.PatAlgos.producersLayer1.muonProducer_cfi import patMuons
# this below is used only in some eras
process.slimmedMuonsUpdated = cms.EDProducer("PATMuonUpdater",
    src = cms.InputTag("slimmedMuons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    computeMiniIso = cms.bool(True),
    pfCandsForMiniIso = cms.InputTag("packedPFCandidates"),
    miniIsoParams = patMuons.miniIsoParams, # so they're in sync
    recomputeMuonBasicSelectors = cms.bool(True),
)
process.isoForMu = cms.EDProducer("MuonIsoValueMapProducer",
    src = cms.InputTag("slimmedMuonsUpdated"),
    relative = cms.bool(False),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    EAFile_MiniIso = cms.FileInPath("PhysicsTools/NanoAOD/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_80X.txt"),
)
process.ptRatioRelForMu = cms.EDProducer("MuonJetVarProducer",
    srcJet = cms.InputTag("slimmedJets"),
    srcLep = cms.InputTag("slimmedMuonsUpdated"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices"),
)
process.slimmedMuonsWithUserData = cms.EDProducer("PATMuonUserDataEmbedder",
     src = cms.InputTag("slimmedMuonsUpdated"),
     userFloats = cms.PSet(
        miniIsoAll = cms.InputTag("isoForMu:miniIsoAll"),
     ),
     userCands = cms.PSet(
        jetForLepJetVar = cms.InputTag("ptRatioRelForMu:jetForLepJetVar") # warning: Ptr is null if no match is found
     ),
)
process.slimmedJetsWithUserData = cms.EDProducer("PATJetUserDataEmbedder",
#    src = cms.InputTag("slimmedJets"),
    src = cms.InputTag(jetsNameAK4),
    userFloats = cms.PSet(
        qgptD   = cms.InputTag("QGTagger:ptD"),
        qgAxis1 = cms.InputTag("QGTagger:axis1"),
        qgAxis2 = cms.InputTag("QGTagger:axis2"),
        ),
    userInts = cms.PSet(
        qgMult = cms.InputTag("QGTagger:mult")
        ),
)
process.load("TopTagger.TopTagger.SHOTProducerforBSM_cfi")
process.SHOTProducerforBSM.ak4JetSrc = cms.InputTag("slimmedJetsWithUserData")
process.SHOTProducerforBSM.muonSrc = cms.InputTag('slimmedMuonsWithUserData')
process.SHOTProducerforBSM.elecSrc = cms.InputTag('slimmedElectronsWithUserData')
process.SHOTProducerforBSM.doLeptonCleaning = cms.bool(True)
Toptagger = cms.Sequence(process.slimmedElectronsUpdated * process.isoForEle * process.ptRatioRelForEle * process.slimmedElectronsWithUserData * process.slimmedMuonsUpdated * process.isoForMu * process.ptRatioRelForMu * process.slimmedMuonsWithUserData * process.QGTagger * process.slimmedJetsWithUserData * process.SHOTProducerforBSM)



## tasks ##
process.tsk = cms.Task()
for mod in process.producers_().itervalues():
  #  if mod != process.egammaPostRecoSeq:
#    if mod != process.slimmedElectrons:
        process.tsk.add(mod)
for mod in process.filters_().itervalues():
    process.tsk.add(mod)

#####
##   PROCESS
#####
process.p = cms.Path(
process.ecalBadCalibReducedMINIAODFilter*
#ecalBadCalibReducedMINIAODFilter is a filter,is'nt it included in the task?
#process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC *
Toptagger*
process.prefiringweight *
#process.regressionApplication *
#process.calibratedPatElectrons  *
#process.electronIDValueMapProducer *
#process.egmGsfElectronIDSequence *
#process.egmPhotonIDSequence *
#process.egammaScaleSmearAndVIDSeq *
#Toptagger*
process.egammaPostRecoSeq *
process.fullPatMetSequenceModifiedMET *
#process.puppiMETSequence *
#process.fullPatMetSequencePuppi *
#process.QGTagger *
#process.rerunMvaIsolationSequence *
#process.NewTauIDsEmbedded*
process.slimmedTausNewID*
#process.selectedHadronsAndPartons*process.genJetFlavourInfos*process.matchGenCHadron*process.matchGenBHadron*
#process.primaryVertexFilter* 
#process.CSCTightHaloFilter*process.eeBadScFilter*process.HBHENoiseFilterResultProducer*process.ApplyBaselineHBHENoiseFilter*
process.TNT,
process.tsk
)
#unscheduled Some EDProducers and EDFilters which have not been explicitly placed on a Path or EndPath will be run the first time someone asks for their data
#The filter decision of an EDFilter is ignored when it is run in unscheduled mode. You must put the EDFilter on a Path to make use of its filter decision.
