import ROOT
import numpy as np

import CMSTDRStyle
CMSTDRStyle.setTDRStyle().cd()
import mystyle

def set_axis(the_histo, coordinate, title, is_energy):

	if coordinate == 'x':
		axis = the_histo.GetXaxis()
	elif coordinate == 'y':
		axis = the_histo.GetYaxis()
	else:
		raise ValueError('x and y axis only')

	axis.SetLabelFont(42)
	axis.SetLabelOffset(0.015)
	axis.SetLabelSize(0.03)
	axis.SetNdivisions(505)
	axis.SetTitleFont(42)
	axis.SetTitleOffset(1.15)
	axis.SetTitleSize(0.04)
	if (coordinate == "y"):axis.SetTitleOffset(1.2)
	if is_energy:
		axis.SetTitle(title+' (GeV)')
	else:
		axis.SetTitle(title) 

f_DPS = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/DPS.root')
f_EWK = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/EWK.root')
f_QCD = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/QCD.root')
f_WWW = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/WWW.root')
f_WWZ = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/WWZ.root')
f_WZTo2L2Q = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/WZTo2L2Q.root')
f_WZTo3LNu = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/WZTo3LNu.root')
f_WZZ = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/WZZ.root')
f_Wg = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Wg.root')
f_ZZTo2L2Nu = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/ZZTo2L2Nu.root')
f_ZZTo2L2Q = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/ZZTo2L2Q.root')
f_ZZTo4L = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/ZZTo4L.root')
f_ZZZ = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/ZZZ.root')
f_Zg = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Zg.root')
f_fake_double_muon = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Fake_double_Mu.root')
f_fake_double_eg = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Fake_double_EG.root')
f_fake_single_muon = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Fake_single_Mu.root')
f_fake_single_eg = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Fake_single_EG.root')
f_fake_muon_eg = ROOT.TFile('/eos/user/m/melu/ssWW_2017/Smaller_ntuple/Fake_Muon_EG.root')

t_DPS = f_DPS.Get('Events')
t_EWK = f_EWK.Get('Events')
t_QCD = f_QCD.Get('Events')
t_WWW = f_WWW.Get('Events')
t_WWZ = f_WWZ.Get('Events')
t_WZTo2L2Q = f_WZTo2L2Q.Get('Events')
t_WZTo3LNu = f_WZTo3LNu.Get('Events')
t_WZZ = f_WZZ.Get('Events')
t_Wg = f_Wg.Get('Events')
t_ZZTo2L2Nu = f_ZZTo2L2Nu.Get('Events')
t_ZZTo2L2Q = f_ZZTo2L2Q.Get('Events')
t_ZZTo4L = f_ZZTo4L.Get('Events')
t_ZZZ = f_ZZZ.Get('Events')
t_Zg = f_Zg.Get('Events')
t_fake_double_muon = f_fake_double_muon.Get('Events')
t_fake_double_eg = f_fake_double_eg.Get('Events')
t_fake_single_muon = f_fake_single_muon.Get('Events')
t_fake_single_eg = f_fake_single_eg.Get('Events')
t_fake_muon_eg = f_fake_muon_eg.Get('Events')

tree = []
tree.append(t_DPS)
tree.append(t_EWK)
tree.append(t_QCD)
tree.append(t_WWW)
tree.append(t_WWZ)
tree.append(t_ZZZ)
tree.append(t_WZZ)
tree.append(t_WZTo2L2Q)
tree.append(t_WZTo3LNu)
tree.append(t_Wg)
tree.append(t_Zg)
tree.append(t_ZZTo2L2Nu)
tree.append(t_ZZTo2L2Nu)
tree.append(t_ZZTo4L)
tree.append(t_fake_double_muon)
tree.append(t_fake_double_eg)
tree.append(t_fake_single_muon)
tree.append(t_fake_single_eg)
tree.append(t_fake_muon_eg)


name = ['DPS','EWK','QCD','WWW','WWZ','ZZZ','WZZ','WZTo2L2Q','WZTo3LNu','Wg','Zg','ZZTo2L2Nu','ZZTo2L2Nu','ZZTo4L','fake_double_muon','fake_double_eg','fake_single_muon','fake_single_eg','fake_muon_eg']

mjj = []
for i in range(0,len(name)):
	mjj_histo_temp = ROOT.TH1F(name[i], name[i], 15, 500, 2000)
	mjj_histo_temp.Sumw2()
	mjj.append(mjj_histo_temp)

