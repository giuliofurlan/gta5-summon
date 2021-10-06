# gta5-summon
control gta5 cars with the web

## requirements
* [vJoy](https://sourceforge.net/projects/vjoystick/)
* [x360ce](https://www.x360ce.com/files/x360ce_x64.zip)


## instructions
* install vJoy
* copy x360ce_x64.exe into gta5 installation folder and open it
* install the requirements with pip install -r requirements.txt 
* start server.py and open the game
* go to http://"your server ip":5000
  
##problems
* only one client can see the video feed for now
* hard to control
* x360ce gives errors, in that case just delete x360ce.ini and restart it
* server not reachable, change "app.run(host='127.0.0.1')" in server.py with your machine ip
 
## screenshots
![Screenshot](../master/screenshots/screen1.png)
