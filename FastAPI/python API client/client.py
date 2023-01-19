import requests


''' This code imports the requests library and creates a client. 
It then opens a PDF file from the specified path and sends it to the server using the client's post method. 
Then, it checks the response status code and prints out a message depending on whether or not the file was uploaded successfully.'''

# create a client
client = requests.Session()

# prepare the PDF file to be sent
file_data = open("./data.pdf", "rb")

# send the PDF file to the server
response = client.post("http://0.0.0.0:8000/upload", files={"file": file_data})

# check the response status code
if response.status_code == 200:
    print("File uploaded successfully")
else:
    print("Failed to upload file")