for i in range(0,len(name)):
	for entry in range(0,tree[i].GetEntries()):
		tree[i].GetEntry(entry)
		if i==14 and (tree[i].Trigger_ElMu or not tree[i].Trigger_dblMu): continue
		if i==15 and (tree[i].Trigger_ElMu or tree[i].Trigger_dblMu or tree[i].Trigger_sngEl or not tree[i].Trigger_dblEl):continue
		if i==16 and (tree[i].Trigger_ElMu or tree[i].Trigger_dblMu or not tree[i].Trigger_sngEl):continue
		if i==17 and (tree[i].Trigger_ElMu or tree[i].Trigger_dblMu or tree[i].Trigger_sngEl or tree[i].Trigger_dblEl or not tree[i].Trigger_sngEl):continue
		if i==18 and not tree[i].Trigger_ElMu: continue
		if i<14:
			weight = tree[i].XSWeight*tree[i].SFweight2l*tree[i].GenLepMatch2l*tree[i].METFilter_MC*41.5
		else:
			weight = tree[i].fakeW2l_ele_mvaFall17Iso_WP90_SS_mu_cut_Tight_HWWW*tree[i].METFilter_FAKE
		if tree[i].mjj<2000:mjj[i].Fill(tree[i].mjj, weight)
		else:mjj[i].Fill(1999, weight)

VVV = ROOT.TH1F('VVV','VVV',15,500,2000)
VVV.Sumw2()
VVV.SetFillColor(ROOT.kSpring-9)
VVV.Add(mjj[3])
VVV.Add(mjj[4])
VVV.Add(mjj[5])
VVV.Add(mjj[6])
VV = ROOT.TH1F('VV','VV',15,500,2000)
VV.Sumw2()
VV.SetFillColor(ROOT.kMagenta-10)
VV.Add(mjj[7])	
VV.Add(mjj[8])	
VV.Add(mjj[11])	
VV.Add(mjj[12])	
VV.Add(mjj[13])
Nonprompt = ROOT.TH1F('Nonprompt','Nonprompt',15,500,2000)
Nonprompt.Sumw2()
Nonprompt.SetFillColor(ROOT.kYellow-4)
Nonprompt.Add(mjj[14])
Nonprompt.Add(mjj[15])
Nonprompt.Add(mjj[16])
Nonprompt.Add(mjj[17])
Nonprompt.Add(mjj[18])
Vg = ROOT.TH1F('Vg','Vg',15,500,2000)
Vg.Sumw2()
Vg.SetFillColor(ROOT.kCyan-7)
Vg.Add(mjj[9])
Vg.Add(mjj[10])
mjj[0].SetFillColor(ROOT.kGray)
mjj[1].SetFillColor(ROOT.kBlue-7)
mjj[2].SetFillColor(ROOT.kViolet-4)

h_stack = ROOT.THStack()
h_stack.Add(VV)
h_stack.Add(Vg)
h_stack.Add(VVV)
h_stack.Add(mjj[0])
h_stack.Add(mjj[2])
h_stack.Add(Nonprompt)
h_stack.Add(mjj[1])
h_stack.SetMaximum(h_stack.GetStack().Last().GetBinContent(1)*1.25)

##MC error
h_error = h_stack.GetStack().Last()
h_error.SetBinErrorOption(ROOT.TH1.kPoisson);
binsize = h_error.GetSize()-2;
x = [];
y = [];
xerror_l = [];
xerror_r = [];
yerror_u = [];
yerror_d = [];
for i in range(0,binsize):
	x.append(h_error.GetBinCenter(i+1))
	y.append(h_error.GetBinContent(i+1))
	xerror_l.append(0.5*h_error.GetBinWidth(i+1))
	xerror_r.append(0.5*h_error.GetBinWidth(i+1))
	yerror_u.append(h_error.GetBinErrorUp(i+1))
	yerror_d.append(h_error.GetBinErrorLow(i+1))
gr = ROOT.TGraphAsymmErrors(len(x), np.array(x), np.array(y),np.array(xerror_l),np.array(xerror_r), np.array(yerror_d), np.array(yerror_u))

