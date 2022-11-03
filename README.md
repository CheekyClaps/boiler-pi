# Boiler-PI

## Why?
I paid allot for a Ithodaalderop electric boiler becuase it came with a good energy saving label. In its lifetime I noticed that the energy saving was only due to it being able to differentiate night and day... so, that sucks.

The electronics broke and it did not switch on an off like it used to. meaning it needed a powerdown to activate the relais and did not remember settings. so instead of buing a new maing board i decided to make my own switching circuitry developed around a everyday raspberry-pi.

## Word of warining
I am an electricien. I verry well know what im doing wrong and am willing to take the risk. I know how these components will fail.
What scares me the most are the solid state relays, they can fail and keep the power switched on. What happens when the heater never stops heating?

## What is the project built around
Its a Raspberry pi running raspbian minimal with a Flask python webserver, SQLite3 DB and a bootstrap 5 frontend.
The RPI reads the boiler temperature via a B18D20 temperaturesensor and uses a bang-bang principle to drive 2 SSR's.

## The goal
The goal is to get a boiler that is per day per hour programmable and had a nice and simple visual interface.

## Which part of the software is mostlikely to fail?


## How to install
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
