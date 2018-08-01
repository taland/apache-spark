FROM bde2020/spark-base:2.3.1-hadoop2.7

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 17077
ENV SPARK_APPLICATION_PYTHON_LOCATION /app/main.py

COPY app /app
COPY run.sh /

COPY .hdfscli.cfg /root

RUN pip3 install hdfs

CMD ["/bin/bash", "/run.sh"]