import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class exampleProducer(Module):
    def __init__(self, jetSelection):
        self.jetSel = jetSelection
	self.count=0
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
	self.count += 1
	if self.count%10000 ==0:
		print "processing ", self.count 
        """process event, return True (go to next module) or False (fail, go to next event)"""
	leptons = Collection(event, "Lepton")
	cleanjets = Collection(event, "CleanJet")

	if len(leptons)<2: return False
	if len(cleanjets)<2: return False

	if leptons[0].pt < 25 or leptons[1].pt < 20: return False
	if cleanjets[0].pt < 30 or cleanjets[1].pt < 30: return False
	if abs(cleanjets[0].eta) > 5.0 or abs(cleanjets[1].eta) > 5.0: return False
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

exampleModuleConstr = lambda : exampleProducer(jetSelection= lambda j : j.pt > 30) 
 
