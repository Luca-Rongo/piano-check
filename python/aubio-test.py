import aubio
total_read = 0
with aubio.source('audio_files/notec.wav') as src:
    for frames in src:
        note = aubio.notes()
        print(note)