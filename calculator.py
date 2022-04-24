class Calculation:
     def __init__(self, num1, num2):
          self.num1 = num1
          self.num2 = num2
          
     def add(num1, num2):
          return num1 + num2
     
     def subtract(num1, num2):
          return num1 - num2
     
     def multiply(num1, num2):
          return num1 * num2
     
     def divide(num1, num2):
          return num1 / num2
     
     def expontent(num1, num2):
          return num1**num2
     
     def quotient(num1, num2):
          return num1 % num2
     
     def fraction_conversion(num1, num2):
          return num1 / num2
     
def operation():
     answer = 0
     operation = input("What operation do you want to perform: ")

     if operation == "fraction Covernversion" or operation == "/.":
          num = input("Enter fraction: ")
               
          numerator = num[0]
          denominator = num[2]
          answer = Calculation.fraction_conversion(int(numerator),int(denominator))
          print(answer)  
     else:
          num1 = int(input("Enter number 1: "))
          num2 = int(input("Enter number 2: "))

          if operation == "add" or operation == "sum" or operation == "+":
               answer = Calculation.add(num1, num2)
               print(str(answer))
          elif operation == "subtract" or operation == "difference" or operation == "-":
               answer = Calculation.subtract(num1, num2)
               print(str(answer))
          elif operation == "multiply" or operation == "product" or operation == "*":
               answer = Calculation.multiply(num1, num2)
               print(str(answer))
          elif operation == "divide" or operation == "division" or operation == "/":
               answer = Calculation.divide(num1, num2)
               print(str(answer))    
          elif operation == "expontent" or operation == "to the power" or operation == "**":
               answer = Calculation.expontent(num1, num2)
               print(str(answer)) 
          elif operation == "quotient" or operation == "remainder" or operation == "%":
               answer = Calculation.quotient(num1, num2)
               print(str(answer)) 
       
