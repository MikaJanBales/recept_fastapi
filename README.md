## Instructions for installing and running the application:

### 1 Method:

1) Up docker, thereby creating a local database, download all dependencies and run the application using the command:

```
docker-compose up
```

2) Go to  http://127.0.0.1:8000/

### 2 Method:

1) Download all the libraries and packages with the required versions required for the project using the command:

```
pip install -r requirements.txt
```

2) We start docker, thereby creating a local database using the command:

```
docker-compose up -d db
```

3) Run the application locally using the command:

```
uvicorn main:app --host localhost --port 8000
```
