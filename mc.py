#!/usr/bin/env python3

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("sudo ip link set dev " + interface + " down", shell=True)
subprocess.call("sudo ip link set dev " + interface + " address " + new_mac, shell=True)
subprocess.call("sudo ip link set dev " + interface + " up", shell=True)

print("")
print("MAC address has been changed")
print("")

subprocess.call("sudo ip link show " + interface, shell=True)

print("")
print("Script Closed")
