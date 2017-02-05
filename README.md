# Flask Relay - Raspberry pi GPIO relay interface with Flask
Flask Relay controls your 5V relays with your raspberry pi by just running a python command with some arguments. It uses Flask (flask.pocoo.org) which uses Werkzeug a Web Server Gateway Interface (WSGI). It also uses an HTML interface which displays fancy CSS buttons to control the relays so you can access and turn on and off anything you want trough any webbrowser you want.

Feel free to let me know if something isn't working as it should at bouwe.ceunen@gmail.com

### Get it running

```sh
$ python relay.py True
```

The first argument sets the inverse to True or False. So set this to True if your relays work with inverted logic and set to False if they don't.

Append further arguments so that the gpio pin is first and the name of the relay second.

[![](https://i.stack.imgur.com/sVvsB.jpg)](https://i.stack.imgur.com/sVvsB.jpg)

Make sure you use the port numbers defined as GPIO BOARD. So not the numbers on the side with the GPIO annotation but the single board numbers in the middle.

```sh
$ python relay.py True 22 Kitchen 
```

You can append as many parameters as you want for as many relays as you have.

```sh
$ python relay.py True 22 Kitchen 32 Livingroom 36 Garage
```

### Interface
Go to localhost:5000 (or ip address of your pi e.g. 192.168.1.115:5000) in your webbrowser (or change the Flask port in the python relay file) and try it out!

[![](http://www.bouweceunen.com/flaskrelay/interface.png)](http://www.bouweceunen.com/flaskrelay/interface.png)
