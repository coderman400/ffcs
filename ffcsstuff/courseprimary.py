from itertools import product


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
import itertools

def generate_slot_combinations(course_data, max_courses=7):
    all_combinations = []
    course_keys = list(course_data.keys())
    
    # Generate slot choices for each course
    course_slots = []
    for course_key in course_keys:
        professors = course_data[course_key]['professors']
        course_slots.append([(course_key, professor, slot) for professor in professors for slot in professors[professor]])

    # Generate combinations of slots with at most `max_courses` courses
    for subset in itertools.combinations(range(len(course_slots)), max_courses):
        for combo in itertools.product(*(course_slots[i] for i in subset)):
            # Ensure no conflicting slots (e.g., same timing across different courses)
            slot_times = []
            valid = True
            for course, prof, slot in combo:
                slot_time = tuple(slot)  # Convert list to tuple to compare
                if slot_time in slot_times:
                    valid = False
                    break
                slot_times.append(slot_time)
            if valid:
                all_combinations.append(combo)

    return all_combinations


# Example usage with test data:
test_courses_data = {
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
    "CSI3003": {
        "title": "Artificial Intelligence and Expert Systems",
        "professors": {
            "Tamizharasi T": [
                ["G1+TG1"]
            ],
            "Jeevanantham A.K.": [
                ["G2+TG2"]
            ]
        }
    }
}


combinations = generate_slot_combinations(courses_data, max_courses=7)

# Print the output
for comb in combinations:
    print(comb)
