import ROOT

f = ROOT.TFile('bjetmap.root')
b_de = ROOT.TH2F()
f.GetObject('h2_BTaggingEff_Denom_b',b_de)
c_de = ROOT.TH2F()
f.GetObject('h2_BTaggingEff_Denom_c',c_de)
usdg_de = ROOT.TH2F()
f.GetObject('h2_BTaggingEff_Denom_usdg',usdg_de)
b_no = ROOT.TH2F()
f.GetObject('h2_BTaggingEff_Num_b',b_no)	
c_no = ROOT.TH2F()
f.GetObject('h2_BTaggingEff_Num_c',c_no)	
usdg_no = ROOT.TH2F()
f.GetObject('h2_BTaggingEff_Num_usdg',usdg_no)

b_eff_eta1 = []
b_eff_eta2 = []
b_eff_eta3 = []
c_eff_eta1 = []
c_eff_eta2 = []
c_eff_eta3 = []
l_eff_eta1 = []
l_eff_eta2 = []
l_eff_eta3 = []

for i in range(1,11):
	b_eff_eta1.append(round(b_no.GetBinContent(i,1)*1.0/b_de.GetBinContent(i,1),3))
	b_eff_eta2.append(round(b_no.GetBinContent(i,2)*1.0/b_de.GetBinContent(i,2),3))
	b_eff_eta3.append(round(b_no.GetBinContent(i,3)*1.0/b_de.GetBinContent(i,3),3))
	c_eff_eta1.append(round(c_no.GetBinContent(i,1)*1.0/c_de.GetBinContent(i,1),3))
	c_eff_eta2.append(round(c_no.GetBinContent(i,2)*1.0/c_de.GetBinContent(i,2),3))
	c_eff_eta3.append(round(c_no.GetBinContent(i,3)*1.0/c_de.GetBinContent(i,3),3))

for i in range(1,5):
	l_eff_eta1.append(round(usdg_no.GetBinContent(i,1)*1.0/usdg_de.GetBinContent(i,1),3))
        l_eff_eta2.append(round(usdg_no.GetBinContent(i,2)*1.0/usdg_de.GetBinContent(i,2),3))
        l_eff_eta3.append(round(usdg_no.GetBinContent(i,3)*1.0/usdg_de.GetBinContent(i,3),3))

print 'b eta1:', b_eff_eta1
print 'b eta2:', b_eff_eta2
print 'b eta3:', b_eff_eta3
print 'c eta1:', c_eff_eta1
print 'c eta1:', c_eff_eta2
print 'c eta1:', c_eff_eta3
print 'light eta1:', l_eff_eta1
print 'light eta1:', l_eff_eta2
print 'light eta1:', l_eff_eta3
