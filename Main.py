import serial
s_name = './ttyclient'
ser = serial.Serial(s_name)
ser.write(b"Your text")
while True:
    print(ser.readline())
print('sent')