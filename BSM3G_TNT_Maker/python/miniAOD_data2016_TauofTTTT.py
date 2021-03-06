import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import copy
#??? what is import copy doing?
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent

options = VarParsing.VarParsing('analysis')
# Variables one can control from the multicrab configuration file.
# When connecting a variable you need to tell the module certain information
# about the object.
#                   - Object name.
#                   - Default value.
#                   - Is object a single number or a list.
#                   - Object type.
#                   - Details of object.
#

# ===== Register new variables =====
#?different JEC meaning?
options.register('optionJECAK4PFchsDATA1',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFchsDATA1 JEC file")

options.register('optionJECAK4PFchsDATA2',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFchsDATA2 JEC file"
)
options.register('optionJECAK4PFchsDATA3',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFchsDATA3 JEC file"
)
options.register('optionJECAK4PFchsDATA4',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFchsDATA4 JEC file"
)
options.register('optionJECAK4PFchsDATAUnc',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK4PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFchsDATAUnc JEC file"
)


options.register('optionJECAK4PFPuppiDATA1',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK4PFPuppi.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFPuppiDATA1 JEC file"
)
options.register('optionJECAK4PFPuppiDATA2',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK4PFPuppi.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFPuppiDATA2 JEC file"
)
options.register('optionJECAK4PFPuppiDATA3',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK4PFPuppi.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFPuppiDATA3 JEC file"
)
options.register('optionJECAK4PFPuppiDATA4',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK4PFPuppi.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFPuppiDATA4 JEC file"
)
options.register('optionJECAK4PFPuppiDATAUnc',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK4PFPuppi.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK4PFPuppiDATAUnc JEC file"
)



options.register('optionJECAK8PFchsDATA1',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L1FastJet_AK8PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK8PFchsDATA1 JEC file"
)
options.register('optionJECAK8PFchsDATA2',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2Relative_AK8PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK8PFchsDATA2 JEC file"
)
options.register('optionJECAK8PFchsDATA3',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L3Absolute_AK8PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK8PFchsDATA3 JEC file"
)
options.register('optionJECAK8PFchsDATA4',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_L2L3Residual_AK8PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK8PFchsDATA4 JEC file"
)
options.register('optionJECAK8PFchsDATAUnc',
'BSMFramework/BSM3G_TNT_Maker/data/JEC/DATA/Summer16_07Aug2017BCD_V11_DATA/Summer16_07Aug2017BCD_V11_DATA_Uncertainty_AK8PFchs.txt',
VarParsing.VarParsing.multiplicity.singleton,
VarParsing.VarParsing.varType.string,
"Name for AK8PFchsDATAUnc JEC file"
)

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
process = cms.Process("BSM")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")
process.load("Configuration.StandardSequences.MagneticField_38T_cff")#differrent than in MC?
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.load("Geometry.CaloEventSetup.CaloTowerConstituents_cfi")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = '94X_dataRun2_v10'
#process.GlobalTag.globaltag = '102X_dataRun2_nanoAOD_2016_v1'
#94X_dataRun2_v10
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')

#####
##   Input files
#####
process.source = cms.Source("PoolSource",
  fileNames = cms.untracked.vstring(
    #'/store/data/Run2017B/SingleMuon/MINIAOD/31Mar2018-v1/100000/005EF8EB-6338-E811-B31C-0025905A6066.root',
#    '/store/data/Run2016B/SingleMuon/MINIAOD/17Jul2018_ver2-v1/90000/FEADEB19-1D92-E811-BAFA-0025905C54D8.root',
    '/store/data/Run2016G/Tau/MINIAOD/17Jul2018-v1/40000/FEA791C5-C291-E811-A99A-A0369FC5EEF4.root',
  ),
  skipEvents = cms.untracked.uint32(0)
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

##### JEC
from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
updateJetCollection(
  process,
  jetSource = cms.InputTag('slimmedJets'),
  pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
  svSource = cms.InputTag('slimmedSecondaryVertices'),
  #labelName = 'UpdatedJEC',
  jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet','L2Relative','L3Absolute','L2L3Residual']), 'None'),
  btagDiscriminators = [
     'pfDeepFlavourJetTags:probb',
     'pfDeepFlavourJetTags:probbb',
     'pfDeepFlavourJetTags:problepb',
     'pfDeepFlavourJetTags:probc',
     'pfDeepFlavourJetTags:probuds',
     'pfDeepFlavourJetTags:probg'
  ],
  postfix='NewDFTraining'
)

jetsNameAK4="selectedUpdatedPatJetsNewDFTraining"

##### L1 Prefire
from PhysicsTools.PatUtils.l1ECALPrefiringWeightProducer_cfi import l1ECALPrefiringWeightProducer
process.prefiringweight = l1ECALPrefiringWeightProducer.clone(
    DataEra = cms.string("2016BtoH"), # 2017BtoF
    UseJetEMPt = cms.bool(False),
    PrefiringRateSystematicUncty = cms.double(0.2),
    SkipWarnings = False)
 

#####
##   ELECTRON ID SECTION
#####
######
### Electron smear and regression
######
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
setupEgammaPostRecoSeq(process, 
#        applyEnergyCorrections=False,
#        applyVIDOnCorrectedEgamma=False,
        runEnergyCorrections=False, # False for 2016/2018, as energy corrections are not yet availible for 2018; corrections by default are fine for 2016 so no need to re-run
        runVID=True, # if you are running on miniAOD v1 or Fall17V2 please enable it 
        era='2016-Legacy') # '2018-Prompt', '2016-Legacy'

#####
##   For tt+X
#####
#####
# Setting input particle collections to be used by the tools
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

updatedTauName = "slimmedTausNewID" #name of pat::Tau collection with new tau-Ids
import RecoTauTag.RecoTau.tools.runTauIdMVA as tauIdConfig
tauIdEmbedder = tauIdConfig.TauIDEmbedder(process, cms, debug = False,
                updatedTauName = updatedTauName,
                toKeep = ["deepTau2017v2p1","dR0p32017v2"]) # pick the one you need: ["2017v1", "2017v2", "newDM2017v2", "dR0p32017v2", "2016v1", "newDM2016v1","deepTau2017v2"]
tauIdEmbedder.runTauID()



############### MET Re-correct ##################
from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
runMetCorAndUncFromMiniAOD (
        process,
        isData = True, # false for MC
        fixEE2017 = False,
        fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139} ,
        postfix = "ModifiedMET"
)

############### MET filter ###############
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
options.ofName += ".root"
#it seems we are not making use of ofName?
process.TFileService = cms.Service("TFileService",
  fileName = cms.string("TauOfTTTT_TopTagger_oldEID.root")
)

#####
##   Analysis parameters
#####
process.TNT = cms.EDAnalyzer("BSM3G_TNT_Maker",
  #### Running options
  # Choose which trigger you want (do NOT need to put * as it will consider all the versions by default)
  ifevtriggers      = cms.bool(False), # True means you want to require the triggers
  maxtriggerversion = cms.double(20), # please leave it as a double
  evtriggers        = cms.vstring(
  #############################
    # https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLT2016#Recommended_trigger_paths_for_20
    # https://indico.cern.ch/event/682891/contributions/2810364/attachments/1570825/2820752/20171206_CMSWeek_MuonHLTReport_KPLee_v3_4.pdf
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonHLT2018#Recommended_trigger_paths_for_20
    # https://twiki.cern.ch/twiki/bin/view/CMS/EgHLTRunIISummary 
    # single electron 
    'HLT_Ele25_eta2p1_WPTight_Gsf_v',
    'HLT_Ele27_WPTight_Gsf_v',
    'HLT_Ele27_eta2p1_WPLoose_Gsf_v',
    'HLT_Ele35_WPTight_Gsf_v',
    'HLT_Ele32_WPTight_Gsf_v',
    # Single Muon
    'HLT_IsoMu24_v', 
    'HLT_IsoTkMu24_v',
    'HLT_IsoMu27_v',
    'HLT_IsoMu22_v',
    'HLT_IsoTkMu22_v',
    'HLT_IsoMu22_eta2p1_v',
    'HLT_IsoTkMu22_eta2p1_v',
    # Double Electron
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v',
    'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v',
    # Double Muon
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v',
    'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v',
    'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v',
    # Muon + Electron
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v', 
    'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v',
    'HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v', 
    'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v', 
    # Triple Leptons
    'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v', 
    'HLT_TripleMu_12_10_5_v',
    'HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v',
    'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v',
    'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v',
    ## bstar ##
    'HLT_TkMu50_v',
    'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v',
    'HLT_Photon200_v',
    'HLT_Photon175_v',
    'HLT_Ele115_CaloIdVT_GsfTrkIdT_v',
    'HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v',
    'HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v',
    'HLT_Ele27_WP85_Gsf_v',
    'HLT_Mu50_v',
  ),
  # Choose which information you want to use
  fillgeninfo           = cms.bool(False),
  fillgenHFCategoryinfo = cms.bool(False),
  filleventinfo         = cms.bool(True),
  filltriggerinfo       = cms.bool(True),
  fillPVinfo            = cms.bool(True),
  fillmuoninfo          = cms.bool(True),
  fillelectronpatinfo   = cms.bool(True),
  filltauinfo           = cms.bool(True),
  filljetinfo           = cms.bool(True),
  filltthjetinfo        = cms.bool(False), #F
  fillBoostedJetinfo    = cms.bool(False),
  fillTopSubJetinfo     = cms.bool(False), #F
  fillTauJetnessinfo    = cms.bool(False),
  fillBJetnessinfo      = cms.bool(False),
  fillBJetnessFVinfo    = cms.bool(False),
  fillBTagReweight      = cms.bool(False),
  fillPileupReweight    = cms.bool(True),
  fillMETinfo           = cms.bool(True),
  fillphotoninfo        = cms.bool(False), #F   
  # Choose format 
  MiniAODv2 = cms.bool(True),
  is_data   = cms.bool(True),
  lepfilter   = cms.int32(0), # at least #lepfilter lepton : muon: CutBaseLoose , Electron : pt/eta
  reHLT     = cms.bool(True),
  debug_    = cms.bool(False),
  super_TNT = cms.bool(False),
  AJVar     = cms.bool(False),
  tthlepVar = cms.bool(True),
  bjetnessselfilter = cms.bool(False),
  PuppiVar  = cms.bool(False),
  qglVar    = cms.bool(True),
  dataEra   = cms.int32(2016),
  # Input tags 
  bits                = cms.InputTag("TriggerResults","","HLT"),
  prescales           = cms.InputTag("patTrigger"),
  objects             = cms.InputTag("selectedPatTrigger"),  
  vertices            = cms.InputTag("offlineSlimmedPrimaryVertices"),
  beamSpot            = cms.InputTag("offlineBeamSpot"),
  muons               = cms.InputTag("slimmedMuons"),
  patElectrons        = cms.InputTag("slimmedElectrons"),
  ebRecHits = cms.InputTag("reducedEgamma","reducedEBRecHits"),
  taus                = cms.InputTag("slimmedTausNewID"),
  #taus                = cms.InputTag("NewTauIDsEmbedded"),
  jets                = cms.InputTag(jetsNameAK4),
  lepjets                = cms.InputTag(jetsNameAK4),
  jetsPUPPI           = cms.InputTag("slimmedJetsPuppi"),
  fatjets             = cms.InputTag("slimmedJetsAK8"),
  topsubjets          = cms.InputTag("slimmedJetsCMSTopTagCHSPacked", "SubJets"),
  mets                = cms.InputTag("slimmedMETsModifiedMET"),
  metsPUPPI           = cms.InputTag("slimmedMETsPuppi"),
  metFilterBits       = cms.InputTag("TriggerResults", "", "RECO"),
  photons             = cms.InputTag("slimmedPhotons"),
  packedPFCandidates  = cms.InputTag("packedPFCandidates"), 
  pruned              = cms.InputTag("prunedGenParticles"),
  # JER
  # it is the same as MC
  jerAK4PFchs     =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK4PFchs.txt"),
  jerAK4PFchsSF   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK4PFchs.txt"),
  jerAK4PFPuppi   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK4PFPuppi.txt"),
  jerAK4PFPuppiSF =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK4PFPuppi.txt"),
  jerAK8PFchs     =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK8PFchs.txt"),
  jerAK8PFchsSF   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK8PFchs.txt"),
  jerAK8PFPuppi   =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_PtResolution_AK8PFPuppi.txt"),
  jerAK8PFPuppiSF =  cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JER/Summer16_25nsV1_MC_SF_AK8PFPuppi.txt"),
  # JEC - CORRECTIONS ON FLY
  #?it is MC here for data and data for MC. why?
  jecPayloadNamesAK4PFchsMC1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsMC2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L2Relative_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsMC3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFchs.txt"),
  jecPayloadNamesAK4PFchsMCUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_UncertaintySources_AK4PFchs.txt"),
  jecPayloadNamesAK4PFPuppiMC1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L1FastJet_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiMC2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L2Relative_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiMC3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L3Absolute_AK4PFPuppi.txt"),
  jecPayloadNamesAK4PFPuppiMCUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_Uncertainty_AK4PFPuppi.txt"),
  jecPayloadNamesAK8PFchsMC1   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L1FastJet_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsMC2   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L2Relative_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsMC3   = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_L3Absolute_AK8PFchs.txt"),
  jecPayloadNamesAK8PFchsMCUnc = cms.FileInPath("BSMFramework/BSM3G_TNT_Maker/data/JEC/MC/Summer16_07Aug2017_V11_MC/Summer16_07Aug2017_V11_MC_Uncertainty_AK8PFchs.txt"),
   #=== DATA ===
   #??
   jecPayloadNamesAK4PFchsDATA1   = cms.FileInPath(options.optionJECAK4PFchsDATA1),
   jecPayloadNamesAK4PFchsDATA2   = cms.FileInPath(options.optionJECAK4PFchsDATA2),
   jecPayloadNamesAK4PFchsDATA3   = cms.FileInPath(options.optionJECAK4PFchsDATA3),
   jecPayloadNamesAK4PFchsDATA4   = cms.FileInPath(options.optionJECAK4PFchsDATA4),
   jecPayloadNamesAK4PFchsDATAUnc = cms.FileInPath(options.optionJECAK4PFchsDATAUnc),
   jecPayloadNamesAK4PFPuppiDATA1   = cms.FileInPath(options.optionJECAK4PFPuppiDATA1),
   jecPayloadNamesAK4PFPuppiDATA2   = cms.FileInPath(options.optionJECAK4PFPuppiDATA2),
   jecPayloadNamesAK4PFPuppiDATA3   = cms.FileInPath(options.optionJECAK4PFPuppiDATA3),
   jecPayloadNamesAK4PFPuppiDATA4   = cms.FileInPath(options.optionJECAK4PFPuppiDATA4),
   jecPayloadNamesAK4PFPuppiDATAUnc = cms.FileInPath(options.optionJECAK4PFPuppiDATAUnc),
   jecPayloadNamesAK8PFchsDATA1   = cms.FileInPath(options.optionJECAK8PFchsDATA1),
   jecPayloadNamesAK8PFchsDATA2   = cms.FileInPath(options.optionJECAK8PFchsDATA2),
   jecPayloadNamesAK8PFchsDATA3   = cms.FileInPath(options.optionJECAK8PFchsDATA3),
   jecPayloadNamesAK8PFchsDATA4   = cms.FileInPath(options.optionJECAK8PFchsDATA4),
   jecPayloadNamesAK8PFchsDATAUnc = cms.FileInPath(options.optionJECAK8PFchsDATAUnc),
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
)

#####
##   Dump gen particle list 
#####
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printGenParticleList = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(-1),
  printVertex = cms.untracked.bool(True),
  src = cms.InputTag("prunedGenParticles")
)

