import re
from pathlib import Path
from .tuning_to_midi_note import tuning_to_midi_note_mapping


# Reads the tabs file and for each guitar string, it extracts the tuning and their notes
# Has an optional riff_script parameter, don't mess with this as it is controlled via run in main
def read_tabs_file(tabs_path, for_riff_script=False):
    # The name of the tabs file is used as the song name
    song_name = extract_file_name(tabs_path)
    
    guitar_tunings = []
    guitar_strings = []
    riff_script_strings = []

    with open(tabs_path) as tabs:
        for string in tabs:
            if for_riff_script:
                tuning, notes, riff_script_notes = extract_string_notes(string, for_riff_script)
                riff_script_strings.append(riff_script_notes)
            else:
                tuning, notes, riff_script_strings = extract_string_notes(string)
            guitar_tunings.append(tuning)
            guitar_strings.append(notes)
    
    # If the call of read_tabs_file is meant for the esoteric language RiffScript, there needs to be an extra return variable
    if for_riff_script:
        return song_name, guitar_tunings, guitar_strings, riff_script_strings
    else:
        return song_name, guitar_tunings, guitar_strings


# TODO: explain
def tune_midi_notes(guitar_tunings, guitar_strings):
    midi_notes = []

    for tuning, notes in zip(guitar_tunings, guitar_strings):
        # The fret numbers in tabs don't mean anything to MIDI, so we have to convert them
        # The midi_number is the MIDI value of the open string, and we add to it the fret number
        midi_number = tuning_to_midi_note_mapping(tuning)
        for i, note in enumerate(notes):
            if type(note) == str:
                continue
            else:
                notes[i] = note + midi_number
        midi_notes.append(notes)

    return midi_notes


# Takes a string representing a single guitar string's notes, and returns the notes and the string's tuning
def extract_string_notes(input_string, for_riff_script=False):
    # This regex expression finds the tuning of the string
    tuning_pattern = r'^[a-zA-Z#b]+\d+'
    tuning = re.match(tuning_pattern, input_string).group(0)

    # This regex expressions validates the input format, so beginning with "$string tuning$ |" and ending with "|" with the notes in between
    format_pattern = r'^[a-zA-Z#b]+\d+ \|(.*)\|$'
    format_match = re.match(format_pattern, input_string)
    
    if not format_match:
        raise ValueError("Input string does not match the required format. It must begin with '$string letter$ |' and end with '|' with the notes in between.")

    # Extracts the string between the "$string tuning$ |" and "|"
    middle_part = format_match.group(1)


    notes = []
    i = 1  # Start from the second character (index 1), skips the first "-"
    while i < len(middle_part):
        # Check if it's a digit and capture the full number
        if middle_part[i].isdigit():
            num_str = middle_part[i]
            # Look ahead to capture the full number if it spans multiple characters
            while i + 1 < len(middle_part) and middle_part[i + 1].isdigit():
                i += 1
                num_str += middle_part[i]
            notes.append(int(num_str))  # Append the full number as an integer
        elif middle_part[i] in ["~", "-"]:
            notes.append(middle_part[i])  # Append "~", or "-"
        
        # Move to the next second character in the pair (skip the current '-')
        i += 2

    
    return tuning, notes, middle_part


# This function returns the name of a file (without the file extension), which is used as the song name
def extract_file_name(tabs_path):
    path = Path(tabs_path)
    file_name = path.stem
    return file_name