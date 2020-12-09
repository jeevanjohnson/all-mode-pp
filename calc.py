from statistics import stdev
"""
0 std
1 taiko
2 ctb
3 rx std 
4 rx taiko
5 rx ctb
"""
def calc_without_mania(pp_values):
	stdF = (pp_values[0] ** 1.06) * 0.85
	stdRF = (pp_values[3] * 1.75) - (pp_values[3] ** 1.01)
	taikoF = (pp_values[1] ** 1.1) * 0.71
	taikoRF = (pp_values[4] ** 1.2) * 0.201
	ctbF = (pp_values[2] * 2.8) - (pp_values[2] ** 1.028)
	ctbRF = (pp_values[5] ** 1.05) * 0.72
	stdevF = stdev([stdF, stdRF, taikoF, taikoRF, ctbF, ctbRF])
	allmodes = (stdF + stdRF + taikoF + taikoRF + ctbF + ctbRF) - stdevF
	return round(allmodes)

'''
def calc_mania(pp_values):
	stdF = (pp_values[0] ** 1.06) * 0.85
	stdRF = (pp_values[4] * 1.75) - (pp_values[4] ** 1.01)
	taikoF = (pp_values[1] ** 1.1) * 0.71
	taikoRF = (pp_values[5] ** 1.2) * 0.201
	ctbF = (pp_values[2] * 2.8) - (pp_values[2] ** 1.028)
	ctbRF = (pp_values[6] ** 1.05) * 0.72
	maniaF = pp_values[3] ** 0.977
	stdevF = stdev([stdF, stdRF, taikoF, taikoRF, ctbF, ctbRF, maniaF])
	allmodes = (stdF + stdRF + taikoF + taikoRF + ctbF + ctbRF + maniaF) - stdevF
	return round(allmodes)
'''