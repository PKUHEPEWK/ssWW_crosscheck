from ROOT import *
import math
from numpy import sign

def signal_region(tree, ientry,itree):
	weight = 0.
	pass_trig = 1.
	jet_veto = 1.
	tau_veto = 1.
	tree.GetEntry(ientry)

	if ientry%10000 ==0: print 'processing ',ientry
	## lepton selection
	if tree.nLepton != 2: return 0
	if sign(tree.Lepton_pdgId[0]) + sign(tree.Lepton_pdgId[1]) ==0: return 0
	if tree.Lepton_pt[0]<30 or tree.Lepton_pt[1]<30: return 0
	if (abs(tree.Lepton_eta[0])>2.4 and abs(tree.Lepton_pdgId[0])==11) or (abs(tree.Lepton_eta[0])>2.5 and abs(tree.Lepton_pdgId[0])==13): return 0
	if (abs(tree.Lepton_eta[1])>2.4 and abs(tree.Lepton_pdgId[1])==11) or (abs(tree.Lepton_eta[1])>2.5 and abs(tree.Lepton_pdgId[1])==13): return 0
	if tree.nVetoLepton>0 and tree.VetoLepton_pt[0]>10: return 0
	## jets selection
	if tree.mjj<500 or tree.detajj<2.5: return 0
	## MET selection
	if tree.MET_pt<30: return 0

	## zepp selection
	if abs(tree.Lepton_eta[0] - (tree.CleanJet_eta[0] + tree.CleanJet_eta[1])/2)/abs(tree.detajj) > 0.5: return 0
	if abs(tree.Lepton_eta[1] - (tree.CleanJet_eta[0] + tree.CleanJet_eta[1])/2)/abs(tree.detajj) > 0.5: return 0

	## veto
	if tree.mll<20 or tree.dmZll_veto<15: return 0
	
	## b veto
	for ijet in range(0,tree.nJet):
		if tree.Jet_pt[ijet]>20 and tree.Jet_btagCSVV2[ijet] > 0.8484: 
			jet_veto = 0.
			break
		else: continue

	## tau veto
	for itau in range(0,tree.nTau):
                if tree.Tau_pt[itau] > 18 and tree.Tau_rawIso[itau]>=1 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[0])*(tree.Tau_eta[itau]-tree.Lepton_eta[0]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)) >=0.3 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[1])*(tree.Tau_eta[itau]-tree.Lepton_eta[1]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)) >=0.3:
                        tau_veto = 0.
                        break
                else: continue


	if itree==14 and (tree.Trigger_ElMu or not tree.Trigger_dblMu): pass_trig=0.
	if itree==15 and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngEl or not tree.Trigger_dblEl):pass_trig=0.
	if itree==16 and (tree.Trigger_ElMu or tree.Trigger_dblMu or not tree.Trigger_sngEl):pass_trig=0.
	if itree==17 and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngEl or tree.Trigger_dblEl or not tree.Trigger_sngEl):pass_trig=0.
	if itree==18 and not tree.Trigger_ElMu: pass_trig=0.
	if itree<14:
		weight = tree.XSWeight*tree.SFweight2l*tree.GenLepMatch2l*tree.METFilter_MC*41.5*jet_veto*tau_veto
	else:
		weight = tree.fakeW2l_ele_mvaFall17Iso_WP90_SS_mu_cut_Tight_HWWW*tree.METFilter_FAKE*pass_trig*jet_veto*tau_veto

	return weight
