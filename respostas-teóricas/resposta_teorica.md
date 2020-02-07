
1 - Qual o objetivo do comando `cache em Spark`?

Caching RDDs no Spark é um mecanismo para acelerar as aplicações que acessam o mesmo RDD diversas vezes. Quando estamos usando um RDD que não é cacheado, a ação que invoca o RDD é reprocessado de novo quando a função é chamada.

Abaixo apresentamos alguns exemplos de quando usarmos o `cache`:

1. RDD re-use em aplicações interative de machine learning
2. RDD re-use em aplicações Spark Standalone
3. Quando uma aplicação RDD consome muita computação, o cache pode ajudar a reduzir o custo de recuperação caso o executor falhe.


2 - O mesmo código implementado em `Spark` é normalmente mais rápido que a implementação equivalente em `MapReduce`. Por quê?

Sim, pois o `Spark` funciona em memória e o `Map Reduce` funciona em disco


3 - Qual é a função do `SparkContext` ?

`SparkContext` é o canal para acessar todas as funcionalidades do `Spark`: apenas um único `SparkContext` existe por JVM. O programa do driver Spark usa-o para conectar-se ao gerenciador do cluster para se comunicar e enviar tarefas do Spark. Ele permite que você ajuste programaticamente os parâmetros de configuração do Spark. E por meio do SparkContext, o driver pode instanciar outros contextos, como `SQLContext`, `HiveContext` e `StreamingContext`, para programar o `Spark`.
Segundo a documentação[1] Spark RDD é uma coleção de elementos particionados através de nodes do cluster que podem ser operados em paralelo.

4 - Explique com suas palavras o que é Resilient Distributed Datasets (RDD).

Segundo a documentação[1] Spark RDD é uma coleção de elementos particionados através de nodes do cluster que podem ser operados em paralelo.

5 - GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê? 

6 - Explique o que o código Scala abaixo faz.

```scala
val textFile = sc.textFile ("hdfs://...")  
val counts = textFile.flatMap(line=>line.split(" "))  
        .map(word =>(word,1))  
        .reduceByKey(_+_)  
counts.saveAsTextFile("hdfs://...")
```
Esse exemplo de código, são usados pequenas transformações de `map` e `reduce` para construir um `dataset` com chave e valor (string, int), os pares são chamados de contadores e então é salvo em um arquivo. Ao fim teremos um contador de palavras [3].