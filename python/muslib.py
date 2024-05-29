import librosa
import math
import numpy as np
from glob import glob
from rich.console import Console
from rich.table import Table

# audio_files = glob("audio/*.wav")
# print(audio_files)
# file = 0
# file = input("Select an audio file to test and press Enter... (Default = 0):   ")  #! Select an audio file to test and press Enter...
# input("Press Enter to continue...")
pitch_mapping = {
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
}
pitch_mapping_it = {
    "Do": 0,
    "Do#": 1,
    "Reb": 1,
    "Re": 2,
    "Re#": 3,
    "Mib": 3,
    "Mi": 4,
    "Fa": 5,
    "Fa#": 6,
    "Solb": 6,
    "Sol": 7,
    "Sol#": 8,
    "Lab": 8,
    "La": 9,
    "La#": 10,
    "Sib": 10,
    "Si": 11,
}


def Test1(audio_file):  #! CORRECT BUT ONLY NOTE, NO SCALE
    y, sr = librosa.load(audio_file)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    first = True
    notes = []
    prev_note_duration = 0
    for onset in onset_frames:
        #print(onset)
        chroma_at_onset = chroma[:, onset]
        #print(chroma_at_onset)
        note_pitch = (
            chroma_at_onset.argmax()
        )  # ? .argmax() Returns the indices of the maximum values along an axis.
        if not first:
            note_duration = librosa.frames_to_time(onset, sr=sr)
            notes.append((note_pitch, onset, note_duration - prev_note_duration))
        else:
            prev_note_duration = librosa.frames_to_time(onset, sr=sr)
            first = False
    #TABLE CREATION
    print("Note \t Note Name It \t Onset frame \t Note Duration \t\t Note pitch")
    for entry in notes:
        print(
            f"{next((key for key in pitch_mapping.keys() if pitch_mapping[key] == entry[0]), None )} \t {next((key for key in pitch_mapping_it.keys() if pitch_mapping_it[key] == entry[0]), None )} \t\t {entry[1]} \t\t {entry[2]} \t {entry[0]}"
        )
    return notes
