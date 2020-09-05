# BSM Output Ntuples Docmentation
## Gobal tag
* DATA
  * 94X_dataRun2_v10
* MC
  * 102X_mcRun2_asymptotic_v8

## Electron
* selection 
  * pt > 5, |eta|<50
* new branch
    * patElectron_relIsoRhoEA_Update
      * please use this branch for the effictve area correction of PF isolation. 
      * The original one patElectron_relIsoRhoEA is not correct, I changed both the calculation and EA version.
    * 18 old electron ID(listed below) in  the output ntuples and the corresponding new names are both kept. They have the same content. Choose either that is of you convenience.  

old branches | new branches
------------ | ------------
patElectron_isPassVeto | patElectron_cutBasedElectronID_Fall17_94X_V2_veto
patElectron_isPassLoose | patElectron_cutBasedElectronID_Fall17_94X_V2_loose
patElectron_isPassMedium | patElectron_cutBasedElectronID_Fall17_94X_V2_medium
patElectron_isPassTight | patElectron_cutBasedElectronID_Fall17_94X_V2_tight
patElectron_isPassMvaIsowp80 | patElectron_mvaEleID_Fall17_iso_V2_wp80
patElectron_isPassMvanonIsowp80 | patElectron_mvaEleID_Fall17_noIso_V2_wp80
patElectron_isPassMvaIsowp90 | patElectron_mvaEleID_Fall17_iso_V2_wp90
patElectron_isPassMvanonIsowp90 | patElectron_mvaEleID_Fall17_noIso_V2_wp90
patElectron_isPassMvaIsowpLoose | patElectron_mvaEleID_Fall17_iso_V2_wpLoose
patElectron_isPassMvanonIsowpLoose | patElectron_mvaEleID_Fall17_noIso_V2_wpLoose
patElectron_mvaValue_nonIso | patElectron_ElectronMVAEstimatorRun2Fall17NoIsoV2Values
patElectron_mvaCategory_nonIso | patElectron_ElectronMVAEstimatorRun2Fall17NoIsoV2Categories
patElectron_mvaValue_Iso | patElectron_ElectronMVAEstimatorRun2Fall17IsoV2Values
patElectron_mvaCategory_Iso | patElectron_ElectronMVAEstimatorRun2Fall17IsoV2Categories
patElectron_isPassMvaHZZwpLoose | patElectron_mvaEleID_Spring16_HZZ_V1_wpLoose
patElectron_mvaValue_HZZ | patElectron_ElectronMVAEstimatorRun2Spring16HZZV1Values
patElectron_mvaCategory_HZZ | patElectron_ElectronMVAEstimatorRun2Spring16HZZV1Categories
patElectron_isPassHEEPId | patElectron_heepElectronID_HEEPV70

* existing branch
## Tau
* selection
  * pt>18, |eta|<5
* existing branches
  * tau are DeepTauv2p1
* new branches
  * Tau_decayMode
    * this one is missing in the old version
  
## JET
* selection
  * pt > 15
 
* updatation
  * update GQ tagger
    * the old Jet_axis1, Jet_ptD, Jet_mult are caculated manually
       * kept in ntuple anyway 
       * Jet_qg is replaced by Jet_qgLikelihood
    * Jet_axis2_fromQGtagger, Jet_mult_fromQGtagger, Jet_ptD_fromQGtager,Jet_qgLikelihood
       * these new branches are results from QGTagger.
       * use these rather than the old ones 
  * toptagger implementation 
    *  TopTagger_jet1Idx, TopTagger_jet2Idx, TopTagger_jet3Idx, TopTagger_type, TopTagger_discriminator
      * these new branches are resuts from toptagger
      * I modified the ED produceer in SUSY tagger to work on the newest output from miniAOD, which mean we take inputs of objects after the POG recommendation procedure.
      
# MET 
* selection 
* update implementation as recommended by POG
##  muon
* no modification or updating 
  


## HLT
* selection
  * no selection on HLT applied
* new branches
  * HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg;
   HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg;
   HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg;
   HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg;
   HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg;
   HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg;
   HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg;
  HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20;
   HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1;
   HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30;
  HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1;
  HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1;
 HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1;
  HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1;
  HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1;
   HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300;






