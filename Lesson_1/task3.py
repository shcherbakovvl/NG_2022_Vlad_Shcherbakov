# function that convert seconds to days, hours, minutes, seconds
def convert(secs):
    days = secs // 86400               # 86400 seconds in 1 day
    secs = secs - (days * 86400)       # back to seconds without days
    hours = secs // 3600               # 3600 seconds in 1 hour
    secs = secs - (hours * 3600)       # back to seconds without days and hours
    min = secs // 60                   # 60 seconds in 1 minute
    secs = secs - (min *60)            # back to seconds without days, hours and minutes
    print(days, "days", hours, "hours", min, "minutes", secs, "seconds")


print ("======================================")
secs = int(input("Enter seconds to covert: "))
print ("======================================")

# function call
convert(secs)
print ("======================================")