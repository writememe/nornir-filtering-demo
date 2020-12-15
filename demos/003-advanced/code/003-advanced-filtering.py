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
import re


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
    print(type(target_host))
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
    # Filter all the groups in the inventory, using the host passed in
    # at the top of the function.
    target_group = nr.inventory.groups[group]
    # Dump the groups data structure to an indented variable
    group_dict_data = json.dumps(target_group.dict(), indent=4)
    # Print seperator
    print("=" * 50)
    # Print header and host data structure
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
    :param mgmt_ip: The management IP to filter on.
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


def filter_group_platform(nr, platform):
    """
    TODO: This function doesn't work
    Filter the groups inventory, based on a certain platform.

    :param nr: An initialised Nornir inventory, used for processing.
    :param platform: The type of platform you want to filter on.
    :type platform: string

    :return target_groups: The targeted nornir groups after being
    processed through nornir filtering.
    """
    # Execute filter based on platform
    target_groups = nr.filter(platform=platform)
    print(type(target_groups))
    # Print seperator and header
    print("=" * 50)
    print(f"The groups which have platform {platform} are:")

    # Iterate over filtered results and printout information
    for group, data in target_groups.inventory.groups.items():
        print(
            f"Group: {Fore.CYAN}{group} "
            + Fore.RESET
            + f"- Platform: {Fore.CYAN}{data.platform}"
        )
    # Print total and seperator
    print(f"Total: {len(target_groups.inventory.hosts.items())}")
    # Print seperator
    print("=" * 50)
    # Return filtered groups
    return target_groups


def filter_group_vendor(nr, vendor):
    """
    TODO: This function doesn't work
    Filter the groups inventory, based on a certain vendor.

    :param nr: An initialised Nornir inventory, used for processing.
    :param vendor: The type of vendor you want to filter on.
    :type vendor: string

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on vendor
    target_groups = nr.filter(vendor=vendor).inventory.groups.keys()
    # Print seperator
    print("=" * 50)
    print(f"The hosts which have vendor {vendor} are:")
    for group in target_groups:
        print(f"Group: {Fore.CYAN}{group}")
    # Print seperator
    print("=" * 50)
    # Return filtered groups
    return target_groups


def filter_host_dev_type_vendor(nr, device_type, vendor):
    """
    Filter the hosts inventory, based on the following:
    - device_type AND,
    - vendor

    :param nr: An initialised Nornir inventory, used for processing.
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string

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
    :param mgmt_ip: The management IP to filter on.
    :type mgmt_ip: string

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


