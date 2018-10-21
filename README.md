# Ecila chatbot
Virtual assistant built with RASA IA as dockerized microservices

## How to run this ?
there is a docker compose file version 3 that works with docker swarm

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
- visit the domain.com:WEB_PORT and test the bot
## Note
This is very experimental project and it ll get updates every now and then
The desired architecture is detailed in the following graph, open the readme is raw mode for a clear view
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
