![nornir-filtering-demo](https://github.com/writememe/nornir-filtering-demo/workflows/nornir-filtering-demo/badge.svg)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Nornir 3 Filtering Demo

This repository contains a set of examples and use-cases using nornir filtering.

# Table of Contents

- [Installation](#installation)
- [Structure](#structure)
- [Videos](#videos)
- [Reference Documentation](#reference-documentation)


## Installation

In order to use the demo, please follow the installation instructions below:

1. Create the virtual environment to run the application in:

```bash
virtualenv --python=`which python3` venv
source venv/bin/activate
```

2. Install the requirements:

```python
pip install -r requirements.txt
```

## Structure

The demos provided in this repository are provided as "canned demos". 

That is, all commands, requirements and dependencies are contained inside each folder.

The demos work their way up in terms of complexity and depth of use-cases and are intended to be followed in the order that is shown below:

| Level | Description |
| ---------- | ------------ | 
|001-basic| Basic nornir filtering using one-dimensional filters|
|002-intermediate| Intermediate nornir filtering using multi-dimensional filters |
|003-advanced| Advanced filtering using the `F` filter, filter functions and "chained" filters|

In addition to this, each demo contains all the code of the previous demo, so you can compare functions and see the differences.

For example, `003-advanced` will contain all code from the `001-basic` and `002-intermediate` demos.


## Videos

Coming soon :)