"""
Question:
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in init method.You can init an object with construct parameter or set the value later
"""

#solution

class Bike:
    name="Bike"

    def __init__(self,name=None):
        self.name=name;

bike1=Bike("Bajaj")

print(f"{Bike.name} name is {bike1.name}")

bike2=Bike("Suzuki")

print(f"{Bike.name} name is {bike2.name}")