from producer import Producer
import csv
import json
from os import listdir, system
from os.path import isfile, join
from datetime import datetime

class Generator():
    def __init__(self, path, delimiter, stream_name):
        self.paths = self.get_paths(path)
        self.delimiter = delimiter
        self.stream_name = stream_name
        self.producer = Producer(self.stream_name)
        self.start_time = datetime.now()
        self.process_csv()

    def get_paths(self, path):
        def prepend_array(path, entity):
            return("{}{}".format(entity, path))


        csv_files = []
        if path[-1] == "/":
            initial_path = path
            csv_files = [f for f in listdir(path) if f.split('.')[-1] == 'csv' and isfile(join(path, f))]
            csv_files = map(prepend_array, csv_files, [path] * len(csv_files))
        elif path[-1] == "*":
            path = path[:-1]
            prefix = path.split('/')[-1]
            initial_path = "{}/".format('/'.join(path.split('/')[:-1]))
            csv_files = [f for f in listdir(initial_path) if f.split('.')[-1] == 'csv' and f[:len(prefix)] == prefix and isfile(join(initial_path, f))]
            csv_files = map(prepend_array, csv_files, [initial_path] * len(csv_files))
        elif len(path.split(',')) > 1:
            csv_files = path.split(',')
            csv_files = map(lambda f: f.strip(), csv_files)
        else:
            csv_files.append(path)
        return csv_files


    def process_csv(self):
        clear = lambda: system('clear')
        clear()
        for path in self.paths:
            total_rows = sum(1 for _ in open(path))
            with open(path, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=self.delimiter)
                msg = []
                x = 0
                for row in csv_reader:
                    x+=1
                    doc = {}
                    for key, value in row.items():
                        doc[key] = value
                    msg.append(doc)
                    if x % 1000 == 0:
                        print('{}: {} of {} elapsed: {}'.format(path, str(x), total_rows, datetime.now() - self.start_time), end='\r', flush=True)
                        self.producer.produce(json.dumps(msg).encode('ascii'))
                        msg = []
                print('{}: {} of {} elapsed: {}'.format(path, str(x), total_rows, datetime.now() - self.start_time), end='\r', flush=True)
                self.producer.produce(json.dumps(msg).encode('ascii'))
            print('')


if __name__ == "__main__":
    # generator = Generator('./raw_data/AIRPORT_COORDINATES.csv', ',', 'blog_airport_coordinates')
    generator = Generator('./raw_data/AIRPORT_COORDINATES.csv', ',', 'blog_airport_coordinates')
