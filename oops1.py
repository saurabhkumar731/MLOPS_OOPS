#initiate a class
class Employee:
    #special method/magic method/dunder method -constructor
    def __init__(self):
        #print(id(self))
        #print("started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        #print("attributes/data have been initiated")
        
    def Travel(self):
        print("This  travel method was called manually")
        print(f"Employee in now travelling to Patna")   
        
#create an obj/instance of the class        
sam=Employee()
# print(id(sam))

# sam.name="Rajat"
# print(sam.name)

# shaktiman=Employee()
# print(id(shaktiman))  

#printing the attributes
#print(sam.salary)   

#calling a  method
#sam.Travel()   

#print(type(sam))