import ROOT
import numpy as np

import CMSTDRStyle
CMSTDRStyle.setTDRStyle().cd()
import CMSstyle
import cuts
import fileCombine

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

t_DPS = fileCombine.DPS_set()
t_EWK = fileCombine.EWK_set()
t_QCD = fileCombine.QCD_set()
t_WWW = fileCombine.WWW_set()
t_WWZ = fileCombine.WWZ_set()
t_WZTo2L2Q = fileCombine.WZTo2L2Q_set()
t_WZTo3LNu = fileCombine.WZTo3LNu_set()
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

#t_DPS = f_DPS.Get('Events')
#t_EWK = f_EWK.Get('Events')
#t_QCD = f_QCD.Get('Events')
#t_WWW = f_WWW.Get('Events')
#t_WWZ = f_WWZ.Get('Events')
#t_WZTo2L2Q = f_WZTo2L2Q.Get('Events')
#t_WZTo3LNu = f_WZTo3LNu.Get('Events')
#t_WZZ = f_WZZ.Get('Events')
#t_Wg = f_Wg.Get('Events')
#t_ZZTo2L2Nu = f_ZZTo2L2Nu.Get('Events')
#t_ZZTo2L2Q = f_ZZTo2L2Q.Get('Events')
#t_ZZTo4L = f_ZZTo4L.Get('Events')
#t_ZZZ = f_ZZZ.Get('Events')
#t_Zg = f_Zg.Get('Events')
#t_fake_double_muon = f_fake_double_muon.Get('Events')
#t_fake_double_eg = f_fake_double_eg.Get('Events')
#t_fake_single_muon = f_fake_single_muon.Get('Events')
#t_fake_single_eg = f_fake_single_eg.Get('Events')
#t_fake_muon_eg = f_fake_muon_eg.Get('Events')

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
	print 'processing ',name[i]
	for entry in range(0,tree[i].GetEntries()):
		weight = cuts.signal_region(tree[i],entry,i)
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

CMSstyle.SetStyle(pad)

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

#f_DPS.Close()
#f_EWK.Close()
#f_QCD.Close()
#f_WWW.Close()
#f_WWZ.Close()
#f_WZTo2L2Q.Close()
#f_WZTo3LNu.Close()
#f_WZZ.Close()
#f_Wg.Close()
#f_ZZTo2L2Nu.Close()
#f_ZZTo2L2Q.Close()
#f_ZZTo4L.Close()
#f_ZZZ.Close()
#f_Zg.Close()
#f_fake_double_muon.Close()
#f_fake_double_eg.Close()
#f_fake_single_muon.Close()
#f_fake_single_eg.Close()
#f_fake_muon_eg.Close()
