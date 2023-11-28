# Data Engineering

## Dependências

* [Docker](https://www.docker.com)
* [Helm](https://helm.sh)
* [Kind](https://kind.sigs.k8s.io)
* [Kubectl](https://kubernetes.io/docs/tasks/tools)

Iniciando ambiente Kubernetes:

```shell
make create-cluster
make create-namespace
make charts
make helm-install
```

Redirecionando a porta da interface do **Apache Airflow**:

```shell
make airflow-port-forward
```

Lançando as *releases* das imagens:

```shell
make airflow-release
```

Atualizando arquivos de código para o ambiente do **Kubernetes**:

```shell
make update
```

Limpando ambiente de desenvolvimento:

```shell
make clear
```
