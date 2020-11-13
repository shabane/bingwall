sudo apt-get install python3-pip
pip3 install -r lib.txt
sudo cp bingwall.py /etc/cron.daily
sudo chmod +x /etc/cron.daily/bingwall.py
echo "Have Fun"