#Tri-Tier Web Application#

Project Overview:

- This is a Web Application, frontend created in Nginx and Backend created in python Flask. Currently database setup is pending.

- Both application are using the lighter base images for containerization.

- currently frontend is just having a static web page, I will improve it as the time progresses

- Backend's business logic revolves around returning the json data.



phase 1: Environment Provisioning:

- I have created a automation script where it will check if the folder name that we are passing while running the automation script exists or not and in both the cases, it will create three files inside it named as : app.log, web.log and db.log
- to run the shell script, run the following command : 

```

./setup.sh folder_name1 folder_name2 folder_name3

```

Phase 2: The Build Phase (Containerization):

The Frontend: 

- Frontend is built with the Nginx alpine image, which is very lightweight and builds faster.

- To build the docker image, run 

```

docker build -t my-frontend . 

```

command and to run it, run 

```

docker run -d -p 8080:80 --name my-web my-frontend 

```



The Backend: 

- Backend is built with the python slim image, which is very lightweight and builds faster.

- To build the docker image, run 

```

docker build -t my-backend . 

```

command and to run it, run 

```

docker run -d -p 5000:5000 --name my-api my-backend

```

### Phase 3: Orchestration & Reverse Proxy

1. The Virtual Cable (Docker Networks):
Initially, the Nginx and Python containers were isolated and could not communicate. To fix the "Localhost Trap," I created a custom bridge network (docker network create tri-tier-net). By attaching both containers to this network, Docker's internal DNS allowed Nginx to securely route traffic to the Python API using only the container's name, without exposing the backend to the public internet.

2. The Traffic Cop (Nginx Reverse Proxy):
By default, Nginx only acts as a static file server. To make the application dynamic, I wrote a custom nginx.conf file to act as a Reverse Proxy.

Traffic hitting the root path (/) serves the static index.html.

Traffic hitting the /api/ endpoint is dynamically intercepted, the URL prefix is stripped, and the request is secretly routed across the Docker network to the Python backend.

3. The Deployment (Network Attachment):
To attach the containers to the network, the --network flag was introduced to the deployment commands:

```
docker run -d --name my-api --network tri-tier-net my-backend
docker run -d -p 8080:80 --name my-web --network tri-tier-net my-frontend
```
 
