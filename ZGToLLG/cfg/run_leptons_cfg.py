##########################################################
##       CONFIGURATION FOR ZGToLLG TREES                ##
##########################################################
import os
import PhysicsTools.HeppyCore.framework.config as cfg
#import re
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

multi_thread = False
#input file(s)
inputSample = cfg.Component(
    'test_component',
    files = [ "root://eoscms//eos/cms/store/data/Run2016B/Charmonium/MINIAOD/PromptReco-v2/000/274/335/00000/D20107C3-EA2A-E611-A9FD-02163E01339F.root" ],
    isData=True,
    )

#Loading from the analyzer (later)
#from CMGTools.ZGToLLG.analyzers.zg2lg_cff import *


selectedComponents = [inputSample]

# a very simple muon analyzer
# read miniaod muons and wrap them in python muons
from CMGTools.ZGToLLG.analyzers.SimpleMuonAnalyzer import SimpleMuonAnalyzer
muons = cfg.Analyzer(
    SimpleMuonAnalyzer,
    'muons',
    filter_func = lambda x : True, #This should let everything pass.
    nmuons = 4 #but keep only the 4 leading.
    )

from CMGTools.ZGToLLG.analyzers.ResonanceBuilder import ResonanceBuilder
dimuons = cfg.Analyzer(
    ResonanceBuilder,
    'dimuons',
    leg_collection = 'muons',
    filter_func = lambda x : x.pt()>6.5, # this should cut on the leg pt.
    #    filter_func2 = lambda x : x.M()>2.5 and x.M()<4.5, #this should cut on the dimuon mass.
    pdgid = 443,
    ndimuons = 4
    )

#build the output tree
from CMGTools.ZGToLLG.analyzers.ZGTree import *
tree = cfg.Analyzer(
    ZGTree
    )

#Make the sequence
sequence = cfg.Sequence( [
        muons,
        dimuons,
        tree
        ] )

# config stuff, not sure if needed, but seems important
# finalization of the configuration object. 
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence, 
                     services = [],
                     events_class = Events)

print config

# The thing above is more polite than the following:
#config = autoConfig(selectedComponents, sequence)

#finally, the main
if __name__ == '__main__':
    # can either run this configuration through heppy, 
    # or directly in python or ipython for easier development. 
    # try: 
    # 
    #   ipython -i simple_example_cfg.py
    # 
    from PhysicsTools.Heppy.physicsutils.LorentzVectors import LorentzVector

    from PhysicsTools.HeppyCore.framework.looper import Looper 
    looper = Looper( 'Loop', config, nPrint = 2, nEvents=100) 
    looper.loop()
    looper.write()

    # and now, let's play with the contents of the event
    print looper.event
#    pz = LorentzVector()
#    for imu, mu in enumerate(looper.event.muons): 
#        print 'muon1', mu, 'abs iso=', mu.relIso()*mu.pt()
#        pz += mu.p4()
#    print 'z candidate mass = ', pz.M()

    for mu in enumerate(looper.event.muons): 
        print 'muon1', mu, 'pt = ',mu.pt()

 
    # you can stay in ipython on a given event 
    # and paste more and more code as you need it until 
    # your code is correct. 
    # then put your code in an analyzer, and loop again. 

    def next():
        looper.process(looper.event.iEv+1)


