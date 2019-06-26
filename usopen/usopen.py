#!/usr/bin/python3

'''
This script is being designed to provide the following automated tasks:
    -ping check the router
    -longin check the router
    -determine if interfaces in use are up
    -Apply new configuration
'''

import os
import pyexcel
from netmiko import ConnectHandler

def retv_excel(par):
    d = {}
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        d.update({record['IP']:record['driver']})
    return d

## Pint router - returns True or False
def pint_router(hostname):
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        return True
    else:
        return False


## Check interfaces - Issue "show ip init brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        my_command = open_connection.send_command("show ip int brief")
    except:
        my_command = "** ISSUING COMMAND FAILED **"
    finally:
        return my_command

## Login to router - SSH Check with Netmiko class ConnetctHandler
def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection =ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        return True
    except:
        return False

## Main function - This is the code that runs our functions
def main():

    ## Determine where *.xls input is
    file_location = str(input("\nWhere is the file location? "))

    ## Entry is now a local dictionary containing IP:driver
    entry = retv_excel(file_location)

    ## Use a loop to check each device for SSH accessability
    print("\n***** BEGIN SSH CHECKING *****")
    for x in entry.keys():
        if login_router(str(entry[x]), x, "admin", "alta3"):
            print("\n\t**IP: - " + x + " - SSH connectivity UP\n")
        else:
            print("\n\t**IP: - " + x + " - SSH connectivity DOWN\n")

## Call main()
main()





