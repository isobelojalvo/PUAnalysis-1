// system include files
#include <memory>
#include "PUAnalysis/RecoTools/interface/SmearedParticleMaker.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/RandomNumberGenerator.h"
#include "CLHEP/Random/RandFlat.h"
#include "CLHEP/Random/RandGauss.h"
#include <TFile.h>
#include <TH1F.h>

#include <TRandom.h>
#include <TRandom3.h>


class ESTauProducerMET : public edm::EDProducer  {
 public:
  explicit ESTauProducerMET(const edm::ParameterSet& iConfig);
  ~ESTauProducerMET();
    
 private:
  void produce(edm::Event& iEvent, const edm::EventSetup& iSetup);

  
  // ----------member data ---------------------------
  bool smearConstituents_;
  edm::EDGetTokenT<pat::TauCollection > src_;           //input Collection
  edm::EDGetTokenT<pat::METCollection > met_;           //input Collection
  edm::EDGetTokenT<reco::GenParticleCollection> genParticles_;
  bool data_;
  double hadronEnergyScale_;
  double gammaEnergyScale_;

  double oneProngEnergyScale_;
  double oneProngPi0EnergyScale_;
  double threeProngEnergyScale_;


  SmearedParticleMaker<pat::Tau,GenJetRetriever<pat::Tau> > *smearingModule;
  
};



 

