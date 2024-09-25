import json
import re
from data import input_data

# Define your slot timings here
theory_slots = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'V1']
lab_slots = ['L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10', 'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20', 
             'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30', 'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 
             'L39+L40', 'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50', 'L51+L52', 'L53+L54', 'L55+L56', 
             'L57+L58', 'L59+L60']

def is_theory_slot(slot):
    return slot.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G'))

def is_lab_slot(slot):
    return slot.startswith('L')

def get_valid_slot_combinations(slots):
    valid_combinations = []
    
    # Check for pairs with theory slots and lab slots
    theory_slots_found = [slot for slot in slots if is_theory_slot(slot)]
    lab_slots_found = [slot for slot in slots if is_lab_slot(slot)]

    if theory_slots_found and lab_slots_found:
        # Generate all combinations of theory and lab slots
        for theory_slot in theory_slots_found:
            for lab_slot in lab_slots_found:
                valid_combinations.append((theory_slot, lab_slot))
    elif theory_slots_found:
        # If no lab slot is found, track theory slots without lab pairs
        for theory_slot in theory_slots_found:
            valid_combinations.append((theory_slot,))
    
    return valid_combinations

def get_faculty_course_valid_pairs(prof_course_slots):
    valid_pairs = {}
    
    for (prof, course), slots in prof_course_slots.items():
        valid_combinations = get_valid_slot_combinations(slots)
        
        # Extract Vn slots (V1, V2, etc.)
        v_slots = [slot for slot in slots if re.match(r'V[0-9]+', slot) or re.match(r'T[A-G][A-G][0-9]+', slot) or re.match(r'T[A-G][0-9]+', slot)]
        
        # Combine valid combinations with Vn slots
        final_combinations = []
        if v_slots:
            # Add Vn slots to each valid combination
            for combination in valid_combinations:
                final_combinations.append(combination + tuple(v_slots))
        else:
            final_combinations.extend(valid_combinations)
        
        valid_pairs[(prof, course)] = final_combinations
        
    return valid_pairs

data = json.loads(input_data)
prof_course_slots = {}

# Collecting slots for each (professor, course code) pair
for course in data['courses']:
    course_code = course['code']
    for slot_option in course['slots']:
        prof = slot_option['prof']
        slots = slot_option['slots'].split(',')
        if (prof, course_code) not in prof_course_slots:
            prof_course_slots[(prof, course_code)] = []
        prof_course_slots[(prof, course_code)].extend(slots)

valid_pairs = get_faculty_course_valid_pairs(prof_course_slots)

# Output the results
for (prof, course), pairs in valid_pairs.items():
    print(f"Professor: {prof}, Course: {course}")
    for pair in pairs:
        print(f"  Valid Pair: {', '.join(pair)}")
