import wave
from scipy.io import wavfile
import numpy as np
import math
import os
import struct
import matplotlib.pyplot as plt


def note_detect(audio_file):
	file_length = audio_file.getnframes()
	f_s = audio_file.getframerate()  # sampling frequency
	sound = np.zeros(file_length)  # blank array
	print(f_s)
	for i in range(file_length):
			wdata = audio_file.readframes(1)
			# params = audio_file.getparams()
			data = struct.unpack("<i", wdata)
			sound[i] = int(data[0])
	sound = np.divide(sound, float(2**15))  # scaling it to 0 - 1
	counter = audio_file.getnchannels()  # number of channels mono/sterio
	fourier = np.fft.fft(sound)
	fourier = np.absolute(fourier)
	imax = np.argmax(fourier[0 : int(file_length / 2)])	# index of max element
	print(imax)
	print(counter)
    # plt.plot(fourier)
    # plt.show()


def noteToFreq(note):
    a = 440  # frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))


samplerate, data = wavfile.read("/audio/notec.wav")


def main():
    path = os.getcwd()
    full_path = path + "/audio/notec.wav"
    audio_file = wave.open(full_path, "r")
    Detected_Note = note_detect(audio_file)
    print(Detected_Note)
