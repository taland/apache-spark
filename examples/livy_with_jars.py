import requests
import json, pprint

host = 'http://localhost:8998'

data = {
    "file": "hdfs://namenode:8020/app/read_df_from_db.py",
    "conf": {
        "spark.jars.packages": "org.postgresql:postgresql:42.1.1",
        "spark.driver.extraClassPath": "file:///root/.ivy2/jars/org.postgresql_postgresql-42.1.1.jar",
    },
}
headers = {'Content-Type': 'application/json'}


r = requests.post(host + '/batches', data=json.dumps(data), headers=headers)
res = r.json()
pprint.pprint(r.json())
