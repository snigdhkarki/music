import json
from music21 import *


def extract_musicxml_information(file_path):
    # Load the MusicXML file
    score = converter.parse(file_path)

    # Create a list to store the extracted information
    music_info_list = []

    # Iterate through each part in the score
    for part in score.parts:
        part_info = {
            'part_name': part.partName,
            'notes': []
        }

        # Iterate through each element in the part
        for element in part.flat.notesAndRests:
            if 'Chord' in element.classes:
                chord_data = []
                for note in element:
                    note_info = {
                    'note': note.pitch.name if note.pitch.name is not None else None,
                    'alter': int(note.pitch.alter) if note.pitch.alter is not None else None,
                    'type': note.duration.type if note.duration.type is not None else None,
                    'dot': note.duration.dots,
                    'octave': note.pitch.octave,}
                    chord_data.append(note_info)
                part_info['notes'].append(chord_data)
                                
            elif element.isNote:
                # Handle note
                note_info = {
                    'note': element.pitch.name if element.pitch.name is not None else None,
                    'alter': int(element.pitch.alter) if element.pitch.alter is not None else None,
                    'type': element.duration.type if element.duration.type is not None else None,
                    'dot': element.duration.dots,
                    'octave': element.pitch.octave,
                }
                part_info['notes'].append(note_info)
            else:                  
                rest_info = {
                    'note': 'rest',
                    'alter':0,
                    'type': element.duration.quarterLength,
                    'dot': element.duration.dots,
                    'octave':0,
                }
                part_info['notes'].append(rest_info)
                

        music_info_list.append(part_info)

    return music_info_list

# Example usage
musicxml_file = r'C:\Users\acer\opticalmusicrecognition\multipletest.musicxml'
result = extract_musicxml_information(musicxml_file)

# Specify the path where you want to save the JSON file
output_json_file = r'C:\Users\acer\opticalmusicrecognition\multipletest.json'

# Save the result to a JSON file
with open(output_json_file, 'w') as json_file:
    json.dump(result, json_file, default=str, indent=2)