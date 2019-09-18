import ROOT
import numpy as np

import cuts
import fileCombine
import plot 
from array import array
from numpy import sign


t_DPS = fileCombine.DPS_set()
t_EWK = fileCombine.EWK_set()
t_QCD = fileCombine.QCD_set()
t_WWW = fileCombine.WWW_set()
t_WWZ = fileCombine.WWZ_set()
t_WWG = fileCombine.WWG_set()
t_WZTo2L2Q = fileCombine.WZTo2L2Q_set()
t_WZTo3LNu = fileCombine.WZTo3LNu_set()
t_WZTo3LNu_EWK = fileCombine.WZTo3LNu_EWK_set()
t_WZZ = fileCombine.WZZ_set()
t_Wg = fileCombine.Wg_set()
t_ZZTo2L2Nu = fileCombine.ZZTo2L2Nu_set()
t_ZZTo2L2Q = fileCombine.ZZTo2L2Q_set()
t_ZZTo4L = fileCombine.ZZTo4L_set()
t_ZZZ = fileCombine.ZZZ_set()
t_Zg = fileCombine.Zg_set()
t_fake_double_muon = fileCombine.fake_double_mu_set()
t_fake_double_eg = fileCombine.fake_double_ele_set()
t_fake_single_muon = fileCombine.fake_single_muon_set()
t_fake_single_eg = fileCombine.fake_single_ele_set()
t_fake_muon_eg = fileCombine.fake_muon_ele_set()
t_double_muon = fileCombine.double_mu_set()
t_double_eg = fileCombine.double_ele_set()
t_single_muon = fileCombine.single_muon_set()
t_single_eg = fileCombine.single_ele_set()
t_muon_eg = fileCombine.muon_ele_set()


tree = []
tree.append(t_DPS)
tree.append(t_EWK)
tree.append(t_QCD)
tree.append(t_WWW)
tree.append(t_WWZ)
tree.append(t_WWG)
tree.append(t_ZZZ)
tree.append(t_WZZ)
tree.append(t_WZTo2L2Q)
tree.append(t_WZTo3LNu)
tree.append(t_WZTo3LNu_EWK)
tree.append(t_Wg)
tree.append(t_Zg)
tree.append(t_ZZTo2L2Nu)
tree.append(t_ZZTo2L2Q)
tree.append(t_ZZTo4L)
tree.append(t_fake_double_muon)
tree.append(t_fake_double_eg)
tree.append(t_fake_single_muon)
tree.append(t_fake_single_eg)
tree.append(t_fake_muon_eg)
tree.append(t_double_muon)
tree.append(t_double_eg)
tree.append(t_single_muon)
tree.append(t_single_eg)
tree.append(t_muon_eg)


name = ['DPS','EWK','QCD','WWW','WWZ','WWG','ZZZ','WZZ','WZTo2L2Q','WZTo3LNu','WZTo3LNu_EWK','Wg','Zg','ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L','fake_double_muon','fake_double_eg','fake_single_muon','fake_single_eg','fake_muon_eg','double_muon','double_eg','single_muon','single_eg','muon_eg']#26

h_mjj = []
h_mll = []
bins = array('f')
bins.append(500.)
bins.append(800.)
bins.append(1200.)
bins.append(1600.)
bins.append(2000.)
for i in range(0,len(name)):
	h_mjj_histo_temp = ROOT.TH1F(name[i]+' mjj', name[i], 4, bins)
	h_mjj_histo_temp.Sumw2()
	h_mjj.append(h_mjj_histo_temp)
	h_mll_histo_temp = ROOT.TH1F(name[i]+' mll', name[i], 12, 20, 320)
	h_mll_histo_temp.Sumw2()
	h_mll.append(h_mll_histo_temp)

for i in range(0,len(name)):
	print 'processing ',name[i]
	for entry in range(0,tree[i].GetEntries()):
	#	tree[i].GetEntry(entry)
	#	if tree[i].nLepton>2 and tree[i].Lepton_pt[2]>10: continue
	#	if sign(tree[i].Lepton_pdgId[0])+sign(tree[i].Lepton_pdgId[1])==0: continue
	#	if (abs(tree[i].Lepton_eta[0])>2.4 and abs(tree[i].Lepton_pdgId[0])==11) or (abs(tree[i].Lepton_eta[0])>2.5 and abs(tree[i].Leptons_pdgId[0])==13):continue
	#	if (abs(tree[i].Lepton_eta[1])>2.4 and abs(tree[i].Lepton_pdgId[1])==11) or (abs(tree[i].Lepton_eta[1])>2.5 and abs(tree[i].Leptons_pdgId[1])==13):continue
	#	if tree[i].mjj<500 or tree[i].detajj<2.5:continue
	#	if tree[i].mll<10 or tree[i].dmZll_veto<10:continue
	#	weight = cuts.top_region(tree[i],entry,i)
	#	weight = cuts.lowmjj_region(tree[i],entry,i)
		weight = cuts.signal_region(tree[i],entry,i)
	#	weight = cuts.WZ_region(tree[i],entry,i)
		if tree[i].mjj<2000:h_mjj[i].Fill(tree[i].mjj,weight)
		else:h_mjj[i].Fill(1999, weight)
	#	if tree[i].mll<320:h_mll[i].Fill(tree[i].mll, weight)
	#	else:h_mll[i].Fill(319, weight)
#c_mll = plot.draw_plots(h_mll, 1, 'mll_mbveto')
c_mjj = plot.draw_plots(h_mjj, 0, 'wz_mediumb_mjj')
