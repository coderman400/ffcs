import json
import itertools
import re
from data import *

# Define your slot timings here
theory_slots = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'V1']
lab_slots = ['L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10', 'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20', 'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30', 'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 'L39+L40', 'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50', 'L51+L52', 'L53+L54', 'L55+L56', 'L57+L58', 'L59+L60']

def is_theory_slot(slot):
    return slot.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G'))

def is_lab_slot(slot):
    return slot.startswith('L')

def get_valid_slot_combinations(slots):
    valid_combinations = []
    
    # Check for pairs with theory slots and lab slots
    for slot_combination in itertools.combinations(slots, 2):
        slot1, slot2 = slot_combination
        if is_theory_slot(slot1) and is_lab_slot(slot2):
            valid_combinations.append((slot1, slot2))
        elif is_theory_slot(slot2) and is_lab_slot(slot1):
            valid_combinations.append((slot2, slot1))
    
    return valid_combinations

def get_faculty_valid_pairs(prof_slots, course_code):
    valid_pairs = {}
    
    for prof, slots in prof_slots.items():
        valid_combinations = get_valid_slot_combinations(slots)
        
        # Extract Vn slots
        v_slots = [slot for slot in slots if re.match(r'V[0-9]+', slot) or re.match(r'T[A-G][A-G][0-9]+', slot) or re.match(r'T[A-G][0-9]+', slot)]
        
        # Combine valid combinations with Vn slots
        final_combinations = []
        if v_slots:
            # Add Vn slots to each valid combination
            for combination in valid_combinations:
                final_combinations.append(combination + tuple(v_slots))
        else:
            final_combinations.extend(valid_combinations)
        
        valid_pairs[(prof, course_code)] = final_combinations
        
    return valid_pairs




data = json.loads(input_data)
prof_slots = {}

for course in data['courses']:
    course_code = course['code']
    for slot_option in course['slots']:
        prof = slot_option['prof']
        slots = slot_option['slots'].split(',')
        if prof not in prof_slots:
            prof_slots[prof] = []
        prof_slots[prof].extend(slots)

    valid_pairs = get_faculty_valid_pairs(prof_slots, course_code)
    for (prof, course_code), pairs in valid_pairs.items():
        print(f"Professor: {prof}, Course: {course_code}")
        for pair in pairs:
            print(f"  Valid Pair: {', '.join(pair)}")
