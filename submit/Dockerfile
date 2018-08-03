FROM bde2020/spark-base:2.3.1-hadoop2.7

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 17077
ENV SPARK_APPLICATION_PYTHON_LOCATION /app/main.py

COPY app /app
COPY run.sh /

COPY .hdfscli.cfg /root

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

CMD ["/bin/bash", "/run.sh"]