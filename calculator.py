from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 

class Calculator(BaseModel):
    num1 : int | float
    num2 : int | float
    operation : str
    
list_of_operations = [] # To store the operations

# Perform the calculation

def perform_calculation(num1: int, num2: int, operation: str):
    try:
        if operation == "addition":
            result = num1 + num2
        elif operation == "modulus":
            result = num1 % num2
        elif operation == "power":
            result = num1 ** num2
        elif operation == "subtraction":
            result = num1 - num2
        elif operation == "multiplication":
            result = num1 * num2
        elif operation == "division":
        
            try:
                result = num1 / num2
            except ZeroDivisionError:
                return {
                    "error": "ZeroDivisionError",
                    "message": "Cannot divide by zero",
                    "num1": num1,
                    "num2": num2
                }
        else:
            return {"error": "Invalid operation"}

        return {
            "number_1": num1,
            "number_2": num2,
            "operation": operation,
            "result": result,
            "message": f"The {operation} between {num1} and {num2} is {result}"
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/calculator/")
def calculate(calc: Calculator):
    list_of_operations.append(calc.operation)
    return perform_calculation(calc.num1, calc.num2, calc.operation)

@app.get("/calculator/{num1}/{num2}/{operation}")
def result_calculate(num1: int, num2: int, operation: str):
    return perform_calculation(num1, num2, operation)
