from ROOT import *
import math
from numpy import sign
import btag_weight

def signal_region(tree, ientry,itree):
	weight = 0.
	tree.GetEntry(ientry)

	if ientry%10000 ==0: print 'processing ',ientry
	## lepton selection
	if tree.nLepton != 2 and tree.Lepton_pt[2]>10: return 0
	if itree<16 or itree>20:
		if abs(tree.Lepton_pdgId[0])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0]!=1: return 0 
		if abs(tree.Lepton_pdgId[1])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1]!=1: return 0 
		if abs(tree.Lepton_pdgId[0])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[0]!=1: return 0 
		if abs(tree.Lepton_pdgId[1])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[1]!=1: return 0 
	if sign(tree.Lepton_pdgId[0]) + sign(tree.Lepton_pdgId[1]) ==0: return 0
	if tree.Lepton_pt[0]<30 or tree.Lepton_pt[1]<30: return 0

	## jets selection, implement in pre-selection 
#	if tree.mjj<500 or tree.detajj<2.5: return 0
	## MET selection
#	if tree.MET_pt<30: return 0
	if tree.zepplep1>0.5 or tree.zepplep2>0.5: return 0

	## zepp selection
#	if abs(tree.Lepton_eta[0] - (tree.CleanJet_eta[0] + tree.CleanJet_eta[1])/2)/abs(tree.detajj) > 0.5: return 0
#	if abs(tree.Lepton_eta[1] - (tree.CleanJet_eta[0] + tree.CleanJet_eta[1])/2)/abs(tree.detajj) > 0.5: return 0

	## veto
	if tree.mll<20: return 0
	l1 = TLorentzVector()
	l2 = TLorentzVector()
	z_window_veto = 0
	if abs(tree.Lepton_pdgId[0])+abs(tree.Lepton_pdgId[1]) ==22:
		l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.000511)
		l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.000511)
		z_window_veto=(l1+l2).M()
#		if abs(tree.Lepton_pdgId[0])==13:
#			l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.10566)
#			l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.10566)
	if abs(z_window_veto - 91.1876)<15: return 0
#	if abs(tree.dmZll_veto - 91.1876)<15: return 0
	
	## b veto
	bveto_sf = 1.
	for ijet in tree.CleanJet_jetIdx:
	#	if tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4 and tree.Jet_btagCSVV2[ijet] > 0.8484: 
		if tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4 and tree.Jet_btagDeepB[ijet]>0.1522: 
			return 0
		if itree<16 and tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4: 
			bveto_sf = bveto_sf*(1 - tree.Jet_btagSF[ijet]*btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))/(1 - btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))
			continue

	## tau veto, implement in pre-selection
#	for itau in range(0,tree.nTau):
#                if tree.Tau_pt[itau] > 18 and tree.Tau_rawIso[itau]>=1 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[0])*(tree.Tau_eta[itau]-tree.Lepton_eta[0]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)) >=0.3 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[1])*(tree.Tau_eta[itau]-tree.Lepton_eta[1]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)) >=0.3:
#			return 0
#                else: continue

	lep_sf = 1.
	if itree<16:
		for ilep in range(0,len(tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF)):
			lep_sf = lep_sf*tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF[ilep]
		for ilep in range(0,len(tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF)):
			lep_sf = lep_sf*tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF[ilep]
	if itree<16:
		trig_sf = 1- (1-tree.TriggerEffWeight_sngEl)*(1-tree.TriggerEffWeight_sngMu)*(1-tree.TriggerEffWeight_dblEl)*(1-tree.TriggerEffWeight_dblMu)*(1-tree.TriggerEffWeight_ElMu)

	if itree<16:mu_roc_sf = tree.Lepton_rochesterSF[0]*tree.Lepton_rochesterSF[1]

	if (itree==16 or itree==21) and (tree.Trigger_ElMu or not tree.Trigger_dblMu): return 0.
	if (itree==17 or itree==22) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or not tree.Trigger_dblEl):return 0.
	if (itree==18 or itree==23) and (tree.Trigger_ElMu or tree.Trigger_dblMu or not tree.Trigger_sngMu):return 0.
	if (itree==19 or itree==24) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or tree.Trigger_dblEl or not tree.Trigger_sngEl):return 0.
	if (itree==20 or itree==25) and not tree.Trigger_ElMu: return 0.
	if itree<16:
		weight = tree.XSWeight*tree.SFweight2l*tree.GenLepMatch2l*tree.PrefireWeight*tree.METFilter_MC*41.5*bveto_sf*lep_sf*trig_sf*mu_roc_sf
	elif itree<21:
		weight = tree.fakeW2l_ele_mvaFall17V2Iso_WP90_SS_mu_cut_Tight_HWWW*tree.METFilter_FAKE
	else: weight = tree.METFilter_DATA
	return weight

