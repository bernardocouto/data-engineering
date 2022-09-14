# Data Engineering

## Dados

Fonte de dados: [Receita Federal](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/consultas/dados-publicos-cnpj)

## Apache Airflow

Acessando diretório do Airflow:

```shell
cd airflow
```

Executando estrutura de inicialização do Airflow:

```shell
docker-compose up airflow-init
```

Executando o Airflow:

```shell
docker-compose up
```

Excluindo estrutura do Airflow:

```shell
docker-compose down --volumes --rmi all
```
