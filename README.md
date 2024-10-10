# Mac-Changer
Python command line tool that enables you to change your mac address on linux platform

## Description

MAC Changer is a cybersecurity tool that allows you to change the MAC address of any interface on your computer, be it Ethernet or WiFi. By changing the MAC address, you can enhance your privacy, security, and bypass certain restrictions imposed by network administrators.

This tool provides a simple and easy-to-use command-line interface (CLI) to modify the MAC address of your interfaces. It also includes a make file that helps you build the required dependencies effortlessly.

## Features

- Change the MAC address of any Ethernet or WiFi interface.

## Requirements

- Python 3.x
- pip package manager
- Linux operating systems

## Installation

1. Clone the repository using the following command:
    git clone https://github.com/ahmeedmalek/mac_changer.git
2. Change to the project's directory:
    cd mac_changer
3. Create virtual environement:
   python3 -m venv venv
4. Activate virtual environment:
   source venv/vin/activate
5. Install the dependencies using the provided make file:
    make install

## Usage

To change the MAC address of an interface, execute the following command:
  python src/mac_changer.py -i <interface> -m <new_mac_address>

- `<interface>`: Specify the interface for which you want to change the MAC address. Example: eth0, wlan0
- `<new_mac_address>`: Enter the new MAC address you wish to assign to the interface. If not specified, a random MAC address will be set.

## Examples
- Changing the MAC address of the wlan0 interface to a specific address:
    python mac_changer.py -i wlan0 -m 12:34:56:78:9A:BC

## Contributing
Thank you for considering contributing to MAC Changer! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
    

    
    
    
