#input json
input_data = '''
{
  "courses": [
    {
      "title": "Front End Design and Testing",
      "code": "CSI:3029",
      "slots": [
        {
          "prof": "Arulkumar V",
          "slots": "C1,C2,L15+L16,L35+L36"
        },
        {
          "prof": "Dhinakaran N",
          "slots": "C2,L1+L2"
        }
      ]
    },
    {
      "title": "Application Development and Deployment Architecture",
      "code": "CSI:3025",
      "slots": [
        {
          "prof": "Sudhakar P",
          "slots": "B1,B2,L1+L2,L55+L56"
        }
      ]
    },
    {
      "title": "Artificial Intelligence and Expert Systems",
      "code": "CSI3:003",
      "slots": [
        {
          "prof": "Tamizharasi T",
          "slots": "G1+TG1"
        },
        {
          "prof": "Madhan E S",
          "slots": "G1+TG1"
        },
        {
          "prof": "Sathya K",
          "slots": "G1+TG1"
        },
        {
          "prof": "Jeevanantham A.K.",
          "slots": "G2+TG2"
        },
        {
          "prof": "Siva Sankari S",
          "slots": "G2+TG2"
        },
        {
          "prof": "Yuvaraj N",
          "slots": "G1+TG1"
        },
        {
          "prof": "Sivakumar V",
          "slots": "G2+TG2"
        },
        {
          "prof": "Ganesh Shamrao Khekare",
          "slots": "G2+TG2"
        }
      ]
    },
    {
      "title": "Applied Cryptography and Network Security",
      "code": "CSI3:002",
      "slots": [
        {
          "prof": "Nivitha K",
          "slots": "A1,A2,L11+L12,L41+L42"
        },
        {
          "prof": "Thangaramya K",
          "slots": "A1,A2,L25+L26,L51+L52"
        },
        {
          "prof": "S M Farooq",
          "slots": "A1,A2,L7+L8,L51+L52"
        },
        {
          "prof": "Sunil Kumar",
          "slots": "A1,A2,L11+L12,L41+L42"
        }
      ]
    },
    {
      "title": "Cloud Computing and methodologies",
      "code": "CSI3:001",
      "slots": [
        {
          "prof": "Dhivyaa CR",
          "slots": "B1+TB1,B2+TB2,L27+L28,L43+L44"
        },
        {
          "prof": "Muthunagai",
          "slots": "B1+TB1,B2+TB2,L13+L14,L43+L44"
        },
        {
          "prof": "Ranjithkumar S",
          "slots": "B1+TB1,B2+TB2,L27+L28,L53+L54"
        },
        {
          "prof": "Pushpa Gothwal",
          "slots": "B1+TB1,B2+TB2,L13+L14,L59+L60"
        }
      ]
    },
    {
      "title": "Data Science Programming",
      "code": "CSI3:004",
      "slots": [
        {
          "prof": "Ganesh Shamrao Khekare",
          "slots": "C1,C2,L21+L22,L31+L32"
        },
        {
          "prof": "Meenakshi SP",
          "slots": "C1,C2,L21+L22,L31+L32"
        }
      ]
    },
    {
      "title": "Advanced Computer Architecture",
      "code": "CSI:3021",
      "slots": [
        {
          "prof": "Thirunavukkarasan M",
          "slots": "E1+TE1"
        },
        {
          "prof": "Sreethar S",
          "slots": "E1+TE1"
        },
        {
          "prof": "Narmalli Jayakrishna",
          "slots": "E1+TE1"
        },
        {
          "prof": "Suresh A",
          "slots": "E1+TE1"
        },
        {
          "prof": "Krishnaraj N",
          "slots": "E2+TE2"
        },
        {
          "prof": "Deepa D",
          "slots": "E2+TE2"
        },
        {
          "prof": "Pushpa Gothwal",
          "slots": "E2+TE2"
        },
        {
          "prof": "Latha Reddy N",
          "slots": "E2+TE2"
        }
      ]
    },
    {
      "title": "Japanese for Beginners",
      "code": "JAP1:001",
      "slots": [
        {
          "prof": "Khanjan",
          "slots": "B1"
        },
        {
          "prof": "Hiya Mukherjee",
          "slots": "C1"
        }
      ]
    },
    {
      "title": "Intelligent Database Systems",
      "code": "MDI3:004",
      "slots": [
        {
          "prof": "Deepika J",
          "slots": "G1+TG1"
        },
        {
          "prof": "Thangaramya K",
          "slots": "G1+TG1"
        },
        {
          "prof": "Saurabh Agrawal",
          "slots": "G2+TG2"
        },
        {
          "prof": "Jeevanajyothi Pujari",
          "slots": "G2+TG2"
        }
      ]
    },
    {
      "title": "Getting Started to Skill Enhancemnets",
      "code": "STS:3021",
      "slots": [
        {
          "prof": "Ethnus",
          "slots": "D1+TD1,D2+TD2"
        },
        {
          "prof": "Face",
          "slots": "D1+TD1,D2+TD2"
        }
      ]
    },
    {
      "title": "Logic and Combanitorics for Computer Science",
      "code": "CSI4:002",
      "slots": [
        {
          "prof": "Bhawana Tyagi",
          "slots": "F1+TF1"
        },
        {
          "prof": "Somasundaram SK",
          "slots": "F1+TF1"
        },
        {
          "prof": "Uma Priya D",
          "slots": "F1+TF1"
        },
        {
          "prof": "Rohini S",
          "slots": "F1+TF1"
        },
        {
          "prof": "Nivethitha k",
          "slots": "F2+TF2"
        },
        {
          "prof": "Dinesh R",
          "slots": "F2+TF2"
        },
        {
          "prof": "Malini S",
          "slots": "F2+TF2"
        },
        {
          "prof": "Pavithra M",
          "slots": "F2+TF2"
        }
      ]
    }
  ]
}
'''

