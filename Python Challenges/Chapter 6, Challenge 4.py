starting_earth_weight = 30
num_kg_gained_per_year = 1
moon_weight_percentage = 0.165
for year in range(1, 15):
	current_moon_weight = (starting_earth_weight + year) * moon_weight_percentage
	print('Year %s = %s' % (year, current_moon_weight))
