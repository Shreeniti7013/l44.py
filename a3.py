class parrot:
    species="birds"
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj1=parrot("Tom",10 )
obj2=parrot("Jerry",12)
obj3=parrot("Tuffy",15)

print("Tom,jerry and tuffy are all{}".format(parrot.species))
print("{} is {} years old".format(obj1.name,obj1.age))
print("{} is {} years old".format(obj2.name,obj2.age))
print("{} is {} years old".format(obj3.name,obj3.age))