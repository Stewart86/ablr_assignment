# ABLR Assignment (MyInfo Data Retriever)

## Todos:
1. Setup Python Project with Git and Django
2. Setup React.js Project 

## Authentication Flow:
1. User click Frontend button for Retrieve MyInfo 
2. button href to django backend `/myinfo`
3. django backend `/myinfo` endpoint provide MyInfo url and decrypt url
4. frontend redirect user to url provided by backend to retrieve auth code
5. auth code received from MyInfo API and pass to backend for decrypt
6. backend received auth code and decrypt with MyInfo API and return data 
7. frontend received user info and display

### 


### Backend Endpoints
- `/myinfo/login`
    - return MyInfo url for redirect and callback
- `/myinfo/retriever`
    - return personal data
