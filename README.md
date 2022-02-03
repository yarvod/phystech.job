## Some basic commands to work with docker

###  Start app with docker-compose

~~~shell
docker compose -f docker-compose.yaml up -d
~~~

### Show all containers

~~~shell
docker ps -a
~~~

### Show running containers

~~~shell
docker ps
~~~

### Stop all docker containers

~~~shell
docker stop $(docker ps -q)
~~~

### Delete all containers

~~~shell
docker rm $(docker ps -q -a)
~~~

_PS:_ <p>
_Please, don't run django, vue client outside containers_