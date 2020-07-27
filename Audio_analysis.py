import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from pydub import AudioSegment
import os
import soundfile as sf
import pylab

def print_wav_spectrogram(wav_file):
    save_path = wav_file.replace(".wav", '.png')
    data, sr = librosa.load(wav_file)
    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=data, sr=sr)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.savefig(save_path, bbox_inches=None, pad_inches=0)
    pylab.close()

def split_mp3_to_wavs(mp3path, howmany):
    AudioSegment.converter = r"D:\ffmpeg\bin\ffmpeg.exe"
    filepath = mp3path
    sound = AudioSegment.from_mp3(filepath)

    totalsize = len(sound)
    interval = int(totalsize / howmany)
    
    for x in range(howmany):
        instance = sound[(x*interval):((x+1)*interval)-1]
        newfilename = mp3path.replace(".mp3", f"_{x}.wav")
        instance.export(newfilename, format="wav")

if __name__ == '__main__':    
    thisdir = os.path.dirname(os.path.abspath(__file__)) + "\\"
    suffix = '.wav'
    filelist = [os.path.join(root,file) \
        for root, _, files in os.walk(thisdir) \
        for file in files if suffix in file]

    for file in filelist:
        print_wav_plot(file)
    #     split_mp3_to_wavs(file, 20)
    

