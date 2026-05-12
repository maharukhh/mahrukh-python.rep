def move_forward():
    print("Robot: Moving Forward")

def turn_left():
    print("Robot: Turning Left")

def turn_right():
    print("Robot: Turning Right")

def stop():
    print("Robot: Stopped")


def control(left, middle, right):
    if middle == 1:
        move_forward()
    elif left == 1:
        turn_left()
    elif right == 1:
        turn_right()
    else:
        stop()

test_cases = [
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 1),
    (0, 0, 0),
]

for sensors in test_cases:
    print("\nSensor:", sensors)
    control(*sensors)