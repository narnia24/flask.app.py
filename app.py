from flask import Flask, request
import serial
import time

# Set up Flask app
app = Flask(_name_)

# Set up Arduino serial connection (adjust COM port and baud rate as needed)
arduino = serial.Serial('COM3', 9600, timeout=1)  # COM port may differ on your system

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    prediction = data.get('prediction')

    if prediction == 1:
        # Send signal to Arduino to turn ON LED
        arduino.write(b'1')
        print("Human detected, LED turned ON")
    else:
        # Send signal to Arduino to turn OFF LED
        arduino.write(b'0')
        print("No human detected, LED turned OFF")

    return "Prediction received and sent to Arduino", 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask server
