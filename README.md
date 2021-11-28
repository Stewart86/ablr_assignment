# ABLR Assignment (MyInfo Data Retriever)

## Setup and Installation

### Running Requirements
1. Python 3.10
2. Poetry `pip install poetry`
3. Install Packages `poetry install`

### Developement Requirements (including running requirements)
1. Node > 14.17.0 < 17.1.0
2. npm >= 8.1.2

### Run local server
Make sure python and poetry is installed.

**NOTE:** port is important here as MyInfo test server only allow this port for callback

Within `poetry shell`

```bash
python ablr/manage.py runserver 127.0.0.1:3001
```

or


Without `poetry shell`
```bash
poetry run ablr/manage.py runserver 127.0.0.1:3001
```

## Flow:
1. User click Frontend button for Retrieve MyInfo 
2. button href to django backend `/api/myinfo/login`
3. django backend `/api/myinfo/login` endpoint provide MyInfo auth url
4. frontend redirect user to MyInfo auth url for user auth and callback 
5. callback received from frontend at `/callback with auth code provided from MyInfo API
6. frontend call `/api/myinfo/retrieve` with auth code
6. backend received auth code and decrypt with private key and return data 
7. frontend received user info and display
8. continue button within the details page provide an access back to home (`/`)

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
