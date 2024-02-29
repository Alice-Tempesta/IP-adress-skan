# Network device scanner

## Program description:

This program is a tool for scanning devices on a local network using ARP requests. It is developed in the Python programming language using the Scapy library for working with network packets.

### The program includes the following main components:

1. Loading the OUI (Organizationally Unique Identifier) ​​database:
  - The OUI database is used to determine the device manufacturer by its MAC address.
  - The user can expand this base by adding MAC address prefixes and their corresponding manufacturers.
2. Determining the router's IP address:
  - Uses netifaces library to determine IProuter addresses.
3. Scanning a network using ARP requests:
  - The program sends ARP requests to discover devices on the local network.
  - Information about found devices (IP address, MAC address, device type) is saved and displayed on the screen.
4. Determining the device type:
  - The program determines the device type based on the MAC prefix addresses using the OUI database.

This program provides a convenient way to analyze devices on your local network and can be used to identify connected devices, their types and manufacturers.

## Usage

Run the script with the command:

```python main.py```

## Settings

- Modify `oui_db` to add new MAC address prefixes and their corresponding manufacturers.
- If necessary, configure the network interface parameters in the `get_router_ip()` function.

## Denial of responsibility

Please,
Use this tool responsibly and with appropriate permissions on your network.
