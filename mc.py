#!/usr/bin/env python3

import subprocess

interface = input("interface > ")
new_mac = input("new MAC > ")

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
