# Important modules
import os
import sys
import json
from math import sqrt, cos, sin, tan
# Unimportant module
from time import sleep
# Setting the max digit limit to 50000 to avoid OverFlow Errors whenn the user makes a huge calculation
sys.set_int_max_str_digits(50000)
# Creating the class that is responsible for the calculations
class Calculator:
    # Initializing each variable thats gonna be used in this class
    def __init__(self, operation, previous_answer, history: list, x, y):
        self.operation = None
        self.previous_answer = 0
        self.history = []
        self.x = 0
        self.y = 0
    # Creating each calculation as a function
    def addition(self):
        self.operation = f"{self.x} + {self.y}"
        self.previous_answer = self.x + self.y
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def subtraction(self):
        self.operation = f"{self.x} - {self.y}"
        self.previous_answer = self.x - self.y
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def multiplication(self):
        self.operation = f"{self.x} X {self.y}"
        self.previous_answer = self.x * self.y
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    # Handling ZeroDivision Errors with operations that include division 
    def division(self):
        try:
            self.operation = f"{self.x} / {self.y}"
            self.previous_answer = self.x / self.y
            self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
            print(f'\n{self.operation} = {self.previous_answer}')
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")
    def floor_division(self):
        try:
            self.operation = f"{self.x} // {self.y}"
            self.previous_answer = self.x // self.y
            self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
            print(f'\n{self.operation} = {self.previous_answer}')
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")
    def remainder(self):
        try:
            self.operation = f"{self.x} % {self.y}"
            self.previous_answer = self.x % self.y
            self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
            print(f'\n{self.operation} = {self.previous_answer}')
        except ZeroDivisionError:
            print("\nError: Cannot divide by zero")
    def exponent(self):
        try:
            self.operation = f"{self.x} ^ {self.y}"
            self.previous_answer = self.x ** self.y
            self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
            print(f'\n{self.operation} = {self.previous_answer}')
        except ZeroDivisionError:
            print("\nError: Zero cannot be raised to a negative number because it will lead to division")
    # Handling negative number square roots
    def square_root_x(self):
        try:
            self.operation = f"√{self.x}"
            self.previous_answer = sqrt(self.x)
            self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
            print(f'\n{self.operation} = {self.previous_answer}')
        except ValueError:
            print("\nError: Negative numbers don't have a square root")
    def square_root_y(self):
        try:
            self.operation = f"√{self.y}"
            self.previous_answer = sqrt(self.y)
            self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
            print(f'\n{self.operation} = {self.previous_answer}')
        except ValueError:
            print("\nError: Negative numbers don't have a square root")
    def absolute_value_x(self):
        self.operation = f"|{self.x}|"
        self.previous_answer = abs(self.x)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def absolute_value_y(self):
        self.operation = f"|{self.y}|"
        self.previous_answer = abs(self.y)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def sin_x(self):
        self.operation = f"sin({self.x})"
        self.previous_answer = sin(self.x)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def sin_y(self):
        self.operation = f"sin({self.y})"
        self.previous_answer = sin(self.y)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def cos_x(self):
        self.operation = f"cos({self.x})"
        self.previous_answer = cos(self.x)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def cos_y(self):
        self.operation = f"cos({self.y})"
        self.previous_answer = cos(self.y)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def tan_x(self):
        self.operation = f"tan({self.x})"
        self.previous_answer = tan(self.x)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
    def tan_y(self):
        self.operation = f"tan({self.y})"
        self.previous_answer = tan(self.y)
        self.history.append({"ID": len(self.history)+1, "Operation": self.operation, "Answer": self.previous_answer})
        print(f'\n{self.operation} = {self.previous_answer}')
# Creating the class that is responsible for the history data saving
class CalculatorHistory:
    # Initializing each variable thats gonna be used in this class
    def __init__(self, history, previous_answer):
        self.history = history
        self.previous_answer = previous_answer
    # Creating a function that reads data from the program
    def read_data(self):
        # Check if data exists
        if os.path.exists("Calculator2.json"):
            with open("Calculator2.json", "r") as f:
                self.history, self.previous_answer = json.load(f)
    # Creating a function that writes data to the file
    def write_data(self):
        with open("Calculator2.json", "w") as f:
            json.dump((self.history, self.previous_answer), f)
