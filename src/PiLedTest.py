import time

import hal.hal_input_switch as switch
import PiDemo as pi

def main():
    switch.init()
    pi.led.init()
    while True:
        switch_status = switch.read_slide_switch()
        if switch_status == 1:
            # left
            pi.blink_led(0.1)
        else:
            # right
            for i in range(50): # 5/0.05/2
                pi.blink_led(0.05)
            pi.led.set_output(0,0)
            time.sleep(10)


if __name__ == "__main__":
    main()