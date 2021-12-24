import tarantool
import pandas as pd
from clickhouse_driver import Client
from json import dumps, loads
from kafka import KafkaProducer

connection = tarantool.connect("localhost", 3301, user='admin', password='pass')

tarantoolDB = connection.space('userlog')

data = tarantoolDB.select()

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for row in data:
    res = {'Day': str(row[0]), 'TickTime': str(row[1]), 'Speed': str(row[2])}
    producer.send('v8', value=res)
    print("KAFKA: Just published  to topic v8:", res)
