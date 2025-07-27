#!/bin/bash

pip3 install -r requirements.txt

sudo apt-get install -y python3-module-rpm
sudo apt-get install -y python3-module-pip

python3 cli.py --branch1 sisyphus --branch2 p11 --output result.json

python3 -m pytest tests/