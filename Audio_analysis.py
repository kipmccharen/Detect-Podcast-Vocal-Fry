import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from pydub import AudioSegment
import os


def all_mp3s_to_wav(dire):
    for filename in os.listdir(dire):
        flnm = filename.split(r".")
        flnm = ".".join(flnm[:-1])
        src = r"{}\{}".format(dire,filename)
        #print(r"{}\{}".format(dire,filename))
        #quit()
        sound = AudioSegment.from_mp3(src)
        sound.export(r"{}\{}.wav".format(dire,flnm), format="wav")

def print_wav_plot(wav_file, png_file):
    #label = wav_file.split(r"\\")[-1].split(".")[0]
    data, sr = librosa.load(wav_file)
    y_harm, y_perc = librosa.effects.hpss(data)
    plt.subplot(3, 1, 3)
    librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
    librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
    plt.title('Harmonic + Percussive')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':    
    folder = r"D:\Py_ML_CS\Podcast\This American Life\2020"
    file = r"D:\Py_ML_CS\Podcast\This American Life\2020\2020.03.15 696 Low Hum of Menace.wav"
    png_f = r"D:\Py_ML_CS\Podcast\This American Life\2020\example.png"
    #all_mp3s_to_wav(folder)
    print_wav_plot(file, png_f)