def lowmjj_region(tree, ientry,itree):
	weight = 0.
	tree.GetEntry(ientry)

	if ientry%10000 ==0: print 'processing ',ientry
	## lepton selection
	if tree.nLepton != 2 and tree.Lepton_pt[2]>10: return 0
	if itree<16 or itree>20:
		if abs(tree.Lepton_pdgId[0])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0]!=1: return 0 
		if abs(tree.Lepton_pdgId[1])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1]!=1: return 0 
		if abs(tree.Lepton_pdgId[0])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[0]!=1: return 0 
		if abs(tree.Lepton_pdgId[1])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[1]!=1: return 0 
	if sign(tree.Lepton_pdgId[0]) + sign(tree.Lepton_pdgId[1]) ==0: return 0
	if tree.Lepton_pt[0]<30 or tree.Lepton_pt[1]<30: return 0
#	if (abs(tree.Lepton_eta[0])>2.5 and abs(tree.Lepton_pdgId[0])==11) or (abs(tree.Lepton_eta[0])>2.4 and abs(tree.Lepton_pdgId[0])==13): return 0
#	if (abs(tree.Lepton_eta[1])>2.5 and abs(tree.Lepton_pdgId[1])==11) or (abs(tree.Lepton_eta[1])>2.4 and abs(tree.Lepton_pdgId[1])==13): return 0

	## jets selection
#	if abs(tree.CleanJet_eta[0])>4.7 or abs(tree.CleanJet_eta[1])>4.7: return 0
	if tree.mjj>500 : return 0
	## MET selection
	if tree.MET_pt<30: return 0

	## veto
	if tree.mll<20: return 0
	l1 = TLorentzVector()
	l2 = TLorentzVector()
	z_window_veto = 0
	if abs(tree.Lepton_pdgId[0])+abs(tree.Lepton_pdgId[1]) ==22:
		l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.000511)
		l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.000511)
		z_window_veto=(l1+l2).M()
#		if abs(tree.Lepton_pdgId[0])==13:
#			l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.10566)
#			l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.10566)
	if abs(z_window_veto - 91.1876)<15: return 0
#	if abs(tree.dmZll_veto - 91.1876)<15: return 0
	
	## b veto
	bveto_sf = 1.
	for ijet in tree.CleanJet_jetIdx:
		if tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4 and tree.Jet_btagDeepB[ijet]>0.1522:
                        return 0
                if itree<16 and tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4:
                        bveto_sf = bveto_sf*(1 - tree.Jet_btagSF[ijet]*btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))/(1 - btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))
                        continue

	## tau veto
