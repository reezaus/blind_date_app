import random


class Candidate:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.gender = ""
        self.age = 0
        self.preference = ""
        self.bio = ""

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_age(self, age):
        self.age = age

    def set_preference(self, preference):
        self.preference = preference

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_preference(self):
        return self.preference

    def add_user(self, id, name, gender, age, preference):
        self.set_id(id)
        self.set_name(name)
        self.set_gender(gender)
        self.set_age(age)
        self.set_preference(preference)

    def display_user(self):
        print("Candidate ", self.id, ":", self.name, ",", self.gender, ",", self.age, ", prefers", self.preference)

    def set_bio(self, bio):
        self.bio = bio

    def get_bio(self):
        return self.bio


def shuffle(alist):
    random.shuffle(alist)
    for i in range(0, len(alist)):
        print("Bio", i+1, ":", alist[i].get_bio())

print("\nList of Candidates: ")
a = Candidate()
a.add_user(1, "Joe", "M", 23, "F")
a.display_user()
a.set_bio("I like long walks along the beach in VR Chat.")

b = Candidate()
b.add_user(2, "Irene", "F", 19, "MF")
b.display_user()
b.set_bio("I love kpop and boba.")

c = Candidate()
c.add_user(3, "JP", "M", 22, "F")
c.display_user()
c.set_bio("Meet girls get money.")

d = Candidate()
d.add_user(4, "Joseph Stalin", "M", 100, "F")
d.display_user()
d.set_bio("My hobbies include drinking vodka and mass murder.")

e = Candidate()
e.add_user(5, "Ellen Degeneres", "F", 35, "F")
e.display_user()
e.set_bio("Hello my name is Ellen I host a show you may have heard of it.")


candidateList = [a, b, c, d, e]

print("\nShuffled list of bios: ")
shuffle(candidateList)

print("\nCan you guess who is who?")




