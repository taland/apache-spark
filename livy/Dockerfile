FROM bde2020/spark-base:2.3.1-hadoop2.7

ENV LIVY_URL=http://apache.cp.if.ua/incubator/livy/0.5.0-incubating/livy-0.5.0-incubating-bin.zip

ENV HADOOP_CONF_DIR /opt/livy/conf
ENV CONF_DIR /opt/livy/conf
ENV SPARK_HOME /spark
ENV SPARK_CONF_DIR /opt/livy/conf

WORKDIR /opt

RUN wget ${LIVY_URL} -O livy.zip && unzip livy.zip && rm livy.zip && mv livy* livy

ADD conf livy/conf
RUN mkdir livy/logs

EXPOSE 8998

CMD ["/opt/livy/bin/livy-server"]