#	for itau in range(0,tree.nTau):
#                if tree.Tau_pt[itau] > 18 and tree.Tau_rawIso[itau]>=1 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[0])*(tree.Tau_eta[itau]-tree.Lepton_eta[0]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)) >=0.3 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[1])*(tree.Tau_eta[itau]-tree.Lepton_eta[1]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)) >=0.3:
#			return 0
#                else: continue

	lep_sf = 1.
	if itree<16:
		for ilep in range(0,len(tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF)):
			lep_sf = lep_sf*tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF[ilep]
		for ilep in range(0,len(tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF)):
			lep_sf = lep_sf*tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF[ilep]
	if itree<16:
		trig_sf = 1- (1-tree.TriggerEffWeight_sngEl)*(1-tree.TriggerEffWeight_sngMu)*(1-tree.TriggerEffWeight_dblEl)*(1-tree.TriggerEffWeight_dblMu)*(1-tree.TriggerEffWeight_ElMu)

	if itree<16:mu_roc_sf = tree.Lepton_rochesterSF[0]*tree.Lepton_rochesterSF[1]

	if (itree==16 or itree==21) and (tree.Trigger_ElMu or not tree.Trigger_dblMu): return 0.
        if (itree==17 or itree==22) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or not tree.Trigger_dblEl):return 0.
        if (itree==18 or itree==23) and (tree.Trigger_ElMu or tree.Trigger_dblMu or not tree.Trigger_sngMu):return 0.
        if (itree==19 or itree==24) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or tree.Trigger_dblEl or not tree.Trigger_sngEl):return 0.
        if (itree==20 or itree==25) and not tree.Trigger_ElMu: return 0.

	if itree<16:
		weight = tree.XSWeight*tree.SFweight2l*tree.GenLepMatch2l*tree.PrefireWeight*tree.METFilter_MC*41.5*bveto_sf*lep_sf*trig_sf*mu_roc_sf
	elif itree<21:
		weight = tree.fakeW2l_ele_mvaFall17V2Iso_WP90_SS_mu_cut_Tight_HWWW*tree.METFilter_FAKE
	else: weight = tree.METFilter_DATA

	return weight


def top_region(tree, ientry,itree):
	weight = 0.
	tree.GetEntry(ientry)

	if ientry%10000 ==0: print 'processing ',ientry
	## lepton selection
	if tree.nLepton != 2 and tree.Lepton_pt[2]>10: return 0
	if itree<16 or itree>20:
		if abs(tree.Lepton_pdgId[0])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0]!=1: return 0 
		if abs(tree.Lepton_pdgId[1])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1]!=1: return 0 
		if abs(tree.Lepton_pdgId[0])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[0]!=1: return 0 
		if abs(tree.Lepton_pdgId[1])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[1]!=1: return 0 
	if sign(tree.Lepton_pdgId[0]) + sign(tree.Lepton_pdgId[1]) ==0: return 0
	if tree.Lepton_pt[0]<30 or tree.Lepton_pt[1]<30: return 0
	if (abs(tree.Lepton_eta[0])>2.5 and abs(tree.Lepton_pdgId[0])==11) or (abs(tree.Lepton_eta[0])>2.4 and abs(tree.Lepton_pdgId[0])==13): return 0
	if (abs(tree.Lepton_eta[1])>2.5 and abs(tree.Lepton_pdgId[1])==11) or (abs(tree.Lepton_eta[1])>2.4 and abs(tree.Lepton_pdgId[1])==13): return 0

	## jets selection
	if tree.mjj<500 or tree.detajj<2.5: return 0
	## MET selection
	if tree.MET_pt<30: return 0
	if tree.zepplep1>0.5 or tree.zepplep2>0.5:return 0

	## veto
	if tree.mll<20: return 0
	l1 = TLorentzVector()
	l2 = TLorentzVector()
	z_window_veto = 0
	if abs(tree.Lepton_pdgId[0])+abs(tree.Lepton_pdgId[1]) ==22:
		l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.000511)
		l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.000511)
		z_window_veto=(l1+l2).M()
#		if abs(tree.Lepton_pdgId[0])==13:
#			l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.10566)
#			l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.10566)
	if abs(z_window_veto - 91.1876)<15: return 0
