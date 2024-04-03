import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd
from itertools import cycle

sns.set_theme(style="white",palette=None)
color_pal = plt.rcParams['axes.prop_cycle'].by_key()['color']
color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

audio_files = glob('audio_files/*.wav')


y, sr = librosa.load(audio_files[0]) #read audio file

print(f"y: {y[:10]}")
print(f"shape: {y.shape}")
print(f"sr: {sr}")

pd.Series(y).plot(figsize=(10, 5), lw=1, title='raw audio trimmed signal')
y_trimmed, _  = librosa.effects.trim(y, top_db=20);
pd.Series(y_trimmed).plot(figsize=(10, 5), lw=1, title='raw audio trimmed signal')

D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
fig, ax  = plt.subplots(figsize=(10, 5))
img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
ax.set_title('Spectrogram')
fig.colorbar(img, ax=ax, format=f"%0.2f")  

S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
S_db_mel = librosa.amplitude_to_db(S, ref=np.max)
fig, ax  = plt.subplots(figsize=(15, 5))
img = librosa.display.specshow(S_db_mel, x_axis='time', y_axis='log', ax=ax)
ax.set_title('Spectrogram')
fig.colorbar(img, ax=ax, format=f"%0.2f")  
plt.show()