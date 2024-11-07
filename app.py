
from flask import Flask, render_template, Response import cv2

app = Flask(name)

def generate_frames(): camera = cv2.VideoCapture(0) while True: success, frame = camera.read() if not success: break else: ret, buffer = cv2.imencode('.jpg', frame) frame = buffer.tobytes() yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/') def index(): return render_template('index.html')

@app.route('/viewer1') def viewer1(): return render_template('viewer1.html')

@app.route('/viewer2') def viewer2(): return render_template('viewer2.html')

@app.route('/video_feed') def video_feed(): return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if name == 'main': app.run(debug=True)