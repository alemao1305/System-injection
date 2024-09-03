from gpiozero import Button, LED
from signal import pause
import time

class SystemControl:
    def __init__(self):
        # Configuração dos botões e LEDs usando gpiozero
        self.drive_button = Button(17, pull_up=True)
        self.sport_button = Button(27, pull_up=True)
        self.racing_button = Button(22, pull_up=True)
        self.off_button = Button(10, pull_up=True)

        self.drive_led = LED(5)
        self.sport_led = LED(6)
        self.racing_led = LED(13)

    def check_buttons(self):
        if self.drive_button.is_pressed:
            return "drive"
        elif self.sport_button.is_pressed:
            return "sport"
        elif self.racing_button.is_pressed:
            return "racing"
        elif self.off_button.is_pressed:
            return "off"
        return None

    def update_leds(self, mode):
        if mode == "drive":
            self.drive_led.on()
            self.sport_led.off()
            self.racing_led.off()
        elif mode == "sport":
            self.drive_led.off()
            self.sport_led.on()
            self.racing_led.off()
        elif mode == "racing":
            self.drive_led.off()
            self.sport_led.off()
            self.racing_led.on()
        elif mode == "off":
            self.drive_led.off()
            self.sport_led.off()
            self.racing_led.off()

    def cleanup(self):
        # Com gpiozero, a limpeza é automática, mas você pode definir aqui
        self.drive_led.off()
        self.sport_led.off()
        self.racing_led.off()

def main():
    system_control = SystemControl()

    try:
        while True:
            mode = system_control.check_buttons()
            if mode:
                print(f"Modo {mode.capitalize()} Ativo")
                system_control.update_leds(mode)
            time.sleep(0.1)
    except KeyboardInterrupt:
        system_control.cleanup()
        print("Sistema encerrado")

if __name__ == "__main__":
    main()
