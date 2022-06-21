import boto3
from botocore.config import Config
import base64

class Producer():
    def __init__(self, stream):
        self.stream_name = stream
        self.authenticate()

    def authenticate(self):
        self.session = boto3.Session()
        self.client = self.session.client('kinesis', config=Config(read_timeout=20,
                                                     max_pool_connections=5000,
                                                     retries={'max_attempts': 10}))
    def produce(self, message):
        result = self.client.put_record(StreamName=self.stream_name,
                                       Data=message,
                                       PartitionKey="0")


if __name__ == "__main__":
    producer = Producer('blog_airport_coordinates')
