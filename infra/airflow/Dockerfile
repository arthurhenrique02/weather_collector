FROM apache/airflow:3.0.2

USER root

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow
COPY ../../requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./dags /opt/airflow/dags
COPY ./plugins /opt/airflow/plugins

WORKDIR /opt/airflow