data = {"CS13003": {"professors": {"MADHAN E.S": [("G1+TG1",)], "YUVARAJ N": [("G1+TG1",)], "TAMIZHARASI T": [("G1+TG1",)], "SIVA. SANKARI.S": [("G2+TG2",)], "GANESH SHAMRAO KHEKARE": [("G2+TG2",)], "SIVAKUMAR V": [("G2+TG2",)], "SATHYA K": [("G1+TG1",)], "JEEVANANTHAM A.K.": [("G2+TG2",)]}, "mandatory": True}, "CS13029": {"professors": {"ARULKUMAR V": [("C2", "L15+L16"), ("C2", "L35+L36"), ("C1", "L15+L16"), ("C1", "L35+L36")], "DHINAKARAN N": [("C2", "L1+L2")]}, "mandatory": False}, "CS13025": {"professors": {"SUDHAKAR P": [("B2", "L1+L2"), ("B2", "L55+L56"), ("B1", "L1+L2"), ("B1", "L55+L56")]}, "mandatory": False}}

import json

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)