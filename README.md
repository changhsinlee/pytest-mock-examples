# Samples for using `pytest-mock`

This repository hosts the code in  

* [How to mock with pytest in Python](https://changhsinlee.com/pytest-mock/)

## Running the code

### Requirements

* Python version `>=3.5` is required.

### Create environment

After cloning the repository, create a virtual environment in the repository with

```sh
python3 -m venv .venv
```

Then activate the virtual environment and install the repository as a package

```sh
# For Macs or Linux
source .venv/bin/activate

# For Windows
.venv\Scripts\activate

# Navigate to where setup.py is
pip install -e .
```

### Running tests

To run the tests, run

```sh
# print out the durations for each test
pytest --durations=0
```