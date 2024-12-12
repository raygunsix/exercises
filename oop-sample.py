class User:

    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
        name_all_caps = self.name.upper()
        return name_all_caps

    def age(self, current_year):
        age = current_year - self.birthyear
        return age


bob = User("bob", 1999)

print(bob.age(2023))

print(bob.get_name())