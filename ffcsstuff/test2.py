from itertools import product
from data import slot_timings

# Sample data (replace this with your actual data)
courses_data = {
    "CSI3029": {
        "title": "Front End Design and Testing",
        "professors": {
            "Arulkumar V": [
                [
                    "C1",
                    "L15+L16"
                ],
                [
                    "C1",
                    "L35+L36"
                ],
                [
                    "C2",
                    "L15+L16"
                ],
                [
                    "C2",
                    "L35+L36"
                ]
            ],
            "Dhinakaran N": [
                [
                    "C2",
                    "L1+L2"
                ]
            ]
        }
    },
    "CSI3025": {
        "title": "Application Development and Deployment Architecture",
        "professors": {
            "Sudhakar P": [
                [
                    "B1",
                    "L1+L2"
                ],
                [
                    "B1",
                    "L55+L56"
                ],
                [
                    "B2",
                    "L1+L2"
                ],
                [
                    "B2",
                    "L55+L56"
                ]
            ]
        }
    },
    "CSI3003": {
        "title": "Artificial Intelligence and Expert Systems",
        "professors": {
            "Tamizharasi T": [
                [
                    "G1+TG1"
                ]
            ],
            "Madhan E S": [
                [
                    "G1+TG1"
                ]
            ],
            "Sathya K": [
                [
                    "G1+TG1"
                ]
            ],
            "Jeevanantham A.K.": [
                [
                    "G2+TG2"
                ]
            ],
            "Siva Sankari S": [
                [
                    "G2+TG2"
                ]
            ],
            "Yuvaraj N": [
                [
                    "G1+TG1"
                ]
            ],
            "Sivakumar V": [
                [
                    "G2+TG2"
                ]
            ],
            "Ganesh Shamrao Khekare": [
                [
                    "G2+TG2"
                ]
            ]
        }
    },
    "CSI3002": {
        "title": "Applied Cryptography and Network Security",
        "professors": {
            "Nivitha K": [
                [
                    "A1",
                    "L11+L12"
                ],
                [
                    "A1",
                    "L41+L42"
                ],
                [
                    "A2",
                    "L11+L12"
                ],
                [
                    "A2",
                    "L41+L42"
                ]
            ],
            "Thangaramya K": [
                [
                    "A1",
                    "L25+L26"
                ],
                [
                    "A1",
                    "L51+L52"
                ],
                [
                    "A2",
                    "L25+L26"
                ],
                [
                    "A2",
                    "L51+L52"
                ]
            ],
            "S M Farooq": [
                [
                    "A1",
                    "L7+L8"
                ],
                [
                    "A1",
                    "L51+L52"
                ],
                [
                    "A2",
                    "L7+L8"
                ],
                [
                    "A2",
                    "L51+L52"
                ]
            ],
            "Sunil Kumar": [
                [
                    "A1",
                    "L11+L12"
                ],
                [
                    "A1",
                    "L41+L42"
                ],
                [
                    "A2",
                    "L11+L12"
                ],
                [
                    "A2",
                    "L41+L42"
                ]
            ]
        }
    },
    "CSI3001": {
        "title": "Cloud Computing and methodologies",
        "professors": {
            "Dhivyaa CR": [
                [
                    "B1+TB1",
                    "L27+L28"
                ],
                [
                    "B1+TB1",
                    "L43+L44"
                ],
                [
                    "B2+TB2",
                    "L27+L28"
                ],
                [
                    "B2+TB2",
                    "L43+L44"
                ]
            ],
            "Muthunagai": [
                [
                    "B1+TB1",
                    "L13+L14"
                ],
                [
                    "B1+TB1",
                    "L43+L44"
                ],
                [
                    "B2+TB2",
                    "L13+L14"
                ],
                [
                    "B2+TB2",
                    "L43+L44"
                ]
            ],
            "Ranjithkumar S": [
                [
                    "B1+TB1",
                    "L27+L28"
                ],
                [
                    "B1+TB1",
                    "L53+L54"
                ],
                [
                    "B2+TB2",
                    "L27+L28"
                ],
                [
                    "B2+TB2",
                    "L53+L54"
                ]
            ],
            "Pushpa Gothwal": [
                [
                    "B1+TB1",
                    "L13+L14"
                ],
                [
                    "B1+TB1",
                    "L59+L60"
                ],
                [
                    "B2+TB2",
                    "L13+L14"
                ],
                [
                    "B2+TB2",
                    "L59+L60"
                ]
            ]
        }
    },
    "CSI3004": {
        "title": "Data Science Programming",
        "professors": {
            "Ganesh Shamrao Khekare": [
                [
                    "C1",
                    "L21+L22"
                ],
                [
                    "C1",
                    "L31+L32"
                ],
                [
                    "C2",
                    "L21+L22"
                ],
                [
                    "C2",
                    "L31+L32"
                ]
            ],
            "Meenakshi SP": [
                [
                    "C1",
                    "L21+L22"
                ],
                [
                    "C1",
                    "L31+L32"
                ],
                [
                    "C2",
                    "L21+L22"
                ],
                [
                    "C2",
                    "L31+L32"
                ]
            ]
        }
    },
    "CSI3021": {
        "title": "Advanced Computer Architecture",
        "professors": {
            "Thirunavukkarasan M": [
                [
                    "E1+TE1"
                ]
            ],
            "Sreethar S": [
                [
                    "E1+TE1"
                ]
            ],
            "Narmalli Jayakrishna": [
                [
                    "E1+TE1"
                ]
            ],
            "Suresh A": [
                [
                    "E1+TE1"
                ]
            ],
            "Krishnaraj N": [
                [
                    "E2+TE2"
                ]
            ],
            "Deepa D": [
                [
                    "E2+TE2"
                ]
            ],
            "Pushpa Gothwal": [
                [
                    "E2+TE2"
                ]
            ],
            "Latha Reddy N": [
                [
                    "E2+TE2"
                ]
            ]
        }
    },
    "JAP1001": {
        "title": "Japanese for Beginners",
        "professors": {
            "Khanjan": [
                [
                    "B1"
                ]
            ],
            "Hiya Mukherjee": [
                [
                    "C1"
                ]
            ]
        }
    },
    "MDI3004": {
        "title": "Intelligent Database Systems",
        "professors": {
            "Deepika J": [
                [
                    "G1+TG1"
                ]
            ],
            "Thangaramya K": [
                [
                    "G1+TG1"
                ]
            ],
            "Saurabh Agrawal": [
                [
                    "G2+TG2"
                ]
            ],
            "Jeevanajyothi Pujari": [
                [
                    "G2+TG2"
                ]
            ]
        }
    },
    "STS3021": {
        "title": "Getting Started to Skill Enhancemnets",
        "professors": {
            "Ethnus": [
                [
                    "D1+TD1"
                ],
                [
                    "D2+TD2"
                ]
            ],
            "Face": [
                [
                    "D1+TD1"
                ],
                [
                    "D2+TD2"
                ]
            ]
        }
    },
    "CSI4002": {
        "title": "Logic and Combanitorics for Computer Science",
        "professors": {
            "Bhawana Tyagi": [
                [
                    "F1+TF1"
                ]
            ],
            "Somasundaram SK": [
                [
                    "F1+TF1"
                ]
            ],
            "Uma Priya D": [
                [
                    "F1+TF1"
                ]
            ],
            "Rohini S": [
                [
                    "F1+TF1"
                ]
            ],
            "Nivethitha k": [
                [
                    "F2+TF2"
                ]
            ],
            "Dinesh R": [
                [
                    "F2+TF2"
                ]
            ],
            "Malini S": [
                [
                    "F2+TF2"
                ]
            ],
            "Pavithra M": [
                [
                    "F2+TF2"
                ]
            ]
        }
    }
}


