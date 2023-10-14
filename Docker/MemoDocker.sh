docker pull paperjam/alpinenode:1

# pour éviter de tapaer sudo à chaque commande docker
sudo usermod -aG docker your-user

docker login -u paperjam

#-- ===== memo Docker
image --> docker run --> container

# -- ======= USING A DOCKER FILE =============================================

# -----
FROM node:16-alpine     # image required
WORKDIR /app            # /app already exist in the image // all the following command will be run from this directory
COPY package.json .     # . -> /app # optimization
RUN npm install 
ARG NODE_ENV
RUN if [ "$NODE_ENV" = "development" ]; \
        then npm install; \
        else npm install --only=production; \
        fi

COPY . ./
# ENV PORT 3000
# EXPOSE $PORT # optionnel ou pas ?? -> oui : --env PORT=4000 suffit
CMD ["node", "index.js"]

# -----
docker build .                  # build image from the Dockerfile
docker build -t node-app-image  # permet de nommer l'image

# .dockerignore indique les fichiers à ignorer


# -- ======= IMAGES ===================================================
# les images officielles ont un nom simple
# les images non-officielles sot de la forme nomUser/nomImage
# une image est composée de couches

docker images                           # liste des images installées
docker image rm .. imageId              # remove image --force if containers relative are still present
docker inspect imageId                  # 
docker pull image_name:image_tag        #  download an image from repository

# full image name 
registry.example.port:port/organisation/image-name:version-tag

# docker run calls docker pull to get image from repo
docker rmi imageId    # remove images ?? 

docker historydocker history			# historique d'une image
docker tag <image> username/repository:tag  	# Tag <image> for upload to registry
docker push username/repository:tag            	# Upload tagged image to registry

#exit = ctrl + d
# -- ======= CONTAINERS

docker run -ti ubuntu:latest bash               # (ti : terminal interactive)
docker ps                                       #running images
docker ps --format $FORMAT                      #améliore l'affichage
docker ps -a                                    #all container
docker ps -l                                    #last container
docker run --rm  -ti ubuntu sleep 5             # remove container after exit
docker run -d -ti ubuntu bash           	# run detach mode
docker run -d --name node-app  node-app-image 	# give a name to the container 
docker attach containerNameOrId
ctrl-p + ctrl-q                         #leaving cont. without stopping it

ctrl p + q                  # sort de conteneur, mais il reste actif
docker attach 2dafdf702d9d  # permet de retourner dans le conteneur
exit                        # sortie et fermeture du conteneur






# run
docker exec -it id_container bash   			#lance bash dans container running in interactive mode
docker commit imageID
docker tag containerID   imageName
docker tag containerName imageName

# while running 
docker inspect containerNameOrId

# commit
docker commit <IdContainerExited> nemNewImage

# stop - rm
docker rm tutonodedockerdevops-node-app-1 -f -v # stop if active, then remov container and volume

# push 
docker image push registry-host:5000/myadmin/rhel-httpd:latest

docker stop containerNameOrId             # stop a container
docker logs containerNameOrId             #display logs  from a container
docker kill containerNameOrId             #kill a container
docker rm   containerNameOrId -f          #remove a container -f force : even if container is still running
docker run --cpu-shares  imageName
docker run --cpu-quota   imageName


# rereun exited container, kkeping changes 
        # --quiet  Only display container IDs 
        # --laster Show the latest created container
docker ps --quiet --latest     
docker start  `docker ps -q -l` # restart it in the background    
docker attach `docker ps -q -l` # reattach the terminal & stdin

# connexion Windows terminal / hdocker image  
docker start --attach -i elastic_goldstine 



#-- 2- exposing port
#-- affectation statique des ports
docker run --rm -ti -p 45678:45678 -p 45679:45679 --name echo-server unbuntu bash
# -p portOutsideContainer:portInsideContainer and the check from browse with localhost:portOutsideContainer

# -- possibilité d'utiliser NETCAT pour diagnostiquer
nc -lp 45678 | nc -lp 45679

#-- affectation automatique des ports
docker run --rm -ti -p 45678 -p 45679 --name echo-server ubuntu:14.04 bash
docker port ContainerNameOrId          # permet de voir les ports dynamiques

#-- exposing UDP port 
docker run --rm -ti -p 45678/udp --name echo-server ubuntu:14.04 bash

#-- ================  Container networking ==================

# network list
docker network ls                                   
- bridge : by default
- host   : full open (-> security concerns)
- none   : no networking

# create a network 
docker network create learning                      

# create 2 servers machine on this network, able to communicate
docker run --rm -ti --net learning --name catserver ubuntu:14.04 bash
docker run --rm -ti --net learning --name catdog ubuntu:14.04 bash

# create another network and connect catserver to it
docker network create catsonly
docker network connect catsonly catserver

