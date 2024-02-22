import scapy.all as scapy
import ipaddress
import netifaces

# Load OUI (Organizationally Unique Identifier) database
# This database contains MAC address prefixes and their corresponding device manufacturers
oui_db = {
    "00:0a:95": "Apple",
    "00:1A:2B": "Samsung",
    # Add other MAC prefixes and their corresponding manufacturers
}


def get_router_ip():
    try:
        # Get the router's IP address from the default gateways
        default_gateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
        return default_gateway
    except Exception as e:
        print(f"Error getting router IP: {e}")
        return None


def is_computer(device_type):
    # Add device types considered as computers
    computer_types = ["Personal computer", "Laptop", "Unknown"]
    return device_type in computer_types


def scan(ip):
    # Create an ARP request for scanning devices in the network
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the request and get the response
    answered_list = scapy.srp(arp_request_broadcast, timeout=6, verbose=False)[0]

    # Create a list of devices with information about the type and whether it's a computer
    clients_list = []
    for element in answered_list:
        ip_address = element[1].psrc
        mac_address = element[1].hwsrc

        # Determine the device type based on the MAC address prefix
        device_type = oui_db.get(mac_address[:8].upper(), "Unknown")

        # Add a dictionary with information about the device and whether it's a computer to the list
        is_computer_device = is_computer(device_type)
        client_dict = {"ip": ip_address, "mac": mac_address, "type": device_type, "is_computer": is_computer_device}
        clients_list.append(client_dict)
    return clients_list


def get_network_range(ip_address, subnet_mask_length):
    # Create a network object for scanning
    ip_network = ipaddress.IPv4Network(f"{ip_address}/{subnet_mask_length}", strict=False)
    return ip_network


def main():
    router_ip = get_router_ip()
    if router_ip:
        print(f"Router IP Address: {router_ip}")

        # Get the subnet from the router's IP address
        subnet = router_ip.split(".")
        subnet.pop(-1)  # Remove the last element (the IP itself)
        subnet.append("0/24")  # Add 0/24 to get the subnet

        subnet_str = ".".join(subnet)
        subnet_mask_length = int(subnet_str.split("/")[-1])

        # Create a network object for scanning
        network_range = get_network_range(router_ip, subnet_mask_length)

        # Get a list of devices in the network with information about the type and whether it's a computer
        clients_list = scan(subnet_str)
        print("\nDevices connected to the network:")
        print("{:<20} {:<20} {:<20} {:<15}".format("IP Address", "MAC Address", "Device Type", "Is Computer"))
        print("-" * 85)
        for client in clients_list:
            # Print IP address, MAC address, device type, and information about whether the device is a computer
            print("{:<20} {:<20} {:<20} {:<15}".format(client['ip'], client['mac'], client['type'], client['is_computer']))
    else:
        print("Unable to retrieve router IP address.")


if __name__ == "__main__":
    main()
