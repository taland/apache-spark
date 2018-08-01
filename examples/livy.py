"""
https://github.com/cloudera/livy
http://gethue.com/how-to-use-the-livy-spark-rest-job-server-api-for-submitting-batch-jar-python-and-streaming-spark-jobs/
"""

import requests
import json, pprint

host = 'http://localhost:8998'

data = {
    "file": "hdfs://namenode:8020/user/root/main.py",
    "args": [
        "hdfs://namenode:8020/user/root/kw.txt"
    ],
}
headers = {'Content-Type': 'application/json'}


r = requests.post(host + '/batches', data=json.dumps(data), headers=headers)
res = r.json()
pprint.pprint(r.json())

r = requests.get(host + '/batches/' + str(res['id']), headers=headers)
pprint.pprint(r.json())
