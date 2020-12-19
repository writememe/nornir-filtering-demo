# Nornir Filtering Cheatsheet

The following cheatsheet has been provided to give you a quick reference
guide to what is possible using F filter object.

## Importing the F filter

```python
from nornir.core.filter import F
```

## F object logical operations

Below are the `F` filter operators:

| Character Pattern | Description |
| ---------- | ------------ |
|`~` | NOT |
|`&` | AND |
|`\|` | OR |

### Example Usage

All examples are "thereotical" are based on you [understanding how to initialise and populate an inventory](https://nornir.readthedocs.io/en/latest/tutorial/initializing_nornir.html)

```python
# Some boiler plate code that gets our nornir inventory
nr = get_nr()
# Filter for equals platform of "junos"
junos = nr.filter(F(platform__eq="junos"))
# Filter for NOT equals platform of "junos"
not_junos = nr.filter(~F(platform__eq="junos"))
# Filter for NOT equals platform of "junos" OR NOT equal platform of "ios"
not_junos_or_ios = nr.filter(~F(platform__eq="junos") | ~F(platform_eq="ios"))
# Filter for NOT equals platform of "junos" AND NOT equal sla of 80
not_junos_or_sla_eighty = nr.filter(~F(platform__eq="junos") & ~F(sla_eq=80))
```


## F object operations

Below are the `F` object operations:

| Character Pattern | Description | Type Usage |
| ---------- | ------------ |------ |
|`eq` | Equals | string, integer |
|`ge` | Greater than or equal to | integer |
|`gt`| Greater than | integer |
|`le` | Less than or equal to | integer |
|`lt`| Less than | integer |
|`contains` | Contains | string |
|`startswith` | Starts with | string |
|`endswith` | ends with | string |
|`any` | Any of the following | string |
|`has_parent_group`| Host has a parent group | string |
|`in`| In | string |
|`all`| All of | list - [See example](https://github.com/nornir-automation/nornir/blob/master/tests/core/test_filter.py#L128) |

### Example Usage

All examples are "thereotical" are based on you [understanding how to initialise and populate an inventory](https://nornir.readthedocs.io/en/latest/tutorial/initializing_nornir.html)

```python
# Some boiler plate code that gets our nornir inventory
nr = get_nr()
# Filter for equals platform of "junos"
junos = nr.filter(F(platform__eq="junos"))
# Filter for sla greater than or equal to 80
sla_eighty_or_greater = nr.filter(F(sla__ge=80))
# Filter for sla greater than 10
sla_more_than_ten = nr.filter(F(sla__gt=10))
# Filter for sla lesser than or equal to 90
sla_ninety_or_lesser = nr.filter(F(sla__le=90))
# Filter for sla lesser than 12
sla_less_than_twelve = nr.filter(F(sla__lt=12))
# Filter for a platform that contains "nos" in it.
# i.e match "paloalto_panos" or "junos" but not "nxos"
network_nos = nr.filter(F(platform__contains="nos"))
# Filter for a platform that starts with "ios".
# i.e match "ios", "iosxe" or "iosxr" but not "nxos"
ios_train_devs = nr.filter(F(platform__startswith="ios"))
# Filter for a platform that ends with "ios".
# i.e match "nxos" but not "ios", "paloalto_panos" or "junos"
nxos_devs = nr.filter(F(platform__endswith="xos"))
# Filter for a platform that is any of elements in our cisco_platforms
# list
cisco_platforms = ["catos", "ios", "iosxe", "iosxr", "nxos"]
cisco_devs = nr.filter(F(platform__any=cisco_platforms))
# Filter for any hosts which have the parent group of test
test_devs  = nr.filter(F(has_parent_group="test"))
# Filter for a platform that is in one of elements in our non_cisco_platforms
# list
# NOTE: Not sure how different this is to the "any" operation in case you
# were wondering too.
non_cisco_platforms = ["eos", "paloalto_panos", "junos"]
non_cisco_devs = nr.filter(F(platform__in=non_cisco_platforms))
```