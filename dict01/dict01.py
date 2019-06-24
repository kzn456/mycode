#!/usr/bin/python3

def main():
    ##create a dictionary
    switch = {'hostname':'sw1', 'ip':'10.0.1.1', 'version':'1.2', 'vendor':'cisco'}

    ## display parts of the dictionary
    print( switch['hostname'])
    print( switch['ip'])
    switch['lync'] = '1.1.1.1'
    ## request a 'fake' key
    print( switch['lync'])

main()