from itertools import combinations

# Function to extract individual slot timings from composite slots
def get_individual_slot_timings(composite_slot, slot_timings):
    slots = composite_slot.split('+')
    timings = []
    for slot in slots:
        if slot in slot_timings:
            timings.extend(slot_timings[slot])
    return timings

# Function to check if two time slots conflict
def has_conflict(slot1_timings, slot2_timings):
    for day1, time1 in slot1_timings:
        for day2, time2 in slot2_timings:
            if day1 == day2:
                start1, end1 = map(lambda t: int(t.replace(':', '')), time1.split('-'))
                start2, end2 = map(lambda t: int(t.replace(':', '')), time2.split('-'))
                if max(start1, start2) < min(end1, end2):
                    return True
    return False

# Function to find valid non-conflicting combinations of slots
def find_valid_combinations(course_data, slot_timings, max_courses=7):
    all_combinations = []
    
    for num_courses in range(1, min(len(course_data), max_courses) + 1):
        for courses_subset in combinations(course_data.keys(), num_courses):
            valid_combos = []
            course_slots = []
            
            # Generate all slot options for the selected courses
            for course in courses_subset:
                for prof, slots in course_data[course]['professors'].items():
                    for slot1 in slots:
                        for slot in slot1:
                            if len(slot) >= 2:
                                composite_slot = slot[1]
                                if '+' in composite_slot:
                                    # Handle composite slots
                                    slot_timings_current = get_individual_slot_timings(composite_slot, slot_timings)
                                else:
                                    # Handle single slots
                                    slot_timings_current = slot_timings.get(composite_slot, [])
                                    
                                course_slots.append((course, prof, composite_slot, slot_timings_current))
                            else:
                                print(f"Unexpected slot format for course {course}, professor {prof}: {slot}")
            
            # Try combinations of the selected courses
            for combo in combinations(course_slots, len(courses_subset)):
                is_valid = True
                used_slots = []
                
                for course, prof, slot, slot_timings_current in combo:
                    # Check if this slot has a conflict with any previously selected slot
                    if any(has_conflict(slot_timings_current, slot_timings[used_slot])
                           for used_slot in used_slots):
                        is_valid = False
                        break
                    
                    used_slots.extend(slot_timings_current)
                
                if is_valid:
                    valid_combos.append(combo)
            
            all_combinations.extend(valid_combos)
    
    return all_combinations



# Find valid combinations with conflict checks
valid_combinations = find_valid_combinations(courses_data, slot_timings)

print(len(valid_combinations))
# Print the results
for combo in valid_combinations:
    print(combo)
