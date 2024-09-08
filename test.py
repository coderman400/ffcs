from itertools import product
# Define your input data
courses_slots = {
    "CSI3029": {
        "title": "Front End Design and Testing",
        "professors": {
            "Arulkumar V": [
                ["C1", "L15+L16"],
                ["C1", "L35+L36"],
                ["C2", "L15+L16"],
                ["C2", "L35+L36"]
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
                ["B1", "L55+L56"],
                ["B2", "L1+L2"],
                ["B2", "L55+L56"]
            ]
        }
    },
    "CSI3003": {
        "title": "Artificial Intelligence and Expert Systems",
        "professors": {
            "Tamizharasi T": [["G1+TG1"]],
            "Madhan E S": [["G1+TG1"]],
            "Sathya K": [["G1+TG1"]],
            "Jeevanantham A.K.": [["G2+TG2"]],
            "Siva Sankari S": [["G2+TG2"]],
            "Yuvaraj N": [["G1+TG1"]],
            "Sivakumar V": [["G2+TG2"]],
            "Ganesh Shamrao Khekare": [["G2+TG2"]]
        }
    },
    "CSI3002": {
        "title": "Applied Cryptography and Network Security",
        "professors": {
            "Nivitha K": [
                ["A1", "L11+L12"],
                ["A1", "L41+L42"],
                ["A2", "L11+L12"],
                ["A2", "L41+L42"]
            ],
            "Thangaramya K": [
                ["A1", "L25+L26"],
                ["A1", "L51+L52"],
                ["A2", "L25+L26"],
                ["A2", "L51+L52"]
            ],
            "S M Farooq": [
                ["A1", "L7+L8"],
                ["A1", "L51+L52"],
                ["A2", "L7+L8"],
                ["A2", "L51+L52"]
            ],
            "Sunil Kumar": [
                ["A1", "L11+L12"],
                ["A1", "L41+L42"],
                ["A2", "L11+L12"],
                ["A2", "L41+L42"]
            ]
        }
    },
    "CSI3001": {
        "title": "Cloud Computing and methodologies",
        "professors": {
            "Dhivyaa CR": [
                ["B1+TB1", "L27+L28"],
                ["B1+TB1", "L43+L44"],
                ["B2+TB2", "L27+L28"],
                ["B2+TB2", "L43+L44"]
            ],
            "Muthunagai": [
                ["B1+TB1", "L13+L14"],
                ["B1+TB1", "L43+L44"],
                ["B2+TB2", "L13+L14"],
                ["B2+TB2", "L43+L44"]
            ],
            "Ranjithkumar S": [
                ["B1+TB1", "L27+L28"],
                ["B1+TB1", "L53+L54"],
                ["B2+TB2", "L27+L28"],
                ["B2+TB2", "L53+L54"]
            ],
            "Pushpa Gothwal": [
                ["B1+TB1", "L13+L14"],
                ["B1+TB1", "L59+L60"],
                ["B2+TB2", "L13+L14"],
                ["B2+TB2", "L59+L60"]
            ]
        }
    },
    "CSI3004": {
        "title": "Data Science Programming",
        "professors": {
            "Ganesh Shamrao Khekare": [
                ["C1", "L21+L22"],
                ["C1", "L31+L32"],
                ["C2", "L21+L22"],
                ["C2", "L31+L32"]
            ],
            "Meenakshi SP": [
                ["C1", "L21+L22"],
                ["C1", "L31+L32"],
                ["C2", "L21+L22"],
                ["C2", "L31+L32"]
            ]
        }
    },
    "CSI3021": {
        "title": "Advanced Computer Architecture",
        "professors": {
            "Thirunavukkarasan M": [["E1+TE1"]],
            "Sreethar S": [["E1+TE1"]],
            "Narmalli Jayakrishna": [["E1+TE1"]],
            "Suresh A": [["E1+TE1"]],
            "Krishnaraj N": [["E2+TE2"]],
            "Deepa D": [["E2+TE2"]],
            "Pushpa Gothwal": [["E2+TE2"]],
            "Latha Reddy N": [["E2+TE2"]]
        }
    },
    "JAP1001": {
        "title": "Japanese for Beginners",
        "professors": {
            "Khanjan": [["B1"]],
            "Hiya Mukherjee": [["C1"]]
        }
    },
    "MDI3004": {
        "title": "Intelligent Database Systems",
        "professors": {
            "Deepika J": [["G1+TG1"]],
            "Thangaramya K": [["G1+TG1"]],
            "Saurabh Agrawal": [["G2+TG2"]],
            "Jeevanajyothi Pujari": [["G2+TG2"]]
        }
    },
    "STS3021": {
        "title": "Getting Started to Skill Enhancemnets",
        "professors": {
            "Ethnus": [
                ["D1+TD1"],
                ["D2+TD2"]
            ],
            "Face": [
                ["D1+TD1"],
                ["D2+TD2"]
            ]
        }
    },
    "CSI4002": {
        "title": "Logic and Combinatorics for Computer Science",
        "professors": {
            "Bhawana Tyagi": [["F1+TF1"]],
            "Somasundaram SK": [["F1+TF1"]],
            "Uma Priya D": [["F1+TF1"]],
            "Rohini S": [["F1+TF1"]],
            "Nivethitha K": [["F2+TF2"]],
            "Dinesh R": [["F2+TF2"]],
            "Malini S": [["F2+TF2"]],
            "Pavithra M": [["F2+TF2"]]
        }
    }
}

