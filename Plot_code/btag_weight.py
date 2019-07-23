import ROOT

#b_eta1 = [0.782, 0.837, 0.866, 0.878, 0.887, 0.889, 0.875, 0.824, 0.779, 0.6]
#b_eta2 = [0.793, 0.849, 0.875, 0.888, 0.899, 0.903, 0.889, 0.856, 0.795, 0.646]
#b_eta3 = [0.775, 0.833, 0.861, 0.875, 0.885, 0.887, 0.88, 0.841, 0.761, 0.333]
#c_eta1 = [0.415, 0.45, 0.448, 0.467, 0.482, 0.472, 0.485, 0.444, 0.416, 0.0]
#c_eta1 = [0.393, 0.428, 0.43, 0.432, 0.442, 0.456, 0.425, 0.426, 0.378, 0.136]
#c_eta1 = [0.418, 0.455, 0.452, 0.464, 0.485, 0.497, 0.482, 0.433, 0.443, 0.0]
#light_eta1 = [0.35, 0.35, 0.261, 0.298]
#light_eta1 = [0.349, 0.375, 0.269, 0.304]
#light_eta1 = [0.351, 0.359, 0.267, 0.227]
def btag_weight(flavor=0, pt=0, eta=0):
	if flavor==5:
		if eta<-0.8:
			if pt<30: return 0.782
			elif pt<50: return 0.837
			elif pt<70: return 0.866
			elif pt<100: return 0.878
			elif pt<140: return 0.887
			elif pt<200: return 0.889
			elif pt<300: return 0.875
			elif pt<600: return 0.824
			elif pt<1000: return 0.779
			else: return 0.6
		elif eta<0.8:
			if pt<30: return 0.793
                        elif pt<50: return 0.849
                        elif pt<70: return 0.875
                        elif pt<100: return 0.888
                        elif pt<140: return 0.899
                        elif pt<200: return 0.903
                        elif pt<300: return 0.889
                        elif pt<600: return 0.856
                        elif pt<1000: return 0.795
                        else: return 0.646
		else:
			if pt<30: return 0.775
                        elif pt<50: return 0.833
                        elif pt<70: return 0.861
                        elif pt<100: return 0.875
                        elif pt<140: return 0.885
                        elif pt<200: return 0.887
                        elif pt<300: return 0.88
                        elif pt<600: return 0.841
                        elif pt<1000: return 0.761
                        else: return 0.333
	elif flavor==4:
		if eta<-0.8:
			if pt<30: return 0.415
			elif pt<50: return 0.45
			elif pt<70: return 0.448
			elif pt<100: return 0.467
			elif pt<140: return 0.482
			elif pt<200: return 0.472
			elif pt<300: return 0.485
			elif pt<600: return 0.444
			elif pt<1000: return 0.416
			else: return 0.
		elif eta<0.8:
			if pt<30: return 0.393
                        elif pt<50: return 0.428
                        elif pt<70: return 0.43
                        elif pt<100: return 0.432
                        elif pt<140: return 0.442
                        elif pt<200: return 0.456
                        elif pt<300: return 0.425
                        elif pt<600: return 0.426
                        elif pt<1000: return 0.378
                        else: return 0.136
		else:
			if pt<30: return 0.418
                        elif pt<50: return 0.455
                        elif pt<70: return 0.452
                        elif pt<100: return 0.464
                        elif pt<140: return 0.485
                        elif pt<200: return 0.497
                        elif pt<300: return 0.482
                        elif pt<600: return 0.433
                        elif pt<1000: return 0.443
                        else: return 0.
	else:
		if eta<-0.8:
			if pt<200: return 0.35
                        elif pt<500: return 0.35
                        elif pt<1000: return 0.261
			else: return 0.298
		elif eta<0.8:
			if pt<200: return 0.349
                        elif pt<500: return 0.375
                        elif pt<1000: return 0.269
                        else: return 0.304
		else:
			if pt<200: return 0.351
                        elif pt<500: return 0.359
                        elif pt<1000: return 0.267
                        else: return 0.227
