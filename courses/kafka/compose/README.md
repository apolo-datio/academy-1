#Hadoop 2.7.1 + Kafka 0.10 + zookeeper 3.4.6 + Mongodb (latest) Docker

Docker compose file to manage kafka, hadoop and zookeeper together in the template project <br/>
###### image sources: ######
hadoop : sequenceiq <br/>
kafka : wurstmeister <br/>
zookeeper : wurstmeister <br/>
mongodb : mongodb <br/>
# Pre-requisites
- install docker [https://docs.docker.com/engine/installation/](https://docs.docker.com/engine/installation/)
- install docker-compose [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)
- install mongodb client: sudo apt-get install mongodb-clients
- modify the ```KAFKA_ADVERTISED_HOST_NAME``` in ```docker-compose.yml``` to match your docker host IP
(Note: Do not use localhost or 127.0.0.1 as the host ip if you want to run multiple brokers.). By default there are two
options depending on the os (ubuntu or mac os x)
- if you want to customise any Kafka parameters, simply add them as environment variables in ```docker-compose.yml```, e.g. in order to increase the ```message.max.bytes``` parameter set the environment to ```KAFKA_MESSAGE_MAX_BYTES: 2000000```. To turn off automatic topic creation set ```KAFKA_AUTO_CREATE_TOPICS_ENABLE: 'false'```

# Usage
 Start a cluster:
 ```
 docker-compose up
 ```
 Check a cluster:
  ```
  docker-compose ps
  ```
 Destroy a cluster:
 ```
 docker-compose down
 ```
##Zookeeper
To access to the zookeeper machine you must use the KAFKA_ADVERTISED_HOST_NAME as ip address and 2181 port
##Kafka
Kafka broker shouldn't be scaled because there is a port map fixed and there will be conflicts. To scale the broker
it's necessary to modify the docker-compose.yml at your own risk.
##Hadoop
The hadoop machine machine as the kafka broker, will be established with KAFKA_ADVERTISED_HOST_NAME ip
##Mongodb
Mongodb server will be available on 27017 port
