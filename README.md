# Desafio-Spark-Nasa
Esse teste consiste em algumas perguntas e exercícios práticos sobre Spark

**Portanto esse desafio consiste nas seguintes perguntas:**

1 - Qual o objetivo do comando `cache em Spark`?

2 - O mesmo código implementado em `Spark` é normalmente mais rápido que a implementação equivalente em `MapReduce`. Por quê?

3 - Qual é a função do `SparkContext` ?

4 - Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

5 - GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

6 - Explique o que o código Scala abaixo faz.

```scala
val textFile = sc.textFile ("hdfs://...")  
val counts = textFile.flatMap(line=>line.split(" "))  
        .map(word =>(word,1))  
        .reduceByKey(_+_)  
counts.saveAsTextFile("hdfs://...")
```

**Por fim, o teste prático visa pegar um conjunto de dados da Nasa e desenvolver o código em `Spark` utilizando uma linguagem de preferência.**

Fonte oficial do dateset : http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html

Dados:

● [Jul 01 to Jul 31, ASCII format, 20.7 MB gzip compressed](ftp://ita.ee.lbl.gov/traces/NASA_access_log_Jul95.gz) , 205.2 MB.

● [Aug 04 to Aug 31, ASCII format, 21.8 MB gzip compressed](ftp://ita.ee.lbl.gov/traces/NASA_access_log_Aug95.gz) , 167.8 MB.

**`Sobre o dataset`** : Esses dois conjuntos de dados possuem todas as requisições HTTP para o servidor da NASA Kennedy
Space Center WWW na Flórida para um período específico.

Os logs estão em arquivos ASCII com uma linha por requisição com as seguintes colunas:

* **Host fazendo a requisição** . Um hostname quando possível, caso contrário o endereço de internet se o nome não puder ser identificado.
* **Timestamp** no formato "DIA/MÊS/ANO:HH:MM:SS TIMEZONE"
* **Requisição (entre aspas)**
* **Código do retorno HTTP**
* **Total de bytes retornados**

**Questões**

1. Número de hosts únicos.

2. O total de erros 404.
   
3. Os 5 URLs que mais causaram erro 404.

4. Quantidade de erros 404 por dia.

5. O total de bytes retornados.

>**Referências**:

> [1] - **Spark SQL, DataFrames and Datasets Guide**, <https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#datasets-and-dataframes>

> [2] - **PySpark SQL DataFrame Union**, <https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=union#pyspark.sql.DataFrame.union>
> 

> [3] - **Spark exemplos**, <https://spark.apache.org/examples.html>

> [4] - **Spark Certificação**, <https://github.com/alancarlosilva/Spark_Certificacao>