#	if abs(tree.dmZll_veto - 91.1876)<15: return 0
	
	## b tag
	bveto_sf = 1.
	btag_flag = 0.
	for ijet in tree.CleanJet_jetIdx:
		if tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4 and tree.Jet_btagDeepB[ijet]>0.1522:
			btag_flag = 1.
                if itree<16 and tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4:
			if tree.Jet_btagDeepB[ijet]>0.1522:bveto_sf = bveto_sf*tree.Jet_btagSF[ijet]
			else:
	                        bveto_sf = bveto_sf*(1 - tree.Jet_btagSF[ijet]*btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))/(1 - btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))
                        continue
	if btag_flag==0: return 0

	## tau veto
	for itau in range(0,tree.nTau):
                if tree.Tau_pt[itau] > 18 and tree.Tau_rawIso[itau]>=1 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[0])*(tree.Tau_eta[itau]-tree.Lepton_eta[0]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)) >=0.3 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[1])*(tree.Tau_eta[itau]-tree.Lepton_eta[1]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)) >=0.3:
			return 0
                else: continue

	lep_sf = 1.
	if itree<16:
		for ilep in range(0,len(tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF)):
			lep_sf = lep_sf*tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF[ilep]
		for ilep in range(0,len(tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF)):
			lep_sf = lep_sf*tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF[ilep]
	if itree<16:
		trig_sf = 1- (1-tree.TriggerEffWeight_sngEl)*(1-tree.TriggerEffWeight_sngMu)*(1-tree.TriggerEffWeight_dblEl)*(1-tree.TriggerEffWeight_dblMu)*(1-tree.TriggerEffWeight_ElMu)

	if itree<16:mu_roc_sf = tree.Lepton_rochesterSF[0]*tree.Lepton_rochesterSF[1]

	if (itree==16 or itree==21) and (tree.Trigger_ElMu or not tree.Trigger_dblMu): return 0.
        if (itree==17 or itree==22) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or not tree.Trigger_dblEl):return 0.
        if (itree==18 or itree==23) and (tree.Trigger_ElMu or tree.Trigger_dblMu or not tree.Trigger_sngMu):return 0.
        if (itree==19 or itree==24) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or tree.Trigger_dblEl or not tree.Trigger_sngEl):return 0.
        if (itree==20 or itree==25) and not tree.Trigger_ElMu: return 0.

	if itree<16:
		weight = tree.XSWeight*tree.SFweight2l*tree.GenLepMatch2l*tree.PrefireWeight*tree.METFilter_MC*41.5*bveto_sf*lep_sf*trig_sf*mu_roc_sf
	elif itree<21:
		weight = tree.fakeW2l_ele_mvaFall17V2Iso_WP90_SS_mu_cut_Tight_HWWW*tree.METFilter_FAKE
	else: weight = tree.METFilter_DATA

	return weight
	return 1

def WZ_region(tree, ientry,itree):
        weight = 0.
        tree.GetEntry(ientry)
	if ientry%10000 ==0: print 'processing ',ientry
        ## lepton selection
        if itree<16 or itree>20:
                if abs(tree.Lepton_pdgId[0])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0]!=1: return 0
                if abs(tree.Lepton_pdgId[1])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1]!=1: return 0
                if abs(tree.Lepton_pdgId[2])==11 and tree.Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[2]!=1: return 0
                if abs(tree.Lepton_pdgId[0])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[0]!=1: return 0
                if abs(tree.Lepton_pdgId[1])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[1]!=1: return 0
                if abs(tree.Lepton_pdgId[2])==13 and tree.Lepton_isTightMuon_cut_Tight_HWWW[2]!=1: return 0
	if tree.Lepton_pt[0]<30 or tree.Lepton_pt[1]<30: return 0
	if tree.mjj<500 or tree.detajj<2.5: return 0
        ## MET selection
        if tree.MET_pt<30: return 0
        if tree.zepplep1>0.5 or tree.zepplep2>0.5:return 0
