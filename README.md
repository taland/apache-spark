# Run all

```bash
docker-compose build
docker-compose up
```

# HDFS

```bash
$ hdfscli upload --alias=<...> -f /local/file.txt file.txt
```

```
$ hdfscli --alias=docker

Welcome to the interactive HDFS python shell.
The HDFS client is available as `CLIENT`.

>>> CLIENT
<InsecureClient(url='http://namenode:50070')>
>>> CLIENT.list("/")
['user']
>>> CLIENT.list("/user")
['root']
>>> CLIENT.list("/user/root")
['file.txt']
```

# Submit

```bash
PYSPARK_PYTHON=python3 /spark/bin/spark-submit --master spark://spark-master:17077 /app/main.py /spark/examples/src/main/resources/kv1.txt
```

# Livy

Start the job:

```bash
$ curl -X POST --data '{"file": "hdfs://namenode:8020/user/root/main.py"}' -H "Content-Type: application/json" localhost:8998/batches
{"id":0,"state":"running","log":[]}
```

We can check the status:

```bash
$ curl localhost:8998/batches/0
{"id":0,"state":"success","log":[]}
```

And the output by adding the /log suffix

```bash
$ curl localhost:8998/batches/0/log
```

# TODO

1. Build base image with Python3 and dependencies
