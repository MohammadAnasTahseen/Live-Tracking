from django.core.management.base import BaseCommand
from confluent_kafka import Consumer,KafkaException,KafkaError

import json
from Home_app.models import DiverLocationUpdate 
import os
conf={'bootstrap.servers':'localhost:9092'}


class Command(BaseCommand):
    help = 'Kafka Consumer'

    def handle(self, *args, **options) -> str | None:
        conf={
            'bootstrap.servers':'localhost:9092',
            'group.id':'location_updates',
            'auto.offset.reset':'earliest'
              
              
              }
        c=Consumer(**conf)
        c.subscribe(['location_updates'])
        try:
            while True:
                msg=c.poll(timeout = 1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break
                data = json.loads(msg.value().decode('utf-8'))
                print("data recived from consumer",data)
                DiverLocationUpdate.objects.create(latitude=data['latitude'],longitude=data['longitude'])
        except KeyboardInterrupt:
            pass
        finally:
            c.close()

        # return super().handle(*args, **options)


# from django.core.management.base import BaseCommand
# from confluent_kafka import Consumer, KafkaException, KafkaError
# import json
# from Home_app.models import DiverLocationUpdate

# conf = {'bootstrap.servers': 'localhost:9092'}

# class Command(BaseCommand):
#     help = 'Kafka Consumer'

#     def handle(self, *args, **options):
#         conf = {
#             'bootstrap.servers': 'localhost:9092',
#             'group.id': 'location_updates',
#             'auto.offset.reset': 'earliest'
#         }
#         c = Consumer(**conf)
#         c.subscribe(['test'])
#         try:
#             while True:
#                 msg = c.poll(timeout=1.0)
#                 if msg is None:
#                     continue
#                 if msg.error():
#                     if msg.error().code() == KafkaError._PARTITION_EOF:
#                         continue
#                     else:
#                         print(msg.error())
#                         break
#                 data = json.loads(msg.value().decode('utf-8'))
#                 print("Data received from consumer", data)
#                 DiverLocationUpdate.objects.create(latitude=data['latitude'], longitude=data['longitude'])
#         except KeyboardInterrupt:
#             pass
#         finally:
#             c.close()

