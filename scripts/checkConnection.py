import os

hosts = ["8.8.8.8"] #Ad-hoc creator IP
response = None

for host in hosts:
   response = os.system("ping -c 1 " + host)


if response == 0:
    print "LED is green"
else:
    print "LED is red"
