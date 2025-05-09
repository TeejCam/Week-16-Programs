from Patient import Patient
from Owner import Owner
from Doctor import Doctor
from PatientDetails import PatientDetails

owner = Owner("John Doe", "john.doe@example.com", 500.0)
patient = Patient("Bruiser", "Dog", 5)
patientDetails = PatientDetails(checkups=2, procedures=["surgery"], appCost=100.0, procedureCost=200.0)

patient.setDetails(patientDetails)

doctor = Doctor("Dr. Smith")
doctor.assignPatient(patient)
doctor.viewPatientInfo()

totalCost = patient.details.calcPrice()
owner.makePayment(totalCost)
