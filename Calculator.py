#Author: Allusura
#A simple Python Calculator I made after 10 days of studying the language.

from art import logo
import os

def add(n1, n2):
    return n1 + n2
  
def subtract(n1, n2):
    return n1 - n2
  
def multiply(n1, n2):
    return n1 * n2
  
def divide(n1, n2):
    return n1 / n2
  
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  os.system('clear')
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  flag = True
  while flag:
    print()
    for operation in operations:
      print(operation)
    
    operation_symbol = input("\nPick an operation from the line above: ")
    num2 = float(input("\nWhat's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"\n{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"\n\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'n':
        flag = False
        calculator()
    else:
      num1 = answer

calculator()
