1.Codebase
One codebase tracked in revision control, many deploys.
⁃	I used GitHub for source control.

2.Dependencies
Explicitly declare and isolate dependencies.
⁃	The dependancies of prod microservice are explicitly declared in requirements.txt

4.Backing services
Treat backing services as attached resources.
⁃	the fact, that the application is managed using docker container ensures Backing services. It is a isolated service which is a part of the application. And its accessible via url. 

6.Processes 
Execute the app as one or more stateless processes.
⁃	The micro service is stateless, the only persistent element is the database. 

7.Port binding
Export services via port binding.
⁃	With the docker compose we expose each service to the designated port via HTTP.

8.Concurrency
Scale out via the process model.
⁃	We treat each part of the application as a process, so that allows the scalability.

I did not implement all 8 requirements, but I would implement following two: 

3.Config
Store config in the environment
⁃	Explicitly declare the database credentials and API routs in globally accessible environment file. 

11.Logs
Treat logs as event streams
⁃	I would implement the logs by recording all the operations in the application and stream them to a centralised source. 

