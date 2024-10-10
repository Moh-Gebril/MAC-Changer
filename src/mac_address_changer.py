import argparse
import netifaces
import subprocess as sp
import re
import sys

def get_command_line_arguments():
    parser = argparse.ArgumentParser(description="A command line tool to change your ethernet interfaces's mac address\nExample: $ sudo mac_address_changer.py -i eth0 -m 12:34:56:78:9A:BC")
    parser.add_argument("-i", "--interface", type=str,
                        help="Add interface name i.e.(mac_address_changer -i eth0)")
    parser.add_argument("-m", "--mac-address", type=str,
                        help="Add interface name i.e.(mac_address_changer -m 12:34:56:78:9A:BC)")
    
    args = parser.parse_args()

    if args.interface == None or args.mac_address == None:
        print("[-] Invalid input arguments, Example: $ sudo mac_address_changer.py -i eth0 -m 12:34:56:78:9A:BC ")
        sys.exit()

    return args.interface, args.mac_address


def get_ethernet_interfaces():
    interfaces = netifaces.interfaces()
    ethernet_interfaces = []

    for interface in interfaces:
        if netifaces.AF_LINK in netifaces.ifaddresses(interface):
            ethernet_interfaces.append(interface)

    return ethernet_interfaces

def get_current_user():
    return sp.getoutput("whoami")

def set_interface_down(interface_name):
    set_interface_down_command = f"ip link set dev {interface_name} down"
    return sp.run(set_interface_down_command, shell=True).returncode

def set_interface_up(interface_name):
    set_interface_up_command = f"ip link set dev {interface_name} up"
    return sp.run(set_interface_up_command, shell=True).returncode

def set_mac_address(interface_name, new_mac_address):
    set_mac_address_command = f"ip link set dev {interface_name} address {new_mac_address}"
    return sp.run(set_mac_address_command, shell=True).returncode
    

def is_mac_address_valid(mac_address):
    pattern = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    if re.match(pattern, mac_address):
        return True
    else:
        return False
    
def change_mac_address():
    if get_current_user() != "root":
        print("[-] The user must be root, Try again using sudo")
        sys.exit()
    ethernet_interface, mac_address = get_command_line_arguments()
    if ethernet_interface not in get_ethernet_interfaces():
        print(f"[-] Invalid ethernet interface name {ethernet_interface},\
               Check your ethernet interfaces using: $ ip addr")
        sys.exit()
    if not is_mac_address_valid(mac_address):
        print(f"[-] Invalid mac address {mac_address},\
               example for right mac address: 12:34:56:78:9A:BC")
        sys.exit()
    if  set_interface_down(ethernet_interface) != 0:
        print(f"[-] Could not set {ethernet_interface} down")
        sys.exit()
    if  set_mac_address(ethernet_interface, mac_address) != 0:
        print(f"[-] Could not set new mac address {mac_address} to\
              {ethernet_interface} interface")
        sys.exit()
    if  set_interface_up(ethernet_interface) != 0:
        print(f"[-] Could not set {ethernet_interface} up")
        sys.exit()
        
def main():
    change_mac_address()

if __name__ == '__main__':
    main()
