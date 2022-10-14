#!/usr/bin/env python3

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("sudo ip link set dev " + interface + " down", shell=True)
    subprocess.call("sudo ip link set dev " + interface + " address " + new_mac, shell=True)
    subprocess.call("sudo ip link set dev " + interface + " up", shell=True)
    print("")
    print("MAC address has been changed")
    print("")

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
