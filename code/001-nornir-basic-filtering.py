"""
This script is the main engine to make backend calls to network
devices and present the data back in a structured format to the
web front end.
"""

# Import modules
from nornir import InitNornir
from nornir.core.filter import F
import os

# Get path of the current dir under which the file is executed
dirname = os.path.dirname(os.path.abspath(__file__))


def get_nr():
    """
    Initialises a Nornir inventory from the various configuration
    files
    :return nr: An initialised Nornir inventory for use in other functions.
    """
    nr = InitNornir(
        inventory={
            "options": {
                "host_file": os.path.join(
                    dirname,
                    "../outputs/001-basic/motherstarter/outputs/nr/inventory/hosts.yaml",
                ),
                "group_file": os.path.join(
                    dirname,
                    "../outputs/001-basic/motherstarter/outputs/nr/inventory/groups.yaml",
                ),
                # "defaults_file": "inventory/defaults.yaml",
            }
        }
    )
    return nr


nr = get_nr()
print(nr.inventory.hosts.keys())
print(f"There are {len(nr.inventory.hosts.keys())} hosts in this inventory.")