VV_yield =round(VV.Integral(),1)
VVV_yield =round(VVV.Integral(),1)
Vg_yield =round(Vg.Integral(),1)
fake_yield = round(Nonprompt.Integral(),1)
DPS_yield = round(mjj[0].Integral(),1)
QCD_yield = round(mjj[2].Integral(),1)
signal_yield = round(mjj[1].Integral(),1)
c = ROOT.TCanvas()
pad = ROOT.TPad()
pad.Draw()
h_stack.Draw('HIST')

gr.SetFillColor(1);
gr.SetFillStyle(3005);
gr.Draw("SAME 2");
set_axis(h_stack,'x', 'm_{jj}', True)
set_axis(h_stack,'y', 'Event/Bin', False)

##CMS style
latex = ROOT.TLatex();
latex.SetNDC()
l = pad.GetLeftMargin();
t = pad.GetTopMargin();
r = pad.GetRightMargin();
b = pad.GetBottomMargin();

#CMS text
cmsText = "CMS";
cmsTextFont = 60;
cmsTextSize = 0.6;
cmsTextOffset = 0.1;
relPosX = 0.12;
relPosY = 0.035;

# extra 
extraText = "  Preliminary";
extraOverCmsTextSize = 0.76;
extraTextFont = 52

lumiText = "41.5 fb^{-1} (13 TeV)";
lumiTextSize = 0.5;
lumiTextOffset = 0.2;
relExtraDY = 1.2;


latex.SetTextAngle(0);
latex.SetTextColor(ROOT.kBlack);
extraTextSize = extraOverCmsTextSize * cmsTextSize;
latex.SetTextFont(42);

latex.SetTextFont(42);
latex.SetTextAlign(31);
latex.SetTextSize(lumiTextSize * t);
latex.DrawLatex(1 - r, 1 - t + lumiTextOffset * t, lumiText);

latex.SetTextFont(cmsTextFont);
latex.SetTextAlign(11);
latex.SetTextSize(cmsTextSize * t);
latex.DrawLatex(l, 1 - t + lumiTextOffset * t, cmsText);

posX_ = 0
posX_ = l + relPosX * (1 - l - r);
posY_ = 1 - t - relPosY * (1 - t - b);
posX_ = l + relPosX * (1 - l - r);
posY_ = 1 - t + lumiTextOffset * t;
alignX_ = 1;
alignY_ = 1;
align_ = 10 * alignX_ + alignY_;
latex.SetTextFont(extraTextFont);
latex.SetTextSize(extraTextSize * t);
latex.SetTextAlign(align_);
latex.DrawLatex(posX_, posY_, extraText);
latex.SetTextAlign(31);
latex.SetTextSize(lumiTextSize * t);

##legend
leg1 = ROOT.TLegend(0.72, 0.72, 0.94, 0.88)
leg2 = ROOT.TLegend(0.34, 0.72, 0.72, 0.88)
leg1.SetMargin(0.4)
leg2.SetMargin(0.4)
leg1.AddEntry(mjj[0], 'DPS ['+str(DPS_yield)+']','f')
leg1.AddEntry(VVV, 'VVV ['+str(VVV_yield)+']','f')
leg1.AddEntry(Vg, 'Vg ['+str(Vg_yield)+']','f')
leg1.AddEntry(VV, 'VV ['+str(VV_yield)+']','f')
leg2.AddEntry(gr,'Stat. Unc','f')
leg2.AddEntry(mjj[1],'EWK ssWW ['+str(signal_yield)+']','f')
leg2.AddEntry(Nonprompt,'Nonprompt ['+str(fake_yield)+']','f')
leg2.AddEntry(mjj[2],'QCD ssWW ['+str(QCD_yield)+']','f')
leg1.SetFillColor(ROOT.kWhite);
leg1.Draw('same');
leg2.SetFillColor(ROOT.kWhite);
leg2.Draw('same');

c.Update()
c.SaveAs('test.png')
c.SaveAs('test.pdf')

pad.Close()
del tree[0:]
del mjj[0:]

f_DPS.Close()
f_EWK.Close()
f_QCD.Close()
f_WWW.Close()
f_WWZ.Close()
f_WZTo2L2Q.Close()
f_WZTo3LNu.Close()
f_WZZ.Close()
f_Wg.Close()
f_ZZTo2L2Nu.Close()
f_ZZTo2L2Q.Close()
f_ZZTo4L.Close()
f_ZZZ.Close()
f_Zg.Close()
f_fake_double_muon.Close()
f_fake_double_eg.Close()
f_fake_single_muon.Close()
f_fake_single_eg.Close()
f_fake_muon_eg.Close()
