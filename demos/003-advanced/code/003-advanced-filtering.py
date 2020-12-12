"""
This script is used to explain the basics of Nornir
filtering and it focuses on using simple filters
"""

# Import modules
from nornir import InitNornir
import os
import json
from colorama import Fore, init
from nornir.core.filter import F


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
    # Filter all the groups in the inventory, using the host passed in
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
    target_hosts = nr.filter(mgmt_ip=mgmt_ip).inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have the management IP address {mgmt_ip} is:")
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)


def filter_group_platform(nr, platform):
    """
    Filter the groups inventory, based on a certain platform.

    :param nr: An initialised Nornir inventory, used for processing.
    :param platform: The type of platform you want to filter on.
    :type platform: string
    """
    target_groups = nr.filter(platform=platform).inventory.groups.keys()
    # Print seperator
    print("=" * 50)
    print(f"The groups which have platform {platform} are:")
    for group in target_groups:
        print(f"Group: {Fore.CYAN}{group}")
    # Print seperator
    print("=" * 50)


def filter_group_vendor(nr, vendor):
    """
    Filter the groups inventory, based on a certain vendor.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The type of vendor you want to filter on.
    :type vendor: string
    """
    target_groups = nr.filter(vendor=vendor).inventory.groups.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have vendor {vendor} are:")
    for group in target_groups:
        print(f"Group: {Fore.CYAN}{group}")
    # Print seperator
    print("=" * 50)


def filter_host_dev_type_vendor(nr, device_type, vendor):
    """
    Filter the hosts inventory, based on the following:
    - device_type AND,
    - vendor

    :param nr: An initialised Nornir inventory, used for processing.
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string
    """
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
    Filter the hosts inventory, based on the following:
    - device_type AND,
    - vendor AND,
    - mgmt_ip

    :param nr: An initialised Nornir inventory, used for processing.
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string
    """
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
    Filter the hosts inventory, based on a certain management
    IP address.

    :param nr: An initialised Nornir inventory, used for processing.
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string
    """
    print(f"Targeting vendor: {vendor}")
    target_vendor = nr.filter(vendor=vendor)
    # Assign to variable for printouts
    target_vendor_hosts = target_vendor.inventory.hosts.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which with vendor - {vendor} are:")
    for host in target_vendor_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    # Print seperator
    print("=" * 50)
    return target_vendor


def filter_dev_type(target_vendor, device_type):
    """"""
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


def filter_hemisphere(nr, hemisphere="southern"):
    """
    TODO: Not working
    Filter all inventory based on hemisphere
    """
    # hemisphere = nr.filter(F(groups__data))
    hemisphere_devs = nr.filter(F(groups__contains=hemisphere))
    print(f"Devices in {hemisphere} hemisphere are:")
    print("=" * 50)
    for host in hemisphere_devs.inventory.groups.keys():
        print(f"Host: {Fore.CYAN}{host}")
    print(f"Total: {len(hemisphere_devs.inventory.groups.keys())}")
    # Print seperator
    print("=" * 50)


def filter_eq_site_code(nr, site_code):
    """
    Filter all inventory based on site_code
    """
    site_code_devs = nr.filter(F(site_code__eq=site_code))
    print(f"Hosts with site code - {site_code} are:")
    print("=" * 50)
    for host, data in site_code_devs.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']}"
        )
    print(f"Total: {len(site_code_devs.inventory.hosts.items())}")
    # Print seperator
    print("=" * 50)


def filter_neq_site_code(nr, site_code):
    """
    Filter all inventory that does not equal a site_code
    """
    not_site_code_devs = nr.filter(~F(site_code__eq=site_code))
    print(f"Hosts WITHOUT site code - {site_code} are:")
    print("=" * 50)
    for host, data in not_site_code_devs.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']}"
        )
    print(f"Total: {len(not_site_code_devs.inventory.hosts.items())}")
    # Print seperator
    print("=" * 50)


def filter_or_site_code(nr, site_code_a, site_code_b):
    """
    Filter all inventory that equals a site_code_a OR site_code_b
    """
    two_site_code_devs = nr.filter(
        F(site_code__eq=site_code_a) | F(site_code__eq=site_code_b)
    )
    print(f"Hosts with site code - {site_code_a} or {site_code_b} are:")
    print("=" * 50)
    for host, data in two_site_code_devs.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']}"
        )
    print(f"Total: {len(two_site_code_devs.inventory.hosts.items())}")
    # Print seperator
    print("=" * 50)


def filter_not_and_dev_type(nr, dev_type_a, dev_type_b):
    """
    Filter all inventory that does not equal a dev_type_a AND dev_type_b
    """
    not_two_dev_type_devs = nr.filter(
        ~F(device_type__eq=dev_type_a) & ~F(device_type__eq=dev_type_b)
    )
    print(f"Hosts which are NOT device_type - {dev_type_a} AND {dev_type_b} are:")
    print("=" * 50)
    # TODO: Refactor code to use this
    for host, data in not_two_dev_type_devs.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Device Type: {Fore.CYAN}{data['device_type']}"
        )
    print(f"Total: {len(not_two_dev_type_devs.inventory.hosts.items())}")
    # Print seperator
    print("=" * 50)


def filter_env_devices(nr, environment):
    """
    Filter all inventory that does not equal a dev_type_a AND dev_type_b
    """
    env_devs = nr.inventory.children_of_group(environment)
    print(f"Hosts which are children of group {environment} are:")
    print("=" * 50)
    for host in env_devs:
        print(f"Host: {Fore.CYAN}{host}")
    print(f"Total: {len(env_devs)}")
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
display_group_dict(nr, group="test")
display_group_dict(nr, group="ptl")
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
# filter_host_dev_type_vendor(nr, device_type="switch", vendor="juniper")
# filter_host_dev_type_vendor_mgmt_ip(
#     nr, device_type="switch", vendor="juniper", mgmt_ip="10.0.0.23"
# )
# cisco_devices = filter_vendor(nr, vendor="cisco")
# filter_dev_type(target_vendor=cisco_devices, device_type="router")
# filter_dev_type(target_vendor=cisco_devices, device_type="switch")
# filter_dev_type(target_vendor=cisco_devices, device_type="firewall")
"""
Advanced filter functions
"""
# filter_hemisphere(nr)
filter_eq_site_code(nr, site_code="mel")
filter_neq_site_code(nr, site_code="mel")
filter_or_site_code(nr, site_code_a="mel", site_code_b="chc")
filter_not_and_dev_type(nr, dev_type_a="switch", dev_type_b="router")
filter_env_devices(nr, environment="test")
