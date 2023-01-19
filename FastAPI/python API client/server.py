
import uvicorn
from fastapi import FastAPI, File, UploadFile

'''
This code creates a FastAPI server and sets up an endpoint for uploading files. 
The endpoint takes in a file as an argument, and writes the file to a file called "responded_data.pdf". 
Finally, the server is run using uvicorn on port 8000.
'''

app = FastAPI()

@app.post("/upload")
async def upload(file: bytes = File(...)):
    with open("./responded_data.pdf", "wb") as f:
        f.write(file)
    

    
if __name__ == '__main__':
    uvicorn.run("server:app", host='0.0.0.0', port=8000, reload=False)








