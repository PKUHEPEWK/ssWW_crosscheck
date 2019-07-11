import ROOT

def DPS_set():
	print 'combining DPS root file'
	chain = ROOT.TChain("Events")
	for i in range(0,19):
		chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/DPS/nanoLatino_WWTo2L2Nu_DoubleScattering__part'+str(i)+'_exaModu_keepdrop.root')
	return chain

def EWK_set():
	print 'combining EWK root file'
        chain = ROOT.TChain("Events")
        for i in range(0,16):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/EWK/nanoLatino_WpWpJJ_EWK__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def QCD_set():
	print 'combining QCD root file'
        chain = ROOT.TChain("Events")
        for i in range(0,12):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/QCD/nanoLatino_WpWpJJ_QCD__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def WWW_set():
	print 'combining WWW root file'
        chain = ROOT.TChain("Events")
        for i in range(0,3):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/WWW/nanoLatino_WWW__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def WWZ_set():
	print 'combining WWZ root file'
        chain = ROOT.TChain("Events")
        for i in range(0,2):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/WWZ/nanoLatino_WWZ__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def WZZ_set():
	print 'combining WZZ root file'
        chain = ROOT.TChain("Events")
        for i in range(0,3):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/WZZ/nanoLatino_WZZ__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def ZZZ_set():
	print 'combining ZZZ root file'
        chain = ROOT.TChain("Events")
        for i in range(0,3):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/ZZZ/nanoLatino_ZZZ__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def WZTo2L2Q_set():
	print 'combining WZTo2L2Q root file'
        chain = ROOT.TChain("Events")
        for i in range(0,24):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/WZTo2L2Q/nanoLatino_WZTo2L2Q__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def WZTo3LNu_set():
	print 'combining WZTo3LNu root file'
        chain = ROOT.TChain("Events")
        for i in range(0,35):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/WZTo3LNu/nanoLatino_WZTo3LNu__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def Wg_set():
	print 'combining Wg root file'
        chain = ROOT.TChain("Events")
        for i in range(0,57):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Wg/nanoLatino_Wg_MADGRAPHMLM__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def ZZTo2L2Nu_set():
	print 'combining ZZTo2L2Nu root file'
        chain = ROOT.TChain("Events")
        for i in range(0,12):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/ZZTo2L2Nu/nanoLatino_ZZTo2L2Nu__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def ZZTo2L2Q_set():
	print 'combining ZZTo2L2Q root file'
        chain = ROOT.TChain("Events")
        for i in range(0,20):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/ZZTo2L2Q/nanoLatino_ZZTo2L2Q__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def ZZTo4L_set():
	print 'combining ZZTo4L root file'
        chain = ROOT.TChain("Events")
        for i in range(0,9):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/ZZTo4L/nanoLatino_ZZTo4L__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def Zg_set():
	print 'combining Zg root file'
        chain = ROOT.TChain("Events")
        for i in range(0,23):
                chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Zg/nanoLatino_Zg__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def fake_double_mu_set():
	print 'combining Fake double_muon root file'
        chain = ROOT.TChain("Events")
        for i in range(0,123):
                if i<8:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017B-31Mar2018-v1__part'+str(i)+'_exaModu_keepdrop.root')
		elif i<33:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017C-31Mar2018-v1__part'+str(i-8)+'_exaModu_keepdrop.root')
		elif i<46:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017D-31Mar2018-v1__part'+str(i-33)+'_exaModu_keepdrop.root')
		elif i<76:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017E-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
		else: chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017F-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
        return chain

def fake_double_ele_set():
	print 'combining Fake double_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,154):
                if i<23:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_EG/nanoLatino_DoubleEG_Run2017B-31Mar2018-v1__part'+str(i)+'_exaModu_keepdrop.root')
                elif i<66:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_EG/nanoLatino_DoubleEG_Run2017C-31Mar2018-v1__part'+str(i-8)+'_exaModu_keepdrop.root')
                elif i<79:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_EG/nanoLatino_DoubleEG_Run2017D-31Mar2018-v1__part'+str(i-33)+'_exaModu_keepdrop.root')
                elif i<108:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_EG/nanoLatino_DoubleEG_Run2017E-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
                else: chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Double_EG/nanoLatino_DoubleEG_Run2017F-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
        return chain

def fake_single_ele_set():
	print 'combining Fake single_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,209):
                if i<24:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_EG/nanoLatino_SingleElectron_Run2017B-31Mar2018-v1__part'+str(i)+'_exaModu_keepdrop.root')
                elif i<89:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_EG/nanoLatino_SingleElectron_Run2017C-31Mar2018-v1__part'+str(i-8)+'_exaModu_keepdrop.root')
                elif i<113:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_EG/nanoLatino_SingleElectron_Run2017D-31Mar2018-v1__part'+str(i-33)+'_exaModu_keepdrop.root')
                elif i<151:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_EG/nanoLatino_SingleElectron_Run2017E-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
                else: chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_EG/nanoLatino_SingleElectron_Run2017F-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
        return chain

def fake_single_muon_set():
	print 'combining Fake single_muon root file'
        chain = ROOT.TChain("Events")
        for i in range(0,273):
                if i<51:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_Muon/nanoLatino_SingleMuon_Run2017B-31Mar2018-v1__part'+str(i)+'_exaModu_keepdrop.root')
                elif i<105:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_Muon/nanoLatino_SingleMuon_Run2017C-31Mar2018-v1__part'+str(i-8)+'_exaModu_keepdrop.root')
                elif i<129:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_Muon/nanoLatino_SingleMuon_Run2017D-31Mar2018-v1__part'+str(i-33)+'_exaModu_keepdrop.root')
                elif i<191:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_Muon/nanoLatino_SingleMuon_Run2017E-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
                else: chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Single_Muon/nanoLatino_SingleMuon_Run2017F-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
        return chain

def fake_muon_ele_set():
	print 'combining Fake muon_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,49):
                if i<3:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Muon_EG/nanoLatino_MuonEG_Run2017B-31Mar2018-v1__part'+str(i)+'_exaModu_keepdrop.root')
                elif i<14:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Muon_EG/nanoLatino_MuonEG_Run2017C-31Mar2018-v1__part'+str(i-8)+'_exaModu_keepdrop.root')
                elif i<22:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Muon_EG/nanoLatino_MuonEG_Run2017D-31Mar2018-v1__part'+str(i-33)+'_exaModu_keepdrop.root')
                elif i<31:chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Muon_EG/nanoLatino_MuonEG_Run2017E-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
                else: chain.Add('/eos/user/m/melu/ssWW_2017/Data_MC/Fake/Muon_EG/nanoLatino_MuonEG_Run2017F-31Mar2018-v1__part'+str(i-46)+'_exaModu_keepdrop.root')
        return chain
