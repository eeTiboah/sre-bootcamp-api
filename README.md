# Student CRUD REST API

This is a simple crud rest api to go through the [SRE Bootcamp exercise](https://playbook.one2n.in/sre-bootcamp/sre-bootcamp-exercises)

# Architecture Diagram
![Student Crud API architecture diagram](docs/student_crud_api.png)

### API Setup

### Step 1: Create virtual environment and install packages
#### 1.1 Create python virtual environment
```
python -m venv venv
```
#### 1.3 Activate python virtual environment
```
source /venv/bin/activate
```
#### 1.4 Install python packages
```
pip install -r requirements.txt
```
### Step 2: Configure Environment Variables
Make a copy of `.env.example`. This newly created file should be `.env`
```
cp .env.example .env
```
#### 2.1 Fill out environment variables
```
DB_NAME=
DB_USER=
DB_PASSWORD=
```

## Running API locally
- Ensure the virtual environment is activated. If not see step 1.3
- Start server with using the code snippet below

```
uvicorn src.main:app --reload
```