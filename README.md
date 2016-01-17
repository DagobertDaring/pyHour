pyHour.py Version 1.0

See "LICENSE" for license and redristibuting


Misc notes


this script provides very simple and easy functionality for tracking minutes in a log (it will be extended)


Using the script

pipeline a textfile(notation see below) into the script for example

	cat example | python pyHour.py

if using the right notation it will provide you with the correct amount of minutes


notation


EBNF:

	G = (V,T,P, Log)

	Log = {"[" date "] " time " > " "started"|"stopped" " > " message ";"}

	date = year"-" month "-" day
	year = twodigit twodigit
	month = twodigit
	day = twodigit
	twodigit = digit digit
	digit = "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"

	time = twodigit":"twodigit

	message = {literal}
	letter = "a"|...|"z"|"A"|...|"Z"
	literal = digit|letter|" "

Example

	[2001-12-24] 23:59 > started > time to work;
	[2008-01-31] 00:00 > stopped > finally done;
	[2009-03-03] 12:11 > started > found a bug;
	[2016-01-17] 14:19 > stopped > done;

