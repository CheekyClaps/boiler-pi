# Boiler-PI
### Raspberry-PI Python Flask Sqlite webserver
A flask server, a bang-bang controler with a simple gui.

### TODO's
- add bang bang
- checkout autorun
- tidy up frontend
- expand controle program (add hours,days,weeks,months)

### Enable 1-wire Interface on pi to use DS18B20 temperature sensor
```
echo "dtoverlay=w1-gpio" >> /boot/config.txt
sudo reboot
```
### Python requirments
```
sudo pip3 install -r requirements.txt
```

### Autorun flask server on startup
