def moon_weight(weight, increase, years):
	for year in range(1, 16):
		years = years + 1
		weight = weight + 1
		moon_weight = weight * 0.165
		print('Year %s = %s' % (year, moon_weight))
