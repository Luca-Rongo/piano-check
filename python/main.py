# import librosa
import json
import os

# import numpy as np
# import pandas as pd
# import IPython.display as ipd
from glob import glob
import music21 as m21
from music21 import converter

# configure.run()

path = "xml/"

#!===GET AUDIO FILE===


def getAudioFile(name):
    audio_file = glob(name)
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
    return 0


#!===CHECK AUDIO FILE===


def checkAudioWithSheet(audio, sheet):
    return True


#!---
def createJsonFile(xml_list, name):
    result = []
    for xml in xml_list:
        note = {
            "Start": xml[0],
            "End": xml[1],
            "Pitch": xml[2],
            "Velocity": xml[3],
            "Instrument":xml[4],
            "IsChord":  xml[5] if len(xml) == 6 else False,
        }
        result.append(note)
    formatted_json = json.dumps(result, indent=4)
    #print(formatted_json)
    if not os.path.exists("json"):
        os.mkdir("json")
    with open(f"json/{name.split('.')[0]}.json", "w") as outfile:
        outfile.write(formatted_json)
    return formatted_json


#!===MAIN===


def main(scoreName, audioName):
    scoreFolder = "xml/"
    audioFolder = "audio/"
    audio_file = getAudioFile(audioFolder + audioName)
    print(audio_file)

    xml_list = loadSheet(scoreFolder + scoreName)
    # print(xml_list)
    if xml_list is not None and audio_file:
        print("Loading...")
        audio = loadAudio(audio_file[0])
        sheet = createJsonFile(xml_list, scoreName)
        #print(sheet)
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
main("C.mxl", "notec.wav")
