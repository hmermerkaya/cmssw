import FWCore.ParameterSet.Config as cms

# output block for alcastream HCAL Dijets
# output module 
#  module alcastreamHcalGammaJetOutput = PoolOutputModule
OutALCARECOHcalCalGammaJet_noDrop = cms.PSet(
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalGammaJet')
    ),
    outputCommands = cms.untracked.vstring( 
              #'keep *')
              'keep recoPhotonCores_*_*_*',
              'keep recoGenParticles_*_*_*',
              'keep recoSuperClusters_*_*_*',
              'keep recoTracks_generalTracks_*_*',
              'keep *_particleFlow_*_*',
              'keep recoPFBlocks_particleFlowBlock_*_*',
              'keep recoPFClusters_*_*_*',
              'keep *_reducedEgamma_*_*',
              'keep *_*_reducedEBRecHits_*',
              'keep *_gedPhotons_*_*',
              'keep *_GammaJetProd_*_*',
              'keep *_egmPhotonIDs_*_*',
              'keep *_fixedGridRhoFastjetAll_*_*',
              'keep *_photonIDValueMapProducer_*_*')



#                 'keep recoPhotonCores_*_*_*',
#                 'keep recoSuperClusters_*_*_*',
#                 'keep recoTracks_generalTracks_*_*',
#                 'keep *_particleFlow_*_*',
#                 'keep recoPFBlocks_particleFlowBlock_*_*',
#                 'keep recoPFClusters_*_*_*',
#                 'keep *_GammaJetProd_*_*')
)

import copy
OutALCARECOHcalCalGammaJet=copy.deepcopy(OutALCARECOHcalCalGammaJet_noDrop)
OutALCARECOHcalCalGammaJet.outputCommands.insert(0, "drop *")
