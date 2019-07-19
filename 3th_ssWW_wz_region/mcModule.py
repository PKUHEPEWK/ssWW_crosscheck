import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import math

sign = lambda x: (1, -1)[x < 0]

class mcProducer(Module):
	def __init__(self):
		self.count = 0
		pass
	def beginJob(self):
		pass
	def endJob(self):
		pass
	def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		self.out = wrappedOutputTree
		self.out.branch('zepplep1','F')
		self.out.branch('zepplep2','F')
	def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass
	def analyze(self, event):
		self.count += 1
		if self.count%10000 ==0: print 'processing ',self.count
      		"""process event, return True (go to next module) or False (fail, go to next event)"""
		leptons = Collection(event, "Lepton")
		if event.nLepton==2: return False
		if leptons[2].pt<10: return False
		if event.nLepton>3 and leptons[3].pt>10: return False
#		if sign(leptons[0].pdgId)+sign(leptons[1].pdgId) == 0: return False
		if (abs(leptons[0].eta)>2.4 and abs(leptons[0].pdgId)==11) or (abs(leptons[0].eta)>2.5 and abs(leptons[0].pdgId)==13): return False
		if (abs(leptons[1].eta)>2.4 and abs(leptons[1].pdgId)==11) or (abs(leptons[1].eta)>2.5 and abs(leptons[1].pdgId)==13): return False
		if (abs(leptons[2].eta)>2.4 and abs(leptons[2].pdgId)==11) or (abs(leptons[2].eta)>2.5 and abs(leptons[2].pdgId)==13): return False

		cleanjets = Collection(event, "CleanJet")
		if event.mjj < 500 or event.detajj < 2.5: return False
		if event.MET_pt < 30: return False
		zepplep1 = abs(leptons[0].eta - (cleanjets[0].eta + cleanjets[1].eta)/2)/abs(event.detajj)
#		if zepplep1 > 0.5: return False
		zepplep2 = abs(leptons[1].eta - (cleanjets[0].eta + cleanjets[1].eta)/2)/abs(event.detajj)
#		if zepplep2 > 0.5: return False

#		if event.mll<10: return False
#		if event.dmZll_veto<10: return False

#		jets = Collection(event, "Jet")
#		for ijet in cleanjets:
#			if jets[ijet].pt > 20 and jets[ijet].btagCSVV2 > 0.8484: return False

		taus = Collection(event, "Tau")
		for itau in range(0,len(taus)):
			if taus[itau].pt > 18 and taus[itau].rawIso>=1 and math.sqrt((taus[itau].eta-leptons[0].eta)*(taus[itau].eta-leptons[0].eta) + (abs(abs(taus[itau].phi - leptons[0].phi) - math.pi)- math.pi)*(abs(abs(taus[itau].phi - leptons[0].phi) - math.pi)- math.pi)) >=0.3 and math.sqrt((taus[itau].eta-leptons[1].eta)*(taus[itau].eta-leptons[1].eta) + (abs(abs(taus[itau].phi - leptons[1].phi) - math.pi)- math.pi)*(abs(abs(taus[itau].phi - leptons[1].phi) - math.pi)- math.pi)) >=0.3:return False

		self.out.fillBranch("zepplep1",zepplep1)
	        self.out.fillBranch("zepplep2",zepplep2)

		return True

mcModule = lambda : mcProducer() 
