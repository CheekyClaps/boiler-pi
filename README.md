# Boiler-PI
### Raspberry-pi python flask sqlite webserver
A flask server to controle a boiler with a simple gui.

### Enable 1-wire Interface on pi to use DS18B20 temperature sensor
```
echo "dtoverlay=w1-gpio" >> /boot/config.txt
sudo reboot
```
### Apt install
```
sudo apt install flask
```

### Python requirments
```
sudo pip3 install -r requirements.txt
```

### Autorun flask server on startup