#slot mapped with it's timing
slot_timings = {
    "A1": [("Monday", "08:00-08:50"), ("Wednesday", "09:00-09:50")],
    "TA1": [("Friday", "10:00-10:50")],
    "TAA1": [("Tuesday", "12:00-12:50")],
    "B1": [("Tuesday", "08:00-08:50"), ("Thursday", "09:00-09:50")],
    "TB1": [("Monday", "11:00-11:50")],
    "C1": [("Wednesday", "08:00-08:50"), ("Friday", "09:00-09:50")],
    "TC1": [("Tuesday", "11:00-11:50")],
    "TCC1": [("Thursday", "12:00-12:50")],
    "D1": [("Thursday", "08:00-08:50"), ("Monday", "10:00-10:50")],
    "TD1": [("Friday", "12:00-12:50")],
    "E1": [("Friday", "08:00-08:50"), ("Tuesday", "10:00-10:50")],
    "TE1": [("Thursday", "11:00-11:50")],
    "F1": [("Monday", "09:00-09:50"), ("Wednesday", "10:00-10:50")],
    "TF1": [("Friday", "11:00-11:50")],
    "G1": [("Tuesday", "09:00-09:50"), ("Thursday", "10:00-10:50")],
    "TG1": [("Monday", "12:00-12:50")],
    "A2": [("Monday", "14:00-14:50"), ("Wednesday", "15:00-15:50")],
    "F2": [("Monday", "15:00-15:50"), ("Wednesday", "16:00-16:50")],
    "D2": [("Monday", "16:00-16:50"), ("Thursday", "14:00-14:50")],
    "TB2": [("Monday", "17:00-17:50")],
    "TG2": [("Monday", "18:00-18:50")],
    "B2": [("Tuesday", "14:00-14:50"), ("Thursday", "15:00-15:50")],
    "G2": [("Tuesday", "15:00-15:50"), ("Thursday", "16:00-16:50")],
    "E2": [("Tuesday", "16:00-16:50"), ("Friday", "14:00-14:50")],
    "TC2": [("Tuesday", "17:00-17:50")],
    "TAA2": [("Tuesday", "18:00-18:50")],
    "C2": [("Wednesday", "14:00-14:50"), ("Friday", "15:00-15:50")],
    "TD2": [("Wednesday", "17:00-17:50")],
    "TBB2": [("Wednesday", "18:00-18:50")],
    "TE2": [("Thursday", "17:00-17:50")],
    "TCC2": [("Thursday", "18:00-18:50")],
    "TA2": [("Friday", "16:00-16:50")],
    "TF2": [("Friday", "17:00-17:50")],
    "TDD2": [("Friday", "18:00-18:50")],
    "L1+L2": [("Monday", "08:00-09:40")],
    "L3+L4": [("Monday", "09:50-11:30")],
    "L5+L6": [("Monday", "11:40-12:30")],
    "L7+L8": [("Tuesday", "08:00-09:40")],
    "L9+L10": [("Tuesday", "09:50-11:30")],
    "L11+L12": [("Tuesday", "11:40-12:30")],
    "L13+L14": [("Wednesday", "08:00-09:40")],
    "L15+L16": [("Wednesday", "09:50-11:30")],
    "L17+L18": [("Wednesday", "11:40-12:30")],
    "L19+L20": [("Thursday", "08:00-09:40")],
    "L21+L22": [("Thursday", "09:50-11:30")],
    "L23+L24": [("Thursday", "11:40-12:30")],
    "L25+L26": [("Friday", "08:00-09:40")],
    "L27+L28": [("Friday", "09:50-11:30")],
    "L29+L30": [("Friday", "11:40-12:30")],
    "L31+L32": [("Monday", "14:00-15:40")],
    "L33+L34": [("Monday", "15:50-17:30")],
    "L35+L36": [("Monday", "18:30-1920")],
    "L37+L38": [("Tuesday", "14:00-15:40")],
    "L39+L40": [("Tuesday", "15:50-17:30")],
    "L41+L42": [("Tuesday", "18:00-1920")],
    "L43+L44": [("Wednesday", "14:00-15:40")],
    "L45+L46": [("Wednesday", "15:50-17:30")],
    "L47+L48": [("Wednesday", "17:40-1920")],
    "L49+L:50": [("Thursday", "14:00-15:40")],
    "L51+L52": [("Thursday", "15:50-17:30")],
    "L53+L54": [("Thursday", "17:40-1920")],
    "L55+L56": [("Friday", "14:00-15:40")],
    "L57+L58": [("Friday", "15:50-17:30")],
    "L59+L60": [("Friday", "17:40-1920")],
    "V1": [("Wednesday", "11:00-11:50")],
    # Add any additional slots if necessary
}


course_data = {
    "CSI:3029": {
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
    "CSI:3025": {
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
    "CSI3:003": {
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
    "CSI3:002": {
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
    "CSI3:001": {
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
    "CSI3:004": {
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
    "CSI:3021": {
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
    "JAP1:001": {
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
    "MDI3:004": {
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
    "STS:3021": {
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
    "CSI4:002": {
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
