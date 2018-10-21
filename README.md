# Ecila chatbot
Virtual assistant built with RASA IA as dockerized microservices

## How to run this ?
there is a docker compose file version 3 that works with docker swarm
EDIT: Traefik support added, you can still use the old docker compose for development purposes

Steps to generate the data:
- Navigate to main/data and download [mitie models](https://github.com/mit-nlp/MITIE/releases/download/v0.4/MITIE-models-v0.2.tar.bz2)
- We only need the total_word_feature_extractor.dat to be in data/mitie
- Now you need to train the model using `python nlu_model.py train mitie`

Steps to run the application
- Using the data.env environment file tweak the variables to your needs (modify the ports in the docker compose file as well)
- Install docker-ce if it is not installed yet
- Initialize the docker swarm `docker swarm init`
- Start the docker stack `docker stack deploy --compose-file docker-compose.yml ecila` ecila is the name of the stack
- Make sure all services are up `docker service ls`
- visit the web.domain.com and test the bot
## Warning
This is an 8 hours project dont expect the finest project it is a POC, will rewrite and refactor it every once and while
## Note
This is very experimental project and it ll get updates every now and then.
I am using traefik to handle the routing between the microservices, as first usage I am using subdomains to serve frontends and thus, you ll need a FQDN which is wildcarded to the server ip so traefik will be able to read the subdomains. You can also use one subdomain and route throught pots but you will need to reconfigure traefik on your own.
The desired architecture is detailed in the following graph, open the readme is raw mode for a clear view

## Architecture
Precaution: will be outdated at some moments, not going to update this always, refer to the source code and the information already cited in the read me file.
```

                                                     +--------------------------------+
                                                     |                                |                                     +-----------------------------+
                                                     |  etc ...                       |                                     |                             |
                                                     |                                |                                     |   Task planner              |
                                                     |                                |                                     |   - Use google calendar     |
                                                     +--------^------+----------------+                                     |   - push notification       |
                                                              |      |                                                      |                             |
                                                              |      |                                                      +--------+------^-------------+
                                                              |      |                                                               |      |
   +-----------------------+                                  |      |                                                               |      |
   |                       |                       +----------+------v------------------------+                                      |      |
   | weather forecast      +----------------------->                                          <--------------------------------------+      |
   |                       |                       |      Chatbot main module                 |                                             |
   |                       <-----------------------+      - manage conversations              |                                             |
   +-----------------------+                       |      - call appropriate modules          |                                             |
                                                   |                                          +---------------------------------------------+
                                                   |                                          |
                                                   |                                          |
                                                   |                                          |
                                                   |                                          |
                                                   |                                          |
                                                   |                                          |
                                                   +---------------+-----^--------------------+
                                                                   |     |
                                                                   |     |
                                                                   |     |
                                                                   |     |
                                                                   |     |
                                                                   |     |
                                                                   |     |
                                                                   |     |
                                                         +---------v-----+----------------+
+----------------------------+                           |                                |                       +-----------------------------+
|                            |                           |   Communication access point   |                       |                             |
|                            <---------------------------+                                |                       |                             |
|                            |                           |                                +----------------------->                             |
|  Fb, slack, telegram etc...|                           |                                |                       |   web app interface         |
|                            +--------------------------->                                <------------------------+                            |
|                            |                           |                                |                       |                             |
+----------------------------+                           |                                |                       +-----------------------------+
                                                         |                                |
                                                         |                                |
                                                         +--------------------------------+
```
