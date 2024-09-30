import json
import re

theory_slots = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'V1']
lab_slots = ['L1+L2', 'L3+L4', 'L5+L6', 'L7+L8', 'L9+L10', 'L11+L12', 'L13+L14', 'L15+L16', 'L17+L18', 'L19+L20', 
             'L21+L22', 'L23+L24', 'L25+L26', 'L27+L28', 'L29+L30', 'L31+L32', 'L33+L34', 'L35+L36', 'L37+L38', 
             'L39+L40', 'L41+L42', 'L43+L44', 'L45+L46', 'L47+L48', 'L49+L50', 'L51+L52', 'L53+L54', 'L55+L56', 
             'L57+L58', 'L59+L60']


class Restructure:
    def __init__(self,data:dict[str,list]):
        self.data = data
        self.data = self.restructure()
    
    def is_theory_slot(self,slot):
        return slot.startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G'))


    def is_lab_slot(self,slot):
        return slot.startswith('L')


    def get_valid_slot_combinations(self,slots):
        valid_combinations = []

        theory_slots_found = [slot for slot in slots if self.is_theory_slot(slot)]
        lab_slots_found = [slot for slot in slots if self.is_lab_slot(slot)]

        if theory_slots_found and lab_slots_found:    
            for theory_slot in theory_slots_found:
                for lab_slot in lab_slots_found:
                    valid_combinations.append((theory_slot, lab_slot))
        elif theory_slots_found:
            for theory_slot in theory_slots_found:
                valid_combinations.append((theory_slot,))
        
        return valid_combinations


    def get_faculty_course_valid_pairs(self,prof_course_slots):
        valid_pairs = {}
        
        for (prof, course), slots in prof_course_slots.items():
            valid_combinations = self.get_valid_slot_combinations(slots)
            v_slots = [slot for slot in slots if re.match(r'V[0-9]+', slot) or re.match(r'T[A-G][A-G][0-9]+', slot) 
                    or re.match(r'T[A-G][0-9]+', slot)]
            
            final_combinations = []

            if v_slots:    
                for combination in valid_combinations:
                    final_combinations.append(combination + tuple(v_slots))
            else:
                final_combinations.extend(valid_combinations)
            
            valid_pairs[(prof, course)] = final_combinations
            
        return valid_pairs

    def restructure(self):
        data = self.data
        prof_course_slots = {}

        for course in data['courses']:
            course_code = course['code']
            for slot_option in course['slots']:
                prof = slot_option['prof']
                slots = slot_option['slots'].split(',')
                if (prof, course_code) not in prof_course_slots:
                    prof_course_slots[(prof, course_code)] = []
                prof_course_slots[(prof, course_code)].extend(slots)

        valid_pairs = self.get_faculty_course_valid_pairs(prof_course_slots)

        flatten = lambda l: [sublist for sublist in l]

        final = {}

        for (prof, course), pairs in valid_pairs.items():
            if course not in final:
                final[course] = {"professors": {}}
            final[course]["professors"][prof] = flatten(pairs)

        return final
