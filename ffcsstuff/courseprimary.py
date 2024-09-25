from itertools import product
from data import slot_timings


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

# Assuming this dict holds mapping of slots to their corresponding timings
slot_timings = {
    'A1': 'Monday 08:00-08:50',
    'B1': 'Monday 09:00-09:50',
    'C1': 'Monday 10:00-10:50',
    'D1': 'Monday 11:00-11:50',
    # Add more slots and timings here
}

# Sample data from your structure
course_slots = {
    "CSI3029": {
        "title": "Front End Design and Testing",
        "professors": {
            "Arulkumar V": [
                ["C1", "L15+L16"],
                ["C1", "L35+L36"]
            ],
            "Dhinakaran N": [
                ["C2", "L1+L2"]
            ]
        }
    },
    "CSI3025": {
        "title": "Application Development and Deployment Architecture",
        "professors": {
            "Sudhakar P": [
                ["B1", "L1+L2"],
                ["B1", "L55+L56"]
            ]
        }
    },
    # Add more courses and professors...
}

def get_slot_timing(slot):
    """Fetch the time range for a given slot."""
    return slot_timings.get(slot)

def has_time_conflict(selected_slots, new_slot):
    """Check for time conflict with the newly selected slot."""
    new_slot_time = get_slot_timing(new_slot)
    
    for slot in selected_slots:
        existing_slot_time = get_slot_timing(slot)
        
        # Check if time ranges overlap (this is simplified, actual time parsing required)
        if new_slot_time == existing_slot_time:
            return True
    return False

def generate_combinations(course_slots):
    all_combinations = []
    selected_slots = []
    
    def pick_slots(course_list, current_combination):
        if len(current_combination) == 7 or len(course_list) == 0:
            all_combinations.append(current_combination[:])
            return
        
        for course, details in course_list.items():
            for professor, slots in details['professors'].items():
                for slot in slots:
                    slot_id = slot[0]
                    if not has_time_conflict(selected_slots, slot_id):
                        selected_slots.append(slot_id)
                        current_combination.append((course, professor, slot_id))
                        
                        # Recurse with the rest of the courses
                        remaining_courses = {k: v for k, v in course_list.items() if k != course}
                        pick_slots(remaining_courses, current_combination)
                        
                        # Backtrack
                        current_combination.pop()
                        selected_slots.remove(slot_id)

    pick_slots(course_slots, [])
    return all_combinations

# Generate combinations
combinations = generate_combinations(course_slots)

# Output the combinations
for combo in combinations:
    print(combo)
