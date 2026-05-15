# Docker Commands

## Build

<code>docker build -t username/repository:v1 .</code>

## Push Changes to Hub

**Requires login access**

<code>docker push username/repository:v1</code>

## Pull Changes from Hub

**Doesn't require login access**

* Latest Change: <code>docker pull username/repository</code>
* Specific Change: <code>docker pull username/repository:v1</code>

## Create and Run Container for the Frst Time

* Container with Latest Image: <code>docker run --name container-latest username/repository</code>
* Container with Specific Image: <code>docker run --name container-v1 username/repository:v1</code>

## Run Container After the First Time

<code>docker start container</code>

## Stop Container

<code>docker stop container</code>

## Push New Changes to Latest Version

**Require login access**

<pre>
docker build -t username/repository .
docker push username/repository
</pre>

## Push New Changes to Specific Version

**Require login access**

<pre>
docker build -t username/repository:v2 .
docker push username/repository:v2
</pre>

## Clean Up Containers and Images

* Remove dangling images (with <code>none</code> tag): <code>docker image prune</code>
* Remove previous versions of the same container: <code>docker compose up --remove-orphans</code>

## Manage Multiple Containers with Docker Compose

**Each service manages a container.**

* Build new image aka push new change: <code>docker compose build</code>
* Create all containers: <code>docker compose up</code>
* Rebuild image and create/start all containers: <code>docker compose up --build</code>
* **Require login access** Push all images: <code>docker compose push</code>
* **Require login access** Push all images from specific service: <code>docker compose push service</code>
* Pull all images: <code>docker compose pull</code>
* Pull all images from specific service: <code>docker compose pull service</code>
* Removes all containers, volumes, and images: <code>docker compose down -v --rmi all</code>
* Stop/Pause all containers: <code>docker compose stop</code>
* Start/Resume all containers: <code>docker compose start</code>
