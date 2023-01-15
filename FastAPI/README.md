* # FastAPI
### 1. we need to create virtual environments:
#### Command: 	`python -m venv env_name`
### 2. activaite enviroment: 
#### Command:  window: `Source\Scripts\activate.bat` , bash: `Source/bin/activate`
### 3. install fastAPI  & uvicorn:
#### Command: `pip install fastAPI & uvicorn[standart]`
### 4. Create file main.py
### 5. start live server: 
#### Command: `uvicorn main:app --reload` 
- #####  NOTE: reload: make server restart after code changes.<br /><br />

## In FastAPI there are various Operations:
#### 1. POST: to create Data.
#### 2. GET: to read Data.
#### 3. PUT: to update Data.
#### 4. DELETE: to delete Data. <br /><br />

* ### Simplest FastAPI file:
![image](/FastAPI/images/Screenshot_20230115_031850.png) <br /><br />
* ### After running the live server:
![image](/FastAPI/images/Screenshot_20230115_032329.png)

* ### We will get in the output:
![image](/FastAPI/images/Screenshot_20230115_032512.png)

* ### Open a browser at: http://127.0.0.1:8000  <br /><br />

* ### We will see the JSON response as:
![image](/FastAPI/images/Screenshot_20230115_032519.png)<br /> <br />
+ ### to see the automatic interactive API documentation (provided by Swagger UI):
    ### we need to go at: http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redocs
![image](/FastAPI/images/Screenshot_20230115_033432.png)