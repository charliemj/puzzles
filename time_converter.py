#takes a string describing a 12-hour time of the following form hh:mm:ssAM (or PM) and coverts it to militarty time
# https://www.hackerrank.com/challenges/time-conversion
time = "12:05:45AM"

if time[8] == "A":
    if time[0:2] == "12":
        print "00"+time[2:8]
    else:
   		print time[0:8]
else:
    if time[0:2] == "12":
        print time[0:8]
    else:
        new = int(time[0:2])+12
        print str(new)+time[2:8]