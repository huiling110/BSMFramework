import FWCore.ParameterSet.Config as cms

process = cms.Process("GetHLT")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
       # '/store/cmst3/user/gpetrucc/miniAOD/v1/TT_Tune4C_13TeV-pythia8-tauola_PU_S14_PAT.root'
       '/store/mc/RunIISummer16MiniAODv3/TTTT_TuneCUETP8M2T4_PSweights_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v1/230000/F61E4EE9-127E-E911-8FF5-549F3525CD78.root'
    )
)

process.getHLT = cms.EDAnalyzer("GetHLT",
    bits = cms.InputTag("TriggerResults","","HLT"),
    prescales = cms.InputTag("patTrigger"),
    objects = cms.InputTag("selectedPatTrigger"),
)

process.p = cms.Path(process.getHLT)
