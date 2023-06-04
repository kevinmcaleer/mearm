from flask import Flask, request
from inventorhatmini import InventorHATMini, SERVO_1, SERVO_2, SERVO_3, SERVO_4
app = Flask(__name__)

# Create a new InventorHATMini and get a servo from it
board = InventorHATMini(init_leds=False)
s = board.servos[SERVO_1]

@app.route('/move_arm', methods=['POST'])
def move_arm():
    command = request.json['command']
    # send command to robot arm
    return 'Success!'

def send_command_to_arm(command):
    # This will depend on your robot arm's library
    # Here's a made-up example:

    # robot_arm.move_servo(command['servo'], command['position'])
    pass

if __name__ == '__main__':
    app.run(host='', port=5000, debug=True)
