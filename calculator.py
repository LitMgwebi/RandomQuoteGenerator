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
     
     def operation():
          answer = 0
          num1 = int(input("Enter number 1: "))
          num2 = int(input("Enter number 2: "))
          operation = input("What operation do you want to perform: ")

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
     
Calculation.operation()