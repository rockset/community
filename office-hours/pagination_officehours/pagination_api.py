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
        self.pagination = True
        self.workspace = workspace
        self.queryLambda = queryLambda
        self.tag = tag
        self.version = version
        self.finalUrl = ""
        self.parameters = parameters
        self.run()

    def run(self):
        self.start_time = datetime.utcnow()
        payload = {}
        payload['paginate'] = self.pagination
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
            # result = self.result['results']
            if self.pagination:
                # print(json.dumps(self.result, indent=4))
                self.totalResults = self.result['results_total_doc_count']
                current_doc_count = self.result['pagination']['current_page_doc_count']
                print(f'Total doc count: {self.totalResults}, current_doc_count: {current_doc_count} time: {self.elapsed_time}')
                self.iterate_query(self.result['query_id'], self.result['pagination']['next_cursor'])
            else:
                print(f'Time: {self.elapsed_time}')
            total_time = datetime.utcnow() - self.start_time
            print("Version: {}, Total Time: {}".format(version, total_time))

    def iterate_query(self, query_id, next_cursor):
        s_time = datetime.utcnow()
        url = "{}/v1/orgs/self/queries/{}/pages/{}?docs={}".format(self.apiServer, query_id, next_cursor, self.initialLimit)
        g = requests.get(url,
                        headers=self.headers)
        if g.status_code != 200:
          print(f'Failed to execute query. Code: {g.status_code}. {g.reason}. {g.text}')
          sys.exit(0)
        self.result = g.json()
        if 'next_cursor' not in self.result['pagination'] or self.result['pagination']['next_cursor'] == None:
            print("Total Time: {}".format(datetime.utcnow() - self.start_time))
        else:
            current_doc_count = self.result['pagination']['current_page_doc_count']
            e_time = datetime.utcnow() - s_time
            print(f'current_doc_count: {current_doc_count} time: {e_time}')
            self.iterate_query(query_id, self.result['pagination']['next_cursor'])


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
    processor = Processor('officehours-pagination', 'pagination_api', 'latest', None, parameters, 50000)