def filter_hemisphere(nr, hemisphere="southern"):
    """
    Filter all inventory based on hemisphere.

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on hemisphere
    target_hosts = nr.filter(F(hemisphere__eq=hemisphere))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts with {hemisphere} hemisphere are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Hemisphere: {Fore.CYAN}{data['hemisphere']} "
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_eq_site_code(nr, site_code):
    """
    Filter all inventory based on site_code

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on site code
    target_hosts = nr.filter(F(site_code__eq=site_code))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts with site code - {site_code} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_neq_site_code(nr, site_code):
    """
    Filter all inventory that does not equal a site_code

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on devices not equal to the site code
    target_hosts = nr.filter(~F(site_code__eq=site_code))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts WITHOUT site code - {site_code} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_or_site_code(nr, site_code_a, site_code_b):
    """
    Filter all inventory that equals a site_code_a OR site_code_b

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on site_code_a OR site_code_b
    target_hosts = nr.filter(
        F(site_code__eq=site_code_a) | F(site_code__eq=site_code_b)
    )
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts with site code - {site_code_a} or {site_code_b} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_not_and_dev_type(nr, dev_type_a, dev_type_b):
    """
    Filter all inventory that does not equal a dev_type_a AND dev_type_b

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter not equal to on dev_type_a OR dev_type_b
    target_hosts = nr.filter(
        ~F(device_type__eq=dev_type_a) & ~F(device_type__eq=dev_type_b)
    )
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which are NOT device_type - {dev_type_a} AND {dev_type_b} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Device Type: {Fore.CYAN}{data['device_type']}"
        )
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_env_devices(nr, environment):
    """
    Filter all inventory that does not equal a dev_type_a AND dev_type_b

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based hosts being children of a group
    target_hosts = nr.inventory.children_of_group(environment)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which are children of group {environment} are:")
    # Iterate over filtered results and printout information
    for host in target_hosts:
        print(f"Host: {Fore.CYAN}{host}")
    print(f"Total: {len(target_hosts)}")
    # Print total and seperator
    print(f"Total: {len(list(target_hosts))}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_ge_sla(nr, sla):
    """
    Filter all inventory that does not equal a dev_type_a AND dev_type_b

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based greater or equal to the SLA integer
    target_hosts = nr.filter(F(sla__ge=sla))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts with SLA greater or equal to {sla} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- SLA: {Fore.CYAN}{data['sla']} "
            + Fore.RESET
            + f"- Production: {Fore.CYAN}{data['production']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_certified_os_version(nr, version_list=None):
    """
    Filter the entire inventory to find devices
    running

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Specify a list of versions, which are deemed "certified"
    # across the inventory
    version_list = [
        "10.0.3",  # panos certified version
        "16.6.4",  # ios certified version
        "4.23.2F",  # eos certified version
        "9.3(6)",  # nxos certified version
        "18.4R2-S5",  # junos certified version
    ]
    # Execute filter based on hosts matching any of the certified versions
    target_hosts = nr.filter(F(os_version__any=version_list))
    # Print seperator and header
    print("=" * 50)
    print(f"Certified OS version(s): {version_list}")
    print(f"The hosts running a certified OS version are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Platform: {Fore.CYAN}{data.platform} "
            + Fore.RESET
            + f"- OS Version: {Fore.CYAN}{data['os_version']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_non_certified_os_version(nr, version_list=None):
    """
    Filter the entire inventory to find devices
    running

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Specify a list of versions, which are deemed "certified"
    # across the inventory
    version_list = [
        "10.0.3",  # panos certified version
        "16.6.4",  # ios certified version
        "4.23.2F",  # eos certified version
        "9.3(6)",  # nxos certified version
        "18.4R2-S5",  # junos certified version
    ]
    # Execute filter based on hosts NOT matching any of the certified versions
    target_hosts = nr.filter(~F(os_version__any=version_list))
    # Print seperator and header
    print("=" * 50)
    print(f"Certified OS version(s): {version_list}")
    print(f"The hosts NOT running a certified OS version are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Platform: {Fore.CYAN}{data.platform} "
            + Fore.RESET
            + f"- OS Version: {Fore.CYAN}{data['os_version']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_production_hosts(nr):
    """
    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on hosts being in production
    target_hosts = nr.filter(F(production__eq=True))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts running in Production are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Platform: {Fore.CYAN}{data.platform} "
            + Fore.RESET
            + f"- OS Version: {Fore.CYAN}{data['os_version']} "
            + Fore.RESET
            + f"- Production?: {Fore.CYAN}{data['production']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_region(nr, region):
    """
    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on hosts in a region
    target_hosts = nr.filter(F(region__eq=region))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts in region {region} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Region: {Fore.CYAN}{data['region']} "
            + Fore.RESET
            + f"- Country: {Fore.CYAN}{data['country']} "
            + Fore.RESET
            + f"- Full Name: {Fore.CYAN}{data['full_name']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def odd_device_naming_convention(host):
    """
    TODO: Doco function
    """
    return bool(re.match(".+\-[0-9][1,3,5,7,9].+", host.name))


def even_device_naming_convention(host):
    """
    TODO: Doco function
    """
    return bool(re.match(".+\-[0-9][2,4,6,8,0].+", host.name))


def test_domain_name_convention(host):
    """
    TODO: Doco function
    """
    return bool(re.match(".+.tst.dfjt.local$", host.name))


def device_name_convention(host):
    """
    TODO: Doco function
    """
    if re.match("\w{3}\-\w+\-\d{2}.\w{3}.dfjt.local", host.name):
        return True
    else:
        return False


def non_device_name_convention(host):
    """
    TODO: Doco function
    """
    if re.match("\w{3}\-\w+\-\d{2}.\w{3}.dfjt.local", host.name):
        return False
    else:
        return True


def filter_odd_devices(nr):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering."""
    # Execute filter which calls a function to detect hosts with an
    # odd number in their naming convention
    target_hosts = nr.filter(filter_func=odd_device_naming_convention)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which match the odd naming convention are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Region: {Fore.CYAN}{data['region']} "
            + Fore.RESET
            + f"- Country: {Fore.CYAN}{data['country']} "
            + Fore.RESET
            + f"- Full Name: {Fore.CYAN}{data['full_name']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_even_devices(nr):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter which calls a function to detect hosts with an
    # even number in their naming convention
    target_hosts = nr.filter(filter_func=even_device_naming_convention)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which match the even naming convention are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Region: {Fore.CYAN}{data['region']} "
            + Fore.RESET
            + f"- Country: {Fore.CYAN}{data['country']} "
            + Fore.RESET
            + f"- Full Name: {Fore.CYAN}{data['full_name']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_test_domain_devices(nr):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter which calls a function to detect hosts with a
    # test domain-name in their naming convention
    target_hosts = nr.filter(filter_func=test_domain_name_convention)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which match the test domain-name naming convention are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(f"Host: {Fore.CYAN}{host} ")
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_device_name_convention(nr):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter which calls a function to detect hosts which
    # match a pre-defined naming convention
    target_hosts = nr.filter(filter_func=device_name_convention)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which match the device naming convention are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(f"Host: {Fore.CYAN}{host} ")
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_device_name_non_convention(nr):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter which calls a function to detect hosts which do not
    # match a pre-defined naming convention
    target_hosts = nr.filter(filter_func=non_device_name_convention)
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which do NOT match the device naming convention are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(f"Host: {Fore.CYAN}{host} ")
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_site_type(nr, site_type):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter based on site type
    target_hosts = nr.filter(F(site_type__eq=site_type))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which match site type {site_type} are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Type: {Fore.CYAN}{data['site_type']} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']} "
            + Fore.RESET
            + f"- Full Name: {Fore.CYAN}{data['full_name']}"
        )
    # Print total and seperator
    print(f"Total: {len(target_hosts.inventory.hosts.items())}")
    print("=" * 50)
    # Return filtered hosts
    return target_hosts


def filter_non_primary_site_type(nr):
    """

    :return target_hosts: The targeted nornir hosts after being
    processed through nornir filtering.
    """
    # Execute filter which the site_type of secondary OR tertiary
    target_hosts = nr.filter(F(site_type__any=["tertiary", "secondary"]))
    # Print seperator and header
    print("=" * 50)
    print(f"The hosts which are at non-primary site types are:")
    # Iterate over filtered results and printout information
    for host, data in target_hosts.inventory.hosts.items():
        print(
            f"Host: {Fore.CYAN}{host} "
            + Fore.RESET
            + f"- Site Type: {Fore.CYAN}{data['site_type']} "
            + Fore.RESET
            + f"- Site Code: {Fore.CYAN}{data['site_code']} "
            + Fore.RESET
            + f"- Full Name: {Fore.CYAN}{data['full_name']}"
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
filter_host_vendor(nr, vendor="arista")
filter_group_vendor(nr, vendor="cisco")
filter_host_platform(nr, platform="ios")
filter_group_platform(nr, platform="nxos_ssh")
filter_host_mgmt_ip(nr, mgmt_ip="10.0.0.1")
"""
Intermediate filter functions
"""
filter_host_dev_type_vendor(nr, device_type="switch", vendor="juniper")
filter_host_dev_type_vendor_mgmt_ip(
    nr, device_type="switch", vendor="juniper", mgmt_ip="10.0.0.23"
)
cisco_devices = filter_vendor(nr, vendor="cisco")
filter_dev_type(target_vendor=cisco_devices, device_type="router")
filter_dev_type(target_vendor=cisco_devices, device_type="switch")
filter_dev_type(target_vendor=cisco_devices, device_type="firewall")
"""
Advanced filter functions
"""
filter_hemisphere(nr, hemisphere="northern")
filter_eq_site_code(nr, site_code="mtl")
filter_neq_site_code(nr, site_code="mel")
filter_or_site_code(nr, site_code_a="ptl", site_code_b="chc")
filter_not_and_dev_type(nr, dev_type_a="switch", dev_type_b="router")
filter_env_devices(nr, environment="test")
filter_ge_sla(nr, sla=80)
filter_certified_os_version(nr)
non_cert_devs = filter_non_certified_os_version(nr)
filter_production_hosts(nr=non_cert_devs)
apac_devices = filter_region(nr, region="apac")
filter_odd_devices(nr)
filter_even_devices(nr)
filter_test_domain_devices(nr)
filter_device_name_convention(nr)
filter_device_name_non_convention(nr)
filter_site_type(nr, site_type="primary")
filter_non_primary_site_type(nr)
"""
Chaining filters together
"""
odd_devices = filter_odd_devices(nr)
compliant_odd_devices = filter_device_name_convention(nr=odd_devices)
apac_compliant_odd_devices = filter_region(nr=compliant_odd_devices, region="apac")
apac_secondary_compliant_odd_devices = filter_non_primary_site_type(
    nr=apac_compliant_odd_devices
)
apac_secondary_compliant_odd_certified_os_devices = filter_certified_os_version(
    nr=apac_secondary_compliant_odd_devices
)
