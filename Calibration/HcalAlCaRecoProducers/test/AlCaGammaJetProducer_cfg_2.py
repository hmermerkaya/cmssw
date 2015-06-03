import FWCore.ParameterSet.Config as cms

process = cms.Process("MYGAMMAJET")

process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag=autoCond['startup']
process.GlobalTag.globaltag = 'PHYS14_25_V1::All'
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
    )

process.maxEvents = cms.untracked.PSet(
   input = cms.untracked.int32(100)
     #  input = cms.untracked.int32(-1)
     )
process.source = cms.Source("PoolSource",
    fileNames = 
    cms.untracked.vstring(
#   'file:/tmp/hmermerk/GJet_pt4013TeV_pythia6.root'
# '/store/mc/Phys14DR/GJet_Pt40_doubleEMEnriched_TuneZ2star_13TeV-pythia6/AODSIM/PU20bx25_PHYS14_25_V1-v1/00000/000B1591-F96E-E411-8885-00266CFFC198.root'
      # 'file:/tmp/andriusj/6EC8FCC8-E2A8-E411-9506-002590596468.root'
          '/store/relval/CMSSW_7_4_0_pre6/RelValPhotonJets_Pt_10_13/GEN-SIM-RECO/MCRUN2_74_V1-v1/00000/6EC8FCC8-E2A8-E411-9506-002590596468.root'
           )
    )


process.load("RecoEgamma/PhotonIdentification/PhotonIDValueMapProducer_cfi")
process.load("Calibration.HcalAlCaRecoProducers.alcagammajet_cfi")
process.load("Calibration.HcalAlCaRecoProducers.ALCARECOHcalCalGammaJet_Output_cff")

#from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format  to be
# DataFormat.AOD or DataFormat.MiniAOD, as appropriate
#if useAOD == True :
#dataFormat = DataFormat.AOD
#else :
#dataFormat = DataFormat.MiniAOD

#switchOnVIDPhotonIdProducer(process, dataFormat)

# define which IDs we want to produce
#my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_PHYS14_PU20bx25_V2_cff']

#add them to the VID producer
#for idmod in my_id_modules:
#          setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)


#process.GammaJetRecos = cms.OutputModule("PoolOutputModule",
#    outputCommands = cms.untracked.vstring('drop *',
##                 'keep recoPhotonCores_*_*_*',
#                 'keep recoSuperClusters_*_*_*',
#                 #'keep recoTracks_*_*_*',
#                 'keep recoTracks_generalTracks_*_*',
#                 #'keep *_PhotonIDProd_*_*',
#               'keep *_particleFlow_*_*',
#              'keep recoPFBlocks_particleFlowBlock_*_*',
#              'keep recoPFClusters_*_*_*',
##                         'keep *_particleFlowPtrs_*_*',
#        'keep *_GammaJetProd_*_*'),
#    fileName = cms.untracked.string('gjet.root')
#)

#process.photonIDValueMapProducer.src=cms.InputTag("GammaJetProd","gedPhotons")


process.GammaJetRecos = cms.OutputModule("PoolOutputModule",
   outputCommands = process.OutALCARECOHcalCalGammaJet.outputCommands,
      fileName = cms.untracked.string('gnew4jet.root')
      )
process.p = cms.Path(process.GammaJetProd*process.photonIDValueMapProducer)
#process.p = cms.Path(process.GammaJetProd*process.PhotonIDValueMapSeq)
#process.p = cms.Path(process.GammaJetProd*process.egmPhotonIDSequence)
process.e = cms.EndPath(process.GammaJetRecos)
