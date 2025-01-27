import smbus2 as smbus
import time
import math
from flask import Flask, jsonify, send_from_directory
import threading

class MPU6050:
    def __init__(self):
        self.bus = smbus.SMBus(1)  # bus = 1 for Raspberry Pi revision 2
        self.device_address = 0x68  # MPU6050 device address
        
        # Wake up the MPU6050
        self.bus.write_byte_data(self.device_address, 0x6B, 0)
    
    def read_raw_data(self, addr):
        # Read raw 16-bit value
        high = self.bus.read_byte_data(self.device_address, addr)
        low = self.bus.read_byte_data(self.device_address, addr + 1)
        
        # Combine high and low for 16-bit value
        value = ((high << 8) | low)
        
        # Get signed value
        if value > 32768:
            value = value - 65536
        return value

    def get_data(self):
        # Read Accelerometer raw values
        acc_x = self.read_raw_data(0x3B)
        acc_y = self.read_raw_data(0x3D)
        acc_z = self.read_raw_data(0x3F)
        
        # Read Gyroscope raw values
        gyro_x = self.read_raw_data(0x43)
        gyro_y = self.read_raw_data(0x45)
        gyro_z = self.read_raw_data(0x47)
        
        # Full scale range +/- 250 degree/C as per sensitivity scale factor
        Ax = acc_x/16384.0
        Ay = acc_y/16384.0
        Az = acc_z/16384.0
        
        Gx = gyro_x/131.0
        Gy = gyro_y/131.0
        Gz = gyro_z/131.0
        
        return {
            'accelerometer': {'x': Ax, 'y': Ay, 'z': Az},
            'gyroscope': {'x': Gx, 'y': Gy, 'z': Gz}
        }

app = Flask(__name__, static_folder='static')

# Global variable to store latest sensor data
current_data = {
    'accelerometer': {'x': 0, 'y': 0, 'z': 0},
    'gyroscope': {'x': 0, 'y': 0, 'z': 0}
}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/data')
def get_sensor_data():
    return jsonify(current_data)

def sensor_loop():
    mpu = MPU6050()
    print("MPU6050 sensor initialized")
    
    while True:
        try:
            global current_data
            current_data = mpu.get_data()
            time.sleep(0.1)  # Update at 10Hz
        except Exception as e:
            print(f"Error reading sensor: {str(e)}")
            time.sleep(1)

def main():
    # Start sensor reading in a separate thread
    sensor_thread = threading.Thread(target=sensor_loop, daemon=True)
    sensor_thread.start()
    
    # Run Flask app
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()
