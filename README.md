# IoT-Based-Dual-LED-Ultrasonic-Sensor-Web-Control-using-Raspberry-Pi
This project uses a Raspberry Pi to control two LEDs and monitor distance using an ultrasonic sensor, all via a Flask-based web interface. Users can turn LEDs on/off and view real-time distance measurements from anywhere using a Cloudflared tunnel, enabling remote access without port forwarding.

---

## Features

- Turn LED1 and LED2 ON or OFF via web buttons.
- Real-time distance measurement using ultrasonic sensor.
- Displays server IP and LED statuses on the web page.
- Responsive and user-friendly web interface.
- Optional remote access using Cloudflared tunnel.

---

## Hardware Components

- Raspberry Pi (any model with GPIO pins)
- 2 LEDs connected to GPIO pins 21 and 20 (with current-limiting resistors)
- Ultrasonic sensor HC-SR04 connected to GPIO pins 19 (TRIG) and 13 (ECHO)
- Jumper wires and breadboard

---

## Software Requirements

- Python 3.x
- Flask (`pip install flask`)
- RPi.GPIO (`pip install RPi.GPIO`)
- Cloudflared (optional, for remote tunneling)

---

## Setup and Usage

### 1. Hardware Setup

- Connect the LEDs to GPIO pins 21 and 20 (include resistors).
- Connect the ultrasonic sensor's TRIG pin to GPIO 19 and ECHO pin to GPIO 13.

### 2. Install Dependencies

```bash
pip install flask RPi.GPIO
