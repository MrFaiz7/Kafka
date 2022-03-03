from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('Sample', b'Hello, World!')
producer.send('Sample', key=b'message-two', value=b'This is Kafka-Python')
producer.flush()


