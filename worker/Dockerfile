FROM bde2020/spark-base:2.3.1-hadoop2.7

COPY worker.sh /

ENV SPARK_WORKER_WEBUI_PORT 18081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-master:17077"

RUN apt-get update && apt-get install gcc -y && \
   apt-get install zip  -y && \
   apt-get install make  -y && \
   apt-get install zlib1g-dev -y && \
   apt-get -y install build-essential python-dev python-setuptools python-pip python-smbus libncursesw5-dev libgdbm-dev libc6-dev zlib1g-dev libsqlite3-dev tk-dev libssl-dev openssl libffi-dev

RUN wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz && \
   tar -xvf Python-3.6.3.tgz && \
   cd Python-3.6.3 && \
   ./configure && \
   make && \
   make install

RUN python3.6 -m pip install --no-cache-dir findspark pyspark ipython hdfs pandas PyArrow>=0.8.0

EXPOSE 18081

CMD ["/bin/bash", "/worker.sh"]
