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
    Initialises a Nornir inventory using various configuration files.

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
    # Iterate over hosts in inventory and printout hosts
    for host in nr.inventory.hosts.keys():
        print(f"Host: {Fore.CYAN}{host}")
    print(f"There are {len(nr.inventory.hosts.keys())} hosts in this inventory.")
    print("=" * 50)
    # Print seperator line and hosts header
    print("=" * 50)
    print("GROUPS IN INVENTORY")
    # Iterate over hosts in inventory and printout groups
    for group in nr.inventory.groups.keys():
        print(f"Group: {Fore.CYAN}{group}")
    print(f"There are {len(nr.inventory.groups.keys())} groups in this inventory.")
    print("=" * 50)


def display_host_dict(nr, host):
    """
    Display entire host dictionary data structure for a given host.

    :param nr: An initialised Nornir inventory, used for processing.
    :param host: The host you want to filter on.
    :type host: string

    :return target_host: The targeted nornir host object.
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
    # Return target host
    return target_host


def display_group_dict(nr, group):
    """
    Display entire group dictionary data structure for a given group.

    :param nr: An initialised Nornir inventory, used for processing.
    :param group: The group you want to filter on.
    :type group: string

    :return target_group: The targeted nornir group object.
    """
    # Filter all the groups in the inventory, using the group passed in
    # at the top of the function.
    target_group = nr.inventory.groups[group]
    # Dump the groups data structure to an indented variable
    group_dict_data = json.dumps(target_group.dict(), indent=4)
    # Print seperator
    print("=" * 50)
    # Print header and group data structure
    print("Displaying information for group: " + Fore.CYAN + f"{group}")
    print(f"{group_dict_data}")
    # Print seperator
    print("=" * 50)
    # Return target group
    return target_group


def filter_host_platform(nr, platform):
    """
    Filter the hosts inventory, based on a certain platform.

    :param nr: An initialised Nornir inventory, used for processing.
    :param platform: The type of platform you want to filter on.
    :type platform: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on platform
    target_hosts = nr.filter(platform=platform)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which have platform {platform} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Platform: {Fore.CYAN}{data.platform}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_host_vendor(nr, vendor):
    """
    Filter the hosts inventory, based on a certain vendor.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The type of vendor you want to filter on.
    :type vendor: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on vendor
    target_hosts = nr.filter(vendor=vendor)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which have vendor {vendor} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Vendor: {Fore.CYAN}{data['vendor']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_host_mgmt_ip(nr, mgmt_ip):
    """
    Filter the hosts inventory, based on a certain management
    IP address.

    :param nr: An initialised Nornir inventory, used for processing.
    :param mgmt_ip: The management IP address to filter on.
    :type mgmt_ip: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on management IP address
    target_hosts = nr.filter(mgmt_ip=mgmt_ip)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which have the management IP address {mgmt_ip} is:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Management IP: {Fore.CYAN}{data['mgmt_ip']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_host_dev_type_vendor(nr, device_type, vendor):
    """
    Filter the hosts inventory, based on the following:
    - device_type AND,
    - vendor

    :param nr: An initialised Nornir inventory, used for processing.
    :param device_type: The device type to filter on.
    :type device_type: string
    :param vendor: The vendor to filter on.
    :type vendor: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on device type AND vendor
    target_hosts = nr.filter(device_type=device_type, vendor=vendor)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts with device_type: {device_type} and vendor: {vendor} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Device Type: {Fore.CYAN}{data['device_type']} "
            + Fore.RESET
            + f"- Vendor: {Fore.CYAN}{data['vendor']} "
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_host_dev_type_vendor_mgmt_ip(nr, device_type, vendor, mgmt_ip):
    """
    Filter the hosts inventory, based on the following:
    - device_type AND,
    - vendor AND,
    - mgmt_ip

    :param nr: An initialised Nornir inventory, used for processing.
    :param device_type: The device type to filter on.
    :type device_type: string
    :param vendor: The vendor to filter on.
    :type vendor: string
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on device type AND vendor AND mgmt_ip
    target_hosts = nr.filter(device_type=device_type, vendor=vendor, mgmt_ip=mgmt_ip)
    # Print seperator and header
    print("=" * 50)
    print(
        f"The host with device_type: {device_type} , vendor: {vendor} and mgmt_ip: {mgmt_ip} is:"
    )
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Device Type: {Fore.CYAN}{data['device_type']} "
            + Fore.RESET
            + f"- Vendor: {Fore.CYAN}{data['vendor']} "
            + Fore.RESET
            + f"- Management IP: {Fore.CYAN}{data['mgmt_ip']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_vendor(nr, vendor):
    """
    Filter the hosts inventory, based on a certain management
    IP address.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The vendor to filter on.
    :type vendor: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on vendor
    target_hosts = nr.filter(vendor=vendor)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which with vendor - {vendor} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Vendor: {Fore.CYAN}{data['vendor']} "
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_dev_type(target_vendor, device_type):
    """
    Filter the already filtered inventory, based on device type.

    :param target_vendor: A pre-filtered Nornir inventory, used for processing.
    :param device_type: The device type to filter on.
    :type device_type: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on device type
    target_hosts = target_vendor.filter(device_type=device_type)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which with device_type - {device_type} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Device Type: {Fore.CYAN}{data['device_type']} "
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


"""
Diagnostic/display functions
"""
# Initialise inventory
# Initialise inventory
nr = get_nr()
# Display entire inventory
display_inventory(nr)
# Display host data structure
display_host_dict(nr, host="lab-arista-01.lab.dfjt.local")
# Display group data structure
display_group_dict(nr, group="test")
display_group_dict(nr, group="nxos_ssh")
"""
Basic filter functions
"""
# filter_host_vendor(nr, vendor="arista")
# filter_host_platform(nr, platform="ios")
# filter_host_mgmt_ip(nr, mgmt_ip="10.0.0.1")
"""
Intermediate filter functions
"""
filter_host_dev_type_vendor(nr, device_type="switch", vendor="juniper")
filter_host_dev_type_vendor_mgmt_ip(
    nr, device_type="switch", vendor="juniper", mgmt_ip="10.0.0.23"
)
cisco_devices = filter_vendor(nr, vendor="cisco")
cisco_routers = filter_dev_type(target_vendor=cisco_devices, device_type="router")
cisco_switches = filter_dev_type(target_vendor=cisco_devices, device_type="switch")
cisco_firewalls = filter_dev_type(target_vendor=cisco_devices, device_type="firewall")