#	if tree.mll<20: return 0
	l1 = TLorentzVector()
        l2 = TLorentzVector()
        l3 = TLorentzVector()
	if abs(sign(tree.Lepton_pdgId[0])+sign(tree.Lepton_pdgId[1])+sign(tree.Lepton_pdgId[2]))==3: return 0
	if abs(tree.Lepton_pdgId[0]+tree.Lepton_pdgId[1]+tree.Lepton_pdgId[2])!=11 and abs(tree.Lepton_pdgId[0]+tree.Lepton_pdgId[1]+tree.Lepton_pdgId[2])!=13: return 0
        if abs(tree.Lepton_pdgId[0])+abs(tree.Lepton_pdgId[1])+abs(tree.Lepton_pdgId[2]) ==33:
                l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.000511)
                l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.000511)
                l3.SetPtEtaPhiM(tree.Lepton_pt[2],tree.Lepton_eta[2],tree.Lepton_phi[2],0.000511)
		if tree.Lepton_pdgId[0]+tree.Lepton_pdgId[1] !=0:
			if abs((l1+l3).M()-91.1876) > 15 and abs((l2+l3).M()-91.1876) > 15: return 0
		elif tree.Lepton_pdgId[0]+tree.Lepton_pdgId[2] ==0:
			if abs((l1+l2).M()-91.1876) > 15 and abs((l1+l3).M()-91.1876) > 15: return 0
		else:
			if abs((l1+l2).M()-91.1876) > 15 and abs((l2+l3).M()-91.1876) > 15: return 0
	elif abs(tree.Lepton_pdgId[0])+abs(tree.Lepton_pdgId[1])+abs(tree.Lepton_pdgId[2]) ==35:
		if abs(tree.Lepton_pdgId[0])==13:
        	        l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.000511)
	                l3.SetPtEtaPhiM(tree.Lepton_pt[2],tree.Lepton_eta[2],tree.Lepton_phi[2],0.000511)
			if abs((l2+l3).M()-91.1876) > 15: return 0
		elif abs(tree.Lepton_pdgId[1])==13:
			l2.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.000511)
                        l3.SetPtEtaPhiM(tree.Lepton_pt[2],tree.Lepton_eta[2],tree.Lepton_phi[2],0.000511)
			if abs((l2+l3).M()-91.1876) > 15: return 0
		else:
			l2.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.000511)
                        l3.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.000511)
			if abs((l2+l3).M()-91.1876) > 15: return 0
	elif abs(tree.Lepton_pdgId[0])+abs(tree.Lepton_pdgId[1])+abs(tree.Lepton_pdgId[2]) ==37:
		if abs(tree.Lepton_pdgId[0])==11:
                        l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.10566)
                        l3.SetPtEtaPhiM(tree.Lepton_pt[2],tree.Lepton_eta[2],tree.Lepton_phi[2],0.10566)
			if abs((l2+l3).M()-91.1876) > 15: return 0
		elif abs(tree.Lepton_pdgId[1])==11:
			l2.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.10566)
                        l3.SetPtEtaPhiM(tree.Lepton_pt[2],tree.Lepton_eta[2],tree.Lepton_phi[2],0.10566)
                        if abs((l2+l3).M()-91.1876) > 15: return 0
		else:
                        l2.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.10566)
                        l3.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.10566)
                        if abs((l2+l3).M()-91.1876) > 15: return 0
	else:
		l1.SetPtEtaPhiM(tree.Lepton_pt[0],tree.Lepton_eta[0],tree.Lepton_phi[0],0.10566)
                l2.SetPtEtaPhiM(tree.Lepton_pt[1],tree.Lepton_eta[1],tree.Lepton_phi[1],0.10566)
                l3.SetPtEtaPhiM(tree.Lepton_pt[2],tree.Lepton_eta[2],tree.Lepton_phi[2],0.10566)
                if tree.Lepton_pdgId[0]+tree.Lepton_pdgId[1] !=0:
                        if abs((l1+l3).M()-91.1876) > 15 and abs((l2+l3).M()-91.1876) > 15: return 0
                elif tree.Lepton_pdgId[0]+tree.Lepton_pdgId[2] ==0:
                        if abs((l1+l2).M()-91.1876) > 15 and abs((l1+l3).M()-91.1876) > 15: return 0
                else:
                        if abs((l1+l2).M()-91.1876) > 15 and abs((l2+l3).M()-91.1876) > 15: return 0
	#b veto
	bveto_sf = 1.
        for ijet in tree.CleanJet_jetIdx:
                if tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4 and tree.Jet_btagDeepB[ijet]>0.1522:
                        return 0
                if itree<16 and tree.Jet_pt[ijet]>20 and abs(tree.Jet_eta[ijet])<2.4:
                        bveto_sf = bveto_sf*(1 - tree.Jet_btagSF[ijet]*btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))/(1 - btag_weight.btag_weight(tree.Jet_partonFlavour[ijet],tree.Jet_pt[ijet],tree.Jet_eta[ijet]))
                        continue

	#4th lepton veto
	for itau in range(0,tree.nTau):
                if tree.Tau_pt[itau] > 18 and tree.Tau_rawIso[itau]>=1 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[0])*(tree.Tau_eta[itau]-tree.Lepton_eta[0]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[0]) - math.pi)- math.pi)) >=0.3 and math.sqrt((tree.Tau_eta[itau]-tree.Lepton_eta[1])*(tree.Tau_eta[itau]-tree.Lepton_eta[1]) + (abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)*(abs(abs(tree.Tau_phi[itau]-tree.Lepton_phi[1]) - math.pi)- math.pi)) >=0.3:
			return 0
	
	
	lep_sf = 1.
        if itree<16:
                for ilep in range(0,len(tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF)):
                        lep_sf = lep_sf*tree.Lepton_tightElectron_mvaFall17V2Iso_WP90_SS_TotSF[ilep]
                for ilep in range(0,len(tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF)):
                        lep_sf = lep_sf*tree.Lepton_tightMuon_cut_Tight_HWWW_TotSF[ilep]
        if itree<16:
                trig_sf = 1- (1-tree.TriggerEffWeight_sngEl)*(1-tree.TriggerEffWeight_sngMu)*(1-tree.TriggerEffWeight_dblEl)*(1-tree.TriggerEffWeight_dblMu)*(1-tree.TriggerEffWeight_ElMu)

        if itree<16:mu_roc_sf = tree.Lepton_rochesterSF[0]*tree.Lepton_rochesterSF[1]*tree.Lepton_rochesterSF[2]

        if (itree==16 or itree==21) and (tree.Trigger_ElMu or not tree.Trigger_dblMu): return 0.
        if (itree==17 or itree==22) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or not tree.Trigger_dblEl):return 0.
        if (itree==18 or itree==23) and (tree.Trigger_ElMu or tree.Trigger_dblMu or not tree.Trigger_sngMu):return 0.
        if (itree==19 or itree==24) and (tree.Trigger_ElMu or tree.Trigger_dblMu or tree.Trigger_sngMu or tree.Trigger_dblEl or not tree.Trigger_sngEl):return 0.
        if (itree==20 or itree==25) and not tree.Trigger_ElMu: return 0.
        if itree<16:
                weight = tree.XSWeight*tree.SFweight3l*tree.GenLepMatch3l*tree.PrefireWeight*tree.METFilter_MC*41.5*bveto_sf*lep_sf*trig_sf*mu_roc_sf
        elif itree<21:
                weight = tree.fakeW2l_ele_mvaFall17V2Iso_WP90_SS_mu_cut_Tight_HWWW*tree.METFilter_FAKE
        else: weight = tree.METFilter_DATA
        return weight

