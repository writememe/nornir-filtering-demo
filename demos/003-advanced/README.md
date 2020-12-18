# 003 - Advanced Filtering

The demo contains all types of feasible nornir filters, but focuses on:

-  nornir `F` filtering
- `filter_func` - Filter functions
- "Chaining" filters to highlight the full flexibility on offer
## Operating Instructions

To see the demo in action, there are two options available.

### Option 1 - motherstarter + nornir demo

This option uses motherstarter to convert the [inventory.json](inputs/inventory.json) and [groups.json](inputs/groups.json) files into the equivalent nornir inventory data, ready to be used by the demo.

1) Convert the inventory/groups.json files into nornir inventory files

```python
motherstarter convert -sd inputs -td templates -st json -o nornir
```

2) Execute the demo, which will printout the results of all the functions:

```python
python code/003-advanced-filtering.py
```

### Option 2 - nornir demo only

This option just runs the demo only and does not use motherstarter.

1) Execute the demo, which will printout the results of all the functions:

```python
python code/003-advanced-filtering.py
```