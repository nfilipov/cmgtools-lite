from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy
import ntuple

class ZGTree(TreeAnalyzerNumpy):
    
    def beginLoop(self, setup):
        super(ZGTree, self).beginLoop(setup)
        ntuple.bookParticle(self.tree, 'muon')
        ntuple.bookParticle(self.tree, 'dimuon')
        ntuple.bookParticle(self.tree, 'dimuon_mu1')
        ntuple.bookParticle(self.tree, 'dimuon_mu2')
        
    def process(self, event):
        self.tree.reset()
        if len(event.muons)>0:
            ntuple.fillParticle(self.tree, 'muon', event.muons[0])
        if len(event.muons)>1:
            if len(event.dimuons)>0:
                ntuple.fillParticle(self.tree, 'dimuon', event.dimuons[0])
                #            ntuple.fillParticle(self.tree, 'dimuon_mu1', event.dimuons.leg1)
                #            ntuple.fillParticle(self.tree, 'dimuon_mu2', event.dimuons.leg2)
        self.tree.tree.Fill()

        
