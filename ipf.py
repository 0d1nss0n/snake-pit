#!/usr/bin/env python3

import subprocess


print("[+] Enabling IP Forwarding"
subprocess.call("echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward", shell=True)
print("")
print("[+] Success")

