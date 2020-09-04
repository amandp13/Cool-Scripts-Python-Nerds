# Define your classes below:
class Mother:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Father:
    def __init__(self, eye_color, hair_color, hair_type):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_type = hair_type


class Child(Mother, Father):
    def __init__(self, eye_color, hair_color, hair_type):
        super().__init__(eye_color, hair_color, hair_type)

j = Child('blue','red','metal')
print(j.eye_color,j.hair_color,j.hair_type)
