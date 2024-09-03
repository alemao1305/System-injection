from frontend.display import Display
from backend.system_control import SystemControl
import time

def main():
    display = Display()
    system_control = SystemControl()

    try:
        while True:
            mode = system_control.check_buttons()
            if mode:
                display.show_message(f"Modo {mode.capitalize()} Ativo")
                system_control.update_leds(mode)
            
            time.sleep(0.1)

    except KeyboardInterrupt:
        system_control.cleanup()
        print("Sistema encerrado")

if __name__ == "__main__":
    main()
