import requests
#!/usr/bin/env python

from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib

delivered_records = 0
url = "https://api.mockaroo.com/api/cbb61270?count=1000&key=5a40bdb0"


    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
def acked(err, msg):
    global delivered_records
    """Delivery report handler called on
    successful or failed delivery of message
    """
    if err is not None:
        print("Failed to deliver message: {}".format(err))
    else:
        delivered_records += 1
        print("Produced record to topic {} partition [{}] @ offset {}"
              .format(msg.topic(), msg.partition(), msg.offset()))

#get mockaroo data records
#make sure mockaroo schema is set to output array
def get_data():
    r = requests.get(url)
    return '{ "data": ' + str(r.text) + '}'

def main():
  # Read arguments and configurations and initialize
  args = ccloud_lib.parse_args()
  config_file = args.config_file
  topic = args.topic
  conf = ccloud_lib.read_ccloud_config(config_file)

  # Create Producer instance
  producer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
  producer = Producer(producer_conf)

  # Create topic if needed
  ccloud_lib.create_topic(conf, topic)

  print("hello world")
  d = get_data()
  djson = json.loads(d)
  darray = djson['data']

  for item in darray:
    record_key = str(item['_id'])
    record_value = json.dumps(item)
    print(record_value)
    producer.produce(topic, key=record_key, value=record_value, on_delivery=acked)
    producer.poll(0)

  producer.flush()

  print("{} messages were produced to topic {}!".format(delivered_records, topic))


if __name__ == '__main__':
  main()


# to run program
# python user_purchases_to_kafka.py -f ~/.confluent/python.config -t user_purchases
# python user_activity_to_kafka.py -f ~/.confluent/python.config -t user_activity
