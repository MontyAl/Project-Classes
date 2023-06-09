class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def get_working_time(self):
        return self.working_time

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"


class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    def format_dr_info(self, doctor):
        return str(doctor)

    def enter_dr_info(self):
        doctor_id = input("Enter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specialization = input("Enter the doctor's specialization: ")
        working_time = input("Enter the doctor's working time: ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        new_doctor = Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
        return new_doctor

    def read_doctors_file(self):
        with open("doctors.txt", "r") as file:
            for line in file:
                doctor_info = line.strip().split("_")
                doctor = Doctor(doctor_info[0], doctor_info[1], doctor_info[2], doctor_info[3], doctor_info[4],
                                doctor_info[5])
                self.doctors.append(doctor)

    def search_doctor_by_id(self):
        doctor_id = input("Enter the doctor ID: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id() == doctor_id:
                print(f"\nID\t Name\t\t Specialization\t Working Time\t Qualification\t Room Number\n\n")
                print(self.display_doctor_info(doctor))
                return
        print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        doctor_name = input("Enter the doctor name: ")
        for doctor in self.doctors:
            if doctor.get_name() == doctor_name:
                print(f"\nID\t Name\t\t Specialization\t Working Time\t Qualification\t Room Number\n\n")
                print(self.display_doctor_info(doctor))
                return
        print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doctor):
        return f"{str(doctor.doctor_id):5}{doctor.name:16}{doctor.specialization:16}{doctor.working_time:16}{doctor.qualification:16}{doctor.room_number}\n"

    def edit_doctor_info_by_id(self):
        edit = input("Enter Doctor ID of doctor you would like to edit\n")
        for i in range(len(self.doctors)):
            if self.doctors[i].get_doctor_id() == edit:
                self.doctors.pop(i)
                new_doctor = self.enter_dr_info()
                self.doctors.append(new_doctor)
                with open("doctors.txt", "w") as file:
                    for doctor in self.doctors:
                        file.write(self.format_dr_info(doctor) + "\n")
                print(f"Doctor whose ID is {new_doctor.doctor_id} has been edited")
                return
        print("Cannot find the doctor with the specified ID...")

    def display_doctors_list(self):
        print(f"ID\t Name\t\t Specialization\t Working Time\t Qualification\t Room Number\n\n")
        for doctor in self.doctors:
            print(self.display_doctor_info(doctor))

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        print(f"Doctor whose ID is {new_doctor.doctor_id} has been added")


class Patient:
    def __init__(self, patient_id="", name="", disease="", gender="", age=""):
        self.id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_disease(self, disease):
        self.disease = disease

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"


class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    def format_patient_info_for_file(self, patient):
        return str(patient.id) + "_" + patient.name + "_" + patient.disease + "_" + patient.gender + "_" + str(
            patient.age)

    def enter_patient_info(self):
        id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")
        return Patient(id, name, disease, gender, age)

    def read_patients_file(self):
        with open("patients.txt", "r") as f:
            for line in f:
                patient_info = line.strip().split("_")
                patient = Patient(patient_info[0], patient_info[1], patient_info[2], patient_info[3], patient_info[4],
                                )
                self.patients.append(patient)

    def search_patient_by_Id(self):
        patient_id = input("Enter the Patient ID: ")
        for patient in self.patients:
            if patient.get_id() == patient_id:
                print(f"\nID\t Name\t\t Disease\t Gender\t Age\n")
                print(f"{self.display_patient_info(patient)}\n")
                return
        print("Can't find the patient with the same id on the system\n")

    def display_patient_info(self, patient):
        return f"{str(patient.id):5}{patient.name:12}{patient.disease:12}{patient.gender:9}{patient.age}"

    def edit_patient_info_by_id(self):
        patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
        for n in range(len(self.patients)):
            if self.patients[n].get_id() == patient_id:
                self.patients.pop(n)
                new_patient = self.enter_patient_info()
                self.patients.append(new_patient)
                with open("patients.txt", "w") as file:
                    for patient in self.patients:
                        file.write(self.format_patient_info_for_file(patient) + "\n")
                print(f"Patient whose ID is {new_patient.id} has been edited")
                return
        print("Cannot find the Patient with the specified ID...")

    def display_patients_list(self):
        for patient in self.patients:
            print(f"{self.display_patient_info(patient)}\n")

    def write_list_of_patients_to_file(self):
        for p in self.patients:
            patient = self.format_patient_info_for_file(p)
            pat = open("patients.txt", "a")
            pat.write(patient)
            pat.close()

    def add_patient_to_file(self):
        add_p = self.enter_patient_info()
        self.patients.append(add_p)
        add_p_formatted = self.format_patient_info_for_file(add_p)
        add_p_to_f = open("patients.txt", "a")
        add_p_to_f.write(add_p_formatted)
        add_p_to_f.close()
        print(f"Patient whose ID is {add_p.id} has been added\n")


panakaj = Patient(patient_id=12, name='Panakaj', disease='Cancer', gender='Male', age=30)
sumit = Patient(patient_id=13, name='Sumit', disease='Cold', gender='Male', age=23)
alok = Patient(patient_id=14, name='Alok', disease='Maleria', gender='Male', age=45)
ravi = Patient(patient_id=15, name='Ravi', disease='Diabetes', gender='Male', age=25)


class Management:

    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        x = 2
        while x > 1:
            user_input = int(input("Welcome to Alberta Hospital (AH) Management system\n Select from the following "
                                   "options,"
                                   "or select 3 to stop:\n1 - Doctors\n2 - Patients\n3 - Exit Program\n"))

            if user_input == 1:
                self.doctors_menu()

            elif user_input == 2:
                self.patients_menu()

            elif user_input == 3:
                print("Thanks for using the program. Bye!\n")
                x = 0

    def doctors_menu(self):
        x = 2
        while x > 1:
            user_input = int(input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search "
                                   "for"
                                   "doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            if user_input == 1:
                self.doctor_manager.display_doctors_list()
            elif user_input == 2:
                self.doctor_manager.search_doctor_by_id()
            elif user_input == 3:
                self.doctor_manager.search_doctor_by_name()
            elif user_input == 4:
                self.doctor_manager.add_dr_to_file()
            elif user_input == 5:
                self.doctor_manager.edit_doctor_info_by_id()
            elif user_input == 6:
                x = 0
            else:
                print("Invalid input")

    def patients_menu(self):
        x = 2
        while x > 1:
            user_input = int(input(
                "Patient Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))

            if user_input == 1:
                self.patient_manager.display_patients_list()
            elif user_input == 2:
                self.patient_manager.search_patient_by_Id()
            elif user_input == 3:
                self.patient_manager.add_patient_to_file()
            elif user_input == 4:
                self.patient_manager.edit_patient_info_by_id()
            elif user_input == 5:
                x = 0
            else:
                print("Invalid input")


Management().display_menu()
