# Raspberry pi GPIO relay interface with Flask

Feel free to let me know if something isn't working as it should at bouwe.ceunen@gmail.com

### Get it running

```sh
$ python relay.py
```
This will display an empty screen, arguments are needed.
Append the arguments so that the gpio pin is first and the name of the relay second.


[![](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)

Make sure you use the port numbers dislayed with the 'GPIO' annotation (GPIO BCM). So not the board numbers in the middle.

```sh
$ python relay.py 22 Kitchen 
```
You can append as many parameters as you want for as many relays as you have.

```sh
$ python relay.py 22 Kitchen 04 Livingroom 27 Garage
```

#### Interface
Go to localhost:5000 (or ip address of your pi e.g. 192.168.1.115:5000) in your webbrowser (or change the Flask port in the python relay file) and try it out!

[![](http://www.bouweceunen.com/flaskrelay/interface.png)](http://www.bouweceunen.com/flaskrelay/interface.png)
