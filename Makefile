SHELL:=/bin/bash

NAME=data-engineering
VERSION=latest

.PHONY: airflow-port-forward
airflow-port-forward:
	kubectl port-forward svc/${NAME}-airflow-webserver 8080:8080 \
		--namespace ${NAME}

.PHONY: airflow-release
airflow-release:
	docker build \
		--tag ${NAME}-airflow:${VERSION} airflow
	kind load docker-image ${NAME}-airflow:${VERSION} \
		--name ${NAME}
	helm upgrade ${NAME}-airflow apache-airflow/airflow \
		--namespace ${NAME} \
		--set images.airflow.repository=${NAME}-airflow \
		--set images.airflow.tag=${VERSION} \
		--values templates/airflow/values.yaml

.PHONY: charts
charts:
	helm repo add apache-airflow https://airflow.apache.org
	helm repo update

.PHONY: clear
clear:
	kind delete cluster \
		--name ${NAME}

.PHONY: create-cluster
create-cluster:
	kind create cluster \
		--image kindest/node:v1.28.0 \
		--name ${NAME}

.PHONY: create-namespace
create-namespace:
	kubectl create namespace ${NAME}

.PHONY: helm-install
helm-install:
	helm install ${NAME}-airflow apache-airflow/airflow \
		--namespace ${NAME}

.PHONY: update
update:
	kubectl exec \
		-it ${RELEASE_NAME}-airflow-worker-0 \
		--bash -c 'rm -rf /opt/airflow/dags/*' \
		--container worker \
		--namespace ${NAME}
	kubectl cp airflow/dags ${NAME}-airflow-worker-0:/opt/airflow \
		--container worker \
		--namespace ${NAME}