slot_timings = {
    "A1": [("Monday", "0800-0850"), ("Wednesday", "0900-0950")],
    "TA1": [("Friday", "1000-1050")],
    "TAA1": [("Tuesday", "1200-1250")],
    "B1": [("Tuesday", "0800-0850"), ("Thursday", "0900-0950")],
    "TB1": [("Monday", "1100-1150")],
    "C1": [("Wednesday", "0800-0850"), ("Friday", "0900-0950")],
    "TC1": [("Tuesday", "1100-1150")],
    "TCC1": [("Thursday", "1200-1250")],
    "D1": [("Thursday", "0800-0850"), ("Monday", "1000-1050")],
    "TD1": [("Friday", "1200-1250")],
    "E1": [("Friday", "0800-0850"), ("Tuesday", "1000-1050")],
    "TE1": [("Thursday", "1100-1150")],
    "F1": [("Monday", "0900-0950"), ("Wednesday", "1000-1050")],
    "TF1": [("Friday", "1100-1150")],
    "G1": [("Tuesday", "0900-0950"), ("Thursday", "1000-1050")],
    "TG1": [("Monday", "1200-1250")],
    "A2": [("Monday", "1400-1450"), ("Wednesday", "1500-1550")],
    "F2": [("Monday", "1500-1550"), ("Wednesday", "1600-1650")],
    "D2": [("Monday", "1600-1650"), ("Thursday", "1400-1450")],
    "TB2": [("Monday", "1700-1750")],
    "TG2": [("Monday", "1800-1850")],
    "B2": [("Tuesday", "1400-1450"), ("Thursday", "1500-1550")],
    "G2": [("Tuesday", "1500-1550"), ("Thursday", "1600-1650")],
    "E2": [("Tuesday", "1600-1650"), ("Friday", "1400-1450")],
    "TC2": [("Tuesday", "1700-1750")],
    "TAA2": [("Tuesday", "1800-1850")],
    "C2": [("Wednesday", "1400-1450"), ("Friday", "1500-1550")],
    "TD2": [("Wednesday", "1700-1750")],
    "TBB2": [("Wednesday", "1800-1850")],
    "TE2": [("Thursday", "1700-1750")],
    "TCC2": [("Thursday", "1800-1850")]
}



# Convert time to minutes
def convert_time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def get_slot_time_range(slot):
    if slot not in slot_timings:
        return None
    times = slot_timings[slot]
    return [(convert_time_to_minutes(start_time), convert_time_to_minutes(end_time)) for _, (start_time, end_time) in times]

def time_conflict(slot1, slot2):
    times1 = get_slot_time_range(slot1)
    times2 = get_slot_time_range(slot2)
    if times1 is None or times2 is None:
        return False
    for (start1, end1) in times1:
        for (start2, end2) in times2:
            if start1 < end2 and start2 < end1:
                return True
    return False

def has_conflict(combination):
    for i, (course1, prof1, slot1) in enumerate(combination):
        for j, (course2, prof2, slot2) in enumerate(combination):
            if i < j and prof1 == prof2 and time_conflict(slot1, slot2):
                return True
    return False

# Generate valid combinations
def generate_valid_combinations(courses_slots):
    all_options = []
    for course, data in courses_slots.items():
        for professor, slots in data['professors'].items():
            for slot_info in slots:
                if len(slot_info) >= 2:
                    slot = slot_info[1]  # Ensure slot_info has at least two elements
                    all_options.append((course, professor, slot))
                else:
                    print(f"Warning: Slot info missing for {course}, {professor}")

    valid_combinations = []
    for combination in product(all_options, repeat=len(courses_slots)):
        if not has_conflict(combination):
            valid_combinations.append(combination)
    
    return valid_combinations

# Print combinations
def print_combinations(combinations):
    for idx, comb in enumerate(combinations):
        print(f"Combination {idx + 1}:")
        for item in comb:
            print(f"  Course: {item[0]}, Professor: {item[1]}, Slot: {item[2]}")
        print()

# Generate and print valid combinations
valid_combinations = generate_valid_combinations(courses_slots)
print_combinations(valid_combinations)
