import FWCore.ParameterSet.Config as cms
process = cms.Process('ANALYSIS')

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.categories+=cms.untracked.vstring('GammaJetAnalysis')
process.MessageLogger.cerr.FwkReport.reportEvery=cms.untracked.int32(1000)

# Specify IdealMagneticField ESSource (needed for CMSSW 730)
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load("MagneticField.Engine.autoMagneticFieldProducer_cfi")
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag=autoCond['startup']

#load the gammaJet analyzer
process.load('Calibration.HcalCalibAlgos.gammaJetAnalysis_cfi')
#  needed for nonCHS
process.load('JetMETCorrections.Configuration.JetCorrectionProducers_cff')

# run over files
process.GammaJetAnalysis.rootHistFilename = cms.string('PhoJet_tree_CHS.root')
process.GammaJetAnalysis.doPFJets = cms.bool(True)
process.GammaJetAnalysis.doGenJets = cms.bool(False)

# trigger names should not end with '_'
process.GammaJetAnalysis.photonTriggers = cms.vstring(
    'HLT_Photon20_CaloIdVL_IsoL','HLT_Photon30_CaloIdVL_IsoL',
    'HLT_Photon50_CaloIdVL_IsoL','HLT_Photon75_CaloIdVL_IsoL',
    'HLT_Photon90_CaloIdVL_IsoL','HLT_Photon135',
    'HLT_Photon150','HLT_Photon160')
# triggers for CMSSW 730
process.GammaJetAnalysis.photonTriggers += cms.vstring(
    'HLT_Photon22', 'HLT_Photon30', 'HLT_Photon36',
    'HLT_Photon50', 'HLT_Photon75',
    'HLT_Photon90', 'HLT_Photon120', 'HLT_Photon175',
    'HLT_Photon250_NoHE', 'HLT_Photon300_NoHE')
# to disable photonTriggers assign an empty vstring
# a clone without CHS
process.GammaJetAnalysis_noCHS= process.GammaJetAnalysis.clone()
process.GammaJetAnalysis_noCHS.rootHistFilename = cms.string('PhoJet_tree_nonCHS.root')
# for 7XY use ak4* instead of ak5
process.GammaJetAnalysis_noCHS.pfJetCollName = cms.string('ak4PFJets')
process.GammaJetAnalysis_noCHS.pfJetCorrName = cms.string('ak4PFL2L3')

process.source = cms.Source("PoolSource", 
                            fileNames = cms.untracked.vstring(
        'file:../../HcalAlCaRecoProducers/test/gnew4jet.root'
#    '/store/relval/CMSSW_7_3_0/RelValPhotonJets_Pt_10_13/GEN-SIM-RECO/MCRUN2_73_V7-v1/00000/522CE329-7B81-E411-B6C3-0025905A6110.root',
#    '/store/relval/CMSSW_7_3_0/RelValPhotonJets_Pt_10_13/GEN-SIM-RECO/MCRUN2_73_V7-v1/00000/5279D224-7B81-E411-BCAA-002618943930.root'
#    '/store/relval/CMSSW_7_3_0/RelValPhotonJets_Pt_10_13/GEN-SIM-RECO/MCRUN2_73_V7-v1/00000/522CE329-7B81-E411-B6C3-0025905A6110.root'
#    '/store/relval/CMSSW_7_4_0_pre6/RelValPhotonJets_Pt_10_13/GEN-SIM-RECO/MCRUN2_74_V1-v1/00000/6EC8FCC8-E2A8-E411-9506-002590596468.root'
    )
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )

# name of the process that used the GammaJetProd producer
process.GammaJetAnalysis.prodProcess = cms.untracked.string('MYGAMMAJET')
# specify 'workOnAOD=2' to apply tokens from GammaJetProd producer
process.GammaJetAnalysis.workOnAOD = cms.int32(2)
process.GammaJetAnalysis.doGenJets = cms.bool(False)
process.GammaJetAnalysis.debug     = cms.untracked.int32(0)



from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
# turn on VID producer, indicate data format  to be
# DataFormat.AOD or DataFormat.MiniAOD, as appropriate
#if useAOD == True :
dataFormat = DataFormat.AOD
#else :
#dataFormat = DataFormat.MiniAOD

switchOnVIDPhotonIdProducer(process, dataFormat)

# define which IDs we want to produce
my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_PHYS14_PU20bx25_V2_cff']

#add them to the VID producer
for idmod in my_id_modules:
         setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection)

process.p = cms.Path(
 #  process.egmPhotonIDSeq*
 process.egmPhotonIDs*process.GammaJetAnalysis

)
