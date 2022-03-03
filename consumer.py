# ![ndsa_0401.png](attachment:ndsa_0401.png)

from kafka import KafkaConsumer
consumer = KafkaConsumer('Sample')
for message in consumer:
    print(message)


