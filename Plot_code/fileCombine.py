import ROOT

#directory = '/eos/user/m/melu/ssWW_2017/Smaller_ntuple/'
directory = '/eos/user/m/melu/ssWW_2017/Signal_ntuple/'
#directory = '/eos/user/m/melu/ssWW_2017/Lowmjj_ntuple/'
#directory = '/eos/user/m/melu/ssWW_2017/WZ_ntuple/'
#directory = '/eos/user/m/melu/ssWW_2017/Data_MC/'
def DPS_set():
	print 'combining DPS root file'
	chain = ROOT.TChain("Events")
	for i in range(0,1):
		chain.Add(directory+'DPS/nanoLatino_WWTo2L2Nu_DoubleScattering__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
	return chain

def EWK_set():
	print 'combining EWK root file'
        chain = ROOT.TChain("Events")
        for i in range(0,2):
                chain.Add(directory+'EWK/nanoLatino_WpWpJJ_EWK__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def QCD_set():
	print 'combining QCD root file'
        chain = ROOT.TChain("Events")
        for i in range(0,1):
                chain.Add(directory+'QCD/nanoLatino_WpWpJJ_QCD__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def WWW_set():
	print 'combining WWW root file'
        chain = ROOT.TChain("Events")
        for i in range(0,3):
                chain.Add(directory+'WWW/nanoLatino_WWW__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def WWZ_set():
	print 'combining WWZ root file'
        chain = ROOT.TChain("Events")
        for i in range(0,1):
                chain.Add(directory+'WWZ/nanoLatino_WWZ__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def WZZ_set():
	print 'combining WZZ root file'
        chain = ROOT.TChain("Events")
        for i in range(0,1):
                chain.Add(directory+'WZZ/nanoLatino_WZZ__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def ZZZ_set():
	print 'combining ZZZ root file'
        chain = ROOT.TChain("Events")
        for i in range(0,1):
                chain.Add(directory+'ZZZ/nanoLatino_ZZZ__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def WWG_set():
        print 'combining WWG root file'
        chain = ROOT.TChain("Events")
        for i in range(0,4):
                chain.Add(directory+'WWg/nanoLatino_WWG__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def WZTo2L2Q_set():
	print 'combining WZTo2L2Q root file'
        chain = ROOT.TChain("Events")
        for i in range(0,17):
                chain.Add(directory+'WZTo2L2Q/nanoLatino_WZTo2L2Q__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                #chain.Add(directory+'WZTo2L2Q/nanoLatino_WZTo2L2Q__part'+str(i)+'_exaModu_keepdrop.root')
        return chain

def WZTo3LNu_set():
	print 'combining QCD WZTo3LNu root file'
        chain = ROOT.TChain("Events")
        for i in range(0,33):
                #chain.Add(directory+'WZTo3LNu_powheg/nanoLatino_WZTo3LNu_mllmin01__part'+str(i)+'_exaModu_keepdrop.root')
                chain.Add(directory+'WZTo3LNu_powheg/nanoLatino_WZTo3LNu_mllmin01__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain
#        for i in range(0,19):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-4To50_QCD_0Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#        for i in range(0,19):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-4To50_QCD_1Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#        for i in range(0,60):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-4To50_QCD_2Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#        for i in range(0,86):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-4To50_QCD_3Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#	for i in range(0,19):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-50_QCD_0Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#        for i in range(0,22):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-50_QCD_1Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#        for i in range(0,53):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-50_QCD_2Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain
#        for i in range(0,74):
#                chain.Add(directory+'WZTo3LNu/nanoLatino_WLLJJToLNu_M-50_QCD_3Jet__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
#        return chain

def WZTo3LNu_EWK_set():
	print 'combining EWK WZTo3LNu root file'
        chain = ROOT.TChain("Events")
	for i in range(0,1):
                chain.Add(directory+'WZTo3LNu_EWK/nanoLatino_WLLJJToLNu_M-60_EWK_4F__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def Wg_set():
	print 'combining Wg root file'
        chain = ROOT.TChain("Events")
        for i in range(0,5):
                chain.Add(directory+'Wg/nanoLatino_Wg_MADGRAPHMLM__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def ZZTo2L2Nu_set():
	print 'combining ZZTo2L2Nu root file'
        chain = ROOT.TChain("Events")
        for i in range(0,9):
                chain.Add(directory+'ZZTo2L2Nu/nanoLatino_ZZTo2L2Nu__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def ZZTo2L2Q_set():
	print 'combining ZZTo2L2Q root file'
        chain = ROOT.TChain("Events")
        for i in range(0,19):
                chain.Add(directory+'ZZTo2L2Q/nanoLatino_ZZTo2L2Q__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def ZZTo4L_set():
	print 'combining ZZTo4L root file'
        chain = ROOT.TChain("Events")
        for i in range(0,14):
                chain.Add(directory+'ZZTo4L/nanoLatino_ZZTo4L__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def Zg_set():
	print 'combining Zg root file'
        chain = ROOT.TChain("Events")
        for i in range(0,122):
                chain.Add(directory+'Zg/nanoLatino_ZGToLLG__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def fake_double_mu_set():
	print 'combining Fake double_muon root file'
        chain = ROOT.TChain("Events")
        for i in range(0,129):
                if i<11:chain.Add(directory+'Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
		elif i<37:chain.Add(directory+'Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017C-Nano14Dec2018-v1__part'+str(i-11)+'_exaModu_keepdrop_Skim_Skim.root')
		elif i<54:chain.Add(directory+'Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017D-Nano14Dec2018-v1__part'+str(i-37)+'_exaModu_keepdrop_Skim_Skim.root')
		elif i<84:chain.Add(directory+'Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017E-Nano14Dec2018-v1__part'+str(i-54)+'_exaModu_keepdrop_Skim_Skim.root')
		else: chain.Add(directory+'Fake/Double_Muon/nanoLatino_DoubleMuon_Run2017F-Nano14Dec2018-v1__part'+str(i-84)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def fake_double_ele_set():
	print 'combining Fake double_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,176):
                if i<34:chain.Add(directory+'Fake/Double_EG/nanoLatino_DoubleEG_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<82:chain.Add(directory+'Fake/Double_EG/nanoLatino_DoubleEG_Run2017C-Nano14Dec2018-v1__part'+str(i-34)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<97:chain.Add(directory+'Fake/Double_EG/nanoLatino_DoubleEG_Run2017D-Nano14Dec2018-v1__part'+str(i-82)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<127:chain.Add(directory+'Fake/Double_EG/nanoLatino_DoubleEG_Run2017E-Nano14Dec2018-v1__part'+str(i-97)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Fake/Double_EG/nanoLatino_DoubleEG_Run2017F-Nano14Dec2018-v1__part'+str(i-127)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def fake_single_ele_set():
	print 'combining Fake single_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,251):
                if i<28:chain.Add(directory+'Fake/Single_EG/nanoLatino_SingleElectron_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<97:chain.Add(directory+'Fake/Single_EG/nanoLatino_SingleElectron_Run2017C-Nano14Dec2018-v1__part'+str(i-28)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<129:chain.Add(directory+'Fake/Single_EG/nanoLatino_SingleElectron_Run2017D-Nano14Dec2018-v1__part'+str(i-97)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<183:chain.Add(directory+'Fake/Single_EG/nanoLatino_SingleElectron_Run2017E-Nano14Dec2018-v1__part'+str(i-129)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Fake/Single_EG/nanoLatino_SingleElectron_Run2017F-Nano14Dec2018-v1__part'+str(i-183)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def fake_single_muon_set():
	print 'combining Fake single_muon root file'
        chain = ROOT.TChain("Events")
        for i in range(0,358):
                if i<67:chain.Add(directory+'Fake/Single_Muon/nanoLatino_SingleMuon_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<133:chain.Add(directory+'Fake/Single_Muon/nanoLatino_SingleMuon_Run2017C-Nano14Dec2018-v1__part'+str(i-67)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<169:chain.Add(directory+'Fake/Single_Muon/nanoLatino_SingleMuon_Run2017D-Nano14Dec2018-v1__part'+str(i-133)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<241:chain.Add(directory+'Fake/Single_Muon/nanoLatino_SingleMuon_Run2017E-Nano14Dec2018-v1__part'+str(i-169)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Fake/Single_Muon/nanoLatino_SingleMuon_Run2017F-Nano14Dec2018-v1__part'+str(i-241)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def fake_muon_ele_set():
	print 'combining Fake muon_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,61):
                if i<7:chain.Add(directory+'Fake/Muon_EG/nanoLatino_MuonEG_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<19:chain.Add(directory+'Fake/Muon_EG/nanoLatino_MuonEG_Run2017C-Nano14Dec2018-v1__part'+str(i-7)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<29:chain.Add(directory+'Fake/Muon_EG/nanoLatino_MuonEG_Run2017D-Nano14Dec2018-v1__part'+str(i-19)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<41:chain.Add(directory+'Fake/Muon_EG/nanoLatino_MuonEG_Run2017E-Nano14Dec2018-v1__part'+str(i-29)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Fake/Muon_EG/nanoLatino_MuonEG_Run2017F-Nano14Dec2018-v1__part'+str(i-41)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain
def double_mu_set():
	print 'combining double_muon root file'
        chain = ROOT.TChain("Events")
        for i in range(0,129):
                if i<11:chain.Add(directory+'Data/Double_Muon/nanoLatino_DoubleMuon_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
		elif i<37:chain.Add(directory+'Data/Double_Muon/nanoLatino_DoubleMuon_Run2017C-Nano14Dec2018-v1__part'+str(i-11)+'_exaModu_keepdrop_Skim_Skim.root')
		elif i<54:chain.Add(directory+'Data/Double_Muon/nanoLatino_DoubleMuon_Run2017D-Nano14Dec2018-v1__part'+str(i-37)+'_exaModu_keepdrop_Skim_Skim.root')
		elif i<84:chain.Add(directory+'Data/Double_Muon/nanoLatino_DoubleMuon_Run2017E-Nano14Dec2018-v1__part'+str(i-54)+'_exaModu_keepdrop_Skim_Skim.root')
		else: chain.Add(directory+'Data/Double_Muon/nanoLatino_DoubleMuon_Run2017F-Nano14Dec2018-v1__part'+str(i-84)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def double_ele_set():
	print 'combining double_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,176):
                if i<34:chain.Add(directory+'Data/Double_EG/nanoLatino_DoubleEG_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<82:chain.Add(directory+'Data/Double_EG/nanoLatino_DoubleEG_Run2017C-Nano14Dec2018-v1__part'+str(i-34)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<97:chain.Add(directory+'Data/Double_EG/nanoLatino_DoubleEG_Run2017D-Nano14Dec2018-v1__part'+str(i-82)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<127:chain.Add(directory+'Data/Double_EG/nanoLatino_DoubleEG_Run2017E-Nano14Dec2018-v1__part'+str(i-97)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Data/Double_EG/nanoLatino_DoubleEG_Run2017F-Nano14Dec2018-v1__part'+str(i-127)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def single_ele_set():
	print 'combining single_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,251):
                if i<28:chain.Add(directory+'Data/Single_EG/nanoLatino_SingleElectron_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<97:chain.Add(directory+'Data/Single_EG/nanoLatino_SingleElectron_Run2017C-Nano14Dec2018-v1__part'+str(i-28)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<129:chain.Add(directory+'Data/Single_EG/nanoLatino_SingleElectron_Run2017D-Nano14Dec2018-v1__part'+str(i-97)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<183:chain.Add(directory+'Data/Single_EG/nanoLatino_SingleElectron_Run2017E-Nano14Dec2018-v1__part'+str(i-129)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Data/Single_EG/nanoLatino_SingleElectron_Run2017F-Nano14Dec2018-v1__part'+str(i-183)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def single_muon_set():
	print 'combining single_muon root file'
        chain = ROOT.TChain("Events")
        for i in range(0,358):
                if i<67:chain.Add(directory+'Data/Single_Muon/nanoLatino_SingleMuon_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<133:chain.Add(directory+'Data/Single_Muon/nanoLatino_SingleMuon_Run2017C-Nano14Dec2018-v1__part'+str(i-67)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<169:chain.Add(directory+'Data/Single_Muon/nanoLatino_SingleMuon_Run2017D-Nano14Dec2018-v1__part'+str(i-133)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<241:chain.Add(directory+'Data/Single_Muon/nanoLatino_SingleMuon_Run2017E-Nano14Dec2018-v1__part'+str(i-169)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Data/Single_Muon/nanoLatino_SingleMuon_Run2017F-Nano14Dec2018-v1__part'+str(i-241)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain

def muon_ele_set():
	print 'combining muon_ele root file'
        chain = ROOT.TChain("Events")
        for i in range(0,61):
                if i<7:chain.Add(directory+'Data/Muon_EG/nanoLatino_MuonEG_Run2017B-Nano14Dec2018-v1__part'+str(i)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<19:chain.Add(directory+'Data/Muon_EG/nanoLatino_MuonEG_Run2017C-Nano14Dec2018-v1__part'+str(i-7)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<29:chain.Add(directory+'Data/Muon_EG/nanoLatino_MuonEG_Run2017D-Nano14Dec2018-v1__part'+str(i-19)+'_exaModu_keepdrop_Skim_Skim.root')
                elif i<41:chain.Add(directory+'Data/Muon_EG/nanoLatino_MuonEG_Run2017E-Nano14Dec2018-v1__part'+str(i-29)+'_exaModu_keepdrop_Skim_Skim.root')
                else: chain.Add(directory+'Data/Muon_EG/nanoLatino_MuonEG_Run2017F-Nano14Dec2018-v1__part'+str(i-41)+'_exaModu_keepdrop_Skim_Skim.root')
        return chain
