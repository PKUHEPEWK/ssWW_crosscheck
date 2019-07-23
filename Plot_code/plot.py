import ROOT
import numpy as np

import CMSTDRStyle
CMSTDRStyle.setTDRStyle().cd()
import CMSstyle
from array import array

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

def draw_plots(hist_array =[], draw_data=0, x_name=''):

	VVV = hist_array[3].Clone()
	VVV.SetFillColor(ROOT.kSpring-9)
	VVV.Add(hist_array[4])
	VVV.Add(hist_array[5])
	VVV.Add(hist_array[6])

	VV = hist_array[7].Clone()
	VV.SetFillColor(ROOT.kMagenta-10)
	VV.Add(hist_array[8])	
	VV.Add(hist_array[11])	
	VV.Add(hist_array[12])	
	VV.Add(hist_array[13])

	Nonprompt = hist_array[14].Clone()
	Nonprompt.SetFillColor(ROOT.kYellow-4)
	Nonprompt.Add(hist_array[15])
	Nonprompt.Add(hist_array[16])
	Nonprompt.Add(hist_array[17])
	Nonprompt.Add(hist_array[18])

	Vg = hist_array[9].Clone()
	Vg.SetFillColor(ROOT.kCyan-7)
	Vg.Add(hist_array[10])
	hist_array[0].SetFillColor(ROOT.kGray)
	hist_array[1].SetFillColor(ROOT.kBlue-7)
	hist_array[2].SetFillColor(ROOT.kViolet-4)
	
	Data = hist_array[19].Clone()
	Data.Add(hist_array[20])
	Data.Add(hist_array[21])
	Data.Add(hist_array[22])
	Data.Add(hist_array[23])
	if not draw_data: Data.Reset('ICE')
	
	Data.SetMarkerStyle(20)
	Data.SetMarkerColor(1)
	Data.SetLineWidth(1)
	
	
	h_stack = ROOT.THStack()
	h_stack.Add(VV)
	h_stack.Add(Vg)
	h_stack.Add(VVV)
	h_stack.Add(hist_array[0])
	h_stack.Add(hist_array[2])
	h_stack.Add(Nonprompt)
	h_stack.Add(hist_array[1])
	max_yields = 0
	for i in range(1,16):
		max_yields_temp = h_stack.GetStack().Last().GetBinContent(i)
		if max_yields_temp>max_yields:max_yields=max_yields_temp
	h_stack.SetMaximum(max_yields*2.)
	
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
	DPS_yield = round(hist_array[0].Integral(),1)
	QCD_yield = round(hist_array[2].Integral(),1)
	signal_yield = round(hist_array[1].Integral(),1)
	c = ROOT.TCanvas()
	pad = ROOT.TPad()
	pad.Draw()
	h_stack.Draw('HIST')
	Data.Draw("SAME pe")
	
	gr.SetFillColor(1);
	gr.SetFillStyle(3005);
	gr.Draw("SAME 2");
	if 'mjj' in x_name:set_axis(h_stack,'x', 'm_{jj}', True)
	if 'mll' in x_name:set_axis(h_stack,'x', 'm_{ll}', True)
	set_axis(h_stack,'y', 'Event/Bin', False)
	
	CMSstyle.SetStyle(pad)
	
	##legend
	leg1 = ROOT.TLegend(0.72, 0.72, 0.94, 0.88)
	leg2 = ROOT.TLegend(0.34, 0.68, 0.72, 0.88)
	leg1.SetMargin(0.4)
	leg2.SetMargin(0.4)
	leg1.AddEntry(hist_array[0], 'DPS ['+str(DPS_yield)+']','f')
	leg1.AddEntry(VVV, 'VVV ['+str(VVV_yield)+']','f')
	leg1.AddEntry(Vg, 'Vg ['+str(Vg_yield)+']','f')
	leg1.AddEntry(VV, 'VV ['+str(VV_yield)+']','f')
	leg2.AddEntry(Data,'Data','lpe')
	leg2.AddEntry(gr,'Stat. Unc','f')
	leg2.AddEntry(hist_array[1],'EWK ssWW ['+str(signal_yield)+']','f')
	leg2.AddEntry(Nonprompt,'Nonprompt ['+str(fake_yield)+']','f')
	leg2.AddEntry(hist_array[2],'QCD ssWW ['+str(QCD_yield)+']','f')
	leg1.SetFillColor(ROOT.kWhite);
	leg1.Draw('same');
	leg2.SetFillColor(ROOT.kWhite);
	leg2.Draw('same');
	
	c.Update()
	c.SaveAs(x_name+'.pdf')
	c.SaveAs(x_name+'.png')
	return c
	pad.Close()
	del hist_array
	
