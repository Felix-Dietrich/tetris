import pygame
import time
import numpy as np

# Initialisiere den Mixer von Pygame
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=512)


def make_tone(notes, times):

    sample_rate = 44100
    samples = np.zeros((sample_rate), dtype=np.int16)
    for index, frequency in enumerate(notes):
        duration = times[index]/2
        samples = np.concatenate((samples,((32767 * np.round(np.sin(2.0 * np.pi * frequency * np.arange(sample_rate * duration) / sample_rate))).astype(np.int16))),axis=0)
    return samples


# Die Tetris-Melodie (Korobeiniki) als Frequenzen (Hz) und Dauer (Sekunden)
# Notes for lead melody
lead_notes = [
    # part 1
    659.25, 493.88, 523.25, 587.33, 523.25, 493.88, 440.00, 440.00, 523.25, 659.25, 587.33, 523.25, 493.88, 493.88, 523.25, 587.33, 659.25, 523.25, 440.00, 440.00, 0,
    587.33, 698.46, 880.00, 783.99, 698.46, 659.25, 523.25, 659.25, 587.33, 523.25, 493.88, 493.88, 523.25, 587.33, 659.25, 523.25, 440.00, 440.00, 0,

    # part 2
    329.63, 261.63, 293.66, 246.94, 261.63, 220.00, 207.65, 246.94,
    329.63, 261.63, 293.66, 246.94, 261.63, 329.63, 440.00, 440.00, 415.30, 0
]

# Durations for lead melody
lead_times = [
    # part 1
    1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.5, 0.5, 1.0, 0.5, 0.5, 1.5, 0.5, 1.0, 0.5, 0.5, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,

    # part 2
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 3.0, 1.0
]

# Notes for bass
bass_notes = [
    # part 1
    82.41, 164.81, 82.41, 164.81, 82.41, 164.81, 82.41, 164.81, 55.00, 110.00, 55.00, 110.00, 55.00, 110.00, 55.00, 110.00,
    51.91, 103.83, 51.91, 103.83, 51.91, 103.83, 51.91, 103.83, 55.00, 110.00, 55.00, 110.00, 55.00, 123.47, 130.81, 164.81,
    73.42, 146.83, 73.42, 146.83, 73.42, 146.83, 73.42, 146.83, 65.41, 130.81, 65.41, 130.81, 65.41, 130.81, 65.41, 130.81,
    61.74, 123.47, 61.74, 123.47, 61.74, 123.47, 61.74, 123.47, 55.00, 110.00, 55.00, 110.00, 55.00, 110.00, 55.00, 110.00,

    # part 2
    55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41,
    55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41,
    55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41,
    55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 55.00, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41, 51.91, 82.41
]

# Durations for bass (all 0.5)
bass_times = [0.5] * len(bass_notes)


# Die Melodie abspielen
try:
    lead = make_tone(lead_notes,lead_times)
    bass = make_tone(bass_notes,bass_times)

    min_length = min(len(lead), len(bass))
    mixed_data = []
    chunk_size = int(44100/15)

    # Durch Iteration die Chunks abwechselnd hinzufügen
    for i in range(0, min_length, chunk_size):
        mixed_data.extend(lead[i:i+int(chunk_size/2)])  # Chunk von array1
        mixed_data.extend(bass[i+int(chunk_size/2):i+chunk_size])  # Chunk von array2


    pygame.sndarray.make_sound(np.array(mixed_data)).play()
    time.sleep(min_length/44100*2)
except KeyboardInterrupt:
    print("\nAbspielen unterbrochen.")
finally:
    pygame.mixer.quit()
