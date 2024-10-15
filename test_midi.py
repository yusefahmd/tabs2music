# TODO: Replace the link below with my own google drive link so I know it won't go down randomly
# https://drive.google.com/file/d/0B4_6p-MMrzwLWGZnQkFVMk1xTG8/view?resourcekey=0-K4EK5n50DqnObCalwBjuqQ

from midiutil import MIDIFile
from midi2audio import FluidSynth

SOUNDFONT_PATH = "/Users/yahmed/Documents/Guitars-Universal-V1.5.sf2"
# SOUNDFONT_PATH = "/Users/yahmed/Documents/Guitars-Universal-V1.5.sf2"
MIDI_SAVE_PATH = "/Users/yahmed/Documents/tabs2music/major-scale.mid" # TODO: Need to remove this file when the whole process is run start to finish
# MIDI_SAVE_PATH = "/Users/yahmed/Documents/tabs2music/major-scale.mid"
WAV_SAVE_PATH = "/Users/yahmed/Documents/tabs2music/output.wav" # TODO: Make the name of the wav file the name of the code/tabs file
# WAV_SAVE_PATH = "/Users/yahmed/Documents/tabs2music/output.wav"


# Initialize the MIDI file variables; TODO: learn what these all do and what should be user input
degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0    # don't change
channel  = 0    # don't change
time     = 0    # In beats (dont change)
duration = 1    # In beats (cannot think of a way to include this unless I use ~ to elongate a note by a beat/tick, helps to enforce a format)
tempo    = 120   # In BPM TODO: make this user input, otherwise default to 120
volume   = 127  # 0-127, as per the MIDI standard (dont change, max volume)

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

########################################
fs = FluidSynth(SOUNDFONT_PATH)
# fs.play_midi(MIDI_SAVE_PATH)
fs.midi_to_audio(MIDI_SAVE_PATH, WAV_SAVE_PATH)