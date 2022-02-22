from datetime import datetime
import os
import re

def get_logins_list():
    #Read the file needed to extract the data ans remove useless lines concerning system boot
    list = os.popen('last -F -d | sed \'/system boot/d\'').read()

    entries = list.split("\n")

    result = []

    since = ""

    for entry in entries:

        #Separate end lines showing the las update fron the other lines
        if(re.match(r"wtmp begins.*", entry)):
            since = entry[12:-1]
            break

        #Handle entry lines, extract all columns and put it in a dictionary
        if(entry != ""):
            result.append( {
            "user": entry[0:8],
            "tty": entry[9:21],
            "ip": entry[22:38],
            "date": datetime.strptime(entry[39:63], "%a %b %d %H:%M:%S %Y"),
            "state/loggedout": entry[66:91],
            "uptime": entry[92:99].replace('(','').replace(')', '').replace('+', 'd ')
        })

    return {"since": since, "entries": result}

if __name__ == "__main__":
    print(get_logins_list())