#!/bin/bash

# run tests in unittest mode
python -m unittest discover -s test

# run tests in nose mode
nosetests

