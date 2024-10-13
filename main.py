from midiutil import MIDIFile


# Reads the text file and parses the tabs into an array of six strings to be used with midi
def read_tabs_file(filepath):
    with open(filepath) as f:
        # All but the last line ends with a "\n", so remove them to be formatted
        lines = [line.rstrip('\n') for line in f]
        
        # Check if all lines are formatted properly
        for line in lines:
            if line[2] != "|" or line[-1] != "|":
                print("""Format error: every line needs to match the following pattern
                    *string letter* |-*fret numbers*-|""")
                return
    
    # If there are multiple mentions of a string, append them all in the right order in one string
    # Before doing any appending, make sure each block has the right format (make the check above into a function)
            
    return lines


def main(filepath, tempo):
    # Get the notes from the file
    lines = read_tabs_file(filepath)

    # Initialize the MIDIFile object (with 1 track)
    guitar_degrees = list(reversed([52, 57, 62, 67, 71, 76]))
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1    # In beats
    tempo    = tempo   # In BPM
    volume   = 100  # 0-127, as per the MIDI standard
    song = MIDIFile(1)
    song.addTempo(track, time, tempo)


if __name__ == "__main__":
    filepath = "test.txt" # Replace this with an input method, or something similar (maybe default to test.txt)
    tempo = 60 # Find a better way to get this value (either input or stored in the .txt file)
    main(filepath, tempo)