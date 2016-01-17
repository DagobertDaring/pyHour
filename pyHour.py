import sys

input = ""

if __name__ == "__main__":
	for line in sys.stdin:
		input += line

x = 0
mark = 0
special = '['

DateInMinutes = 0.0
MinutesWorked = 0.0
WorkTime = 0.0
if input is not None:
	while x < len(input):
		if input[x] is special:
			mark = x
			if input[mark+21:mark+28] ==  "started":
				DateInMinutes += (float(input[mark+1:mark+5]) * 525600.0) + (float(input[mark+6:mark+8]) * 43800.0) + (float(input[mark+9:mark+11]) * 1440.0) + (float(input[mark+13:mark+15]) * 60.0) + (float(input[mark+16:mark+18]) * 1.0)
			elif input[mark+21:mark+28] == "stopped":
				MinutesWorked += (float(input[mark+1:mark+5]) * 525600.0) + (float(input[mark+6:mark+8]) * 43800.0) + (float(input[mark+9:mark+11]) * 1440.0) + (float(input[mark+13:mark+15]) * 60.0) + (float(input[mark+16:mark+18]) * 1.0)
				MinutesWorked -= DateInMinutes
				DateInMinutes = 0
				WorkTime += MinutesWorked
				MinutesWorked = 0
		x+=1

print int(WorkTime), " minutes"
print "or ", float(WorkTime/60), " hours"


