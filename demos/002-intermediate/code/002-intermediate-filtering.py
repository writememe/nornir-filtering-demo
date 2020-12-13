"""
This script is used to explain the basics of Nornir
filtering and it focuses on using simple filters
"""

# Import modules
from nornir import InitNornir
import os
import json
from colorama import Fore, init


# Auto-reset colorama colours back after each print statement
init(autoreset=True)

# Get path of the current dir under which the file is executed
dirname = os.path.dirname(os.path.abspath(__file__))


def get_nr():
    """
    Initialises a Nornir inventory using various configuration files

    :return nr: An initialised Nornir inventory for use in other functions.
    """
    # Initialise nornir
    nr = InitNornir(
        inventory={
            "options": {
                "host_file": os.path.join(
                    dirname,
                    "../motherstarter/outputs/nr/inventory/hosts.yaml",
                ),
                "group_file": os.path.join(
                    dirname,
                    "../motherstarter/outputs/nr/inventory/groups.yaml",
                ),
            }
        }
    )
    return nr


def display_inventory(nr):
    """
    Basic function to display the entire inventory for this demonstration.

    :param nr: An initialised Nornir inventory, used for processing.
    """
    # Print seperator line and hosts header
    print("=" * 50)
    print("HOSTS IN INVENTORY")
    # Iterate over hosts in inventory
    for host in nr.inventory.hosts.keys():
        # Print the hosts in the inventory
        print(f"Host: {Fore.CYAN}{host}")
    print(f"There are {len(nr.inventory.hosts.keys())} hosts in this inventory.")
    print("=" * 50)
    # Print seperator line and hosts header
    print("=" * 50)
    print("GROUPS IN INVENTORY")
    # Iterate over groups in inventory
    for group in nr.inventory.groups.keys():
        # Print the groups in the inventory
        print(f"Group: {Fore.CYAN}{group}")
    print(f"There are {len(nr.inventory.groups.keys())} groups in this inventory.")
    print("=" * 50)


def display_host_dict(nr, host):
    """
    Display entire host dictionary data structure for a given host.

    :param nr: An initialised Nornir inventory, used for processing.
    :param host: The host you want to filter on.
    :type host: string
    """
    # Filter all the hosts in the inventory, using the host passed in
    # at the top of the function.
    target_host = nr.inventory.hosts[host]
    # Dump the hosts data structure to an indented variable
    host_dict_data = json.dumps(target_host.dict(), indent=4)
    # Print seperator
    print("=" * 50)
    # Print header and host data structure
    print("Displaying information for host: " + Fore.CYAN + f"{host}")
    print(f"{host_dict_data}")
    # Print seperator
    print("=" * 50)


def display_group_dict(nr, group):
    """
    Display entire group dictionary data structure for a given group.

    :param nr: An initialised Nornir inventory, used for processing.
    :param group: The group you want to filter on.
    :type group: string
    """
    # Filter all the groups in the inventory, using the group passed in
    # at the top of the function.
    target_group = nr.inventory.groups[group]
    # Dump the groups data structure to an indented variable
    host_group_data = json.dumps(target_group.dict(), indent=4)
    # Print seperator
    print("=" * 50)
    # Print header and host data structure
    print("Displaying information for group: " + Fore.CYAN + f"{group}")
    print(f"{host_group_data}")
    # Print seperator
    print("=" * 50)


def filter_host_platform(nr, platform):
    """
    Filter the hosts inventory, based on a certain platform.

    :param nr: An initialised Nornir inventory, used for processing.
    :param platform: The type of platform you want to filter on.
    :type platform: string
    """
    # Filter the inventory, based on the platform provided to the
    # function
    target_hosts = nr.filter(platform=platform).inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have platform {platform} are:")
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


def filter_host_vendor(nr, vendor):
    """
    Filter the hosts inventory, based on a certain vendor.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The type of vendor you want to filter on.
    :type vendor: string
    """
    # Filter the inventory, based on the vendor provided to the
    # function
    target_hosts = nr.filter(vendor=vendor).inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have vendor {vendor} are:")
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


def filter_host_mgmt_ip(nr, mgmt_ip):
    """
    Filter the hosts inventory, based on a certain management
    IP address.

    :param nr: An initialised Nornir inventory, used for processing.
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string
    """
    # Filter the inventory, based on the management IP address provided to
    # the function
    target_hosts = nr.filter(mgmt_ip=mgmt_ip).inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have the management IP address {mgmt_ip} is:")
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


