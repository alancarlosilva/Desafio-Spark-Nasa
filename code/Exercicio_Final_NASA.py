# Databricks notebook source
#importando as bibliotecas
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, column, substring
import pyspark.sql.functions as F
import pandas as pd
import csv


#localização dos arquivos no Databricks
data_a = "/FileStore/tables/NASA_Jul95.csv"
data_b = "/FileStore/tables/NASA_Aug95.csv"

# COMMAND ----------

#Iniciando a sessão Spark usando SparkSession
spark = SparkSession \
    .builder \
    .appName("Python Spark - Nasa") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# COMMAND ----------

#Definindo o tipo de arquivo como "csv", a primeira linha não vai como cabeçalho.
#Passado como parâmetro e exibindo os primeiros registros. As variáveis df_data_a e df_data_b conterá o DataFrame correspondente ao arquivo aberto
df_data_a = spark.read.format("csv")\
            .option("delimiter", " ")\
            .option("multilines", "true")\
            .option("quotes", '""')\
            .option("header", "false")\
            .load(data_a)\
            .toDF("host", "a", "b", "dias", "time_zone", "request", "http", "bytes")

df_data_b = spark.read.format("csv")\
            .option("delimiter", " ")\
            .option("multilines", "true")\
            .option("quotes", '""')\
            .option("header", "false")\
            .load(data_b)\
            .toDF("host", "a", "b", "dias", "time_zone", "request", "http", "bytes")

# COMMAND ----------

#mostrando os dez primeiros resultados de NASA_Jul95
df_data_a.show(10,truncate = False)
df_data_b.show(10,truncate = False)

# COMMAND ----------

#Vamos tirar algumas colunas desnecessárias em nosso data Frame utilizando spark.sql
df_data_a.createOrReplaceTempView("NASA_Jul95")
df_data_b.createOrReplaceTempView("NASA_Aug95")

df1 = spark.sql("Select host, dias, request, http, bytes from NASA_Jul95")
df2 = spark.sql("Select host, dias, request, http, bytes from NASA_Aug95")

#Vamos fazer um union dos dois datasets para respondermos as perguntas abaixo 
access_log = df1.union(df2)

# COMMAND ----------

#1. Número de hosts únicos.
#Vamos utlizar a função select com filtro em host e distinct
access_log.select("host").distinct().count()

# COMMAND ----------

#2. O total de erros 404.
#Existem algumas maneiras de fazermos esse filtro pelo código de erro 404, primeiro vamos usar código SQL
access_log.createOrReplaceTempView("Erro404")

spark.sql("Select * from Erro404 where http='404'").count()

#Segundo vamos usar filter
access_log.filter(access_log['http'].contains('404')).count()

# COMMAND ----------

#3. Os 5 URLs que mais causaram erro 404.
#Primeiro exemplo vamos usar SQL para mostrar as 5 URLs com mais erros
spark.sql("Select host, count(host) as qtde from Erro404 where http='404' group by host order by 2 desc limit 5").show(10, truncate=False)

#Segundo vamos utilizar funções
access_log.select('host').where("http='404'").groupBy('host').count().orderBy('count',ascending=False).limit(5).show(truncate=False)

# COMMAND ----------

#4. Quantidade de erros 404 por dia.

spark.sql("Select substring(dias, 2,11) as dias, count('dias') from Erro404 where http='404' group by 1").show(10, truncate=False)


# COMMAND ----------

#5. O total de bytes retornados.
#Utilizando função select
access_log.select(F.sum('bytes')).show()

#Utilizando spark.sql
access_log.createOrReplaceTempView("TotalBytes")

spark.sql("Select sum(bytes) as total_bytes from TotalBytes").show(truncate=False)
