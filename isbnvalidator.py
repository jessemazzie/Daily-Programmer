#Written by: Jesse Mazzie
#this script is inspired by Reddit's daily programmer subreddit. Its purpose is to validate ISBN numbers
#Arguments must be given through command line, ISBN format must be ISBN-10.

import sys

#Accepts ISBN-10 numbers as parameters. Returns boolean value 'true' for valid ISBNs, 'false' for invalid ISBNs
def Validate(ISBN):
	i = 10
	total = 0
	for digit in ISBN:
		if digit.isdigit():
			total += i * int(digit)
			i -= 1
	return total % 11 is 0

#loops through command line arguments
for i in range(1, len(sys.argv)):
	print(Validate(sys.argv[i]))