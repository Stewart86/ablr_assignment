# ABLR Assignment (MyInfo Data Retriever)

## Flow:
1. User click Frontend button for Retrieve MyInfo 
2. button href to django backend `/api/myinfo/login`
3. django backend `/api/myinfo/login` endpoint provide MyInfo auth url
4. frontend redirect user to MyInfo auth url for user auth and callback 
5. callback received from frontend at `/callback with auth code provided from MyInfo API
6. frontend call `/api/myinfo/retrieve` with auth code
6. backend received auth code and decrypt with private key and return data 
7. frontend received user info and display

### Tests

for MyInfo Endpoints tests run this command from root folder

```bash
python ablr/manage.py test myinfo        
```

### Frontend Endpoints
- `/`
    - home page with a retrieve MyInfo button
- `/callback`
    - for recieving callback from MyInfo authorised request

### Backend Endpoints
- `/myinfo/login`
    - return MyInfo url for redirect and callback
- `/myinfo/retriever`
    - return personal data
