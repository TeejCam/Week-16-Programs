class Doctor:
    def __init__(self, name):
        self.name = name
        # Patients this doctor is treating
        self.patients = []

    def viewPatientInfo(self):
        if not self.patients:
            print("No patients found.")
        else:
            for patient in self.patients:
                print(f"Patient Name: {patient.name}, Species: {patient.species}, Age: {patient.age}")

    def assignPatient(self, patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} has been assigned to Dr. {self.name}")
    