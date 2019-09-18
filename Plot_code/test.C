void test()
{
//=========Macro generated from canvas: c1/c1
//=========  (Thu Jul 18 16:40:56 2019) by ROOT version6.10/09
   TCanvas *c1 = new TCanvas("c1", "c1",0,0,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   c1->SetHighLightColor(2);
   c1->Range(218.75,-11.42954,2093.75,76.49001);
   c1->SetFillColor(0);
   c1->SetBorderMode(0);
   c1->SetBorderSize(2);
   c1->SetTickx(1);
   c1->SetTicky(1);
   c1->SetLeftMargin(0.15);
   c1->SetRightMargin(0.05);
   c1->SetBottomMargin(0.13);
   c1->SetFrameFillStyle(0);
   c1->SetFrameBorderMode(0);
   c1->SetFrameFillStyle(0);
   c1->SetFrameBorderMode(0);
   
   THStack * = new THStack();
   ->SetName("");
   ->SetTitle("");
   ->SetMaximum(65.31167);
   Double_t xAxis1[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *_stack_1 = new TH1F("_stack_1","",4, xAxis1);
   _stack_1->SetMinimum(0);
   _stack_1->SetMaximum(68.57725);
   _stack_1->SetDirectory(0);
   _stack_1->SetStats(0);
   _stack_1->SetLineStyle(0);
   _stack_1->SetLineWidth(0);
   _stack_1->SetMarkerStyle(20);
   _stack_1->GetXaxis()->SetTitle("m_{jj} (GeV)");
   _stack_1->GetXaxis()->SetNdivisions(505);
   _stack_1->GetXaxis()->SetLabelFont(42);
   _stack_1->GetXaxis()->SetLabelOffset(0.015);
   _stack_1->GetXaxis()->SetLabelSize(0.03);
   _stack_1->GetXaxis()->SetTitleOffset(1.15);
   _stack_1->GetXaxis()->SetTitleFont(42);
   _stack_1->GetYaxis()->SetTitle("Event/Bin");
   _stack_1->GetYaxis()->SetNdivisions(505);
   _stack_1->GetYaxis()->SetLabelFont(42);
   _stack_1->GetYaxis()->SetLabelOffset(0.015);
   _stack_1->GetYaxis()->SetLabelSize(0.03);
   _stack_1->GetYaxis()->SetTitleOffset(1.2);
   _stack_1->GetYaxis()->SetTitleFont(42);
   _stack_1->GetZaxis()->SetLabelFont(42);
   _stack_1->GetZaxis()->SetLabelOffset(0.007);
   _stack_1->GetZaxis()->SetTitleSize(0.06);
   _stack_1->GetZaxis()->SetTitleFont(42);
   ->SetHistogram(_stack_1);
   
   Double_t xAxis2[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *VV_stack_1 = new TH1F("VV_stack_1","VV",4, xAxis2);
   VV_stack_1->SetBinContent(1,0.4431463);
   VV_stack_1->SetBinContent(2,0.04857324);
   VV_stack_1->SetBinContent(4,0.001692434);
   VV_stack_1->SetBinError(1,0.2817317);
   VV_stack_1->SetBinError(2,0.04092386);
   VV_stack_1->SetBinError(4,0.001692434);
   VV_stack_1->SetEntries(893);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ffccff");
   VV_stack_1->SetFillColor(ci);
   VV_stack_1->SetLineStyle(0);
   VV_stack_1->SetLineWidth(0);
   VV_stack_1->SetMarkerStyle(20);
   VV_stack_1->GetXaxis()->SetLabelFont(42);
   VV_stack_1->GetXaxis()->SetLabelOffset(0.007);
   VV_stack_1->GetXaxis()->SetTitleSize(0.06);
   VV_stack_1->GetXaxis()->SetTitleOffset(0.9);
   VV_stack_1->GetXaxis()->SetTitleFont(42);
   VV_stack_1->GetYaxis()->SetLabelFont(42);
   VV_stack_1->GetYaxis()->SetLabelOffset(0.007);
   VV_stack_1->GetYaxis()->SetTitleSize(0.06);
   VV_stack_1->GetYaxis()->SetTitleOffset(1.1);
   VV_stack_1->GetYaxis()->SetTitleFont(42);
   VV_stack_1->GetZaxis()->SetLabelFont(42);
   VV_stack_1->GetZaxis()->SetLabelOffset(0.007);
   VV_stack_1->GetZaxis()->SetTitleSize(0.06);
   VV_stack_1->GetZaxis()->SetTitleFont(42);
   ->Add(VV_stack_1,"");
   Double_t xAxis3[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *Vg_stack_2 = new TH1F("Vg_stack_2","Vg",4, xAxis3);
   Vg_stack_2->SetEntries(154);

   ci = TColor::GetColor("#66ffff");
   Vg_stack_2->SetFillColor(ci);
   Vg_stack_2->SetLineStyle(0);
   Vg_stack_2->SetLineWidth(0);
   Vg_stack_2->SetMarkerStyle(20);
   Vg_stack_2->GetXaxis()->SetLabelFont(42);
   Vg_stack_2->GetXaxis()->SetLabelOffset(0.007);
   Vg_stack_2->GetXaxis()->SetTitleSize(0.06);
   Vg_stack_2->GetXaxis()->SetTitleOffset(0.9);
   Vg_stack_2->GetXaxis()->SetTitleFont(42);
   Vg_stack_2->GetYaxis()->SetLabelFont(42);
   Vg_stack_2->GetYaxis()->SetLabelOffset(0.007);
   Vg_stack_2->GetYaxis()->SetTitleSize(0.06);
   Vg_stack_2->GetYaxis()->SetTitleOffset(1.1);
   Vg_stack_2->GetYaxis()->SetTitleFont(42);
   Vg_stack_2->GetZaxis()->SetLabelFont(42);
   Vg_stack_2->GetZaxis()->SetLabelOffset(0.007);
   Vg_stack_2->GetZaxis()->SetTitleSize(0.06);
   Vg_stack_2->GetZaxis()->SetTitleFont(42);
   ->Add(Vg_stack_2,"");
   Double_t xAxis4[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *VVV_stack_3 = new TH1F("VVV_stack_3","VVV",4, xAxis4);
   VVV_stack_3->SetBinContent(1,0.01161067);
   VVV_stack_3->SetBinContent(2,0.0258127);
   VVV_stack_3->SetBinError(1,0.0114277);
   VVV_stack_3->SetBinError(2,0.0258127);
   VVV_stack_3->SetEntries(95);

   ci = TColor::GetColor("#99ff33");
   VVV_stack_3->SetFillColor(ci);
   VVV_stack_3->SetLineStyle(0);
   VVV_stack_3->SetLineWidth(0);
   VVV_stack_3->SetMarkerStyle(20);
   VVV_stack_3->GetXaxis()->SetLabelFont(42);
   VVV_stack_3->GetXaxis()->SetLabelOffset(0.007);
   VVV_stack_3->GetXaxis()->SetTitleSize(0.06);
   VVV_stack_3->GetXaxis()->SetTitleOffset(0.9);
   VVV_stack_3->GetXaxis()->SetTitleFont(42);
   VVV_stack_3->GetYaxis()->SetLabelFont(42);
   VVV_stack_3->GetYaxis()->SetLabelOffset(0.007);
   VVV_stack_3->GetYaxis()->SetTitleSize(0.06);
   VVV_stack_3->GetYaxis()->SetTitleOffset(1.1);
   VVV_stack_3->GetYaxis()->SetTitleFont(42);
   VVV_stack_3->GetZaxis()->SetLabelFont(42);
   VVV_stack_3->GetZaxis()->SetLabelOffset(0.007);
   VVV_stack_3->GetZaxis()->SetTitleSize(0.06);
   VVV_stack_3->GetZaxis()->SetTitleFont(42);
   ->Add(VVV_stack_3,"");
   Double_t xAxis5[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *DPS_stack_4 = new TH1F("DPS_stack_4","DPS",4, xAxis5);
   DPS_stack_4->SetBinContent(1,0.006221681);
   DPS_stack_4->SetBinError(1,0.005411647);
   DPS_stack_4->SetEntries(157);

   ci = TColor::GetColor("#cccccc");
   DPS_stack_4->SetFillColor(ci);
   DPS_stack_4->SetLineStyle(0);
   DPS_stack_4->SetLineWidth(0);
   DPS_stack_4->SetMarkerStyle(20);
   DPS_stack_4->GetXaxis()->SetLabelFont(42);
   DPS_stack_4->GetXaxis()->SetLabelOffset(0.007);
   DPS_stack_4->GetXaxis()->SetTitleSize(0.06);
   DPS_stack_4->GetXaxis()->SetTitleOffset(0.9);
   DPS_stack_4->GetXaxis()->SetTitleFont(42);
   DPS_stack_4->GetYaxis()->SetLabelFont(42);
   DPS_stack_4->GetYaxis()->SetLabelOffset(0.007);
   DPS_stack_4->GetYaxis()->SetTitleSize(0.06);
   DPS_stack_4->GetYaxis()->SetTitleOffset(1.1);
   DPS_stack_4->GetYaxis()->SetTitleFont(42);
   DPS_stack_4->GetZaxis()->SetLabelFont(42);
   DPS_stack_4->GetZaxis()->SetLabelOffset(0.007);
   DPS_stack_4->GetZaxis()->SetTitleSize(0.06);
   DPS_stack_4->GetZaxis()->SetTitleFont(42);
   ->Add(DPS_stack_4,"");
   Double_t xAxis6[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *QCD_stack_5 = new TH1F("QCD_stack_5","QCD",4, xAxis6);
   QCD_stack_5->SetBinContent(1,0.05484344);
   QCD_stack_5->SetBinContent(2,0.01711827);
   QCD_stack_5->SetBinContent(3,0.00183533);
   QCD_stack_5->SetBinContent(4,0.0004155916);
   QCD_stack_5->SetBinError(1,0.01551364);
   QCD_stack_5->SetBinError(2,0.008785074);
   QCD_stack_5->SetBinError(3,0.00183533);
   QCD_stack_5->SetBinError(4,0.0003917325);
   QCD_stack_5->SetEntries(1361);

   ci = TColor::GetColor("#cc66ff");
   QCD_stack_5->SetFillColor(ci);
   QCD_stack_5->SetLineStyle(0);
   QCD_stack_5->SetLineWidth(0);
   QCD_stack_5->SetMarkerStyle(20);
   QCD_stack_5->GetXaxis()->SetLabelFont(42);
   QCD_stack_5->GetXaxis()->SetLabelOffset(0.007);
   QCD_stack_5->GetXaxis()->SetTitleSize(0.06);
   QCD_stack_5->GetXaxis()->SetTitleOffset(0.9);
   QCD_stack_5->GetXaxis()->SetTitleFont(42);
   QCD_stack_5->GetYaxis()->SetLabelFont(42);
   QCD_stack_5->GetYaxis()->SetLabelOffset(0.007);
   QCD_stack_5->GetYaxis()->SetTitleSize(0.06);
   QCD_stack_5->GetYaxis()->SetTitleOffset(1.1);
   QCD_stack_5->GetYaxis()->SetTitleFont(42);
   QCD_stack_5->GetZaxis()->SetLabelFont(42);
   QCD_stack_5->GetZaxis()->SetLabelOffset(0.007);
   QCD_stack_5->GetZaxis()->SetTitleSize(0.06);
   QCD_stack_5->GetZaxis()->SetTitleFont(42);
   ->Add(QCD_stack_5,"");
   Double_t xAxis7[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *Nonprompt_stack_6 = new TH1F("Nonprompt_stack_6","Nonprompt",4, xAxis7);
   Nonprompt_stack_6->SetBinContent(1,39.92035);
   Nonprompt_stack_6->SetBinContent(2,13.18336);
   Nonprompt_stack_6->SetBinContent(3,5.454594);
   Nonprompt_stack_6->SetBinContent(4,4.944594);
   Nonprompt_stack_6->SetBinError(1,4.500458);
   Nonprompt_stack_6->SetBinError(2,2.442512);
   Nonprompt_stack_6->SetBinError(3,1.389599);
   Nonprompt_stack_6->SetBinError(4,1.654178);
   Nonprompt_stack_6->SetEntries(8099);

   ci = TColor::GetColor("#ffff33");
   Nonprompt_stack_6->SetFillColor(ci);
   Nonprompt_stack_6->SetLineStyle(0);
   Nonprompt_stack_6->SetLineWidth(0);
   Nonprompt_stack_6->SetMarkerStyle(20);
   Nonprompt_stack_6->GetXaxis()->SetLabelFont(42);
   Nonprompt_stack_6->GetXaxis()->SetLabelOffset(0.007);
   Nonprompt_stack_6->GetXaxis()->SetTitleSize(0.06);
   Nonprompt_stack_6->GetXaxis()->SetTitleOffset(0.9);
   Nonprompt_stack_6->GetXaxis()->SetTitleFont(42);
   Nonprompt_stack_6->GetYaxis()->SetLabelFont(42);
   Nonprompt_stack_6->GetYaxis()->SetLabelOffset(0.007);
   Nonprompt_stack_6->GetYaxis()->SetTitleSize(0.06);
   Nonprompt_stack_6->GetYaxis()->SetTitleOffset(1.1);
   Nonprompt_stack_6->GetYaxis()->SetTitleFont(42);
   Nonprompt_stack_6->GetZaxis()->SetLabelFont(42);
   Nonprompt_stack_6->GetZaxis()->SetLabelOffset(0.007);
   Nonprompt_stack_6->GetZaxis()->SetTitleSize(0.06);
   Nonprompt_stack_6->GetZaxis()->SetTitleFont(42);
   ->Add(Nonprompt_stack_6,"");
   Double_t xAxis8[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *EWK_stack_7 = new TH1F("EWK_stack_7","EWK",4, xAxis8);
   EWK_stack_7->SetBinContent(1,0.3836178);
   EWK_stack_7->SetBinContent(2,0.4758588);
   EWK_stack_7->SetBinContent(3,0.3106417);
   EWK_stack_7->SetBinContent(4,0.3322596);
   EWK_stack_7->SetBinError(1,0.04472116);
   EWK_stack_7->SetBinError(2,0.04676623);
   EWK_stack_7->SetBinError(3,0.03759675);
   EWK_stack_7->SetBinError(4,0.03677736);
   EWK_stack_7->SetEntries(14547);

   ci = TColor::GetColor("#6666ff");
   EWK_stack_7->SetFillColor(ci);
   EWK_stack_7->SetLineStyle(0);
   EWK_stack_7->SetLineWidth(0);
   EWK_stack_7->SetMarkerStyle(20);
   EWK_stack_7->GetXaxis()->SetLabelFont(42);
   EWK_stack_7->GetXaxis()->SetLabelOffset(0.007);
   EWK_stack_7->GetXaxis()->SetTitleSize(0.06);
   EWK_stack_7->GetXaxis()->SetTitleOffset(0.9);
   EWK_stack_7->GetXaxis()->SetTitleFont(42);
   EWK_stack_7->GetYaxis()->SetLabelFont(42);
   EWK_stack_7->GetYaxis()->SetLabelOffset(0.007);
   EWK_stack_7->GetYaxis()->SetTitleSize(0.06);
   EWK_stack_7->GetYaxis()->SetTitleOffset(1.1);
   EWK_stack_7->GetYaxis()->SetTitleFont(42);
   EWK_stack_7->GetZaxis()->SetLabelFont(42);
   EWK_stack_7->GetZaxis()->SetLabelOffset(0.007);
   EWK_stack_7->GetZaxis()->SetTitleSize(0.06);
   EWK_stack_7->GetZaxis()->SetTitleFont(42);
   ->Add(EWK_stack_7,"");
   ->Draw("hist");
   Double_t xAxis9[5] = {500, 800, 1200, 1600, 2000}; 
   
   TH1F *Data__1 = new TH1F("Data__1","Data",4, xAxis9);
   Data__1->SetBinContent(1,44);
   Data__1->SetBinContent(2,21);
   Data__1->SetBinContent(3,8);
   Data__1->SetBinContent(4,8);
   Data__1->SetBinError(1,6.63325);
   Data__1->SetBinError(2,4.582576);
   Data__1->SetBinError(3,2.828427);
   Data__1->SetBinError(4,2.828427);
   Data__1->SetEntries(2749);
   Data__1->SetLineStyle(0);
   Data__1->SetMarkerStyle(20);
   Data__1->GetXaxis()->SetLabelFont(42);
   Data__1->GetXaxis()->SetLabelOffset(0.007);
   Data__1->GetXaxis()->SetTitleSize(0.06);
   Data__1->GetXaxis()->SetTitleOffset(0.9);
   Data__1->GetXaxis()->SetTitleFont(42);
   Data__1->GetYaxis()->SetLabelFont(42);
   Data__1->GetYaxis()->SetLabelOffset(0.007);
   Data__1->GetYaxis()->SetTitleSize(0.06);
   Data__1->GetYaxis()->SetTitleOffset(1.1);
   Data__1->GetYaxis()->SetTitleFont(42);
   Data__1->GetZaxis()->SetLabelFont(42);
   Data__1->GetZaxis()->SetLabelOffset(0.007);
   Data__1->GetZaxis()->SetTitleSize(0.06);
   Data__1->GetZaxis()->SetTitleFont(42);
   Data__1->Draw("SAME pe");
   
   Double_t Graph0_fx3001[4] = {
   650,
   1000,
   1400,
   1800};
   Double_t Graph0_fy3001[4] = {
   40.81979,
   13.75072,
   5.767071,
   5.278962};
   Double_t Graph0_felx3001[4] = {
   150,
   200,
   200,
   200};
   Double_t Graph0_fely3001[4] = {
   4.509534,
   2.443454,
   1.390109,
   1.654588};
   Double_t Graph0_fehx3001[4] = {
   150,
   200,
   200,
   200};
   Double_t Graph0_fehy3001[4] = {
   4.509534,
   2.443454,
   1.390109,
   1.654588};
   TGraphAsymmErrors *grae = new TGraphAsymmErrors(4,Graph0_fx3001,Graph0_fy3001,Graph0_felx3001,Graph0_fehx3001,Graph0_fely3001,Graph0_fehy3001);
   grae->SetName("Graph0");
   grae->SetTitle("Graph");
   grae->SetFillColor(1);
   grae->SetFillStyle(3005);
   grae->SetMarkerStyle(20);
   
   TH1F *Graph_Graph3001 = new TH1F("Graph_Graph3001","Graph",100,350,2150);
   Graph_Graph3001->SetMinimum(3.261937);
   Graph_Graph3001->SetMaximum(49.49982);
   Graph_Graph3001->SetDirectory(0);
   Graph_Graph3001->SetStats(0);
   Graph_Graph3001->SetLineStyle(0);
   Graph_Graph3001->SetLineWidth(0);
   Graph_Graph3001->SetMarkerStyle(20);
   Graph_Graph3001->GetXaxis()->SetLabelFont(42);
   Graph_Graph3001->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph3001->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph3001->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph3001->GetXaxis()->SetTitleFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelFont(42);
   Graph_Graph3001->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph3001->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph3001->GetYaxis()->SetTitleOffset(1.1);
   Graph_Graph3001->GetYaxis()->SetTitleFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelFont(42);
   Graph_Graph3001->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph3001->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph3001->GetZaxis()->SetTitleFont(42);
   grae->SetHistogram(Graph_Graph3001);
   
   grae->Draw(" 2");
   TLatex *   tex = new TLatex(0.95,0.928,"41.5 fb^{-1} (13 TeV)");
tex->SetNDC();
   tex->SetTextAlign(31);
   tex->SetTextFont(42);
   tex->SetTextSize(0.045);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.15,0.928,"CMS");
tex->SetNDC();
   tex->SetTextFont(60);
   tex->SetTextSize(0.054);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.246,0.928,"  Preliminary");
tex->SetNDC();
   tex->SetTextFont(52);
   tex->SetTextSize(0.04104);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TLegend *leg = new TLegend(0.72,0.72,0.94,0.88,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("DPS_stack_4","DPS [0.0]","f");

   ci = TColor::GetColor("#cccccc");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("VVV_stack_3","VVV [0.0]","f");

   ci = TColor::GetColor("#99ff33");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Vg_stack_2","Vg [0.0]","f");

   ci = TColor::GetColor("#66ffff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("VV_stack_1","VV [0.5]","f");

   ci = TColor::GetColor("#ffccff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   
   leg = new TLegend(0.34,0.68,0.72,0.88,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   entry=leg->AddEntry("Data","Data","lpe");
   entry->SetLineColor(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Graph0","Stat. Unc","f");
   entry->SetFillColor(1);
   entry->SetFillStyle(3005);
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("EWK_stack_7","EWK ssWW [1.5]","f");

   ci = TColor::GetColor("#6666ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("Nonprompt_stack_6","Nonprompt [63.5]","f");

   ci = TColor::GetColor("#ffff33");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   entry=leg->AddEntry("QCD_stack_5","QCD ssWW [0.1]","f");

   ci = TColor::GetColor("#cc66ff");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1001);
   entry->SetLineColor(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(42);
   leg->Draw();
   c1->Modified();
   c1->cd();
   c1->SetSelected(c1);
}
