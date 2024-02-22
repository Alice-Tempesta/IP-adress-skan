# IP-adress-skan
This code scans devices on a local network using ARP requests and displays information about connected devices, such as their IP address, MAC address, device type, and whether the device is a computer.

Briefly, the program performs the following steps:

1. Gets the router (gateway) IP address from the default gateways
2. Creates ARP requests to scan devices on the network.
3. Sends ARP requests and receives responses, and then parses those responses.
4. Uses the OUI database to determine the device manufacturer based on the MAC address prefix.
5. Detects the device type and checks whether it is a computer based on a predefined list of device types.
6. Displays information about found devices.
