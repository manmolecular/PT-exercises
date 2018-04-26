# Structure

```
PT-exercises/src
│   __init__.py
│   get_config.py
│   get_db.py
│   main.py
|   transports.py
|
└─── configs
│   │   config.json
│   │   controls.json
|   |   ...
│   
└─── scripts
|   │   __init__.py
|   │   mdl.py
|   |   ...
|
└─── tests
    │   __init__.py
    │   test.py
    |   ...
```

### Main code:  
- `src/get_config.py` - *Parsing of json configuration file*
- `src/get_db.py` - *Parsing of json configuration file for db*
- `src/main.py` - *Main module*
- `src/transports.py` - *SSH transport class*
- `src/configs/` - *Json configs files*
- `src/scripts/` - *Directory for importing libs*
- `src/tests/` - *Pytest tests*
### Other:  
- `img-ubuntu-python` - docker with ubuntu and python3  
- `img-ubuntu-sshd` - docker with ubuntu and sshd  
# Build containers
For python:  
```
cd ./img-ubuntu-python/ && docker build . -t img-ubuntu-python
```
For sshd:
```
cd ./img-ubuntu-sshd/ && docker build . -t img-ubuntu-sshd
```
# Run & connect SSH
Run:
```
docker run -d -p 22022:22 --name cont-ubuntu-sshd img-ubuntu-sshd 
# password: pwd (change it if you want)
```
Connect:
```
ssh root@localhost -p 22022
# password: pwd
```
# Paramiko
```
sudo pip3 install paramiko
```
# Pytest
```
pytest main-project/unit_test.py
```
