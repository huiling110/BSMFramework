#include "BSMFramework/BSM3G_TNT_Maker/interface/TriggerSelector.h"
#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream, std::stringbuf
TriggerSelector::TriggerSelector(std::string name, TTree* tree, bool debug, const pset& iConfig):baseTree(name,tree,debug){
  triggerBits_       = iConfig.getParameter<edm::InputTag>("bits");// bits  = cms.InputTag("TriggerResults","","HLT"),
  _maxtriggerversion = iConfig.getParameter<double>("maxtriggerversion");//20
  _is_data = iConfig.getParameter<bool>("is_data");
  _reHLT   = iConfig.getParameter<bool>("reHLT");
  SetBranches();
}
TriggerSelector::~TriggerSelector(){
  delete tree_;
}
void TriggerSelector::Fill(const edm::Event& iEvent, const edm::EventSetup& iSetup){
  if(debug_)    std::cout<<"getting met info"<<std::endl;
  Clear();//if the HLT is not contained then it is set to -9999 I think
  //?call TriggerSelector::Clear()300?
  if(_reHLT || _is_data){
    //Trigget paths 
    //?what is the point of resetHL
    edm::Handle<edm::TriggerResults> triggerBits;
    iEvent.getByLabel(triggerBits_, triggerBits);
    const edm::TriggerNames &trigNames = iEvent.triggerNames(*triggerBits);
    for(double tv=0.; tv<=_maxtriggerversion; tv++){
        //?what is maxtriggerversion doing?
        //try for different versions of HLT I think.
      char buffer[20]; sprintf(buffer,"%g",tv);//Write formatted data to string.g:  Use the shortest representation: %e or %f
      //jet
      uint HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v(trigNames.triggerIndex(("HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v"+string(buffer)).c_str()));/*{{{*/
      if(HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v<triggerBits->size()) HLT_PFHT650_WideJetMJJ900DEtaJJ1p5 = triggerBits->accept(HLT_PFHT650_WideJetMJJ900DEtaJJ1p5_v);
      uint HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v(trigNames.triggerIndex(("HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v"+string(buffer)).c_str()));
      if(HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v<triggerBits->size()) HLT_PFHT650_WideJetMJJ950DEtaJJ1p5 = triggerBits->accept(HLT_PFHT650_WideJetMJJ950DEtaJJ1p5_v);
      uint HLT_PFHT800_v(trigNames.triggerIndex(("HLT_PFHT800_v"+string(buffer)).c_str()));
      if(HLT_PFHT800_v<triggerBits->size()) HLT_PFHT800 = triggerBits->accept(HLT_PFHT800_v);
      uint HLT_PFHT900_v(trigNames.triggerIndex(("HLT_PFHT900_v"+string(buffer)).c_str()));
      if(HLT_PFHT900_v<triggerBits->size()) HLT_PFHT900 = triggerBits->accept(HLT_PFHT900_v);
      uint HLT_PFJet450_v(trigNames.triggerIndex(("HLT_PFJet450_v"+string(buffer)).c_str()));
      if(HLT_PFJet450_v<triggerBits->size()) HLT_PFJet450 = triggerBits->accept(HLT_PFJet450_v);
      uint HLT_PFJet500_v(trigNames.triggerIndex(("HLT_PFJet500_v"+string(buffer)).c_str()));
      if(HLT_PFJet500_v<triggerBits->size()) HLT_PFJet500 = triggerBits->accept(HLT_PFJet500_v);
      uint HLT_AK8PFJet450_v(trigNames.triggerIndex(("HLT_AK8PFJet450_v"+string(buffer)).c_str()));
      if(HLT_AK8PFJet450_v<triggerBits->size()) HLT_AK8PFJet450 = triggerBits->accept(HLT_AK8PFJet450_v);
      uint HLT_AK8PFJet500_v(trigNames.triggerIndex(("HLT_AK8PFJet500_v"+string(buffer)).c_str()));
      if(HLT_AK8PFJet500_v<triggerBits->size()) HLT_AK8PFJet500 = triggerBits->accept(HLT_AK8PFJet500_v);
      uint HLT_AK8PFJet360_TrimMass30_v(trigNames.triggerIndex(("HLT_AK8PFJet360_TrimMass30_v"+string(buffer)).c_str()));
      if(HLT_AK8PFJet360_TrimMass30_v<triggerBits->size()) HLT_AK8PFJet360_TrimMass30 = triggerBits->accept(HLT_AK8PFJet360_TrimMass30_v);
      uint HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v(trigNames.triggerIndex(("HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v"+string(buffer)).c_str()));
      if(HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v<triggerBits->size()) HLT_AK8PFHT700_TrimR0p1PT0p03Mass50 = triggerBits->accept(HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v);
      //Electron
      uint HLT_Ele35_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele35_WPTight_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele35_WPTight_Gsf_v<triggerBits->size()) HLT_Ele35_WPTight_Gsf = triggerBits->accept(HLT_Ele35_WPTight_Gsf_v);
      uint HLT_Ele32_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele32_WPTight_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele32_WPTight_Gsf_v<triggerBits->size()) HLT_Ele32_WPTight_Gsf = triggerBits->accept(HLT_Ele32_WPTight_Gsf_v);
      uint HLT_Ele27_eta2p1_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele27_eta2p1_WPTight_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele27_eta2p1_WPTight_Gsf_v<triggerBits->size()) HLT_Ele27_eta2p1_WPTight_Gsf = triggerBits->accept(HLT_Ele27_eta2p1_WPTight_Gsf_v);
      uint HLT_Ele27_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele27_WPTight_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele27_WPTight_Gsf_v<triggerBits->size()) HLT_Ele27_WPTight_Gsf = triggerBits->accept(HLT_Ele27_WPTight_Gsf_v);
      uint HLT_Ele25_eta2p1_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele25_eta2p1_WPTight_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele25_eta2p1_WPTight_Gsf_v<triggerBits->size()) HLT_Ele25_eta2p1_WPTight_Gsf = triggerBits->accept(HLT_Ele25_eta2p1_WPTight_Gsf_v);
      uint HLT_Ele115_CaloIdVT_GsfTrkIdT_v(trigNames.triggerIndex(("HLT_Ele115_CaloIdVT_GsfTrkIdT_v"+string(buffer)).c_str()));
      if(HLT_Ele115_CaloIdVT_GsfTrkIdT_v<triggerBits->size()) HLT_Ele115_CaloIdVT_GsfTrkIdT = triggerBits->accept(HLT_Ele115_CaloIdVT_GsfTrkIdT_v);
      uint HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v(trigNames.triggerIndex(("HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v"+string(buffer)).c_str()));
      if(HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v<triggerBits->size()) HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf = triggerBits->accept(HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf_v);
      uint HLT_DoubleEle33_CaloIdL_MW_v(trigNames.triggerIndex(("HLT_DoubleEle33_CaloIdL_MW_v"+string(buffer)).c_str()));
      if(HLT_DoubleEle33_CaloIdL_MW_v<triggerBits->size()) HLT_DoubleEle33_CaloIdL_MW = triggerBits->accept(HLT_DoubleEle33_CaloIdL_MW_v);
      uint HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v(trigNames.triggerIndex(("HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v"+string(buffer)).c_str()));
      if(HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v<triggerBits->size()) HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW = triggerBits->accept(HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v);
      uint HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v(trigNames.triggerIndex(("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v<triggerBits->size()) HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = triggerBits->accept(HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v);
      uint HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v(trigNames.triggerIndex(("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v"+string(buffer)).c_str()));
      if(HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v<triggerBits->size()) HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL = triggerBits->accept(HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v);
      //Muon
      uint HLT_IsoMu27_v(trigNames.triggerIndex(("HLT_IsoMu27_v"+string(buffer)).c_str()));
      if(HLT_IsoMu27_v<triggerBits->size()) HLT_IsoMu27 = triggerBits->accept(HLT_IsoMu27_v);
      uint HLT_IsoMu22_v(trigNames.triggerIndex(("HLT_IsoMu22_v"+string(buffer)).c_str()));
      if(HLT_IsoMu22_v<triggerBits->size()) HLT_IsoMu22 = triggerBits->accept(HLT_IsoMu22_v);
      uint HLT_IsoTkMu22_v(trigNames.triggerIndex(("HLT_IsoTkMu22_v"+string(buffer)).c_str()));
      if(HLT_IsoTkMu22_v<triggerBits->size()) HLT_IsoTkMu22 = triggerBits->accept(HLT_IsoTkMu22_v);
      uint HLT_IsoMu24_v(trigNames.triggerIndex(("HLT_IsoMu24_v"+string(buffer)).c_str()));
      if(HLT_IsoMu24_v<triggerBits->size()) HLT_IsoMu24 = triggerBits->accept(HLT_IsoMu24_v);
      uint HLT_IsoTkMu24_v(trigNames.triggerIndex(("HLT_IsoTkMu24_v"+string(buffer)).c_str()));
      if(HLT_IsoTkMu24_v<triggerBits->size()) HLT_IsoTkMu24 = triggerBits->accept(HLT_IsoTkMu24_v);
      uint HLT_IsoMu22_eta2p1_v(trigNames.triggerIndex(("HLT_IsoMu22_eta2p1_v"+string(buffer)).c_str()));
      if(HLT_IsoMu22_eta2p1_v<triggerBits->size()) HLT_IsoMu22_eta2p1 = triggerBits->accept(HLT_IsoMu22_eta2p1_v);
      uint HLT_IsoTkMu22_eta2p1_v(trigNames.triggerIndex(("HLT_IsoTkMu22_eta2p1_v"+string(buffer)).c_str()));
      if(HLT_IsoTkMu22_eta2p1_v<triggerBits->size()) HLT_IsoTkMu22_eta2p1 = triggerBits->accept(HLT_IsoTkMu22_eta2p1_v);
      uint HLT_Mu50_v(trigNames.triggerIndex(("HLT_Mu50_v"+string(buffer)).c_str()));
      if(HLT_Mu50_v<triggerBits->size()) HLT_Mu50 = triggerBits->accept(HLT_Mu50_v);
      uint HLT_TkMu50_v(trigNames.triggerIndex(("HLT_TkMu50_v"+string(buffer)).c_str()));
      if(HLT_TkMu50_v<triggerBits->size()) HLT_TkMu50 = triggerBits->accept(HLT_TkMu50_v);
      uint HLT_DoubleMu33NoFiltersNoVtx_v(trigNames.triggerIndex(("HLT_DoubleMu33NoFiltersNoVtx_v"+string(buffer)).c_str()));
      if(HLT_DoubleMu33NoFiltersNoVtx_v<triggerBits->size()) HLT_DoubleMu33NoFiltersNoVtx = triggerBits->accept(HLT_DoubleMu33NoFiltersNoVtx_v);
      uint HLT_DoubleMu23NoFiltersNoVtxDisplaced_v(trigNames.triggerIndex(("HLT_DoubleMu23NoFiltersNoVtxDisplaced_v"+string(buffer)).c_str()));
      if(HLT_DoubleMu23NoFiltersNoVtxDisplaced_v<triggerBits->size()) HLT_DoubleMu23NoFiltersNoVtxDisplaced = triggerBits->accept(HLT_DoubleMu23NoFiltersNoVtxDisplaced_v);
      uint HLT_Mu30_TkMu11_v(trigNames.triggerIndex(("HLT_Mu30_TkMu11_v"+string(buffer)).c_str()));
      if(HLT_Mu30_TkMu11_v<triggerBits->size()) HLT_Mu30_TkMu11 = triggerBits->accept(HLT_Mu30_TkMu11_v);
      uint HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL = triggerBits->accept(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v);
      uint HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ = triggerBits->accept(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v);
      uint HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8 = triggerBits->accept(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v);
      uint HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v(trigNames.triggerIndex(("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v"+string(buffer)).c_str()));
      if(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v<triggerBits->size()) HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL = triggerBits->accept(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v);
      uint HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v(trigNames.triggerIndex(("HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v<triggerBits->size()) HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ = triggerBits->accept(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v);
      uint HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v(trigNames.triggerIndex(("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"+string(buffer)).c_str()));
      if(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v<triggerBits->size()) HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL = triggerBits->accept(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v);
      uint HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v(trigNames.triggerIndex(("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v<triggerBits->size()) HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = triggerBits->accept(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v);
      uint HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v(trigNames.triggerIndex(("HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v<triggerBits->size()) HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ = triggerBits->accept(HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v);
      uint HLT_TripleMu_12_10_5_v(trigNames.triggerIndex(("HLT_TripleMu_12_10_5_v"+string(buffer)).c_str()));
      if(HLT_TripleMu_12_10_5_v<triggerBits->size()) HLT_TripleMu_12_10_5 = triggerBits->accept(HLT_TripleMu_12_10_5_v);
      uint HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v(trigNames.triggerIndex(("HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v"+string(buffer)).c_str()));
      if(HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v<triggerBits->size()) HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ = triggerBits->accept(HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v);
      uint HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v(trigNames.triggerIndex(("HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v"+string(buffer)).c_str()));
      if(HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v<triggerBits->size()) HLT_Mu8_DiEle12_CaloIdL_TrackIdL = triggerBits->accept(HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v);
      uint HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v(trigNames.triggerIndex(("HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v"+string(buffer)).c_str()));
      if(HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v<triggerBits->size()) HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL = triggerBits->accept(HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v);
      uint HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v(trigNames.triggerIndex(("HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v<triggerBits->size()) HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = triggerBits->accept(HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v);
      uint HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL = triggerBits->accept(HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v);
      uint HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = triggerBits->accept(HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v);
      uint HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v(trigNames.triggerIndex(("HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v"+string(buffer)).c_str()));
      if(HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v<triggerBits->size()) HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL = triggerBits->accept(HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v);
      uint HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v(trigNames.triggerIndex(("HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v<triggerBits->size()) HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = triggerBits->accept(HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v);
      uint HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 = triggerBits->accept(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v);
      uint HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v(trigNames.triggerIndex(("HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v"+string(buffer)).c_str()));
      if(HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v<triggerBits->size()) HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL = triggerBits->accept(HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL_v);
      uint HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v(trigNames.triggerIndex(("HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v"+string(buffer)).c_str()));
      if(HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v<triggerBits->size()) HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL = triggerBits->accept(HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v);
      uint HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v(trigNames.triggerIndex(("HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v"+string(buffer)).c_str()));
      if(HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v<triggerBits->size()) HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL = triggerBits->accept(HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v);
      uint HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v(trigNames.triggerIndex(("HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v<triggerBits->size()) HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ = triggerBits->accept(HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v);
      uint HLT_TripleMu_10_5_5_DZ_v(trigNames.triggerIndex(("HLT_TripleMu_10_5_5_DZ_v"+string(buffer)).c_str()));
      if(HLT_TripleMu_10_5_5_DZ_v<triggerBits->size()) HLT_TripleMu_10_5_5_DZ = triggerBits->accept(HLT_TripleMu_10_5_5_DZ_v);
      uint HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v(trigNames.triggerIndex(("HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v"+string(buffer)).c_str()));
      if(HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v<triggerBits->size()) HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ = triggerBits->accept(HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ_v);
      uint HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v(trigNames.triggerIndex(("HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v"+string(buffer)).c_str()));
      if(HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v<triggerBits->size()) HLT_DiMu9_Ele9_CaloIdL_TrackIdL = triggerBits->accept(HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v);
      uint HLT_Ele27_eta2p1_WPLoose_Gsf_v(trigNames.triggerIndex(("HLT_Ele27_eta2p1_WPLoose_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele27_eta2p1_WPLoose_Gsf_v<triggerBits->size()) HLT_Ele27_eta2p1_WPLoose_Gsf = triggerBits->accept(HLT_Ele27_eta2p1_WPLoose_Gsf_v);
      uint HLT_Ele32_WPTight_Gsf_L1DoubleEG_v(trigNames.triggerIndex(("HLT_Ele32_WPTight_Gsf_L1DoubleEG_v"+string(buffer)).c_str()));
      if(HLT_Ele32_WPTight_Gsf_L1DoubleEG_v<triggerBits->size()) HLT_Ele32_WPTight_Gsf_L1DoubleEG = triggerBits->accept(HLT_Ele32_WPTight_Gsf_L1DoubleEG_v);
      uint HLT_Photon200_v(trigNames.triggerIndex(("HLT_Photon200_v"+string(buffer)).c_str()));
      if(HLT_Photon200_v<triggerBits->size()) HLT_Photon200 = triggerBits->accept(HLT_Photon200_v);
      uint HLT_Photon175_v(trigNames.triggerIndex(("HLT_Photon175_v"+string(buffer)).c_str()));
      if(HLT_Photon175_v<triggerBits->size()) HLT_Photon175 = triggerBits->accept(HLT_Photon175_v);
      uint HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v(trigNames.triggerIndex(("HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v"+string(buffer)).c_str()));
      if(HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v<triggerBits->size()) HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 = triggerBits->accept(HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165_v);
      uint HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v(trigNames.triggerIndex(("HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v"+string(buffer)).c_str()));
      if(HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v<triggerBits->size()) HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50 = triggerBits->accept(HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50_v);
      uint HLT_Ele27_WP85_Gsf_v(trigNames.triggerIndex(("HLT_Ele27_WP85_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele27_WP85_Gsf_v<triggerBits->size()) HLT_Ele27_WP85_Gsf = triggerBits->accept(HLT_Ele27_WP85_Gsf_v);
      //add
      uint HLT_Ele32_eta2p1_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele32_eta2p1_WPTight_Gsf_v"+string(buffer)).c_str()));
      if(HLT_Ele32_eta2p1_WPTight_Gsf_v<triggerBits->size()) HLT_Ele32_eta2p1_WPTight_Gsf = triggerBits->accept(HLT_Ele32_eta2p1_WPTight_Gsf_v);
  //    uint HLT_Ele27_WPTight_Gsf_v(trigNames.triggerIndex(("HLT_Ele27_WPTight_Gsf_v"+string(buffer)).c_str()));
//      if(HLT_Ele27_WPTight_Gsf_v<triggerBits->size()) HLT_Ele27_WPTight_Gsf = triggerBits->accept(HLT_Ele27_WPTight_Gsf_v);
      uint HLT_DoubleMu8_Mass8_PFHT300_v(trigNames.triggerIndex(("HLT_DoubleMu8_Mass8_PFHT300_v"+string(buffer)).c_str()));
      if(HLT_DoubleMu8_Mass8_PFHT300_v<triggerBits->size()) HLT_DoubleMu8_Mass8_PFHT300 = triggerBits->accept(HLT_DoubleMu8_Mass8_PFHT300_v);
      uint HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v(trigNames.triggerIndex(("HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v"+string(buffer)).c_str()));
      if(HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v<triggerBits->size())  HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300 = triggerBits->accept(HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300_v);
      uint HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v(trigNames.triggerIndex(("HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v"+string(buffer)).c_str()));
      if(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v<triggerBits->size()) HLT_PFHT400_SixJet30_DoubleBTagCSV_p056 = triggerBits->accept(HLT_PFHT400_SixJet30_DoubleBTagCSV_p056_v);
      uint HLT_PFHT450_SixJet40_BTagCSV_p056_v(trigNames.triggerIndex(("HLT_PFHT450_SixJet40_BTagCSV_p056_v"+string(buffer)).c_str()));
      if(HLT_PFHT450_SixJet40_BTagCSV_p056_v<triggerBits->size())HLT_PFHT450_SixJet40_BTagCSV_p056  = triggerBits->accept(HLT_PFHT450_SixJet40_BTagCSV_p056_v);
      uint HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg = triggerBits->accept(HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg_v);
      uint HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg = triggerBits->accept(HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg_v);
      uint HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg = triggerBits->accept(HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v);
      uint HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg = triggerBits->accept(HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v);
      uint HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg = triggerBits->accept(HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v);
      uint HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg = triggerBits->accept(HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v);
      uint HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v(trigNames.triggerIndex(("HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v"+string(buffer)).c_str()));
      if(HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v<triggerBits->size()) HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg = triggerBits->accept(HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v);
      uint HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v(trigNames.triggerIndex(("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v"+string(buffer)).c_str()));
      if(HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v<triggerBits->size()) HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20 = triggerBits->accept(HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v);
      uint HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v(trigNames.triggerIndex(("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v"+string(buffer)).c_str()));
      if(HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v<triggerBits->size()) HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1 = triggerBits->accept(HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v);
      uint HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v(trigNames.triggerIndex(("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v"+string(buffer)).c_str()));
      if(HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v<triggerBits->size()) HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30 = triggerBits->accept(HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v);
      uint HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v(trigNames.triggerIndex(("HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v"+string(buffer)).c_str()));
      if(HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v<triggerBits->size()) HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1 = triggerBits->accept(HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v);
      uint HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v(trigNames.triggerIndex(("HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v"+string(buffer)).c_str()));
      if(HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v<triggerBits->size()) HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1 = triggerBits->accept(HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v);
      uint HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v(trigNames.triggerIndex(("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v"+string(buffer)).c_str()));
      if(HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v<triggerBits->size()) HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1 = triggerBits->accept(HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v);
      uint HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v(trigNames.triggerIndex(("HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v"+string(buffer)).c_str()));
      if(HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v<triggerBits->size()) HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1 = triggerBits->accept(HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v);
      uint HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v(trigNames.triggerIndex(("HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v"+string(buffer)).c_str()));
      if(HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v<triggerBits->size()) HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1 = triggerBits->accept(HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v);
      uint HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v(trigNames.triggerIndex(("HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v"+string(buffer)).c_str()));
      if(HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v<triggerBits->size()) HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300 = triggerBits->accept(HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300_v);
//      uint _v(trigNames.triggerIndex(("_v"+string(buffer)).c_str()));
//      if(_v<triggerBits->size())  = triggerBits->accept(_v);



      /*}}}*/
    }
  }
  else {
    //?why set HLT to 1 here? kind of dangerous? 
    HLT_PFHT650_WideJetMJJ900DEtaJJ1p5 = 1;/*{{{*/
    HLT_PFHT650_WideJetMJJ950DEtaJJ1p5 = 1;
    HLT_PFHT800 = 1;
    HLT_PFHT900 = 1;
    HLT_PFJet450 = 1;
    HLT_PFJet500 = 1;
    HLT_AK8PFJet450 = 1;
    HLT_AK8PFJet500 = 1;
    HLT_AK8PFJet360_TrimMass30 = 1;
    HLT_AK8PFHT700_TrimR0p1PT0p03Mass50 = 1;
    HLT_Ele27_eta2p1_WPTight_Gsf = 1;
    HLT_Ele27_WPTight_Gsf = 1;
    HLT_Ele25_eta2p1_WPTight_Gsf = 1;
    HLT_Ele115_CaloIdVT_GsfTrkIdT = 1;
    HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf = 1;
    HLT_DoubleEle33_CaloIdL_MW = 1;
    HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW = 1;
    HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = 1;
    HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL = 1;
    HLT_IsoMu22 = 1;
    HLT_IsoTkMu22 = 1;
    HLT_IsoMu24 = 1;
    HLT_IsoTkMu24 = 1;
    HLT_IsoMu22_eta2p1 = 1;
    HLT_IsoTkMu22_eta2p1 = 1;
    HLT_Mu50 = 1;
    HLT_TkMu50 = 1;
    HLT_DoubleMu33NoFiltersNoVtx = 1;
    HLT_DoubleMu23NoFiltersNoVtxDisplaced = 1;
    HLT_Mu30_TkMu11 = 1;
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ = 1;
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8 = 1;
    HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL = 1;
    HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ = 1;
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL = 1;
    HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = 1;
    HLT_Ele32_WPTight_Gsf = 1;
    HLT_Ele35_WPTight_Gsf = 1;
    HLT_IsoMu27 = 1;
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL = 1;
    HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ = 1;
    HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL = 1;
    HLT_Mu8_DiEle12_CaloIdL_TrackIdL = 1;
    HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ = 1;
    HLT_TripleMu_12_10_5 = 1;
    HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = 1;
    HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL = 1;
    HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = 1;
    HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL = 1;
    HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = 1;
    HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 = 1;
    HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL = 1;
    HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL = 1;
    HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL = 1;
    HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ = 1;
    HLT_TripleMu_10_5_5_DZ = 1;
    HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ = 1;
    HLT_DiMu9_Ele9_CaloIdL_TrackIdL = 1;
    HLT_Ele27_eta2p1_WPLoose_Gsf = 1;
    HLT_Ele32_WPTight_Gsf_L1DoubleEG = 1;
    HLT_Photon200 = 1;
    HLT_Photon175 = 1;
    HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 = 1;
    HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50 = 1;
    HLT_Ele27_WP85_Gsf = 1;
    //add
    HLT_Ele32_eta2p1_WPTight_Gsf = 1;
//    HLT_Ele27_WPTight_Gsf = 1;
    HLT_DoubleMu8_Mass8_PFHT300 = 1;
    HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300 = 1;
    HLT_PFHT400_SixJet30_DoubleBTagCSV_p056 = 1;
    HLT_PFHT450_SixJet40_BTagCSV_p056 = 1;
    HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg = 1;
    HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg = 1;
    HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg = 1;
    HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg = 1;
    HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg = 1;
    HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg = 1;
    HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg = 1;
    HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20 = 1;
    HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1 = 1;
    HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30 = 1;
    HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1 = 1;
    HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1 = 1;
    HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1 = 1;
    HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1 = 1;
    HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1 = 1;
    HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300 = 1;
    /*}}}*/
  }
}

void TriggerSelector::SetBranches(){
  if(debug_)    std::cout<<"setting branches: calling AddBranch of baseTree"<<std::endl;
  AddBranch(&HLT_PFHT650_WideJetMJJ900DEtaJJ1p5       ,"HLT_PFHT650_WideJetMJJ900DEtaJJ1p5");/*{{{*/
  AddBranch(&HLT_PFHT650_WideJetMJJ950DEtaJJ1p5       ,"HLT_PFHT650_WideJetMJJ950DEtaJJ1p5");
  AddBranch(&HLT_PFHT800                              ,"HLT_PFHT800");
  AddBranch(&HLT_PFHT900                              ,"HLT_PFHT900");
  AddBranch(&HLT_PFJet450                             ,"HLT_PFJet450");
  AddBranch(&HLT_PFJet500                             ,"HLT_PFJet500");
  AddBranch(&HLT_AK8PFJet450                          ,"HLT_AK8PFJet450");
  AddBranch(&HLT_AK8PFJet500                          ,"HLT_AK8PFJet500");
  AddBranch(&HLT_AK8PFJet360_TrimMass30               ,"HLT_AK8PFJet360_TrimMass30");
  AddBranch(&HLT_AK8PFHT700_TrimR0p1PT0p03Mass50      ,"HLT_AK8PFHT700_TrimR0p1PT0p03Mass50");
  AddBranch(&HLT_Ele27_eta2p1_WPTight_Gsf             ,"HLT_Ele27_eta2p1_WPTight_Gsf");
  AddBranch(&HLT_Ele27_WPTight_Gsf              ,"HLT_Ele27_WPTight_Gsf");
  AddBranch(&HLT_Ele25_eta2p1_WPTight_Gsf          ,"HLT_Ele25_eta2p1_WPTight_Gsf");
  AddBranch(&HLT_Ele115_CaloIdVT_GsfTrkIdT          ,"HLT_Ele115_CaloIdVT_GsfTrkIdT");
  AddBranch(&HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf    ,"HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf");
  AddBranch(&HLT_DoubleEle33_CaloIdL_MW              ,"HLT_DoubleEle33_CaloIdL_MW");
  AddBranch(&HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW    ,"HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW");
  AddBranch(&HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ,"HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ");
  AddBranch(&HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL,"HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL");
  AddBranch(&HLT_IsoMu22                  ,"HLT_IsoMu22");
  AddBranch(&HLT_IsoTkMu22                      ,"HLT_IsoTkMu22");
  AddBranch(&HLT_IsoMu24                  ,"HLT_IsoMu24");
  AddBranch(&HLT_IsoTkMu24                      ,"HLT_IsoTkMu24");
  AddBranch(&HLT_IsoMu22_eta2p1                  ,"HLT_IsoMu22_eta2p1");
  AddBranch(&HLT_IsoTkMu22_eta2p1              ,"HLT_IsoTkMu22_eta2p1");
  AddBranch(&HLT_Mu50                      ,"HLT_Mu50");
  AddBranch(&HLT_TkMu50                      ,"HLT_TkMu50");
  AddBranch(&HLT_DoubleMu33NoFiltersNoVtx          ,"HLT_DoubleMu33NoFiltersNoVtx");
  AddBranch(&HLT_DoubleMu23NoFiltersNoVtxDisplaced    ,"HLT_DoubleMu23NoFiltersNoVtxDisplaced");
  AddBranch(&HLT_Mu30_TkMu11                  ,"HLT_Mu30_TkMu11");
  AddBranch(&HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ      ,"HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ");
  AddBranch(&HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8      ,"HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8");
  AddBranch(&HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL      ,"HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL");
  AddBranch(&HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ      ,"HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ");
  AddBranch(&HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL      ,"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL");
  AddBranch(&HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ      ,"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ");
  AddBranch(&HLT_Ele32_WPTight_Gsf                      ,"HLT_Ele32_WPTight_Gsf");
  AddBranch(&HLT_Ele35_WPTight_Gsf                      ,"HLT_Ele35_WPTight_Gsf");
  AddBranch(&HLT_IsoMu27                      ,"HLT_IsoMu27");
  AddBranch(&HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL                      ,"HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL");
  AddBranch(&HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ                      ,"HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ");
  AddBranch(&HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL                      ,"HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL");
  AddBranch(&HLT_Mu8_DiEle12_CaloIdL_TrackIdL                      ,"HLT_Mu8_DiEle12_CaloIdL_TrackIdL");
  AddBranch(&HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ                      ,"HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ");
  AddBranch(&HLT_TripleMu_12_10_5                      ,"HLT_TripleMu_12_10_5");
  AddBranch(&HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ                      ,"HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ");
  AddBranch(&HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL                      ,"HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL");
  AddBranch(&HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ                      ,"HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ");
  AddBranch(&HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL                      ,"HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL");
  AddBranch(&HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ                      ,"HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ");
  AddBranch(&HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8                      ,"HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8");
  AddBranch(&HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL                      ,"HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL");
  AddBranch(&HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL                      ,"HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL");
  AddBranch(&HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL                      ,"HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL");
  AddBranch(&HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ                      ,"HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ");
  AddBranch(&HLT_TripleMu_10_5_5_DZ                      ,"HLT_TripleMu_10_5_5_DZ");
  AddBranch(&HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ                      ,"HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ");
  AddBranch(&HLT_DiMu9_Ele9_CaloIdL_TrackIdL                      ,"HLT_DiMu9_Ele9_CaloIdL_TrackIdL");
  AddBranch(&HLT_Ele27_eta2p1_WPLoose_Gsf                      ,"HLT_Ele27_eta2p1_WPLoose_Gsf");
  AddBranch(&HLT_Ele32_WPTight_Gsf_L1DoubleEG                      ,"HLT_Ele32_WPTight_Gsf_L1DoubleEG");
  AddBranch(&HLT_Photon200                      ,"HLT_Photon200");
  AddBranch(&HLT_Photon175                      ,"HLT_Photon175");
  AddBranch(&HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165                      ,"HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165");
  AddBranch(&HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50                      ,"HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50");
  AddBranch(&HLT_Ele27_WP85_Gsf                      ,"HLT_Ele27_WP85_Gsf");
  //add
  AddBranch(&HLT_Ele32_eta2p1_WPTight_Gsf                      ,"HLT_Ele32_eta2p1_WPTight_Gsf");
//  AddBranch(&HLT_Ele27_WPTight_Gsf                      ,"HLT_Ele27_WPTight_Gsf");//not in datadaset//HLT_Ele27_WPTight_Gsf
  AddBranch(&HLT_DoubleMu8_Mass8_PFHT300                      ,"HLT_DoubleMu8_Mass8_PFHT300");
  AddBranch(&HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300                      ,"HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300");
//  AddBranch(&HLT_PFHT300_SixJet30_DoubleBTagCSV_p056                      ,"HLT_PFHT300_SixJet30_DoubleBTagCSV_p056");
  AddBranch(&HLT_PFHT450_SixJet40_BTagCSV_p056                      ,"HLT_PFHT450_SixJet40_BTagCSV_p056");
  AddBranch(&HLT_PFHT400_SixJet30_DoubleBTagCSV_p056                      ,"HLT_PFHT400_SixJet30_DoubleBTagCSV_p056");
  AddBranch(&HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg                      ,"HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg");
  AddBranch(&HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg                      ,"HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg");
  AddBranch(&HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg                      ,"HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg");
  AddBranch(&HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg                      ,"HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg");
  AddBranch(&HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg                      ,"HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg");
  AddBranch(&HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg                      ,"HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg");
  AddBranch(&HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg                      ,"HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg");
  AddBranch(&HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20                      ,"HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20");
  AddBranch(&HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1                      ,"HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1");
  AddBranch(&HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30                      ,"HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30");
  AddBranch(&HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1                      ,"HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1");
  AddBranch(&HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1                      ,"HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1");
  AddBranch(&HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1                      ,"HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1");
  AddBranch(&HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1                      ,"HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1");
  AddBranch(&HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1                      ,"HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1");
  AddBranch(&HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300                      ,"HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300");

  if(debug_)    std::cout<<"set branches"<<std::endl;
}/*}}}*/

void TriggerSelector::Clear(){
  HLT_PFHT650_WideJetMJJ900DEtaJJ1p5 = -9999;/*{{{*/
  HLT_PFHT650_WideJetMJJ950DEtaJJ1p5 = -9999;
  HLT_PFHT800 = -9999;
  HLT_PFHT900 = -9999;
  HLT_PFJet450 = -9999;
  HLT_PFJet500 = -9999;
  HLT_AK8PFJet450 = -9999;
  HLT_AK8PFJet500 = -9999;
  HLT_AK8PFJet360_TrimMass30 = -9999;
  HLT_AK8PFHT700_TrimR0p1PT0p03Mass50 = -9999;
  HLT_Ele27_eta2p1_WPTight_Gsf = -9999;
  HLT_Ele27_WPTight_Gsf = -9999;
  HLT_Ele25_eta2p1_WPTight_Gsf = -9999;
  HLT_Ele115_CaloIdVT_GsfTrkIdT = -9999;
  HLT_DoubleEle24_22_eta2p1_WPLoose_Gsf = -9999;
  HLT_DoubleEle33_CaloIdL_MW = -9999;
  HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW = -9999;
  HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = -9999;
  HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL = -9999;
  HLT_IsoMu22 = -9999;
  HLT_IsoTkMu22 = -9999;
  HLT_IsoMu24 = -9999;
  HLT_IsoTkMu24 = -9999;
  HLT_IsoMu22_eta2p1 = -9999;
  HLT_IsoTkMu22_eta2p1 = -9999;
  HLT_Mu50 = -9999;
  HLT_TkMu50 = -9999;
  HLT_DoubleMu33NoFiltersNoVtx = -9999;
  HLT_DoubleMu23NoFiltersNoVtxDisplaced = -9999;
  HLT_Mu30_TkMu11 = -9999;
  HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ = -9999;
  HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8 = -9999;
  HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL = -9999;
  HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ = -9999;
  HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL = -9999;
  HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = -9999;
  HLT_Ele32_WPTight_Gsf = -9999;
  HLT_Ele35_WPTight_Gsf = -9999;
  HLT_IsoMu27 = -9999;
  HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL = -9999;
  HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ = -9999;
  HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL = -9999;
  HLT_Mu8_DiEle12_CaloIdL_TrackIdL = -9999;
  HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ = -9999;
  HLT_TripleMu_12_10_5 = -9999;
  HLT_Ele17_Ele12_CaloIdL_TrackIdL_IsoVL_DZ = -9999;
  HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL = -9999;
  HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = -9999;
  HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL = -9999;
  HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ = -9999;
  HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 = -9999;
  HLT_Mu8_TrkIsoVVL_Ele17_CaloIdL_TrackIdL_IsoVL = -9999;
  HLT_Mu17_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL = -9999;
  HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL = -9999;
  HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ = -9999;
  HLT_TripleMu_10_5_5_DZ = -9999;
  HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ = -9999;
  HLT_Ele27_eta2p1_WPLoose_Gsf = -9999;
  HLT_Ele32_WPTight_Gsf_L1DoubleEG = -9999;
  HLT_Ele50_CaloIdVT_GsfTrkIdT_PFJet165 = -9999;
  HLT_Ele45_CaloIdVT_GsfTrkIdT_PFJet200_PFJet50 = -9999;
  HLT_Photon200 = -9999;
  HLT_Photon175 = -9999;
  HLT_Ele27_WP85_Gsf = -9999;
  //add for TTTT
  HLT_Ele32_eta2p1_WPTight_Gsf = -9999;//for single lepton
//  HLT_Ele27_WPTight_Gsf = -9999;
  HLT_DoubleMu8_Mass8_PFHT300 = -9999;
  HLT_DoubleEle8_CaloIdM_TrackIdM_Mass8_PFHT300 = -9999;
  HLT_PFHT400_SixJet30_DoubleBTagCSV_p056 = -9999;
  HLT_PFHT450_SixJet40_BTagCSV_p056 = -9999;
  HLT_DoubleMediumIsoPFTau35_Trk1_eta2p1_Reg = -9999;
  HLT_DoubleMediumCombinedIsoPFTau35_Trk1_eta2p1_Reg = -9999;
  HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg = -9999;
  HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg = -9999;
  HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg = -9999;
  HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg = -9999;
  HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg = -9999;
  HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20 = -9999;
  HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1 = -9999;
  HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30 = -9999;
  HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1 = -9999;
  HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1 = -9999;
  HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1 = -9999;
  HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1 = -9999;
  HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1 = -9999;
  HLT_Mu8_Ele8_CaloIdM_TrackIdM_Mass8_PFHT300 = -9999;
}/*}}}*/

void TriggerSelector::startTrigger(edm::EventSetup const& iSetup, edm::Run const & iRun){
  bool changed(true);
  //if(_is_data) hltConfig_.init(iRun,iSetup,"HLT",changed);
  //else         hltConfig_.init(iRun,iSetup,"HLT2",changed);
  hltConfig_.init(iRun,iSetup,"HLT",changed);
  //?what is  hltConfig_?
}
