# import the proper libraries
import pygame
import Adafruit_PCA9685

# setup the pi hat
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

# setup pygame to work with joystick
pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

# get the number of joysticks
joystick_count = pygame.joystick.get_count()

# if there is a joystick - initialize it
# if there isnt a joystick - close the program
if joystick_count != 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print "ERROR: There is no controller plugged in."
    pygame.quit()
    quit()

# program loop, this is what keeps the program running after every cycle
while True:
    # get every event in the events list
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            send('client terminate')
            pygame.quit()
            quit()

    # get the input types value
    x_axis = joystick.get_axis(0)

    # using abs() gets the absolute value of the number
    if abs(x_axis) > 0.1:
        # this axis is only printed if the value is between -0.1 and 0.1
        # this will filter out the resting position's inconsistencies
        print x_axis

    if abs(y_axis) > 0.1:
        print y_axis

    if a_button == 1:
        print 'button 0 down'

    if b_button == 1:
        print 'button 1 down'

    # compute the value to send to the motor
    motor_1 = 230*x_axis+390
    # 230 is the difference between the max and min of the motor controller divided by two (diff/2)
    # 390 is the average between the max and min of the motor controller

    # send the computed pwm value to the proper port on the hat
    pwm.set_pwm(motor_1, 0, 625)

    # time delay, limits the program to run 20 times per second
    clock.tick(20)
