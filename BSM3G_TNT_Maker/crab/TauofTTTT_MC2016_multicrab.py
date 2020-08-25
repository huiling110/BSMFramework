import CRABClient
if __name__ == '__main__':
 #####
 ##   Multicrab configuration
 #####
 import sys
 from multiprocessing import Process
 from CRABClient.UserUtilities import config #, getUsernameFromSiteDB
 #?
 config = config()
 from CRABAPI.RawCommand import crabCommand
 from CRABClient.ClientExceptions import ClientException
 from httplib import HTTPException
 config.General.workArea = 'Crab_projects'

 def submit(config):
  try:
   crabCommand('submit', config = config)
  except HTTPException as hte:
   print "Failed submitting task: %s" % (hte.headers)
  except ClientException as cle:
   print "Failed submitting task: %s" % (cle)
 #####
 ##   Crab configuration
 #####
 datasetnames  = [#{{{
# signal
#'Legacy16V2_TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8',#S 
#'Legacy16V2_TTTT_TuneCUETP8M2T4_PSweights_13TeV',#S
#'Legacy16V2_TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',#S 
#'Legacy16V2_TT_TuneCUETP8M2T4_13TeV-powheg-pythia8',# S 
#'Legacy16V2_TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8', #S 
#'Legacy16V2_TTGamma_SingleLept_TuneEE5C_13TeV-madgraph-herwigpp',#S
#'Legacy16V2_TTGamma_Dilept_TuneEE5C_13TeV-madgraph-herwigpp',#F
'Legacy16V2_TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',#F
#'Legacy16V2_ttZJets_13TeV_madgraphMLM-pythia8',#F
#'Legacy16V2_TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',#########
#'Legacy16V2_TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',#F
#'Legacy16V2_ttWJets_13TeV_madgraphMLM',
#'Legacy16V2_TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',#F
#'Legacy16V2_TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#'Legacy16V2_TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8',#F
#'Legacy16V2_ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix',#F
#'Legacy16V2_ttbb_4FS_ckm_amcatnlo_madspin_pythia8',#F
#'Legacy16V2_WZ_TuneCUETP8M1_13TeV-pythia8',#F
#'Legacy16V2_WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8',#F
#'Legacy16V2_WW_TuneCUETP8M1_13TeV-pythia8',#F
#'Legacy16V2_WWTo2L2Nu_DoubleScattering_13TeV-pythia8',#F
#'Legacy16V2_WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8',#F
#'Legacy16V2_ZZ_TuneCUETP8M1_13TeV-pythia8',#F
#'Legacy16V2_ZZTo2Tau2Nu_1Jets_ZZOnShell_13TeV-amcatnloFXFX-madspin-pythia8',#F
#'Legacy16V2_ZZTo2Tau2Nu_0Jets_ZZOnShell_13TeV-amcatnloFXFX-madspin-pythia8',#F

##below is for Zhanngyu to run
#'Legacy16V2_ZZTo2Q2Nu_13TeV_powheg_pythia8',
#'Legacy16V2_ZZTo4L_13TeV_powheg_pythia8_ext1',
#'Legacy16V2_ZZTo2L2Q_13TeV_powheg_pythia8',
#'Legacy16V2_WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#'Legacy16V2_WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph',
#'Legacy16V2_ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
#'Legacy16V2_ZGJetsToLLG_EW_LO_13TeV-sherpa',
#'Legacy16V2_WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_WGG_5f_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_WGGJets_TuneCUETP8M1_13TeV_madgraphMLM_pythia8',
#'Legacy16V2_ZGGToLLGG_5f_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
#'Legacy16V2_ZGGJets_ZToHadOrNu_5f_LO_madgraph_pythia8',
#'Legacy16V2_WZJToLLLNu_TuneCUETP8M1_13TeV-amcnlo-pythia8',
#'Legacy16V2_WWJTo2L2Nu_NNLOPS_TuneCUEP8M1_13TeV-powheg-pythia8',
#'Legacy16V2_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#'Legacy16V2_DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext1',
#'Legacy16V2_DYjetstotautau_01234jets_Pt-0ToInf_13TeV-sherpa',
#'Legacy16V2_tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
#'Legacy16V2_tZq_nunu_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1',
#'Legacy16V2_TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8',
#'Legacy16V2_ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4',
#'Legacy16V2_ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4',
#'Legacy16V2_VHToNonbb_M125_DiLeptonFilter_TuneCUETP8M1_13TeV_amcatnloFXFX_madspin_pythia8',
#'Legacy16V2_GluGluToHHTo4Tau_node_SM_13TeV-madgraph',
#'Legacy16V2_GluGluToHHTo4B_node_SM_13TeV-madgraph',
#'Legacy16V2_GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph',
#'Legacy16V2_GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph',
#'Legacy16V2_GluGluToHHTo2B2G_node_SM_13TeV-madgraph',
#'Legacy16V2_TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#'Legacy16V2_TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
#}}}
]

 datasetinputs = [
#{{{
#signal
#'/TTTT_TuneCUETP8M2T4_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTTT_TuneCUETP8M2T4_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_correctnPartonsInBorn/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/TTGamma_SingleLept_TuneEE5C_13TeV-madgraph-herwigpp/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTGamma_Dilept_TuneEE5C_13TeV-madgraph-herwigpp/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
'/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/ttZJets_13TeV_madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/MINIAODSIM', 
#'/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ttWJets_13TeV_madgraphMLM/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/MINIAODSIM',
#'/ttHToNonbb_M125_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ttHJetToNonbb_M125_13TeV_amcatnloFXFX_madspin_pythia8_mWCutfix/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/ttbb_4FS_ckm_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WpWpJJ_EWK-QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16MiniAODv3-PU/ZZTo2Tau2Nu_2Jets_ZZOnShell_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ZZTo2Tau2Nu_1Jets_ZZOnShell_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ZZTo2Tau2Nu_0Jets_ZZOnShell_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#
###below for Zhanngyu to run
#'''
#'/ZZTo2Q2Nu_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ZZTo4L_13TeV_powheg_pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/WGJets_MonoPhoton_PtG-40to130_TuneCUETP8M1_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/ZGJetsToLLG_EW_LO_13TeV-sherpa/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WZG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/WGG_5f_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/WGGJets_TuneCUETP8M1_13TeV_madgraphMLM_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/ZGGToLLGG_5f_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/ZGGJets_ZToHadOrNu_5f_LO_madgraph_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/WZJToLLLNu_TuneCUETP8M1_13TeV-amcnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/WWJTo2L2Nu_NNLOPS_TuneCUEP8M1_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/MINIAODSIM',
#'/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_ext1/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/DYjetstotautau_01234jets_Pt-0ToInf_13TeV-sherpa/RunIISummer16MiniAODv3-PUMoriond17_QCDEWNLO_correct_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/tZq_nunu_4f_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16MiniAODv3-94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/MINIAODSIM',
#'/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M2T4/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/VHToNonbb_M125_DiLeptonFilter_TuneCUETP8M1_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/GluGluToHHTo4Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/GluGluToHHTo4B_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/GluGluToHHTo2B2VTo2L2Nu_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/GluGluToHHTo2B2Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-FlatPU28to62HcalNZSRAW_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM',
#'/GluGluToHHTo2B2G_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM',
#'/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',
#'/TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/MINIAODSIM',

#}}}
]

