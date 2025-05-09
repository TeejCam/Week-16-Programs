class Patient:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        # Corresponds to PatientDetails class
        self.details = None

    def setName(self, name):
        self.name = name

    def setSpecies(self, species):
        self.species = species

    def setAge(self, age):
        self.age = age

    def setDetails(self, details):
        self.details = details