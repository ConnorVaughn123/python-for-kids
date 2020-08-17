room_height = input('Enter height of the room in feet: ')
room_width = input('Enter width of room in feet: ')
room_length = input('Enter length of the room in feet: ')
doors_num = input('Enter number of doors: ')
windows_num = input('Enter number of windows: ')
room_height = int(room_height)
room_width = int(room_width)
room_length = int(room_length)
doors_num = int(doors_num)
windows_num = int(windows_num)
wall_area = (room_length * room_width * room_height)
print('Total surface area to paint:', wall_area)
nopaintarea = 20 * doors_num + 15 * windows_num
paintarea = wall_area - nopaintarea
gallons = wall_area / 350
gallons = int(gallons)
round(gallons, 2)
print('Number of gallons of paint needed:', gallons)
