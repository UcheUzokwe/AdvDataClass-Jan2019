
# Use the system function to get input from the commandline	
import sys
	
name = sys.argv[1]
wage = float(sys.argv[2])
hours = int(sys.argv[3])

if hours <= 40:
	pay = wage * hours
else:
	overtime = hours - 40
	pay = wage * 40 + (1.5 * wage) * overtime
	
print ('\n' + name + '\'s' + ' weekly wage is $', format(pay,',.2f'))
