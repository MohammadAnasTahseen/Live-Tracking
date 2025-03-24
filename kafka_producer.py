import json
import time
from confluent_kafka import Producer
import os
conf={'bootstrap.servers':'localhost:9092'}
p=Producer(**conf)




start_latitude = 19.0760
starting_longitude = 72.8777
end_latitude = 18.5204
end_longitude = 73.8567

num_steps = 1000


step_size_lat = (end_latitude - start_latitude) / num_steps
step_size_lon = (end_longitude - starting_longitude) / num_steps
current_steps = 0





def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

topic = 'location_updates'
while True:
    latitude = start_latitude + step_size_lat * current_steps
    longitude = starting_longitude + step_size_lon * current_steps

    data = {
    'latitude': latitude,
    'longitude': longitude
    }


    print("*********",data)


    p.produce(topic, json.dumps(data).encode('utf-8'),callback=delivery_report)
    p.flush()
    current_steps += 1
    if current_steps == num_steps:
        current_steps = 0

    time.sleep(2)

        