# Creating the class that is responsible for the inputs(CLI)
class CalculatorCLI:
    # Initializing each variable thats gonna be used in this class
    def __init__(self, option, previous_answer, history, x, y):
        self.option = option
        self.previous_answer = previous_answer
        self.history = history
        self.x = x
        self.y = y
    # Creating a function that asks for the numbers
    def ask_num(self):
        while True:
            try:
                self.x = float(input("Enter a number ->: "))
                self.y = float(input("Enter another number ->: "))
                break
            except ValueError:
                print("Invalid choice")
    # Creating a function that displays the menu and asks for the option
    def display_menu(self):
        CalculatorHistory.read_data(self)
        while True:
            print("\n1. Addition(+)")
            print("2. Subtraction(-)")
            print("3. Multiplication(X)")
            print("4. Division(/)")
            print("5. Floor division(//)")
            print("6. Remainder(%)")
            print("7. Exponent(^)")
            print("8. Square root(√)")
            print("9. Absolute value(|x|)")
            print(f"10. Trigonometry equations(sin, cos, tan) for {self.x}")
            print(f"11. Trigonometry equations(sin, cos, tan) for {self.y}")
            print("12. Use the previous answer with a new number")
            print("13. Enter new numbers")
            print("14. View history")
            print("15. Delete from history")
            print("16. Clear history")
            print("17. Exit")
            self.option = input("Enter your choice(1-17) ->: ")
            try:
                if self.option == '1':
                    Calculator.addition(self)
                    print(self.history)
                elif self.option == '2':
                    Calculator.subtraction(self)
                elif self.option == '3':
                    Calculator.multiplication(self)
                elif self.option == '4':
                    Calculator.division(self)
                elif self.option == '5':
                    Calculator.floor_division(self)
                elif self.option == '6':
                    Calculator.remainder(self)
                elif self.option == '7':
                    Calculator.exponent(self)
                elif self.option == '8':
                    sqrt_option = input(f'Would you like the square root of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ').lower().strip()
                    if sqrt_option == 'x':
                        Calculator.square_root_x(self)
                    elif sqrt_option == 'y':
                        Calculator.square_root_y(self)
                    else:
                        print("\nInvalid choice")
                elif self.option == '9':
                    abs_option = input(f'Would you like the absolute value of {self.x} or {self.y}?(Enter x for {self.x} y for {self.y}) ->: ').lower().strip()
                    if abs_option == 'x':
                        Calculator.absolute_value_x(self)
                    elif abs_option == 'y':
                        Calculator.absolute_value_y(self)
                    else:
                        print("\nInvalid choice")
                elif self.option == '10':
                    trigonometry_operation = input(f'Would you like the sine, cosine or tangent of {self.x}?(Enter sin for sine, cos for cosine, tan for tangent) ->: ').lower().strip()
                    if trigonometry_operation == 'sin':
                        Calculator.sin_x(self)
                    elif trigonometry_operation == 'cos':
                        Calculator.cos_x(self)
                    elif trigonometry_operation == 'tan':
                        Calculator.tan_x(self)
                    else:
                        print("\nInvalid choice")
                elif self.option == '11':
                    trigonometry_operation = input(f'Would you like the sine, cosine or tangent of {self.y}?(Enter sin for sine, cos for cosine, tan for tangent) ->: ').lower().strip()
                    if trigonometry_operation == 'sin':
                        Calculator.sin_y(self)
                    elif trigonometry_operation == 'cos':
                        Calculator.cos_y(self)
                    elif trigonometry_operation == 'tan':
                        Calculator.tan_y(self)
                    else:
                        print("\nInvalid choice")      
                elif self.option == '12':
                    # Check if a previous answer even exists
                    if self.previous_answer == None:
                        print("\nEnter at least one operation to initialize the previous answer")
                    else:
                        self.x = self.previous_answer
                        while True:
                            try:
                                self.y = float(input(f"Enter another number to use alongside the previous answer ->: "))
                                break
                            except ValueError:
                                print("Invalid choice")
                elif self.option == '13':
                    self.ask_num()
                elif self.option == '14':
                    # Check if history data exists
                    if not self.history:
                        print('\nNo history data found to proceed')
                    else:
                        # For display
                        print("ID            Operation          Answer")
                        # Loop through each history data
                        for history_data in self.history:
                            print(f'{history_data["ID"]}            {history_data["Operation"]}            {history_data["Answer"]}')
                elif self.option == '15':
                    # Check if history data exists
                    if not self.history:
                        print('\nNo history data found to proceed')
                    else:
                        # Storing found IDs in a list to handle invalid IDs
                        found_IDs = [history_data["ID"] for history_data in self.history]
                        # Delete ID input
                        while True:
                            try:
                                delete_ID = int(input("Enter the ID that you would like to delete(Enter 0 if you don't remember what you wanted to delete) ->: "))
                                break
                            except ValueError:
                                print("Invalid choice")
                        # Check if the ID is found or if the user wants to skip
                        if delete_ID == 0:
                            print("\nOk we will proceed as usual")
                        elif delete_ID not in found_IDs:
                            print("\nNo such ID found")
                        else:
                            # Loop through each history data
                            for history_data in self.history:
                                if history_data["ID"] == delete_ID:
                                    print(f'\nThe operation {history_data["Operation"]} has been successfully deleted')
                                    self.history.remove(history_data)
                                    break
                                else:
                                    continue
                elif self.option == '16':
                    # Check if history data exists
                    if not self.history:
                        print('\nNo history data found to proceed')
                    else:
                        self.history.clear()
                        print("\nThe history has been successfully cleared")
                elif self.option == '17':
                    print("Ok wait a moment...")
                    sleep(1.5)
                    print("Saving data...")
                    CalculatorHistory.write_data(self)
                    sleep(2)
                    print("Exiting...")
                    sleep(1.5)
                    break
                else:
                    print('\nInvalid choice')
            except OverflowError:
                print("\nError: Overflow")
calculator = CalculatorCLI(None, None, [], None, None)
calculator.ask_num()
calculator.display_menu()
        





            
