import smbus2 as smbus
import time
import math

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

def main():
    try:
        mpu = MPU6050()
        print("MPU6050 sensor initialized")
        
        while True:
            data = mpu.get_data()
            print("\nAccelerometer data:")
            print(f"X: {data['accelerometer']['x']:.2f}g")
            print(f"Y: {data['accelerometer']['y']:.2f}g")
            print(f"Z: {data['accelerometer']['z']:.2f}g")
            
            print("\nGyroscope data:")
            print(f"X: {data['gyroscope']['x']:.2f}°/s")
            print(f"Y: {data['gyroscope']['y']:.2f}°/s")
            print(f"Z: {data['gyroscope']['z']:.2f}°/s")
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