# samples also used in tW or bstar
# minimum lepton are set to 1 instead of 2 
tWLists = [
]
#?nothing in twLists?

# baseDir
#baseDir = "/afs/cern.ch/work/b/binghuan/private/TTHLep_RunII/CMSSW_10_2_16/src/BSMFramework/"
#baseDir = "/workfs/cms/huahuil/BSM/CMSSW_10_2_20_UL/src/BSMFramework/"
baseDir = "/workfs/cms/huahuil/BSM_UpdateVersion/CMSSW_10_2_20_UL/src/BSMFramework/"

for d in range(0,len(datasetnames)):
#for d in range(0,1):
    print 'multicrab.py: Running datasetname: ', datasetnames[d]
#    lepFilt = 2
    lepFilt = 0
    if datasetnames[d] in tWLists:
        lepFilt = 1
        print 'multicrab_MC2016.py: Run ', datasetnames[d], ' lepFilt 1 for tW samples '
    
    if "ctcvcp" in datasetnames[d]:
        lepFilt = 0
        print 'multicrab_MC2016.py: Run ', datasetnames[d], ' lepFilt 0 for ctcvcp samples '
    
    nameLepFilt = 'optionlepfilt={}'.format(lepFilt) #The format() method formats the specified value(s) and insert them inside the string's placeholder.
    
    config.section_('General')
    config.General.requestName = datasetnames[d]#it is used by CRAB to create a project directory (named crab_<requestName>) where files corresponding to this particular task will be stored.
 #   config.General.workArea    = datasetnames[d]#The area (full or relative path) where to create the CRAB project directory
    config.General.workArea    = '/workfs/cms/huahuil/BSM_UpdateVersion/CMSSW_10_2_20_UL/src/BSMFramework/BSM3G_TNT_Maker/crab/crab_resulsts_8_22/'+datasetnames[d]#The area (full or relative path) where to create the CRAB project directory
    config.General.transferLogs = True  #Whether or not to copy the jobs log files to the storage site

    config.section_('JobType')
    config.JobType.pluginName  = 'Analysis'
    # List of parameters to pass to CMSSW parameter-set configuration file:
