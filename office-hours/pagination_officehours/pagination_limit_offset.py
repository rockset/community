import os
import requests
import sys
from datetime import datetime
import json

class Processor():
    def __init__(self, workspace, queryLambda, tag=None, version=None, parameters = None, page_size=100):
        self.apiServer = os.getenv('ROCKSET_APISERVER')
        self.apiKey = os.getenv('ROCKSET_APIKEY')
        self.baseURL = self.apiServer + '/v1/orgs/self/ws'
        self.headers = {'Authorization': 'ApiKey ' + self.apiKey , 'Content-Type': 'application/json'}
        self.initialLimit = page_size
        self.workspace = workspace
        self.queryLambda = queryLambda
        self.tag = tag
        self.version = version
        self.finalUrl = ""
        self.parameters = parameters
        self.iteration = 0
        self.run()

    def run(self):
        self.start_time = datetime.utcnow()
        payload = {}
        payload['initial_paginate_response_doc_count'] = self.initialLimit
        payload['parameters'] = []
        payload['parameters'] = self.parameters
        self.finalUrl = self.buildURL()
        r = requests.post(self.finalUrl,
                            json=payload,
                            headers=self.headers)
        self.elapsed_time = datetime.utcnow() - self.start_time
        if r.status_code != 200:
          print(f'Failed to execute query. Code: {r.status_code}. {r.reason}. {r.text}')
          sys.exit(0)


        self.result = r.json()
        version = self.result['query_lambda_path'].split("::")[1]
        if 'query_errors' in self.result.keys():
            print('Error: {}'.format(self.result['query_errors'] ))
        else:
            current_doc_count = len(self.result['results'])
            print(f'current_doc_count: {current_doc_count} time: {self.elapsed_time}')
            if current_doc_count > 0:
                self.iterate_query()
            total_time = datetime.utcnow() - self.start_time
            print("Version: {}, Total Time: {}".format(version, total_time))

    def iterate_query(self):
        start_time = datetime.utcnow()
        self.iteration+=1
        self.parameters[2]['value'] = str(self.iteration * int(self.parameters[1]['value']))
        payload = {}
        payload['initial_paginate_response_doc_count'] = self.initialLimit
        payload['parameters'] = []
        payload['parameters'] = self.parameters
        r = requests.post(self.finalUrl,
                            json=payload,
                            headers=self.headers)
        self.elapsed_time = datetime.utcnow() - start_time
        if r.status_code != 200:
          print(f'Failed to execute query. Code: {r.status_code}. {r.reason}. {r.text}')
          sys.exit(0)

        self.result = r.json()
        version = self.result['query_lambda_path'].split("::")[1]
        if 'query_errors' in self.result.keys():
            print('Error: {}'.format(self.result['query_errors'] ))
        else:
            current_doc_count = len(self.result['results'])
            print(f'current_doc_count: {current_doc_count} time: {self.elapsed_time}')
            if current_doc_count > 0:
                self.iterate_query()


    def buildURL(self):
        if self.version != None:
            url = "{}/{}/lambdas/{}/versions/{}".format(self.baseURL,
                                                        self.workspace,
                                                        self.queryLambda,
                                                        self.version)
        elif self.tag != None:
            url = "{}/{}/lambdas/{}/tags/{}".format(self.baseURL,
                                                    self.workspace,
                                                    self.queryLambda,
                                                    self.tag)
        else:
            raise Exception
        return url

if __name__ == '__main__':
    parameters = []
    parameters.append({"name": "name","type": "string","value": "Diamond"})
    parameters.append({"name": "limit","type": "int","value": "50000"})
    parameters.append({"name": "offset","type": "int","value": "0"})
    processor = Processor('officehours-pagination', 'pagination_limit_offset', 'latest', None, parameters, None)
