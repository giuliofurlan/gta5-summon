from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
import os
import pyvjoy
import time
import cv2 as cv
from windowcapture import WindowCapture

j = pyvjoy.VJoyDevice(1)
MAX_VJOY = 32767
MIN_VJOY = -32767
os.chdir(os.path.dirname(os.path.abspath(__file__)))
wincap = WindowCapture('Grand Theft Auto V')


def increase_throttle():
    n = j.data.wAxisZRot
    print(n)
    j.data.wAxisZRot = n+1
    j.update()

def decreare_throttle():
    n = j.data.wAxisZRot
    print(n)
    j.data.wAxisZRot = n-1
    j.update()

def throttle(speed = int(MAX_VJOY/2)): #speed range 0 - 32767
    j.data.wAxisZRot = speed
    j.update()

def steer(r):
    j.data.wAxisX =r
    j.update()

def brake(n):
    j.data.wAxisZ = n
    j.update()

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        return render_template('index.html')


    @app.route('/steer', methods = ['POST'])
    def get_post_javascript_data():
        jsdata = request.form['javascript_data']
        print(jsdata)
        steer(int(jsdata))
        return jsdata

    @app.route('/throttle', methods = ['POST'])
    def go():
        jsdata = request.form['javascript_data']
        print(jsdata)
        throttle(int(jsdata))
        return "going"

    @app.route('/brake', methods = ['POST'])
    def not_go():
        jsdata = request.form['javascript_data']
        print(jsdata)
        brake(int(jsdata))
        return "stopping"

    
    

    @app.route('/video_feed')
    def video_feed():
        return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

    def gen_frames():  
        while True:
            frame = wincap.get_screenshot()
            success = True
            if not success:
                break
            else:
                ret, buffer = cv.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result




    app.run(host='127.0.0.1')
    #runs after server killed



