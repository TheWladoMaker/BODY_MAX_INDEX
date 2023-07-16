#instructions
'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.'''

print("--Welcome to the BMI Calculator--")
print("\nThis program will calculate your BMI and interpret it for you.")

class Calculator_BMI:
    def __init__(self, number):
        self.number = number
        self.data = [0 for i in range(number)]

    def ingressData(self):
        self.data = [int(input("\nWhat's your weight in kg?: ")), float(input("\nWhat's your height in m?: "))]

''' We are creating a subclass called BMI_Op_basics that inherits from the Calculator_BMI superclass.
This means that BMI_Op_basics will have all the attributes and methods of Calculator_BMI, 
and can also have additional attributes and methods of its own.'''
class BMI_Op_basics(Calculator_BMI):
    def __init__(self):
        '''Here we are calling the __init__ method of the Calculator_BMI superclass.
        This sets up the BMI_Op_basics instance with the same initial state as a Calculator_BMI instance.
        In this case, it means that the instance will have a 'number' attribute set to 2, 
        and a 'data' attribute which is a list of two zeros.'''
        Calculator_BMI.__init__(self, 2)

    def BMI_Op(self):
        # Here we are calling the ingressData method of the Calculator_BMI superclass.
        # a, b = self.data is the same as a = self.data[0] and b = self.data[1]
        # This means that the BMI_Op_basics instance will have a 'data' attribute which is a list of two numbers.
        a, b = self.data
        self.BMI = round((a / b ** 2),2)
        return (f"\nYour BMI is {self.BMI}")
    
    def BMI_Op_interpretation(self):
        if 0 < self.BMI < 18.5:
            return (f"\nYour BMI is {self.BMI}, you are underweight.")
        elif self.BMI < 25:
            return (f"\nYour BMI is {self.BMI}, you have a normal weight.")
        elif self.BMI < 30:
            return (f"\nYour BMI is {self.BMI}, you are slightly overweight.")
        elif self.BMI < 35:
            return (f"\nYour BMI is {self.BMI}, you are obese.")
        else:
            return (f"\nYour BMI is {self.BMI}, you are clinically obese.")
        
BMI_Op = BMI_Op_basics()
BMI_Op.ingressData()
print(BMI_Op.BMI_Op())
print(BMI_Op.BMI_Op_interpretation())

result = BMI_Op.BMI_Op()
interpretation = BMI_Op.BMI_Op_interpretation()

# Write the results to a file
with open('BMI_results.txt', 'a') as f:
    f.write(result + '\n')
    f.write(interpretation + '\n')