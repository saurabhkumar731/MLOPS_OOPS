# #simple inheritance
# #Base class
# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         print(f"{self.name} make a sound.")
        
# #Derived class
# class Dog(Animal):
    
#     def __init__(self):
#         self.behaviour="friendly"
    
#     def speak(self):
#         print(f"Buddy barks.He is very {self.behaviour}")          
        
        
# #create an instance of animal
# #animal=Animal("gengeric animal") 
# #animal.speak()

# #create an instance of dog
# dog=Dog()
# dog.speak()    

#super keyword 

#Base class
class Animal:
    def __init__(self):
        self.name="Buddy"
        
    def speak(self):
        print(f"{self.name} make a sound")
        
#Derived class:
class Dog(Animal):
    def __init__(self,bread):
        super().__init__()
        self.bread=bread
        
    def speak(self):
        super().speak()# call the base class method
        print(f"{self.name} barks.It is a {self.bread}.")  
        
#create an instance of dog
dog=Dog("Golden Retriever")  
dog.speak()                       