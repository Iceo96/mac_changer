#! usr/bin/env python

import subprocess
import optparse
from subprocess import check_output
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change to mac address")
    parser.add_option("-n", "--newMac", dest="new_mac", help="New Mac Address")
    (options,arguments)=parser.parse_args() # Here is spliting
    if not options.interface:
        parser.error("[-] Please specify an interface , use --help")
    elif not options.new_mac:
        parser.error("[-] Please specify an mac , use --help")
    return options
def change_mac(interface,new_mac):
    print("[+] Changing the Mac addresss ---->")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    Mac_Address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if Mac_Address_search:
        return Mac_Address_search.group(0)
    else:
        print(" There is no mac address here or there :-( ")
options=get_arguments()
current_mac = get_current_mac(options.interface)
print("The current mac is = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if  current_mac == options.new_mac:
    print("[+] Mac address was successfully changed " + current_mac)
else:
    print("[-] Mac address was not changed ")



