# Kafka
## What is Kafka?
Kafka is a distributed publish-subscribe messaging system that maintains feeds of messages in partitioned and replicated topics. In the simplest way there are three players in the Kafka ecosystem: producers, topics (run by brokers) and consumers.
### Producers- 
produce messagesto a topic of their choice. It is possible to attach a key to each message, in which case the producer guarantees that all messages with the same key will arrive to the same partition.
### Topics-
are logs that receive data from the producers and store them across their partitions. Producers always write new messages at the end of the log. In our example we can make abstraction of the partitions, since we’re working locally.
### Consumers-
read the messages of a set of partitions of a topic of their choice at their own pace. If the consumer is part of a consumer group, i.e. a group of consumers subscribed to the same topic, they can commit their offset. This can be important if you want to consume a topic in parallel with different consumers.
![image](https://user-images.githubusercontent.com/70899814/156561339-14119d48-2e79-4152-82a1-6659215b5401.png)
