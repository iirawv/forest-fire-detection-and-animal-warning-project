import tkinter as tk
from PIL import Image, ImageTk
import sounddevice as sd
import numpy as np
import random

class FireAnimalWarningSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fire and Animal Warning System")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")  # Set background color

        # Load and display a smaller logo
        self.logo_image = Image.open("Lorem_ipsum_dolor_sit_amet__consectetur_adipiscing_elit._Etiam_id_urna_sed_dui_lacinia_molestie_in_ac_est.-removebg-preview (1).png")  # Replace "logo.png" with your logo file path
        self.logo_image = self.logo_image.resize((250, 250), Image.ANTIALIAS)  # Resize the logo
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(root, image=self.logo_photo, bg="#f0f0f0")  # Set background color of the label
        self.logo_label.pack(pady=10)

        self.title_label = tk.Label(root, text="Forest Fire and Animal Warning System", font=("Arial", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.bird_button = tk.Button(root, text="Warn Birds", command=self.warn_birds, width=20, height=2)
        self.bird_button.pack(pady=10)

        self.mammal_button = tk.Button(root, text="Warn Mammals", command=self.warn_mammals, width=20, height=2)
        self.mammal_button.pack(pady=10)



        self.warning_system = AnimalWarningSystem()

    def warn_birds(self):
        self.warning_system.warn_birds()

    def warn_mammals(self):
        self.warning_system.warn_mammals()

    def detect_fire(self):
        # Simulate gathering temperature data over a period of time (e.g., 10 seconds)
        temperatures = [random.uniform(60, 80) for _ in range(10)]  # Generate 10 random temperatures
        max_temperature = max(temperatures)
        print(f"Maximum Temperature Detected: {max_temperature}°C")

        fire_threshold = 70  # Simulated fire detection threshold (temperature in Celsius)
        if max_temperature > fire_threshold:
            print("Fire Detected!")
            self.warning_system.play_frequency(8000)  # Play a higher frequency for fire warning

class AnimalWarningSystem:
    def __init__(self):
        self.bird_frequency = 5000  # Example frequency for birds (5 kHz)
        self.mammal_frequency = 2000  # Example frequency for mammals (2 kHz)

    def warn_birds(self):
        print("Warning birds!")
        self.play_frequency(self.bird_frequency)

    def warn_mammals(self):
        print("Warning mammals!")
        self.play_frequency(self.mammal_frequency)

    def play_frequency(self, frequency):
        duration = 3  # Duration of the warning sound in seconds
        sample_rate = 44100  # Standard sample rate for audio
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        audio_signal = 0.5 * np.sin(2 * np.pi * frequency * t)
        sd.play(audio_signal, sample_rate)
        sd.wait()

if __name__ == "__main__":
    root = tk.Tk()
    app = FireAnimalWarningSystemGUI(root)
    root.mainloop()
