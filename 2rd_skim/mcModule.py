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
	def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
		pass
	def analyze(self, event):
		self.count += 1
		if self.count%10000 ==0: print 'processing ',self.count
      		"""process event, return True (go to next module) or False (fail, go to next event)"""
		if event.MET_pt<30 or event.mjj<150: return False

		return True

mcModule = lambda : mcProducer() 
