# import librosa
import json
import os
#import numpy as np
#import pandas as pd
#import IPython.display as ipd
from glob import glob
import music21 as m21
from music21 import converter

# configure.run()

path = "xml/"

#!===GET AUDIO FILE===


def getAudioFile():
    audio_file = glob("python/audio_files/*.wav")
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

                for chord_note in note.pitches:
                    pitch = chord_note.ps
                    volume = note.volume.realized
                    score.append([start, duration, pitch, volume, instrument])
            else:
                start = note.offset
                duration = note.quarterLength
                pitch = note.pitch.ps
                volume = note.volume.realized
                score.append([start, duration, pitch, volume, instrument])
    score = sorted(score, key=lambda x: (x[0], x[2]))
    return score


#!===CHECK AUDIO FILE===


def checkAudioWithSheet():
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
          "Instrument": xml[4],
      }
      result.append(note)
  formatted_json = json.dumps(result, indent=4)
  #print(formatted_json)
  if not os.path.exists("json"):
    os.mkdir("json")
  with open(f"json/{name.split('.')[0]}.json", "w") as outfile:
    outfile.write(formatted_json)

#!===MAIN===


def main(name):
    folder = "xml/"
    #audio = getAudioFile()
    xml_list = loadSheet(folder + name)
    #print(xml_list)
    if xml_list is not None:
        print("Sheet loaded")
        createJsonFile(xml_list, name)
        # checkAudioWithSheet()
    else:
        print("No audio or sheet file found")


if not os.path.exists("xml"):
    os.mkdir("xml")

main("Schubert.mxl")
