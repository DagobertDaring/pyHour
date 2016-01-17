input = "[2016-01-02] 12:11 > started; message\n[2016-01-02] 12:12 > stopped; message"
x = 0
mark = 0
special = '['
DateYear = 0
DateMonth = 0
DateDay = 0
DateHours = 0
DateMinutes = 0
MinutesWorked = 0

while x < len(input):
	if input[x] is special:
		mark = x
		if input[mark+21:mark+28] ==  "started":
			DateYear = int(input[mark+1:mark+5])
			DateMonth = int(input[mark+6:mark+8])
			DateDay = int(input[mark+9:mark+11])
		elif input[mark+21:mark+28] == "stopped":
			
	x=x+1
print DateYear, "-" , DateMonth, "-", DateDay
print MinutesWorked


