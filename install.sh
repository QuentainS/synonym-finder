#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

cp syn.py /usr/bin/syn
chmod +x /usr/bin/syn
python3 -m pip install -r requirements.txt > /dev/null 2>&1

echo ""
echo "Installed"
echo "Try : syn word"