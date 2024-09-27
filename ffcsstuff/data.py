#input json
input_data = '''
{
    "courses": [
        {
            "slots": [
                {
                    "prof": "SIVA SANKARI S",
                    "slots": "G2+TG2"
                },
                {
                    "prof": "SIVAKUMAR V",
                    "slots": "G2+TG2"
                },
                {
                    "prof": "GANESH SHAMRAO KHEKARE",
                    "slots": "G2+TG2"
                },
                {
                    "prof": "YUVARAJ N",
                    "slots": "G1+TG1"
                },
                {
                    "prof": "JEEVANANTHAM A.K.",
                    "slots": "G2+TG2"
                },
                {
                    "prof": "MADHAN E S",
                    "slots": "G1+TG1"
                },
                {
                    "prof": "TAMIZHARASI T",
                    "slots": "G1+TG1"
                },
                {
                    "prof": "SATHYA K",
                    "slots": "G1+TG1"
                }
            ],
            "title": "Artificial Intelligence and Expert Systems",
            "code": "CS13003",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "DHINAKARAN N",
                    "slots": "C2,L1+L2"
                },
                {
                    "prof": "ARULKUMAR V",
                    "slots": "C2,C1,L15+L16,L35+L36"
                }
            ],
            "title": "Front End Design and Testing",
            "code": "CS13029",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "SUDHAKAR P",
                    "slots": "B2,B1,L1+L2,L55+L56"
                }
            ],
            "title": "Application Development and Deployment Architecture",
            "code": "CS13025",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "THANGARAMYA K",
                    "slots": "A2,A1,L25+L26,L51+L52"
                },
                {
                    "prof": "S M FAROOQ",
                    "slots": "A2,A1,L7+L8,L51+L52"
                },
                {
                    "prof": "NIVITHA K",
                    "slots": "A2,A1,L11+L12,L41+L42"
                },
                {
                    "prof": "SUNIL KUMAR",
                    "slots": "A2,A1,L11+L12,L41+L42"
                }
            ],
            "title": "Applied Cryptography and Network Security",
            "code": "CSJ3002",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "MUTHUNAGAI S U",
                    "slots": "F2+TF2"
                },
                {
                    "prof": "NIVITHA K.",
                    "slots": "F1+TF1"
                },
                {
                    "prof": "MOHAMMAD ARIF",
                    "slots": "F1+TF1"
                }
            ],
            "title": "Advanced Graph Algorithms",
            "code": "CS13020",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "KHANJAN",
                    "slots": "B1"
                },
                {
                    "prof": "HIYA MUKHERJEE",
                    "slots": "C1"
                }
            ],
            "title": "Japanese for Beginners",
            "code": "JAP1001",
            "semester": "Fall Semester 2024-25",
            "category": "UC - University Core"
        },
        {
            "slots": [
                {
                    "prof": "DHANOJ GUPTA",
                    "slots": "TCC1"
                },
                {
                    "prof": "SUMANGALA T P",
                    "slots": "TAA1"
                },
                {
                    "prof": "SASMITA MOHAKUD",
                    "slots": "TAA2"
                },
                {
                    "prof": "AMRITA DEY",
                    "slots": "TCC2"
                }
            ],
            "title": "Introduction to Innovative Projects",
            "code": "PHY1901",
            "semester": "Fall Semester 2024-25",
            "category": "UC - University Core"
        },
        {
            "slots": [
                {
                    "prof": "NIVETHITHA K",
                    "slots": "F2+TF2"
                },
                {
                    "prof": "UMA PRIYA D",
                    "slots": "F1+TF1"
                },
                {
                    "prof": "PAVITHRA M",
                    "slots": "F2+TF2"
                },
                {
                    "prof": "MALINI S",
                    "slots": "F2+TF2"
                },
                {
                    "prof": "SOMASUNDARAM S K",
                    "slots": "F1+TF1"
                },
                {
                    "prof": "DINESH R",
                    "slots": "F2+TF2"
                },
                {
                    "prof": "BHAWANA TYAGI",
                    "slots": "F1+TF1"
                },
                {
                    "prof": "ROHINI S",
                    "slots": "F1+TF1"
                }
            ],
            "title": "Logic and Combinatorics for Computer Science",
            "code": "CS14002",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "SAYAN SIKDER",
                    "slots": "G1+TG1"
                },
                {
                    "prof": "KAMANASISH BHATTACHARJEE",
                    "slots": "G2+TG2"
                }
            ],
            "title": "Game Theory",
            "code": "CS14006",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "THIRUNAVUKKARASAN M",
                    "slots": "C1,L7+L8,L51+L52,C2"
                }
            ],
            "title": "Advanced Server Side Programming",
            "code": "CS13023",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "DINESH R",
                    "slots": "A2+TA2,A1+TA1,L15+L16,L53+L54"
                },
                {
                    "prof": "PRIYANKA N",
                    "slots": "A1+TA1,A2+TA2,L15+L16,L37+L38"
                },
                {
                    "prof": "RAGAVAN K",
                    "slots": "A1+TA1,A2+TA2,L21+L22,L53+L54"
                }
            ],
            "title": "Advanced Wireless Networks",
            "code": "CSJ3009",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "PUSHPA GOTHWAL",
                    "slots": "E2+TE2"
                },
                {
                    "prof": "LATHA REDDY N",
                    "slots": "E2+TE2"
                },
                {
                    "prof": "THIRUNAVUKKARASAN M",
                    "slots": "E1+TE1"
                },
                {
                    "prof": "NARMALLI JAYAKRISHNA",
                    "slots": "E1+TE1"
                },
                {
                    "prof": "SREEHARI S",
                    "slots": "E1+TE1"
                },
                {
                    "prof": "SURESH A",
                    "slots": "E1+TE1"
                },
                {
                    "prof": "DEEPA D",
                    "slots": "E2+TE2"
                },
                {
                    "prof": "KRISHNARAJ N",
                    "slots": "E2+TE2"
                }
            ],
            "title": "Advanced Computer Architecture",
            "code": "CS13021",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "EBENEZER JULIET S",
                    "slots": "B1+TB1,B2+TB2,L27+L28,L43+L44"
                },
                {
                    "prof": "ARPAN GARAI",
                    "slots": "B1+TB1,B2+TB2,L27+L28,L43+L44"
                },
                {
                    "prof": "GAYATHRI S",
                    "slots": "B1+TB1,B2+TB2,L13+L14,L43+L44"
                }
            ],
            "title": "Computer Graphics and Multimedia",
            "code": "CS3011",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "SIVA SANKARI S",
                    "slots": "C2+TC2,C1+TC1,L5+L6,L49+L50"
                },
                {
                    "prof": "PARTHIBAN K",
                    "slots": "C1+TC1,C2+TC2,L5+L6,L35+L36"
                },
                {
                    "prof": "KATARI BALAKRISHNA",
                    "slots": "C2+TC2,L5+L6"
                }
            ],
            "title": "Cyber Security and Application Security",
            "code": "CS13022",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "MEENAKSHI S P",
                    "slots": "C1,C2,L21+L22,L31+L32"
                },
                {
                    "prof": "GANESH SHAMRAO KHEKARE",
                    "slots": "C1,C2,L21+L22,L31+L32"
                }
            ],
            "title": "Data Science Programming",
            "code": "CS13004",
            "semester": "Fall Semester 2024-25",
            "category": "UE - University Elective"
        },
        {
            "slots": [
                {
                    "prof": "NAVEEN KUMAR N",
                    "slots": "F2+TF2"
                },
                {
                    "prof": "BALAJI N",
                    "slots": "F1+TF1"
                },
                {
                    "prof": "ARUMUGA ARUN R",
                    "slots": "F2+TF2"
                }
            ],
            "title": "Advanced Data Compression Techniques",
            "code": "CS13019",
            "semester": "Fall Semester 2024-25",
            "category": "PE - Programme Elective"
        },
        {
            "slots": [
                {
                    "prof": "KRISHNA RANI SAMAL K",
                    "slots": "G2+TG2"
                }
            ],
            "title": "Software Application Architecture",
            "code": "CS13024",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "PUSHPA GOTHWAL",
                    "slots": "B2+TB2,B1+TB1,L13+L14,L59+L60"
                },
                {
                    "prof": "MUTHUNAGAI S U",
                    "slots": "B2+TB2,B1+TB1,L13+L14,L43+L44"
                },
                {
                    "prof": "DHIVYA C R",
                    "slots": "B2+TB2,B1+TB1,L43+L44,L27+L28"
                },
                {
                    "prof": "RANJITHKUMAR S",
                    "slots": "B2+TB2,B1+TB1,L27+L28,L53+L54"
                }
            ],
            "title": "Cloud Computing Methodologies",
            "code": "CSJ3001",
            "semester": "Fall Semester 2024-25",
            "category": "PC - Programme Core"
        },
        {
            "slots": [
                {
                    "prof": "FACE (APT)",
                    "slots": "D2+TD2,D1+TD1,D2+TD2,D2+TD2,D2+TD2,D2+TD2,D1+TD1,D1+TD1,D1+TD1,D2+TD2"
                },
                {
                    "prof": "ETHNUS (APT)",
                    "slots": "D1+TD1,D2+TD2,D1+TD1,D1+TD1,D2+TD2,D2+TD2,D1+TD1,D1+TD1"
                }
            ],
            "title": "Getting Started to Skill Enhancement",
            "code": "STS3021"
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
