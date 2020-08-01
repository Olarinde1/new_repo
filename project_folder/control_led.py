import serial
ser = serial.Serial('COM8', 9600)

def control(command):
    if 'on' in command:
        ser.write(b'Y')
    if 'off' in command:
        ser.write(b'N')


while True:
    command = input('Enter on to turn on the bulb and enter off to turn off the bulb')
    control(command)
    if command == 'quit':
        quit()