#    config.JobType.psetName    = baseDir+'BSM3G_TNT_Maker/python/miniAOD_MC2016.py'
    config.JobType.psetName    = baseDir+'BSM3G_TNT_Maker/python/miniAOD_MC2016_Study.py'
    config.JobType.inputFiles = [(baseDir+'BSM3G_TNT_Maker/data/QG/QGL_AK4chs_94X.db')]
    #?what is QGdoing?
    config.JobType.sendExternalFolder = True
    config.JobType.maxMemoryMB = 2000 # Default == 2Gb : maximum guaranteed to run on all sites
    #config.JobType.allowUndistributedCMSSW = True
    ofParam = 'ofName=' + datasetnames[d]
    config.JobType.pyCfgParams = [nameLepFilt,
                                    ofParam]
    config.section_('Data')
    config.Data.allowNonValidInputDataset = True
    config.Data.inputDataset   = datasetinputs[d]
    config.Data.inputDBS       = 'global'
  #  config.Data.splitting      = 'FileBased'
    config.Data.splitting      = 'Automatic'
   # config.Data.totalUnits     = 40000 #With 'FileBased' splitting tells how many files to analyse
    config.Data.unitsPerJob    = 2000 
#    config.Data.outLFNDirBase = '/store/user/binghuan/'# First part of LFN for output files (must be /store/user/<username>/ or /store/group/<username>/  )
    config.Data.outLFNDirBase = '/store/user/hhua/'# First part of LFN for output files (must be /store/user/<username>/ or /store/group/<username>/  )
    config.Data.outputDatasetTag = datasetnames[d]+"HLTAdded_EJetMetUpdated"

#    print 'multicrab.py: outLFNDirBase = /store/user/binghuan/'
    print 'multicrab.py: outLFNDirBase = /store/user/hhua/'
    #config.Data.publication = True

    config.section_('Site')
    config.Site.storageSite    = 'T2_CN_Beijing'#'T2_CH_CERN' # Site to which output is permenantly copied by crab3
    print 'multicrab.py: Submitting Jobs'
    #submit(config)
    p = Process(target=submit, args=(config,))
    #?
    p.start()
    p.join()
