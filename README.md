# Structure
`img-ubuntu-python` - docker with ubuntu and python3  
`img-ubuntu-sshd` - docker with ubuntu and sshd  
`project` - code  
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
