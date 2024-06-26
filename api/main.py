# import librosa
import json
import os

# import numpy as np
# import pandas as pd
# import IPython.display as ipd
from glob import glob
import music21 as m21
from music21 import converter
from pydub import AudioSegment
from muslib import TestGPT
# configure.run()

path = "xml/"

#!===GET AUDIO FILE===


def getAudioFile(name):
    audio_file = glob(name)
    print(name)
    return audio_file


#!===GET SHEET FILE===


def getSheetFile():
    sheet_file = glob("python/sheet_files/*.musicxml")
    return sheet_file


#!===CONVERT SHEET FILE===


def loadSheet(xml):
    # b.show('musicXML')
    if isinstance(xml, str):
        xml_data = converter.parse(xml)
    elif isinstance(xml, m21.stream.Score):
        xml_data = xml
    else:
        raise RuntimeError(
            "midi must be a path to a midi file or a music21.stream.Score"
        )

    score = []

    for part in xml_data.parts:
        instrument = part.getInstrument().instrumentName

        for note in part.flatten().notes:
            if note.isChord:
                start = note.offset
                duration = note.quarterLength
                isChord = True
                for chord_note in note.pitches:
                    pitch = chord_note.ps
                    volume = note.volume.realized
                    score.append([start, duration, pitch, volume, instrument, isChord])
            else:
                start = note.offset
                duration = note.quarterLength
                pitch = note.pitch.ps
                volume = note.volume.realized
                score.append([start, duration, pitch, volume, instrument])
    score = sorted(score, key=lambda x: (x[0], x[2]))
    return score


#!===LOAD AUDIO FILE===


def loadAudio(audio_file):
    notes = TestGPT(audio_file)
    return notes


#!===CHECK AUDIO FILE===


def checkAudioWithSheet(audio, sheet):
    j_sheet = json.loads(sheet)
    # print(j_sheet)
    #for note in audio:
        #if note[0] == int(j_sheet[0]["Pitch"]):
            #print("Note is correct")
        #else:
            #print("Note is incorrect")


#!---0
def createJsonFile(xml_list, name):
    result = []
    for xml in xml_list:
        note = {
            "Start": xml[0],
            "End": xml[1],
            "Pitch": xml[2],
            "Velocity": xml[3],
            "Instrument": xml[4],
            "IsChord": xml[5] if len(xml) == 6 else False,
        }
        result.append(note)
    formatted_json = json.dumps(result, indent=4)
    # print(formatted_json)
    real_name = name.split("\\")[1].split(".")[0]
    if not os.path.exists("json"):
        os.mkdir("json")
    with open(f"json/{real_name}.json", "w") as outfile:
        outfile.write(formatted_json)
    return formatted_json


#!===MAIN===


def main():
    # ? SELECT AUDIO
    audio_files = glob("audio/*.wav")
    print(audio_files)
    audio_selected = 0
    audio_selected = input(
        "Select an audio file to test and press Enter... (Default = 0):   "
    )  #! Select an audio file to test and press Enter...

    # ? SELECT SHEET
    xml_files = glob("xml/*")
    print(xml_files)
    xml = 0
    xml = input(
        "Select a sheet file to test and press Enter... (Default = 0):   "
    )  #! Select a sheet file to test and press Enter...

    audio_file = getAudioFile(audio_files[int(audio_selected)])
    # print(audio_file)
    xml_list = loadSheet(xml_files[int(xml)])
    # print(xml_list)
    if xml_list is not None and audio_file:
        print("Loading...")
        audio = loadAudio(audio_file[0])
        # print(audio)
        # print(xml_files[int(xml)])  #  xml_files[int(audio)]
        sheet = createJsonFile(xml_list, xml_files[int(xml)])
        print("JSON file created successfully!")
        checkAudioWithSheet(audio, sheet)
    else:
        print("No audio or sheet file found")


if not os.path.exists("xml"):
    os.mkdir("xml")
if not os.path.exists("audio"):
    os.mkdir("audio")

# audioName = "notec.wav"
# audioFolder = "audio/"
# audio = getAudioFile(audioFolder + audioName)
# print(audio)
main()
