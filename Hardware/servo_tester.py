import time
import RPi.GPIO as GPIO

SERVO_PIN = 18   # GPIO18 (physical pin 12)
FREQUENCY = 50   # Standard servo frequency: 50 Hz

def angle_to_duty_cycle(angle):
    # Convert angle (0–180) to duty cycle
    # 2.5% = 0°, 12.5% = 180°
    return 2.5 + (angle / 180.0) * 10

def main():
    print("[Servo Test] Setting up GPIO")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)

    pwm = GPIO.PWM(SERVO_PIN, FREQUENCY)
    pwm.start(0)

    try:
        # Sweep test
        for angle in [0, 45, 90, 135, 180, 90]:
            dc = angle_to_duty_cycle(angle)
            print(f"[Servo Test] Moving to {angle}° (DC={dc:.2f}%)")
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.7)

        print("[Servo Test] Holding center position")
        pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
        time.sleep(1)

    except KeyboardInterrupt:
        pass

    print("[Servo Test] Stopping servo")
    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
