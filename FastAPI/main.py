import io 
import json
import pandas as pd 
from fastapi import FastAPI, File, Response,Path, HTTPException, Depends, status
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED


# add description to the app.
description = """ ## File types: csv, pdf, json, html ,image"""

# create a FastAPI "instance"
app = FastAPI(description=description)


''' Authentication types: '''

# 1. Basic Authentication:
security = HTTPBasic()



'''
This function gets the current username from a set of credentials. 
It takes in an HTTPBasicCredentials object as an argument and checks if the username and password match the correct ones. 
If they don't, an HTTPException is raised. Otherwise, it returns the username.
'''

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(status_code=400, detail="Incorrect login credentials")
    return credentials.username
    


'''
This function creates and uploads data of different file types. 
It takes in a file type (str) and file (bytes) as parameters, as well as credentials (HTTPBasicCredentials). 
Depending on the file type, it will create a response object with the appropriate content and media type. 
For PDF, JSON, HTML, and CSV files, it will return a Response object with the corresponding content and media type. 
For images, it will return a Response object with the image content and media type "image/jpeg".
'''

# a path operation decorator
@app.post("/uploadfile/{file_type}")

# a path opreation function
async def create_upload_data(file_type:str,file: bytes = File(...),
                              credentials: HTTPBasicCredentials = Depends(get_current_username)):
        
        if file_type == 'pdf':
            response = Response(content=file, media_type="application/pdf")
            response.headers["Content-Disposition"] = "attachment; filename=file.pdf"
            return response

        if file_type == 'json':
            json_file = json.loads(file)
            return JSONResponse(content=json_file)
        
        if file_type == 'html':
            return HTMLResponse(content=file, status_code=200)

        if file_type == 'csv':
            df = pd.read_csv(io.BytesIO(file))
            csv_str = df.to_csv(index=False)
            response = Response(content=csv_str, media_type="text/csv")
            return response
        
        if file_type == 'img':
            response = Response(content=file, media_type="image/jpeg")
            response.headers["Content-Disposition"] = "attachment; filename=file.jpg"
            return response






