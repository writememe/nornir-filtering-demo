"""
This script is the main engine to make backend calls to network
devices and present the data back in a structured format to the
web front end.
"""

# Import modules
from nornir import InitNornir

# from nornir.core.filter import F
import os
import json

# Get path of the current dir under which the file is executed
dirname = os.path.dirname(os.path.abspath(__file__))


def get_nr():
    """
    Initialises a Nornir inventory using various configuration files

    :return nr: An initialised Nornir inventory for use in other functions.
    """
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
    Basic function to display the inventory for this demonstration.

    :param nr: An initialised Nornir inventory, used for processing.
    """
    print("*" * 20 + "  HOSTS  " + "*" * 20)
    # Iterate over hosts in inventory
    for host in nr.inventory.hosts.keys():
        # Print the hosts in the inventory
        print(f"Host: {host}")
    print(f"There are {len(nr.inventory.hosts.keys())} hosts in this inventory.")
    print("*" * 50)
    print("*" * 20 + "  GROUPS  " + "*" * 20)
    # Iterate over groups in inventory
    for group in nr.inventory.groups.keys():
        # Print the groups in the inventory
        print(f"Group: {group}")
    print(f"There are {len(nr.inventory.groups.keys())} groups in this inventory.")
    print("*" * 50)


def display_host(nr, host):
    """
    Display information for a given host.
    """
    # Ref Doco
    # https://nornir.readthedocs.io/en/latest/api/nornir/core/inventory.html#nornir.core.inventory.Host
    target_host = nr.inventory.hosts[host]
    print(f"Host Keys: {target_host.keys()}")
    print(f"Host Items: {target_host.items()}")
    print(f"Host Dict for {host}:")
    print(json.dumps(target_host.dict(), indent=4))
    print(f"Host: {target_host}")
    print(f"Host: {target_host} - Groups: {target_host.groups}")


def display_group(nr, group):
    """
    Display information for a given group.
    """
    # Ref Doco
    # https://nornir.readthedocs.io/en/latest/api/nornir/core/inventory.html#nornir.core.inventory.Host
    target_group = nr.inventory.groups[group]
    print(f"Group Keys: {target_group.keys()}")
    print(f"Group Items: {target_group.items()}")
    print(f"Group Dict for {target_group}:")
    print(json.dumps(target_group.dict(), indent=4))
    print(f"Group: {target_group}")
    print(f"Group: {target_group} - Groups: {target_group.groups}")


def filter_platform(nr, platform):
    """
    Filter the inventory, based on a certain platform.

    :param nr: An initialised Nornir inventory, used for processing.
    :param platform: The type of platform you want to filter on.
    :type platform: string
    """
    target_hosts = nr.filter(platform=platform).inventory.hosts.keys()
    print(f"The hosts which have platform {platform} are:")
    for host in target_hosts:
        print(f"Host: {host}")


def filter_vendor(nr, vendor):
    """
    Filter the inventory, based on a certain vendor.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The type of vendor you want to filter on.
    :type vendor: string
    """
    target_hosts = nr.filter(vendor=vendor).inventory.hosts.keys()
    print(f"The hosts which have vendor {vendor} are:")
    for host in target_hosts:
        print(f"Host: {host}")


# Initialise inventory
nr = get_nr()
# Display entire inventory
# display_inventory(nr)
display_host(nr, host="lab-arista-02.lab.dfjt.local")
display_group(nr, group="junos")
filter_vendor(nr, vendor="arista")
filter_platform(nr, platform="junos")
