class Patient:
    def __init__(self,id, name, disease, gender, age):
        self.id = id
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

    def set_id(self,id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_disease(self,disease):
        self.disease = disease

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"


panakaj = Patient(id= 12, name='Panakaj', disease='Cancer', gender='Male', age=30)
sumit = Patient(id= 13, name='Sumit', disease='Cold', gender='Male', age=23)
alok = Patient(id=14, name='Alok', disease='Maleria', gender='Male', age=45)
ravi = Patient(id=15, name='Ravi', disease='Diabetes', gender='Male', age=25)

