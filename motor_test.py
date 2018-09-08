#this import is needed for the adafruit hat to operate
import Adafruit_PCA9685

#defines 'pwm'
pwm = Adafruit_PCA9685.PCA9685()
#sets the pwm frequency, 60hz is best for servos and motor controllers
pwm.set_pwm_freq(60)

#defines all of the motor ports on the Adafruit hat (port numbers can be seen on the hat itself)
motor_1 = 0 #port number '0'

#sets the pwm signal to the port number
pwm.set_pwm(motor_1, 0, 415) #parameters = (pwm pin number, not sure to be honest, pwm signal)
