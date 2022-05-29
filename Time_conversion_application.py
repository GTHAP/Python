# This code converts time from standard or 12 hour format to military or 24 hour format.
# I wrote this code when I had just started off with coding in python and did not know about all the available tools and libraries
# Much better and simpler designs are available online

def timeconversion(timeinput):
    morningstart = "00:00:00"
    noonstart = "12:00:00"
    if timeinput == "12:00:00AM":
        return print (morningstart)
    if timeinput == "12:00:00PM":
        return print (noonstart)
    militarytime = timeinput
    if militarytime[-2] == "A":
        militarytime = str.strip(militarytime, "AM")
        return print (militarytime)
    if militarytime[-2] == "P":
        militarytime = str.strip(militarytime, "PM")
        if militarytime[0] == "0":
            if militarytime[1] != "8" and militarytime[1] != "9":
                x = int(militarytime[1]) + 2
                militarytime = str.replace(militarytime, militarytime[1], str(x), 1)
                militarytime = str.replace(militarytime, "0", "1", 1)
                return print (militarytime)
            if militarytime[1] == "8" or militarytime[1] == "9":
                x = int(militarytime[1]) + 12
                militarytime = str.replace(militarytime, militarytime[1], str(x), 1)
                militarytime = str.replace(militarytime, militarytime[0], "", 1)
                return print (militarytime)
        if militarytime[0] == "1" and militarytime[1] == "0":
            militarytime = str.replace(militarytime, militarytime[0], "2", 1)
            militarytime = str.replace(militarytime, militarytime[1], "2", 1)
            return print (militarytime)
        if militarytime[0] == "1" and militarytime[1] == "1":
            militarytime = str.replace(militarytime, militarytime[0], "2", 1)
            militarytime = str.replace(militarytime, militarytime[1], "3", 1)
            return print (militarytime)
