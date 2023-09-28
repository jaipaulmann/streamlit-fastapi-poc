from fastapi import FastAPI
from pydantic import BaseModel
from streamlit_fastapi.calculator import calculate

# can modularize below function w/ following: from streamlit_fastapi.calculator import calculate
# def calculate(operation, x, y):
#     '''
#     operation - takes the string add, sub, mul, div
#     x & y - two numbers
#     '''

#     if operation == 'Addition':
#         return x + y
    
#     elif operation == 'Subtraction':
#         return x - y

#     elif operation == 'Multiplication':
#         return x * y
    
#     elif operation == 'Division':
#         return x/y
    

# pydantic base model
class UserInput(BaseModel):
    operation: str
    x: float
    y: float

app = FastAPI()

# define /calculate endpoint
    # handles a post request
    # expected input format of post request is defined by UserInput pydantic class
    # "input" is the name of the parameter, ":UserInput" is the expected type, could equivalently been input:str or input:float
    # since input is a class, I think we can access the attributes in the input.<attribute_name> way. if param name was response & response was a class object, we would do response.x for example

@app.post("/calculate")
def operate(input:UserInput):
    result = calculate(input.operation, input.x, input.y)
    return result

# test api
    # poetry run uvicorn streamlit_fastapi.fast_api:app
    # from pwd: /Users/jaipaulmann/Documents/projects/streamlit-fastapi-proj/streamlit-fastapi

