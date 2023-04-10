clock = " 05 : 45 "
clock_split = clock.split( " : ")
hour = int (clock_split[0])
mint = int (clock_split[1])
print(hour,mint)
clock_angle = 30 * hour + 0.5 * mint - 6 * mint #30/5 360/12 30/60
if (clock_angle <= -1):
	clock_angle *= -1
print("clock angle from mint hand to hour hand is " , clock_angle)