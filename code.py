cloudflared tunnel --url http://localhost:5000
from flask import Flask, redirect, url_for
import RPi.GPIO as GPIO
import socket
import time

app = Flask(__name__)

# LED GPIO setup
LED1_PIN = 21
LED2_PIN = 20

# Ultrasonic sensor pins
TRIG_PIN = 19
ECHO_PIN = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.output(LED1_PIN, GPIO.LOW)
GPIO.output(LED2_PIN, GPIO.LOW)

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def get_real_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def measure_distance():
    GPIO.output(TRIG_PIN, False)
    time.sleep(0.05)

    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    start_time = time.time()
    timeout = start_time + 0.04  # 40ms timeout

    while GPIO.input(ECHO_PIN) == 0 and time.time() < timeout:
        start_time = time.time()

    stop_time = time.time()
    timeout = stop_time + 0.04

    while GPIO.input(ECHO_PIN) == 1 and time.time() < timeout:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return round(distance, 2)

@app.route("/")
def index():
    led1_state = GPIO.input(LED1_PIN)
    led2_state = GPIO.input(LED2_PIN)
    led1_status = "ON" if led1_state else "OFF"
    led2_status = "ON" if led2_state else "OFF"
    real_ip = get_real_ip()

    return f"""
    <html>
    <head>
        <title>LED + Ultrasonic Sensor Control</title>
        <style>
            body {{
                background-color: #89CFF0;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
                color: Black;
            }}
            .info strong {{
                color: black;
            }}
            h1, h2 {{
                color: brown;
            }}
            button {{
                padding: 15px 30px;
                margin: 10px;
                font-size: 18px;
                background-color: #ffffff;
                color: #2196F3;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }}
            button:hover {{ background-color: #e0e0e0; }}
            button:disabled {{
                background-color: #e0e0e0;
                color: Black;
                cursor: default;
            }}
            .info {{ margin: 20px; font-size: 20px; }}
            .button-group {{
                display: flex;
                justify-content: center;
                gap: 10px;
                margin: 15px 0;
            }}
            footer {{
                position: fixed;
                bottom: 10px;
                width: 100%;
                text-align: center;
                font-size: 16px;
                color: black;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>G. PULLA REDDY ENGINEERING COLLEGE</h1>
        <h2>BATCH B6</h2>
        <div class="info">Server IP: <strong>{real_ip}:5000</strong></div>
        <div class="info">LED1 is currently: <strong>{led1_status}</strong></div>
        <div class="info">LED2 is currently: <strong>{led2_status}</strong></div>

        <div>
            <button id="distance-btn" disabled>Ultrasonic value: Loading...</button>
        </div>

        <div class="button-group">
            <form action="/on1" method="get"><button type="submit">LED1 ON</button></form>
            <form action="/off1" method="get"><button type="submit">LED1 OFF</button></form>
        </div>
        <div class="button-group">
            <form action="/on2" method="get"><button type="submit">LED2 ON</button></form>
            <form action="/off2" method="get"><button type="submit">LED2 OFF</button></form>
        </div>

        <footer>
            Team Members: Vardhan, Karthikeya, Rahul, Koushik, Sharan, Vamsi
        </footer>

        <script>
            function updateDistance() {{
                fetch("/distance")
                    .then(response => response.text())
                    .then(data => {{
                        document.getElementById("distance-btn").innerText = "Ultrasonic value: " + data + " cm";
                    }})
                    .catch(error => {{
                        document.getElementById("distance-btn").innerText = "Ultrasonic value: Error";
                    }});
            }}
            setInterval(updateDistance, 1000);
            updateDistance();
        </script>
    </body>
    </html>
    """

@app.route("/on1")
def led1_on():
    GPIO.output(LED1_PIN, GPIO.HIGH)
    return redirect(url_for('index'))

@app.route("/off1")
def led1_off():
    GPIO.output(LED1_PIN, GPIO.LOW)
    return redirect(url_for('index'))

@app.route("/on2")
def led2_on():
    GPIO.output(LED2_PIN, GPIO.HIGH)
    return redirect(url_for('index'))

@app.route("/off2")
def led2_off():
    GPIO.output(LED2_PIN, GPIO.LOW)
    return redirect(url_for('index'))

@app.route("/distance")
def get_distance():
    try:
        distance = measure_distance()
    except:
        distance = "Error"
    return str(distance)

if __name__ == "__main__":
    try:
        ip = get_real_ip()
        print(f"\nServer is running. Access it at: http://{ip}:5000/\n")
        app.run(host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup() 
