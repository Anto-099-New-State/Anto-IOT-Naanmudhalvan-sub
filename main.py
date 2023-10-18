from machine import Pin, ADC
from time import sleep
import math

def setup_microphone(pin, attenuation=ADC.ATTN_11DB):
    mic = ADC(Pin(pin))
    mic.atten(attenuation)
    return mic

def measure_noise_level(mic, calibration_constant, noise_threshold):
    mic_level = mic.read()
    mic_level_db = 20 * math.log10(mic_level / calibration_constant)
    return mic_level_db

def main():
    mic_pin = 2
    calibration_constant = 2.0
    noise_threshold = 6000
    
    mic = setup_microphone(mic_pin)
    
    while True:
        mic_level_db = measure_noise_level(mic, calibration_constant, noise_threshold)
        
        if mic_level_db > noise_threshold:
            print("Warning: Noise pollution exceeds threshold!")
        
        print("dB: {:.2f}".format(mic_level_db))
        sleep(0.3)

if __name__ == "__main__":
    main()
