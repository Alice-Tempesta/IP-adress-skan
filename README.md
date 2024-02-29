# Network device scanner

### Program description:

This program is a tool for scanning devices on a local network using ARP requests. Developed in the Python programming language using the Scapy library for working with network packets.

### Main components of the program:

1. Loading the OUI (Organizationally Unique Identifier) ​​database:
   - The OUI database is used to determine the device manufacturer by its MAC address.
   - The user can expand this base by adding MAC address prefixes and corresponding manufacturers.

2. Determining the router's IP address:
   -The netifaces library is used to determine the router's IP address.

3. Scanning the network using ARP requests:
   - The program sends ARP requests to detect devices on the local network.
   - Information about found devices (IP address, MAC address, device type) is saved and displayed.

4. Determining the device type:
   - The program determines the device type based on MAC address prefixes using the OUI database.

This program provides a convenient way to analyze devices on your local network and can be used to identify connected devices, their types and manufacturers.

### Installation

1. **Clone repository:**
<br> ```git clone git@github.com:Alice-Tempesta/IP-adress-skan.git```<br/>
<br> ```cd IP-address-scan```<br/>
2. **Installing dependencies:**
<br>```pip install -r requirements.txt```<br/>

3. **Setting up the OUI database:**
   - Modify the `oui_db` dictionary in the `IP-adress-skan.py` file to add new MAC prefixes-
addresses and corresponding manufacturers.

4. **Running the script:**
<br>```python IP-adress-skan.py```<br/>

### Settings

- Modify `oui_db` to add new MAC address prefixes and corresponding manufacturers.
- If necessary, configure the network interface parameters in the `get_router_ip()` function.

### Denial of responsibility

Please,
Use this tool responsibly and with appropriate permissions on your network.
