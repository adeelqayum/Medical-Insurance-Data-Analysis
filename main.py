import csv
from enum import Enum

class PatientInformation():
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.cost = charges
               
class Region(Enum):
    NE = 1
    SE = 2
    NW = 3
    SW = 4

#member variables
patients = []
    
def get_region_enum(region_string):
    match region_string.upper():
        case "NORTHEAST":
            return Region.NE
        case "SOUTHEAST":
            return Region.SE
        case "NORTHWEST":
            return Region.NW
        case "SOUTHWEST":
            return Region.SW
        case _:
            return Region.NE

def create_patient_objects(list_records):
    for patient_info in list_records:
        age = int(patient_info["age"])
        sex = patient_info["sex"]
        bmi = patient_info["bmi"]
        children = patient_info["children"]
        smoker = False if patient_info["smoker"].upper() == "NO" else True
        region = get_region_enum(patient_info["region"])
        charges = patient_info["charges"]
        patient_instance = PatientInformation(age, sex, bmi, children, smoker, region, charges)
        patients.append(patient_instance)

def load_data_from_file(csv_file_path):
    list_records = []
    with open(csv_file_path) as insurance_data:
        data_reader = csv.DictReader(insurance_data)
        for row in data_reader:
            list_records.append(row)
        create_patient_objects(list_records)

def perform_analysis():
    num_rows = len(patients)
    print(f"There are a total of {num_rows} medical records in the dataset.")
    
    age_sum = 0
    for patient in patients:
        age_sum += patient.age
    average_age = round(age_sum/num_rows, 2)
    print(f"The average age of the dataset is {average_age}")
        

load_data_from_file('insurance.csv')
perform_analysis()