# -- Legacy Linking : links all ports, though only in one way


# -- Sharing data -> Volumes Persistent or Ephemeral => local to disk host

# sharing a folder
docker run -ti -v /home/francis/docker/exo:/shared-folder ubuntu bash

# -- ============== volumes
# -- les différents type de volumes 
#  - bind mount : path on local machine <-> path on server
#  - anonymous : only a path to the container
#  - name volumes : name:path to the container
docker volume ls 
docker volume rm volumeName
docker rm nomContainer -fv  # delete container AND volume
docker volume prune 		# cleaning unvolumes
docker run -v pathToFolderOnLocal:pathToFolderOnContainer -d ...

# -- ======= SWARM
docker stack ls                                            # List stacks or apps
docker stack deploy -c <composefile> <appname>  # Run the specified Compose file
docker service ls                 # List running services associated with an app
docker service ps <service>                  # List tasks associated with an app
docker inspect <task or container>                   # Inspect task or container
docker container ls -q                                      # List container IDs
docker stack rm <appname>                             # Tear down an application
docker swarm leave --force      # Take down a single node swarm from the manager


# -- ============== docker compose ====================== 

# https://docs.docker.com/compose/compose-file/compose-versioning/
docker-compose build            # construction des images
docker-compose up 		# construction pui run
docker-compose up -d            # idem + garde le conteneur actif (d pour detach)
docker-compose up -build	# idem + force rebuid
docker-compose ps               # état des services
docker-compose start            # démare les conteneurs du service
docker-compose stop             # stop les conteneurs du service
docker-compose rm               # supprime les services
docker-compose down -v 		# remove volumes

docker-compose scale SERVICE=3    # lance 3 instances
docker-compose pull               # mise à jour des images



# -- ====== Dockerfile
docker build -t node-app-image .    # -t <nomImage> pour donner un nom à l'image


# ne plus mettre le flag -v, sinon quoi le volume est supprimé
docker-compose -f docker-compose.yml -f docker-compose.dev.yml down


# -- logs 
docker logs idNameContainer  -f     # follow log output

# -- network                       
docker network ls       # ridge and host are default network
docker network inspect networkName


container                       network                             @ IP    
tutonodedockerdevops-mongo-1    tutonodedockerdevops_default        172.21.0.2
tutonodedockerdevops-mongo-1    tutonodedockerdevops_default        172.21.0.2



-- ======= liste des commandes pour le tuto ===================
docker run -v C:\dev\tests\tutoNodeDockerDevops\:/app -p 3000:3000 -d --name node-app node-app-image
docker run -v %cd%:/app -p 3000:3000 -d --name node-app node-app-image # on windows terminal
docker run -v ${pwd}%:/app -p 3000:3000 -d --name node-app node-app-image # on windows powershell
docker run -v $(pwd)%:/app -p 3000:3000 -d --name node-app node-app-image # on mac or linux
docker rm node-app -f  # remove container -f force 
docker run -v %cd%:/app -v /app/node_modules -p 3000:3000 -d --name node-app node-app-image

docker run -v %cd%:/app:ro -v /app/node_modules -p 3000:3000 -d --name node-app node-app-image #in RO mode
docker run -v %cd%:/app:ro -v /app/node_modules -p 3000:4000 --env PORT=4000 -d --name node-app node-app-image # add ENV var
docker run -v %cd%:/app:ro -v /app/node_modules -p 3000:4000 --env-file ./env -d --name node-app node-app-image # add ENV file

# -- ========= DOCKER-COMPOSE ===================
docker-compose up -d 
docker-compose down -v          # remove volume
docker-compose up -d --build    # rebuild image 

# attention : l'ordre des options en -f a une importance, start build, remove
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d 
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build
docker-compose -f docker-compose.yml -f docker-compose.dev.yml down -v

# using named volumes for mongo -> remove the -v flag as downing the container
docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

# astuce : permet de reprndre en compte des modifs sur docker-compose.yml
# sans avoir à arrêter et relancer les containers actifs
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

# starting only node, not mongo 
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --no-deps node-app

# logs 
docker logs tutonodedockerdevops-node-app-1  -f 



# -- ====== Mongodb
mongo -u "bob" -p "pass"
db.auth("bob", "pass")
docker exec -it tutonodedockerdevops-node-app-1 ash
docker exec -it tutonodedockerdevops-mongo-1 bash
docker exec -it tutonodedockerdevops-mongo-1 mongo -u "bob" -p "pass"
db.books.insert({"name":"harry potter"})
db.books.find()


// reprendre  : 03:21:27
// il semblerait que secret sot deprecated



-- étudier la possibilité de synchroniser le démarrage des applications
-- pour éviter de faire une boucle d'attente pou la connexion mongo
