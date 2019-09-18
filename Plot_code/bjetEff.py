import ROOT
from array import array

directory = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv4_Full2017v5/MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5/nanoLatino_TTWjets__part'

bcbins = array('f')
bcbins.append(20)
bcbins.append(30)
bcbins.append(50)
bcbins.append(70)
bcbins.append(100)
bcbins.append(140)
bcbins.append(200)
bcbins.append(300)
bcbins.append(600)
bcbins.append(1000)
bcbins.append(3000)

bcbins_eta = array('f')
bcbins_eta.append(-2.5)
bcbins_eta.append(-0.8)
bcbins_eta.append(0.8)
bcbins_eta.append(2.5)

lbins = array('f')
lbins.append(20)
lbins.append(200)
lbins.append(500)
lbins.append(1000)
lbins.append(3000)

lbins_eta = array('f')
lbins_eta.append(-2.4)
lbins_eta.append(-0.8)
lbins_eta.append(0.8)
lbins_eta.append(2.4)

h2_btag_eff_denom_b = ROOT.TH2F('h2_BTaggingEff_Denom_b',';p_{T} [GeV];#eta',10,bcbins,3,bcbins_eta)
h2_btag_eff_denom_c = ROOT.TH2F('h2_BTaggingEff_Denom_c',';p_{T} [GeV];#eta',10,bcbins,3,bcbins_eta)
h2_btag_eff_denom_usdg = ROOT.TH2F('h2_BTaggingEff_Denom_usdg',';p_{T} [GeV];#eta',4,lbins,3,lbins_eta)
h2_btag_eff_num_b = ROOT.TH2F('h2_BTaggingEff_Num_b',';p_{T} [GeV];#eta',10,bcbins,3,bcbins_eta)
h2_btag_eff_num_c = ROOT.TH2F('h2_BTaggingEff_Num_c',';p_{T} [GeV];#eta',10,bcbins,3,bcbins_eta)
h2_btag_eff_num_usdg = ROOT.TH2F('h2_BTaggingEff_Num_usdg',';p_{T} [GeV];#eta',4,lbins,3,lbins_eta)

chain = ROOT.TChain("Events")
for i in range(0,9):
	chain.Add(directory+str(i)+'.root')

ii=0
for entry in range(0,chain.GetEntries()):
	if ii%10000==0: print 'processing ',entry
	chain.GetEntry(entry)
	for ijet in chain.CleanJet_jetIdx:
		if chain.Jet_partonFlavour[ijet]==5:
			h2_btag_eff_denom_b.Fill(chain.Jet_pt[ijet],chain.Jet_eta[ijet])
			if chain.Jet_btagDeepB[ijet]>0.4941: h2_btag_eff_num_b.Fill(chain.Jet_pt[ijet],chain.Jet_eta[ijet])
		elif chain.Jet_partonFlavour[ijet]==4:
			h2_btag_eff_denom_c.Fill(chain.Jet_pt[ijet],chain.Jet_eta[ijet])
                        if chain.Jet_btagDeepB[ijet]>0.4941: h2_btag_eff_num_c.Fill(chain.Jet_pt[ijet],chain.Jet_eta[ijet])
		else:
			h2_btag_eff_denom_usdg.Fill(chain.Jet_pt[ijet],chain.Jet_eta[ijet])
                        if chain.Jet_btagDeepB[ijet]>0.4941: h2_btag_eff_num_usdg.Fill(chain.Jet_pt[ijet],chain.Jet_eta[ijet])
	ii = ii+1

f = ROOT.TFile('bjetmap.root','RECREATE')
f.cd()
h2_btag_eff_denom_b.Write()
h2_btag_eff_denom_c.Write()
h2_btag_eff_denom_usdg.Write()
h2_btag_eff_num_b.Write()
h2_btag_eff_num_c.Write()
h2_btag_eff_num_usdg.Write()
f.Close()
