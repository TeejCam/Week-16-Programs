class PatientDetails:
    def __init__(self, checkups=0, procedures=None, appCost=0.0, procedureCost=0.0):
        if procedures is None:
            procedures = []
        self.checkups = checkups
        # Proceudres include xrays, surgeries, etc
        self.procedures = procedures
        self.appCost = appCost
        self.procedureCost = procedureCost

    def calcPrice(self):
        totalPrice = self.appCost + self.procedureCost
        print(f"Total cost for the appointment: {totalPrice}")
        return totalPrice

    def addProcedure(self, procedure, cost):
        self.procedures.append(procedure)
        self.procedureCost += cost
        print(f"Added procedure: {procedure}, cost: {cost}")

    