# import libraries 
from fastapi import FastAPI

# create a FastAPI instance
app = FastAPI() 

# define a path operation decorator
@app.get("/")

# define the path operation function
async def root():

    #  return the content
    return {"message": "Hello World"}

# Command: (uvicorn main:app --reload) to run the server. 
# pip install "uvicorn[standard]"
# pip install fastapi
