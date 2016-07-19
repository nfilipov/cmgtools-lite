import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.core.all import *
from PhysicsTools.Heppy.analyzers.objects.all import *
from PhysicsTools.Heppy.analyzers.gen.all import *


from CMGTools.TTHAnalysis.analyzers.ttHFastLepSkimmer import ttHFastLepSkimmer
fastSkim2LnoSip = cfg.Analyzer(ttHFastLepSkimmer, name="fastLepSkim2LnoSIP",
                               muons = 'slimmedMuons', muCut = lambda mu : mu.pt() > 5,
                               electrons = 'slimmedElectrons', eleCut = lambda ele : ele.pt() > 7,
                               minLeptons = 2,
                               )
