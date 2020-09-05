# BSM Output Ntuples Docmentation
## Gobal tag
* DATA
  * 94X_dataRun2_v10
* MC
  * 102X_mcRun2_asymptotic_v8

## Electron
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





