from hub import port
import motor
import time

lmotor = port.B
rmotor = port.A

forward_speed = 300
backward_speed = -300


def left():
    motor.run(rmotor, forward_speed)
    motor.run(lmotor,forward_speed)
    
def right():
    motor.run(rmotor,backward_speed)
    motor.run(lmotor,backward_speed)
    
def forward():
    motor.run(rmotor,forward_speed)
    motor.run(lmotor,backward_speed)
    
def backward():
    motor.run(rmotor, backward_speed)
    motor.run(lmotor, forward_speed)
    
def stop():
    motor.stop(lmotor)
    motor.stop(rmotor)
    
def move(message):
    if (messgae == "l"):
        left()
    elif (message == "r"):
        right()
    elif (message == "f"):
        forward()
    elif (message == "b"):
        backward()
    else:
        stop()
forward()
time.sleep(2)
right()
time.sleep(2)
left()
time.sleep(2)
backward()
time.sleep(2)
stop()
    


