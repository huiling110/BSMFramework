#include "BSMFramework/BSM3G_TNT_Maker/interface/BSM3G_TNT_Maker.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
//Trigger
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include <memory>
#include <string>       // std::string
#include <iostream>     // std::cout
#include <sstream>      // std::stringstream, std::stringbuf
BSM3G_TNT_Maker::BSM3G_TNT_Maker(const edm::ParameterSet& iConfig):
  triggerBits_(consumes<edm::TriggerResults>(iConfig.getParameter<edm::InputTag>("bits"))),//bits = cms.InputTag("TriggerResults","","HLT")
  muon_h_(consumes<edm::View<pat::Muon> >(iConfig.getParameter<edm::InputTag>("muons"))),
  electron_pat_(consumes<edm::View<pat::Electron> >(iConfig.getParameter<edm::InputTag>("patElectrons"))),
  //now do what ever initialization is needed
  MaxN(200)
    //?what is MaxN?
{
  _Muon_pt_min        = iConfig.getParameter<double>("Muon_pt_min");
  _Muon_eta_max       = iConfig.getParameter<double>("Muon_eta_max");
  _patElectron_pt_min  = iConfig.getParameter<double>("patElectron_pt_min");
  _patElectron_eta_max = iConfig.getParameter<double>("patElectron_eta_max");
  PUInfo_          = consumesCollector().consumes<std::vector< PileupSummaryInfo> >(edm::InputTag("slimmedAddPileupInfo"));
  genEvtInfo_    = consumesCollector().consumes<GenEventInfoProduct>(edm::InputTag("generator"));
  //?why not just consumes?
  debug_                 = iConfig.getParameter<bool>("debug_");
  bjetnessselfilter      = iConfig.getParameter<bool>("bjetnessselfilter");
  _is_data               = iConfig.getParameter<bool>("is_data");
  _lepfilter          = iConfig.getParameter<int>("lepfilter");
  _ifevtriggers          = iConfig.getParameter<bool>("ifevtriggers"); 
  _evtriggers            = iConfig.getParameter<vector<string> >("evtriggers");
  _fillgeninfo           = iConfig.getParameter<bool>("fillgeninfo"); 
  _fillgenHFCategoryinfo = iConfig.getParameter<bool>("fillgenHFCategoryinfo");
  _filleventinfo         = iConfig.getParameter<bool>("filleventinfo"); 
  _filltriggerinfo       = iConfig.getParameter<bool>("filltriggerinfo");
  _fillPVinfo            = iConfig.getParameter<bool>("fillPVinfo");  
  _fillmuoninfo          = iConfig.getParameter<bool>("fillmuoninfo");
  _fillelectronpatinfo   = iConfig.getParameter<bool>("fillelectronpatinfo");
  _filltauinfo           = iConfig.getParameter<bool>("filltauinfo");
  _filljetinfo           = iConfig.getParameter<bool>("filljetinfo"); 
  _filltthjetinfo        = iConfig.getParameter<bool>("filltthjetinfo"); 
  _fillBoostedJetinfo    = iConfig.getParameter<bool>("fillBoostedJetinfo"); 
  _fillTopSubJetinfo     = iConfig.getParameter<bool>("fillTopSubJetinfo"); 
  _fillTauJetnessinfo    = iConfig.getParameter<bool>("fillTauJetnessinfo"); 
  _fillBJetnessinfo      = iConfig.getParameter<bool>("fillBJetnessinfo"); 
  _fillBJetnessFVinfo    = iConfig.getParameter<bool>("fillBJetnessFVinfo"); 
  _fillBTagReweight      = iConfig.getParameter<bool>("fillBTagReweight");
  _fillPileupReweight    = iConfig.getParameter<bool>("fillPileupReweight");
  _fillMETinfo           = iConfig.getParameter<bool>("fillMETinfo");
  _fillphotoninfo        = iConfig.getParameter<bool>("fillphotoninfo");

  edm::Service<TFileService> fs;
  evtree_ = fs->make<TTree>("evtree","evtree");
  evtree_->Branch("eventnum",&eventnum,"eventnum/I");
  evtree_->Branch("eventnumnegative",&eventnumnegative,"eventnumnegative/I");
  evtree_->Branch("nPUVertices",&nPUVertices,"nPUVertices/I");
  evtree_->Branch("TrueInteractions",&TrueInteractions,"TrueInteractions/D");
  genWeight_ = fs->make<TH1D>("GenEventWeight","GenEventWeight",1,-0.5,0.5);


  tree_   = fs->make<TTree>("BOOM","BOOM");
  if(_fillgeninfo)           genselector        = new GenParticleSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  //?where is the declaration of genselector?
  if(_fillgenHFCategoryinfo) genhfselector      = new GenHFHadrMatchSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_filleventinfo)         eventinfoselector  = new EventInfoSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_filltriggerinfo)       trselector         = new TriggerSelector("miniAOD", tree_, debug_, iConfig);
  if(_fillPVinfo)            pvselector         = new PVSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillmuoninfo)          muselector         = new MuonSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillelectronpatinfo)   elpatselector      = new ElectronPatSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_filltauinfo)           tauselector        = new TauSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_filljetinfo)           jetselector        = new JetSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_filltthjetinfo)        tthjetselector     = new TTHJetSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillBoostedJetinfo)    BoostedJetselector = new BoostedJetSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillTopSubJetinfo)     TopSubJetselector  = new TopSubJetSelector("miniAOD", tree_, debug_, iConfig);
  if(_fillTauJetnessinfo)    TauJetnessselector = new TauJetnessSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillBJetnessinfo)      BJetnessselector   = new BJetnessSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillBJetnessFVinfo)    BJetnessFVselector = new BJetnessFVSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillBTagReweight)      btagreweight       = new BTagReweight("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillPileupReweight)    pileupreweight     = new PileupReweight("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillMETinfo)           metselector        = new METSelector("miniAOD", tree_, debug_, iConfig, consumesCollector());
  if(_fillphotoninfo)        photonselector     = new PhotonSelector("miniAOD", tree_, debug_, iConfig);
}
BSM3G_TNT_Maker::~BSM3G_TNT_Maker()
{
  //do anything here that needs to be done at desctruction time
  //(e.g. close files, deallocate resources etc.)
}
/////
//   Member functions
/////
// ------------ method called for each event  ------------
void BSM3G_TNT_Maker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)/*{{{*/
{
  //Namespace
  using namespace edm;
  using namespace pat;
  using namespace reco;
  // Recall collections
  edm::Handle<edm::View<pat::Muon> > muon_h;
  iEvent.getByToken(muon_h_, muon_h);
  edm::Handle<edm::View<pat::Electron> > electron_pat;
  iEvent.getByToken(electron_pat_, electron_pat);
  eventnum = -1;
  eventnum = iEvent.id().event();
  //?what is this eventnum?
  eventnumnegative = 1;
  //?where is the declaration of eventnum and eventnumnegtive?
  nPUVertices = 0;
  TrueInteractions = 0;
  std::vector<PileupSummaryInfo>::const_iterator PVI;
  //?where is the instuction for this way of getting pileup information?
  if(!_is_data){
      edm::Handle<GenEventInfoProduct> genEvtInfo;
      iEvent.getByToken(genEvtInfo_,genEvtInfo);//25
      //iEvent.getByLabel("generator",genEvtInfo);
      eventnumnegative = (genEvtInfo->weight())/abs(genEvtInfo->weight());
      genWeight_->Fill(0.0,genEvtInfo->weight());


      //?
      Handle<std::vector< PileupSummaryInfo > >  PUInfo;
      iEvent.getByToken(PUInfo_, PUInfo); //24  PUInfo_    = consumesCollector().consumes<std::vector< PileupSummaryInfo> >(edm::InputTag("slimmedAddPileupInfo"));
      for(PVI = PUInfo->begin(); PVI != PUInfo->end(); ++PVI){
         if(PVI->getBunchCrossing() == 0){
         nPUVertices += PVI->getPU_NumInteractions();
         TrueInteractions = PVI->getTrueNumInteractions();
        }
      if(debug_)std::cout << " Pileup Information: bunchXing, nvtx,true nvtx: " << PVI->getBunchCrossing() << " " << PVI->getPU_NumInteractions()<< " "<< PVI->getTrueNumInteractions()<< std::endl;
      }//loop over pileup info
  }
  evtree_->Fill();
  //Require trigger on the event
  bool evtriggered = false;//171
  if(_ifevtriggers){
    edm::Handle<edm::TriggerResults> triggerBits;//I think it holds all the trigger of the event.
    iEvent.getByToken(triggerBits_, triggerBits);//bits = cms.InputTag("TriggerResults","","HLT")
    const edm::TriggerNames &trigNames = iEvent.triggerNames(*triggerBits);
    for(uint tb = 0; tb<triggerBits->size(); tb++){
      for(uint tn = 0; tn<_evtriggers.size(); tn++){
        if(strstr(trigNames.triggerName(tb).c_str(),_evtriggers[tn].c_str()) && triggerBits->accept(tb)){
            //strstr:Returns a pointer to the first occurrence of str2 in str1, or a null pointer if str2 is not part of str1.
            //?where is the accept()method?
          evtriggered = true;
          break;//When break is used with nested loops, break terminates the inner loop
        } 
      }
    }
  }
  //Require at least two leptons on the event
  Bool_t pass_nlep = false;//173
  if(_lepfilter > 0){
    Int_t n_lep = 0;
    for(edm::View<pat::Muon>::const_iterator mu = muon_h->begin(); mu != muon_h->end(); mu++){
        if(mu->pt() < _Muon_pt_min)         continue;
        if(fabs(mu->eta()) > _Muon_eta_max) continue;  
        if(mu->passed(reco::Muon::CutBasedIdLoose) <0.5) continue;
        n_lep++;
        //std::cout<< " EventNumber " << eventnum << " n_lep in mu " << n_lep << std::endl;
        if(n_lep >= _lepfilter ){
            pass_nlep = true;
            break;
        }
    }
    for(edm::View<pat::Electron>::const_iterator el = electron_pat->begin(); el != electron_pat->end(); el++){
        if(pass_nlep) break;
        if(el->pt() < _patElectron_pt_min)         continue;
        if(fabs(el->eta()) > _patElectron_eta_max) continue;  
        n_lep++;
        //std::cout<< " EventNumber " << eventnum << " n_lep in ele " << n_lep << std::endl;
        if(n_lep >= _lepfilter ){
            pass_nlep = true;
            break;
        }
    }
  }
  //Call classes
  if(((_ifevtriggers && evtriggered) || !_ifevtriggers) && (pass_nlep || _lepfilter <= 0)){
    bjetnesssel_filter = 0;
    if(_fillBJetnessinfo)      BJetnessselector->Fill(iEvent, iSetup, bjetnesssel_filter);
    if((bjetnessselfilter && bjetnesssel_filter==1) || !bjetnessselfilter){
      //cout<<"bjetnesssel_filter aft "<<bjetnesssel_filter<<endl;
      if(_fillBJetnessFVinfo)    BJetnessFVselector->Fill(iEvent, iSetup);
      if(_fillgeninfo)           genselector->Fill(iEvent); 
      if(_fillgenHFCategoryinfo) genhfselector->Fill(iEvent);
      if(_filleventinfo)         eventinfoselector->Fill(iEvent);
      if(_filltriggerinfo)       trselector->Fill(iEvent,iSetup);//missing a i in both declaration and call here.
      if(_fillPVinfo)            pvselector->Fill(iEvent); 
      if(_fillmuoninfo)          muselector->Fill(iEvent,iSetup);
      if(_fillelectronpatinfo)   elpatselector->Fill(iEvent,iSetup); 
      if(_filltauinfo)           tauselector->Fill(iEvent,iSetup); 
      if(_filljetinfo)           jetselector->Fill(iEvent);
      if(_filltthjetinfo)        tthjetselector->Fill(iEvent,iSetup);
      if(_fillBoostedJetinfo)    BoostedJetselector->Fill(iEvent);
      if(_fillTopSubJetinfo)     TopSubJetselector->Fill(iEvent);
      if(_fillTauJetnessinfo)    TauJetnessselector->Fill(iEvent, iSetup);
      if(_fillBTagReweight)      btagreweight->Fill(iEvent);
      if(_fillPileupReweight)    pileupreweight->Fill(iEvent);
      if(_fillMETinfo)           metselector->Fill(iEvent);
      if(_fillphotoninfo)        photonselector->Fill(iEvent);
      tree_->Fill();
    }
  }
}/*}}}*/
// ------------ method called once each job just before starting event loop  ------------
void BSM3G_TNT_Maker::beginJob()
{
}
// ------------ method called once each job just after ending the event loop  ------------
void BSM3G_TNT_Maker::endJob() 
{
}
// ------------ method called when starting to processes a run  ------------
void BSM3G_TNT_Maker::beginRun(edm::Run const & iRun, edm::EventSetup const& iSetup)
{
  if( _filltriggerinfo) trselector->startTrigger(iSetup, iRun);
  //?why startTrigger first?
}
// ------------ method called when ending the processing of a run  ------------
//void BSM3G_TNT_Maker::endRun(edm::Run const&, edm::EventSetup const&)
//{
//}
// ------------ method called when starting to processes a luminosity block  ------------
//void BSM3G_TNT_Maker::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
//{
//}
// ------------ method called when ending the processing of a luminosity block  ------------
//void BSM3G_TNT_Maker::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
//{
//}
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void BSM3G_TNT_Maker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(BSM3G_TNT_Maker);
