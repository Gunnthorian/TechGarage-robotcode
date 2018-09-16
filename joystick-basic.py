import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.joystick.init()

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

    # number of inputs
    name = joystick.get_name()
    axes = joystick.get_numaxes()
    buttons = joystick.get_numbuttons()
    hats = joystick.get_numhats()

    # get the input types value
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)

    a_button = joystick.get_button(0)
    b_button = joystick.get_button(1)

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

    # time delay, limits the program to run 20 times per second
    clock.tick(20)
