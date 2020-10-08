#!/bin/bash

if ! hash python3 > /dev/null 2>&1; then
    echo "Could not find python3"
    exit
fi

source ./venv.sh

./venv/bin/python spaceship-scraper/app.py
