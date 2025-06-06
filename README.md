# IoT-Based-Dual-LED-Ultrasonic-Sensor-Web-Control-using-Raspberry-Pi
This project uses a Raspberry Pi to control two LEDs and monitor distance using an ultrasonic sensor, all via a Flask-based web interface. Users can turn LEDs on/off and view real-time distance measurements from anywhere using a Cloudflared tunnel, enabling remote access without port forwarding.
![Project Banner](https://via.placeholder.com/800x400?text=IoT+LED+and+Distance+Monitoring) <!-- Replace with actual image -->

A web-controlled IoT system for managing LEDs and monitoring distance using ultrasonic sensors, accessible locally or remotely via Cloudflare Tunnel.

## Features

- ✅ Real-time LED control (ON/OFF)
- 📏 Live ultrasonic distance monitoring
- 🌐 Web interface accessible from any device
- 🔒 Secure remote access via Cloudflare Tunnel
- 📱 Mobile-responsive design
- 📊 Automatic sensor data refresh

## Hardware Requirements

| Component | Quantity |
|-----------|----------|
| Raspberry Pi/ESP32 | 1 |
| HC-SR04 Ultrasonic Sensor | 1 |
| LEDs | 2 |
| 220Ω Resistors | 2 |
| Breadboard | 1 |
| Jumper Wires | As needed |

## Wiring Diagram

```plaintext
LED1 (GPIO21) ----[220Ω]---- GND
LED2 (GPIO20) ----[220Ω]---- GND
TRIG (GPIO19) ---- HC-SR04 Trig
ECHO (GPIO13) ---- HC-SR04 Echo
VCC (5V) -------- HC-SR04 VCC
GND ------------ HC-SR04 GND

# Clone repository
git clone https://github.com/yourusername/iot-led-distance-monitor.git
cd iot-led-distance-monitor

# Install dependencies
pip install flask RPi.GPIO

# Run the application
python app.py
