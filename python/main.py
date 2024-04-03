import librosa
import math
import numpy as np
from glob import glob

audio_files = glob('audio_files/*.wav')

pitch_mapping = {
          "C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4,
          "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8, "Ab": 8, "A": 9,
          "A#": 10, "Bb": 10, "B": 11
      }



def Test1(): #! CORRECT BUT ONLY NOTE, NO SCALE
  y, sr = librosa.load(audio_files[1])
  chroma = librosa.feature.chroma_stft(y=y, sr=sr)
  onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
  first = True 
  notes = []

  for onset in onset_frames:
    chroma_at_onset = chroma[:, onset]
    note_pitch = chroma_at_onset.argmax()
    if not first:
      note_duration = librosa.frames_to_time(onset, sr=sr)
      notes.append((note_pitch, onset, note_duration  - prev_note_duration))
    else:
      prev_note_duration = librosa.frames_to_time(onset, sr=sr)
      first = False
  print("note pitch \t Onset frame \t Note Duration \t\t Note")
  for entry in notes:
    print(f"{entry[0]} \t\t {entry[1]} \t\t {entry[2]} \t {next((key for key in pitch_mapping.keys() if pitch_mapping[key] == entry[0]), None )}")
    
    
def Test2(): #! MAYBE CORRECT, WITH SCALE
  y, sr = librosa.load(audio_files[1])
  stft = librosa.stft(y)
  onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
  first = True
  notes = []
  
  print(stft.shape)
  
  for onset in onset_frames:
    stft_at_onset = stft[:, onset]
    note = librosa.hz_to_note(440 * math.pow(2, (onset - 49)/12)) # stft_at_onset.argmax()* 43.06640625
    if not first:
      note_duration = librosa.frames_to_time(onset, sr=sr)
      notes.append((note, onset, note_duration  - prev_note_duration))
    else:
      prev_note_duration = librosa.frames_to_time(onset, sr=sr)
      first = False
  print("Note \t Onset frame \t Note Duration")
  for entry in notes:
    print(f"{entry[0]} \t\t {entry[1]} \t\t {entry[2]}")


def Test3(): #! WRONG
  y, sr = librosa.load(audio_files[1])
  chroma = librosa.feature.chroma_stft(y=y, sr=sr)
  onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
  first = True 
  notes = []

  for onset in onset_frames:
    chroma_at_onset = chroma[:, onset]
    note = librosa.hz_to_note(440 * math.pow(2, (chroma_at_onset.argmax() - 49)/12)) # stft_at_onset.argmax()* 43.06640625
    if not first:
      note_duration = librosa.frames_to_time(onset, sr=sr)
      notes.append((note, onset, note_duration  - prev_note_duration))
    else:
      prev_note_duration = librosa.frames_to_time(onset, sr=sr)
      first = False
  print("Note \t Onset frame \t Note Duration")
  for entry in notes:
    print(f"{entry[0]} \t\t {entry[1]} \t\t {entry[2]}")

 
Test1()
Test2()