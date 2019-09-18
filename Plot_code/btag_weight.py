import ROOT
#b eta1: [0.564, 0.665, 0.708, 0.722, 0.722, 0.695, 0.625, 0.517, 0.315, 0.111]
#b eta2: [0.605, 0.708, 0.743, 0.762, 0.767, 0.763, 0.726, 0.59, 0.376, 0.233]
#b eta3: [0.554, 0.651, 0.697, 0.715, 0.719, 0.693, 0.645, 0.528, 0.284, 0.444]
#c eta1: [0.125, 0.127, 0.143, 0.14, 0.148, 0.134, 0.114, 0.097, 0.091, 0.0]
#c eta1: [0.103, 0.112, 0.108, 0.108, 0.127, 0.132, 0.143, 0.094, 0.016, 0.0]
#c eta1: [0.123, 0.13, 0.137, 0.138, 0.146, 0.126, 0.139, 0.07, 0.058, 0.0]
#light eta1: [0.199, 0.165, 0.046, 0.022]
#light eta1: [0.243, 0.238, 0.099, 0.026]
#light eta1: [0.196, 0.166, 0.057, 0.029]
def btag_weight(flavor=0, pt=0, eta=0):
	if flavor==5:
		if eta<-0.8:
			if pt<30: return 0.564
			elif pt<50: return 0.665
			elif pt<70: return 0.708
			elif pt<100: return 0.722
			elif pt<140: return 0.722
			elif pt<200: return 0.695
			elif pt<300: return 0.625
			elif pt<600: return 0.517
			elif pt<1000: return 0.315
			else: return 0.111
		elif eta<0.8:
			if pt<30: return 0.605
                        elif pt<50: return 0.708
                        elif pt<70: return 0.743
                        elif pt<100: return 0.762
                        elif pt<140: return 0.767
                        elif pt<200: return 0.763
                        elif pt<300: return 0.726
                        elif pt<600: return 0.59
                        elif pt<1000: return 0.376
                        else: return 0.233
		else:
			if pt<30: return 0.554
                        elif pt<50: return 0.651
                        elif pt<70: return 0.697
                        elif pt<100: return 0.715
                        elif pt<140: return 0.719
                        elif pt<200: return 0.693
                        elif pt<300: return 0.645
                        elif pt<600: return 0.528
                        elif pt<1000: return 0.284
                        else: return 0.444
	elif flavor==4:
		if eta<-0.8:
			if pt<30: return 0.125
			elif pt<50: return 0.127
			elif pt<70: return 0.143
			elif pt<100: return 0.14
			elif pt<140: return 0.148
			elif pt<200: return 0.134
			elif pt<300: return 0.114
			elif pt<600: return 0.097
			elif pt<1000: return 0.091
			else: return 0.0
		elif eta<0.8:
			if pt<30: return 0.103
                        elif pt<50: return 0.112
                        elif pt<70: return 0.108
                        elif pt<100: return 0.108
                        elif pt<140: return 0.127
                        elif pt<200: return 0.132
                        elif pt<300: return 0.143
                        elif pt<600: return 0.094
                        elif pt<1000: return 0.016
                        else: return 0.
		else:
			if pt<30: return 0.123
                        elif pt<50: return 0.13
                        elif pt<70: return 0.137
                        elif pt<100: return 0.138
                        elif pt<140: return 0.146
                        elif pt<200: return 0.126
                        elif pt<300: return 0.139
                        elif pt<600: return 0.07
                        elif pt<1000: return 0.058
                        else: return 0.
	else:
		if eta<-0.8:
			if pt<200: return 0.199
                        elif pt<500: return 0.165
                        elif pt<1000: return 0.046
			else: return 0.022
		elif eta<0.8:
			if pt<200: return 0.243
                        elif pt<500: return 0.238
                        elif pt<1000: return 0.099
                        else: return 0.026
		else:
			if pt<200: return 0.196
                        elif pt<500: return 0.166
                        elif pt<1000: return 0.057
                        else: return 0.029
