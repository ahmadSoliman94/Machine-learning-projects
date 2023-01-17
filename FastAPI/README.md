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
![image](/FastAPI/images/Screenshot_20230115_033432.png)  <br /><br />

+  ## **FastAPI Authentication**:

1. #### **Basic Authentication**: This is a simple authentication scheme that involves sending a user's credentials (username and password) in the request headers. It can be implemented using the *`HTTPAuthorization`*  middleware from the *`fastapi.security`* module.
2. #### **OAuth2 Authentication:**: This is a more complex authentication scheme that involves obtaining an access token from an OAuth2 provider, such as Google or Facebook, and sending it in the request headers. You can use a library like *`Authlib`* to implement OAuth2 authentication in your FastAPI app.


3. #### **JWT (JSON Web Token) Authentication**: This is a popular authentication scheme that involves sending a JSON Web Token (JWT) in the request headers. The token contains claims about the identity of the authenticated user and can be verified using a secret key. You can use a library like *`fastapi_jwt_auth`* to implement JWT authentication in your FastAPI app.

4. #### **Session-based Authentication**: This is a traditional authentication scheme that uses cookies to store a session ID on the client and a session object on the server. The session object contains information about the authenticated user. You can use a library like *`FastAPI-Session`* to implement session-based authentication in your FastAPI app.

5. #### **API Key Authentication**: this is a simple authentication scheme that involves sending an api key in the request headers or query params. You can create your own authentication method to check for the key or use a library like *`fastapi-apikey`*.
<br /><br />

* ##  **Limitations of the authentication types**:
1. #### **Basic Authentication**: is a simple scheme that sends user credentials in plain text.  Additionally, it requires the storage of user's plaintext password which is not secure.
2. #### **OAuth2 Authentication**: can be complex to set up and maintain. It also requires that users have accounts with the OAuth2 provider, which can be a limitation if you want to allow users to create accounts within your app.
 3. #### **JWT (JSON Web Token) Authentication**: carry all the information needed to authenticate a user. This can make them large and unwieldy, and it also means that any information stored in a JWT is visible to anyone who can access the token. 
 4. #### **Session-based Authentication**: relies on the server to store  information. This can be a limitation if you want to scale your app to multiple servers, as you will need to implement a way to share session data across servers. Additionally, cookies can be vulnerable to hack attacks if not properly secured.
5. #### **API Key Authentication**: can be less secure than other methods because the key is typically a simple string and can be easily guessed or stolen if not properly secured. Additionally, it can be difficult to track and revoke specific keys, making it difficult to block access if a key is compromised.</b> </b>

* ##  **Dependency Injection**: 
### means, that there is a way for the path operation functions to declare things that it requires to work and use: "dependencies". And then FastAPI will take care of doing whatever is needed to provide the path operation function with those needed dependencies ("inject" the dependencies).
