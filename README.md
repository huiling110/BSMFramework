

This code is based on a preliminary version of the BSM3G code initiated by:
Andres Florez (Los Andes), Alfredo Gurrola (Vanderbilt) and Amandeep Kalsi (Panjab) 
(See https://github.com/florez/NtupleMaker_740)

It has been extended and further developed by Francesco Romeo (IHEP) and Aniello Spiezia (IHEP).
It has been modified for RunII analysis by Binghuan Li (IHEP) and further modified by Huiling Hua(IHEP)
This version of code is used for 2016 miniAOD v3 && 2017 miniAOD v2 and v1 & 2018 miniAOD  Ntuple production:


# Instruction
## step1
- export SCRAM_ARCH=slc7_amd64_gcc700
- cmsrel CMSSW_10_2_20_UL
- cd CMSSW_10_2_20_UL/src
- cmsenv
- git cms-init
- git config merge.renameLimit 999999

## step2
- set up Egamma Tools https://twiki.cern.ch/twiki/bin/view/CMS/EgammaMiniAODV2#2018_Preliminary_Energy_Correcti 
  - git cms-merge-topic cms-egamma:EgammaPostRecoTools 
  - git cms-merge-topic cms-egamma:PhotonIDValueMapSpeedup1029 
  - git cms-merge-topic cms-egamma:slava77-btvDictFix_10210 
  - git cms-addpkg EgammaAnalysis/ElectronTools
  - rm EgammaAnalysis/ElectronTools/data -rf
  - git clone git@github.com:cms-data/EgammaAnalysis-ElectronTools.git EgammaAnalysis/ElectronTools/data
  - scram b -j 8
        
- set up MET corrections with EE nosie fix https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Instructions_for_9_4_X_X_9_for_2
  - ~~git cms-merge-topic cms-met:METFixEE2017_949_v2_backport_to_102X~~
  - ~~scram b -j 8~~

- set up MetFilters https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#How_to_run_ecal_BadCalibReducedM
  - git cms-addpkg RecoMET/METFilters
  - scram b

- set up DeepTau v2p1 https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuidePFTauID#Running_of_the_DNN_based_tau_ID
  - git cms-merge-topic -u cms-tau-pog:CMSSW_10_2_X_tau-pog_DeepTau2017v2p1_nanoAOD
  - scram b -j 4

- set up JEC for 2018 https://github.com/cms-sw/cmssw/pull/28098
  - git cms-merge-topic 28098
  - scram b -j 4
## step 3
- implement SUSY HOT toptagger https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSYHOTGroup
  - git cms-merge-topic -u pastika:AddAxis1_1026
  - git clone git@github.com:huiling110/TopTagger.git
  - scram b -j4
  - mkdir -p ${CMSSW_BASE}/src/TopTagger/TopTagger/data
  - source TopTagger/TopTagger/test/taggerSetup.sh
  - getTaggerCfg.sh -o -n -t DeepResolved_DeepCSV_GR_noDisc_Release_v1.0.0 -d $CMSSW_BASE/src/TopTagger/TopTagger/data
  - getTaggerCfg.sh -t MVAAK8_Tight_noQGL_binaryCSV_v1.0.2
  
## step 4
- set BSM Framework
  - git clone https://github.com/huiling110/BSMFramework.git (git clone git@github.com:huiling110/BSMFramework.git)
  - cd BSMFramework/
  - git checkout CMSSW_10_2_20_UL
  - cd ..
  - scram b -j 8
  


## step 5
- To Run 
  - cd BSMFramework/BSM3G_TNT_Maker/python/
  - cmsRun miniAOD_MC2016_Study.py
- crab
  - voms-proxy-init --voms cms
  - source /cvmfs/cms.cern.ch/crab3/crab.sh
  - source /cvmfs/cms.cern.ch/common/crab-setup.sh
  - cd BSMFramework/BSM3G_TNT_Maker/crab/
  - python muticrab_MC2016_TauOfTTTT.py

- Job Recover
  - <crab kill -d> to kill the job and make sure the jobs are in killed status before you move to next step
  - <crab report -d> to create the notFinishedLumis.json
  - Feed this json file to multicrab_MC(DATA).py : 
     - set config.Data.lumiMask to this json file
     - see multicrab_DATA2018.py for example.
     - For convenience, I create a directory crab_dataInfo and move my crab task directory into it.



## Notice 
- Use < crab status -d > instead of TaskMonitors to check job information 
  < crab status -d > may show information contradicting TaskMonitors
  This is due to automatic splitting:
  https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3FAQ#What_is_the_Automatic_splitting
  

- Please change the absolute path of baseDir in multicrab_MC(DATA)2016(2017)(2018).py
- Please set outLFNDirBase to your DIR path at IHEP Tier 2 farm
  Highly suggest to create an empty DIR as output for the IHEP Tier 2 to Tier 3 Ntuple Handlings

- Always check HLT, make sure
    HLT you want is contained in TriggerSelector
    ifevtriggers in miniADO_RD(MC).py is set to true (false)

 