def filter_host_dev_type_vendor(nr, device_type, vendor):
    """
    Filter the hosts inventory, based on the following criteria:
    - device_type AND
    - vendor

    :param nr: An initialised Nornir inventory, used for processing.
    :param device_type: The device_type to filter on.
        For example: "router", "switch"
    :type device_type: string
    :param vendor: The vendor to filter on.
            For example: "cisco", "palo alto"
    :type vendor: string
    """
    # Filter the inventory to match the device_type AND vendor provided to
    # the function
    target_hosts = nr.filter(
        device_type=device_type, vendor=vendor
    ).inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which with device_type: {device_type} and vendor: {vendor} are:")
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


def filter_host_dev_type_vendor_mgmt_ip(nr, device_type, vendor, mgmt_ip):
    """
    Filter the hosts inventory, based on the following criteria:
    - device_type AND
    - vendor AND
    - mgmt_ip

    :param nr: An initialised Nornir inventory, used for processing.
    :param device_type: The device_type to filter on.
        For example: "router", "switch"
    :type device_type: string
    :param vendor: The vendor to filter on.
            For example: "cisco", "palo alto"
    :type vendor: string
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string
    """
    # Filter the inventory to match the device_type AND vendor AND mgmt_ip
    # provided to the function
    target_hosts = nr.filter(
        device_type=device_type, vendor=vendor, mgmt_ip=mgmt_ip
    ).inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(
        f"The host with device_type - {device_type} , vendor - {vendor} and mgmt_ip {mgmt_ip} is:"
    )
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


def filter_vendor(nr, vendor):
    """
    Filter the hosts inventory, based on a certain vendor.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The vendor to filter on.
        For example: "cisco", "palo alto"
    :type vendor: string

    :return target_vendor: The filtered nornir inventory which match
    the vendor supplied at the top of the function.
    """
    # Debug printout
    print(f"Targeting hosts with vendor: {vendor}")
    # Filter the entire inventory, based on the vendor provided to the function
    target_vendor = nr.filter(vendor=vendor)
    # Assign to variable for printouts
    target_vendor_hosts = target_vendor.inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have vendor - {vendor} are:")
    for host in target_vendor_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)
    # Return target_vendor object for further processing
    return target_vendor


def filter_dev_type(target_vendor, device_type):
    """
    Filter the hosts inventory on a device type, after the initial
    inventory has been filtered through a vendor.

    :param target_vendor: The filtered nornir inventory, filtered by a vendor.
    :param device_type: The device_type to filter on.
        For example: "router", "switch"
    :type device_type: string
    """
    # Filter the entire inventory even further, based on the device_type
    target_dev_type = target_vendor.filter(
        device_type=device_type
    ).inventory.hosts.keys()
    print(f"Targeting device_type: {device_type}")
    # Print seperator
    print("=" * 50)
    print(f"The hosts which with device_type - {device_type} are:")
    for host in target_dev_type:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


"""
Diagnostic/display functions
"""
# Initialise inventory
nr = get_nr()
# Display entire inventory
display_inventory(nr)
# Display host data structure
display_host_dict(nr, host="lab-arista-01.lab.dfjt.local")
# Display group data structure
display_group_dict(nr, group="ios")
display_group_dict(nr, group="nxos_ssh")
"""
Basic filter functions
"""
# filter_host_vendor(nr, vendor="arista")
# filter_group_vendor(nr, vendor="cisco")
# filter_host_platform(nr, platform="ios")
# filter_group_platform(nr, platform="nxos_ssh")
# filter_host_mgmt_ip(nr, mgmt_ip="10.0.0.1")
"""
Intermediate filter functions
"""
filter_host_dev_type_vendor(nr, device_type="switch", vendor="juniper")
filter_host_dev_type_vendor_mgmt_ip(
    nr, device_type="switch", vendor="juniper", mgmt_ip="10.0.0.23"
)
cisco_devices = filter_vendor(nr, vendor="cisco")
cisco_switches = filter_dev_type(target_vendor=cisco_devices, device_type="router")
cisco_routers = filter_dev_type(target_vendor=cisco_devices, device_type="switch")
cisco_firewalls = filter_dev_type(target_vendor=cisco_devices, device_type="firewall")