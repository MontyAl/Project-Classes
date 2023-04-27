class Doctor:
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def formatDrInfo(self):
        return str(self.id) + "_" + self.name + "_" + self.specialization + "_" + self.working_time + "_" + self.qualification + "_" + str(self.room_number)

    def enterDrInfo(self):
        self.id = input("Enter Doctor ID: ")
        self.name = input("Enter Doctor Name: ")
        self.specialization = input("Enter Doctor Specialization: ")
        self.working_time = input("Enter Doctor Working Time: ")
        self.qualification = input("Enter Doctor Qualification: ")
        self.room_number = int(input("Enter Room Number: "))

    def readDoctorsFile(self):
        doctors = []
        with open('doctors.txt', 'r') as file:
            for line in file:
                data = line.strip().split("_")
                doctor = Doctor(data[0], data[1], data[2], data[3], data[4], data[5])
                doctors.append(doctor)
        return doctors

    def searchDoctorById(self, id):
        doctors = self.readDoctorsFile()
        for doctor in doctors:
            if doctor.id == id:
                return doctor
        return None

    def searchDoctorByName(self, name):
        doctors = self.readDoctorsFile()
        for doctor in doctors:
            if doctor.name == name:
                return doctor
        return None

    def displayDoctorInfo(self):
        print("ID: ", self.id)
        print("Name: ", self.name)
        print("Specialization: ", self.specialization)
        print("Working Time: ", self.working_time)
        print("Qualification: ", self.qualification)
        print("Room Number: ", self.room_number)

    def editDoctorInfo(self):
        self.enterDrInfo()

    def displayDoctorsList(self):
        doctors = self.readDoctorsFile()
        for doctor in doctors:
            print(doctor.formatDrInfo())

    def writeListOfDoctorsToFile(self, doctors):
        with open('doctors.txt', 'w') as file:
            for doctor in doctors:
                file.write(doctor.formatDrInfo() + "\n")

    def addDrToFile(self):
        self.enterDrInfo()
        with open('doctors.txt', 'a') as file:
            file.write(self.formatDrInfo() + "\n")



class Facility:
    def __init__(self, facility_name):
        self.facility_name = facility_name

    def addFacility(self):
        self.facility_name = input("Enter Facility Name: ")
        with open('facilities.txt', 'a') as file:
            file.write(self.facility_name + "\n")

    def displayFacilities(self):
        with open('facilities.txt', 'r') as file:
            for line in file:
                print(line.strip())

    def writeListOfFacilitiesToFile(self, facilities):
        with open('facilities.txt', 'w') as file:
            for facility in facilities:
                file.write(facility.facility_name + "\n")

                

class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def addLabToFile(self):
        with open("laboratories.txt", "a") as f:
            f.write(self.formatLabInfo() + "\n")

    def writeListOfLabsToFile(self, labs):
        with open("laboratories.txt", "w") as f:
            for lab in labs:
                f.write(lab.formatLabInfo() + "\n")

    def displayLabsList(self):
        labs = self.readLaboratoriesFile()
        for lab in labs:
            print(lab.lab_name, lab.cost)

    def formatLabInfo(self):
        return f"{self.lab_name},{self.cost}"

    def enterLaboratoryInfo():
        lab_name = input("Enter laboratory name: ")
        cost = float(input("Enter laboratory cost: "))
        return Laboratory(lab_name, cost)

    def readLaboratoriesFile():
        labs = []
        with open("laboratories.txt", "r") as f:
            for line in f:
                lab_name, cost = line.strip().split(",")
                labs.append(Laboratory(lab_name, float(cost)))
        return labs