#QG likelihood
#https://github.com/cms-nanoAOD/cmssw/pull/271#
#load db explicitly
'''
from CondCore.DBCommon.CondDBSetup_cfi import *
process.QGPoolDBESSource = cms.ESSource("PoolDBESSource",
      CondDBSetup,
      toGet = cms.VPSet(
         cms.PSet(
         record = cms.string('QGLikelihoodRcd'),
         tag    = cms.string('QGLikelihoodObject_v1_AK4'),
         label  = cms.untracked.string('QGL_AK4PFchs')
         ),
      ),
      connect = cms.string('sqlite:QGL_AK4chs_94X.db')
     )

process.es_prefer_qg = cms.ESPrefer('PoolDBESSource','QGPoolDBESSource')
'''
process.load('RecoJets.JetProducers.QGTagger_cfi')
#process.QGTagger.srcJets       = cms.InputTag('slimmedJets')
process.QGTagger.srcJets       = cms.InputTag(jetsNameAK4)
process.QGTagger.jetsLabel     = cms.string('QGL_AK4PFchs')

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
    process.tsk.add(mod)
for mod in process.filters_().itervalues():
    process.tsk.add(mod)

#####
##   PROCESS
#####
process.p = cms.Path(
process.ecalBadCalibReducedMINIAODFilter*
#process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC *
Toptagger*
process.prefiringweight *
#process.egmPhotonIDSequence *
#process.egammaScaleSmearAndVIDSeq *
process.egammaPostRecoSeq *
process.fullPatMetSequenceModifiedMET *
#process.QGTagger *
#process.rerunMvaIsolationSequence *
process.slimmedTausNewID*
#process.selectedHadronsAndPartons*process.genJetFlavourInfos*process.matchGenCHadron*process.matchGenBHadron*
#process.primaryVertexFilter* 
#process.CSCTightHaloFilter*process.eeBadScFilter*process.HBHENoiseFilterResultProducer*process.ApplyBaselineHBHENoiseFilter*
process.TNT,
process.tsk
)
