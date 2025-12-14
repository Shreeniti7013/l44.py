class vehicle:
    def __init__(self,name,max_speed,milleage):
         self.name=name
         self.max_speed=max_speed
         self.milleage=milleage

obj1=vehicle("School volvo",180,12)
obj2=vehicle("audi Q5",240,18)
obj3=vehicle("BMW",260,15)
print("vehicle name:",obj1.name,"Speed:",obj1.max_speed,"milleage:",obj1.milleage)
print("vehicle name:",obj2.name,"Speed:",obj2.max_speed,"milleage:",obj2.milleage)
print("vehicle name:",obj3.name,"Speed:",obj3.max_speed,"milleage:",obj3.milleage)

    