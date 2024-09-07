#input json
input_data = '''
{
  "courses": [
    {
      "title": "Front End Design and Testing",
      "code": "CSI3029",
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
      "code": "CSI3025",
      "slots": [
        {
          "prof": "Sudhakar P",
          "slots": "B1,B2,L1+L2,L55+L56"
        }
      ]
    },
    {
      "title": "Artificial Intelligence and Expert Systems",
      "code": "CSI3003",
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
      "code": "CSI3002",
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
      "code": "CSI3001",
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
      "code": "CSI3004",
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
      "code": "CSI3021",
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
      "code": "JAP1001",
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
      "code": "MDI3004",
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
      "code": "STS3021",
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
      "code": "CSI4002",
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
