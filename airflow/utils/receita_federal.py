from pyspark.sql import SparkSession
from pyspark.sql.types import DateType, DecimalType, StringType, StructField, StructType

def main():

    spark = (
        SparkSession
        .builder
        .appName("receita_federal")
        .getOrCreate()
    )

    empresas_schema = (
        StructType(
            [
                StructField("cnpj_basico", StringType(), True),
                StructField("razao_social", StringType(), True),
                StructField("natireza_juridica", StringType(), True),
                StructField("qualificacao_responsavel", StringType(), True),
                StructField("capital_social", DecimalType(scale=2), True),
                StructField("porte", StringType(), True),
                StructField("ente_federativo_responsavel", StringType(), True)
            ]
        )
    )

    empresas_df = (
        spark
        .read
        .options(
            delimiter=";"
        )
        .csv(
            path="/Users/bernardocouto/Documents/Development/Studies/data-engineering/data/raw/receita_federal/empresas",
            schema=empresas_schema
        )
    )

    print(empresas_df.printSchema())
    print(empresas_df.show())

    empresas_df.createOrReplaceTempView("empresas")

    estabelecimentos_schema = (
        StructType(
            [
                StructField("cnpj_basico", StringType(), True),
                StructField("cnpj_ordem", StringType(), True),
                StructField("cnpj_digito_verificador", StringType(), True),
                StructField("identificador_matriz_filial", StringType(), True),
                StructField("nome_fantasia", StringType(), True),
                StructField("situacao_cadastral", StringType(), True),
                StructField("data_situacao_cadastral", DateType(), True),
                StructField("motivo_situacao_cadastral", StringType(), True),
                StructField("nome_cidade_exterior", StringType(), True),
                StructField("pais", StringType(), True),
                StructField("data_inicio_atividade", DateType(), True),
                StructField("cnae_principal", StringType(), True),
                StructField("cnae_secundario", StringType(), True),
                StructField("tipo_logradouro", StringType(), True),
                StructField("logradouro", StringType(), True),
                StructField("numero", StringType(), True),
                StructField("complemento", StringType(), True),
                StructField("bairro", StringType(), True),
                StructField("cep", StringType(), True),
                StructField("uf", StringType(), True),
                StructField("municipio", StringType(), True),
                StructField("ddd_1", StringType(), True),
                StructField("telefone_1", StringType(), True),
                StructField("ddd_2", StringType(), True),
                StructField("telefone_2", StringType(), True),
                StructField("ddd_fax", StringType(), True),
                StructField("telefone_fax", StringType(), True),
                StructField("email", StringType(), True),
                StructField("situacao_especial", StringType(), True),
                StructField("data_situacao_especial", DateType(), True)
            ]
        )
    )

    estabelecimentos_df = (
        spark
        .read
        .options(
            delimiter=";"
        )
        .csv(
            path="/Users/bernardocouto/Documents/Development/Studies/data-engineering/data/raw/receita_federal/estabelecimentos",
            schema=estabelecimentos_schema
        )
    )

    print(estabelecimentos_df.printSchema())
    print(estabelecimentos_df.show())

    estabelecimentos_df.createOrReplaceTempView("estabelecimentos")

    socios_schema = (
        StructType(
            [
                StructField("cnpj_basico", StringType(), True),
                StructField("identificador", StringType(), True),
                StructField("nome_razao_social", StringType(), True),
                StructField("cnpj_cpf", StringType(), True),
                StructField("qualificacao", StringType(), True),
                StructField("data_entrada_sociedade", DateType(), True),
                StructField("pais", StringType(), True),
                StructField("representante_legal", StringType(), True),
                StructField("nome_representante_legal", StringType(), True),
                StructField("qualificacao_representante_legal", StringType(), True),
                StructField("faixa_etaria", StringType(), True)
            ]
        )
    )

    socios_df = (
        spark
        .read
        .options(
            delimiter=";"
        )
        .csv(
            path="/Users/bernardocouto/Documents/Development/Studies/data-engineering/data/raw/receita_federal/socios",
            schema=socios_schema
        )
    )

    print(socios_df.printSchema())
    print(socios_df.show())

    socios_df.createOrReplaceTempView("socios")

    df = (
        spark
        .sql(
            """
            SELECT *
            FROM empresas e1
            INNER JOIN estabelecimentos e2
            ON e1.cnpj_basico = e2.cnpj_basico
            WHERE e1.cnpj_basico = '00000000'
            """
        )
    )

    print(df.show(100))

if __name__ == "__main__":
    main()
