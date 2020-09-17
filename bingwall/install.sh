#!/usr/bin/bash
sudo mkdir /var/log/bingwall
sudo chmod o+rwx /var/log/bingwall
sudo mkdir /opt/bingwall
sudo cp bingwall.py /opt/bingwall
sudo apt-get install python3-pip
pip3 install -r lib.txt
sudo cp bingwall.service /lib/systemd/system
sudo systemctl daemon-reload
systemctl enable bingwall.service
sudo systemctl start bingwall.service