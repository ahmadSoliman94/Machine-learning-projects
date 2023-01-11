# import libraries 
from fastapi import FastAPI

# create a FastAPI instance
app = FastAPI() 

''' Path Parameters '''
# # define a path operation decorator with path "parameters" or "variables"
# @app.get("/items/{item_id}")

# # define the path operation function
# async def read_item(item_id):

#     #  return the content
#     return {"item_id": item_id}

''' Path parameters with types '''

# app = FastAPI()

# @app.get("/")
# #async def read_root():
#     #return {"Hello": "World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int=5, q: str = 'hey'):
#     return {"item_id": item_id, "q": q}

''' Order matters '''

# Note: Because path operations are evaluated in order, 
# you need to make sure that the path for /users/me is declared before the one for /users/{user_id}.

# async def read_user_me():
#     return {"user_id": "the current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}


''' Predefined values '''

# Import Enum
from enum import Enum

from fastapi import FastAPI

# create sub-class
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")

# create a path parameter with a type annotation using the enum class 
async def get_model(model_name: ModelName):

    # Compare enumeration members
    if model_name is ModelName.alexnet:

        # to return enumeration members
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    # Compare enumeration members
    if model_name.value == "lenet":

        # to return enumeration members
        return {"model_name": model_name, "message": "LeCNN all the images"}

    # to return enumeration members
    return {"model_name": model_name, "message": "Have some residuals"}
