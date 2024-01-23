import json
import copy
def extract_notes_in_order(music_structure):
    notes_in_order = []

    for part_info in music_structure:
        for group_of_notes in part_info['notes']:
            if isinstance(group_of_notes, list):
                for note_info in group_of_notes:
                    note = note_info.get('note')
                    if note is not None:
                        notes_in_order.append(note)
            else:
                note = group_of_notes.get('note')
                if note is not None:
                    notes_in_order.append(note)
    return notes_in_order


json_file_path_original = r'C:\Users\acer\opticalmusicrecognition\multipletest.json'
json_file_path_duplicate = r'C:\Users\acer\opticalmusicrecognition\multipletest_duplicate.json'

with open(json_file_path_original, 'r') as file:
    music_structure1 = json.load(file)
with open(json_file_path_duplicate, 'r') as file:
    music_structure2 = json.load(file)

array1 = extract_notes_in_order(music_structure1)     #array with original notes
array2= extract_notes_in_order(music_structure2)
array1_copy = copy.deepcopy(music_structure1)

# array1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
# array2 = [0,1,4,5,6,7,8,9,22,11,96,13,14,15,18,19,20,21,22,23,24,25,26,27]

for i in range(len(array1)):
    array1[i] = [array1[i], i]

change_posi_list = []
skip_posi_list = []

while len(array1) != 5:    #last 5 always says correct
    if array1[0][0] == array2[0]:
        array1 = array1[1:]
        array2 = array2[1:]
    else:
        flag = False        
        if array1[1][0] == array2[0] and array1[2][0] == array2[1] and array1[3][0] == array2[2] and array1[4][0] == array2[3] and array1[5][0] == array2[4]:
            skip_posi_list.append(array1[0][1])
            array1 = array1[1:]
        elif array1[2][0] == array2[0] and array1[3][0] == array2[1] and array1[4][0] == array2[2] and array1[5][0] == array2[3] and array1[6][0] == array2[4]:
            skip_posi_list.append(array1[0][1])
            skip_posi_list.append(array1[1][1])
            array1 = array1[2:]
        elif array1[3][0] == array2[0] and array1[4][0] == array2[1] and array1[5][0] == array2[2] and array1[6][0] == array2[3] and array1[7][0] == array2[4]:
            skip_posi_list.append(array1[0][1])
            skip_posi_list.append(array1[1][1])
            skip_posi_list.append(array1[2][1])
            array1 = array1[3:]    
        elif array1[4][0] == array2[0] and array1[5][0] == array2[1] and array1[6][0] == array2[2] and array1[7][0] == array2[3] and array1[8][0] == array2[4]:
            skip_posi_list.append(array1[0][1])
            skip_posi_list.append(array1[1][1])
            skip_posi_list.append(array1[2][1])
            skip_posi_list.append(array1[3][1])
            array1 = array1[4:]
        elif array1[5][0] == array2[0] and array1[6][0] == array2[1] and array1[7][0] == array2[2] and array1[8][0] == array2[3] and array1[9][0] == array2[4]:
            skip_posi_list.append(array1[0][1])
            skip_posi_list.append(array1[1][1])
            skip_posi_list.append(array1[2][1])
            skip_posi_list.append(array1[3][1])
            skip_posi_list.append(array1[4][1])
            array1 = array1[5:]
        else:
            change_posi_list.append(array1[0][1])
            array1 = array1[1:]
            array2 = array2[1:]



print(skip_posi_list)
print(change_posi_list)

i = 0
for part_info in array1_copy:
    for group_of_notes in part_info['notes']:
        if isinstance(group_of_notes, list):
            for note_info in group_of_notes:
                note = note_info.get('note')
                if note is not None:
                    if i in skip_posi_list:
                        note_info['skiped'] = True
                    else:
                        note_info['skiped'] = False
                    if i in change_posi_list:
                        note_info['changed'] = True
                    else:
                        note_info['changed'] = False
                    i = i+1                   
        else:
            note = group_of_notes.get('note')
            if note is not None:
                if i in skip_posi_list:
                    group_of_notes['skiped'] = True
                else:
                    group_of_notes['skiped'] = False
                if i in change_posi_list:
                    group_of_notes['changed'] = True
                else:
                    group_of_notes['changed'] = False 
                i = i+1  
                





output_json_file = r'C:\Users\acer\opticalmusicrecognition\multipletestoutput.json'
with open(output_json_file, 'w') as json_file:
    json.dump(array1_copy, json_file, default=str, indent=2)
    




