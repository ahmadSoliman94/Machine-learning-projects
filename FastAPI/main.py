from fastapi import FastAPI, File, Response,Path
from fastapi.responses import JSONResponse, HTMLResponse
import json
import pandas as pd 

description = """ ## File types: csv, pdf, json, html ,image"""
app = FastAPI(description=description)

@app.post("/uploadfile/{file_type}")
async def create_upload_data(file_type:str = Path(title='file types: pdf,json,img,html,csv'),file: bytes = File(...)):
    
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
        df = pd.read_csv(file.file)
        csv_str = df.to_csv(index=False)
        response = Response(content=csv_str, media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=file.csv"
        return response
    
    if file_type == 'img':
        response = Response(content=file, media_type="image/jpeg")
        response.headers["Content-Disposition"] = "attachment; filename=file.jpg"
        return response


