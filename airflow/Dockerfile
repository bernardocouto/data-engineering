FROM apache/airflow:latest

ENV PYTHONPATH "${PYTHONPATH}:${AIRFLOW_HOME}"

USER root

RUN usermod --uid 1000 airflow && chown --recursive airflow ${AIRFLOW_HOME}

USER airflow

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --requirement ./requirements.txt
