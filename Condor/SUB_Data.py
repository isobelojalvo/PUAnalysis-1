import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
import FWCore.ParameterSet.Config as cms

process = cms.Process("ANALYSIS")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.GlobalTag.globaltag = '94X_dataRun2_v6'

process.options   = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100000


process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        #'file:singleMu.root'
        #'/store/data/Run2016D/Tau/MINIAOD/07Aug17-v1/10000/3208BBC1-52A3-E711-A21C-0242AC110008.root'
        #'file:VBFHttFXFX.root',
        #'/store/mc/RunIISummer16MiniAODv2/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/02810E61-F5C5-E611-A78A-002590FD5A78.root'
        '/store/data/Run2017B/Tau/MINIAOD/17Nov2017-v1/40000/065C0361-C7D8-E711-BFE8-0CC47ABB517C.root'
		),
		inputCommands=cms.untracked.vstring(
						'keep *',
						'keep *_l1extraParticles_*_*',
		)
)

#import FWCore.PythonUtilities.LumiList as LumiList #check lumilist name, not sure it matches to golden
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt').getVLuminosityBlockRange() 


#Default Reconstruction from the analysTools.py config file
#The main 'setup' processes can be found in "defaultReconstruction" and "defaultReconstructionMC"
#analysisTools takes care of pre-selections, adding in extra ID's that do not come in the miniAOD
#files and embedding trigger matching (the trigger for di-Tau hadronic still should be added and checked)
#defaultRecontruction and defaultReconstructionMC are generic enough to work for any final state
#needed: muTau, tauTau, eTau, mumuTauTau, ect. However, different analyses may want to embed
#different ID's, isolations, ect. Trigger paths are input below. These plugins are typically
#found in RecoTools/plugins/
from PUAnalysis.Configuration.tools.analysisTools import *
defaultReconstruction(process,'HLT',
        [
        #'hltDoublePFTau35TrackPt1TightChargedIsolationAndTightOOSCPhotonsDz02Reg',
        'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v',
        'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v'        
        ])

#EventSelection
#Most of the selections for the analysis go in hTauTau_cff
#The selections proceed sequentially, each time a "di-candidate pair" fails a cut in
#this configuration then the sequence will start over with another di-candidate pair.
#The final 'sorting' is implemented there as well, either by di-tau PT or isolation.
process.load("PUAnalysis.Configuration.hTauTau_cff")

process.metCalibration.applyCalibration = cms.bool(False)

#Name of the path in hTauTau_cff
process.eventSelectionTT = cms.Path(process.selectionSequenceTT)


#Create the Ntuples, the name "analysis.root" is set here as well
#This takes the output from the configuration sequence and fills
#the tree that will later be used for plotting. Notice the names
#added here 'diTauOS' is the default, however, this 'diTauOS' can
#be replaced with any of the labled collections produced in htautau_cff.py
#in order to create two different trees, one with all the final selections
#and one with looser selections.
from PUAnalysis.Configuration.tools.ntupleTools import addDiTauEventTree
addDiTauEventTree(process,'diTauEventTreeFinalLoose','diTausAntiMu','TightMuons','TightElectrons',triggerCollection='HLT')
addDiTauEventTree(process,'diTauEventTree')
addDiTauEventTree(process,'diTauEventTreeFinal','diTausOS')


#This event summary tells you how many objects pass each of the steps
#in the configuration. It is extremely useful for debugging. 
#Normally does not need to be touched. :) 
addEventSummary(process,True,'TT','eventSelectionTT')

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            $inputFileNames
            ),
        inputCommands=cms.untracked.vstring(
            'keep *',
            )
        )

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

#process.TFileService.fileName=cms.string("$outputFileName")
process.TFileService = cms.Service(
        "TFileService",
        fileName = cms.string("$outputFileName")
        )
