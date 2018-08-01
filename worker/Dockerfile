FROM bde2020/spark-base:2.3.1-hadoop2.7

COPY worker.sh /

ENV SPARK_WORKER_WEBUI_PORT 18081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-master:17077"

EXPOSE 18081

CMD ["/bin/bash", "/worker.sh"]
