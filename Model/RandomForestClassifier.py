from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer, IndexToString
from pyspark.ml.classification import OneVsRest
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.linalg import DenseVector
from pyspark.ml.classification import RandomForestClassifier

if __name__ == '__main__':
    spark = SparkSession.builder.master('yarn').appName('data-processing').getOrCreate()
    table = 'features.ten_genres'
    # Load data from BigQuery.
    bucket = "train_test_data_spotify"
    spark.conf.set('temporaryGcsBucket', bucket)
    sql_context = SQLContext(sparkContext=spark.sparkContext, sparkSession=spark)
    sparkDF = sql_context.read.format('bigquery') \
    .option('table', table) \
    .load()
    sparkDF.printSchema()

    genre_list = [row[0] for row in sparkDF.select('super_genre').distinct().collect()]

    # VectorAssembler Transformation - Converting column to vector type    
    features = ['danceability', 'energy', 'loudness',
                'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
                'valence', 'tempo', 'time_signature', 'popularity',
                'pitch0', 'pitch1', 'pitch2', 'pitch3', 'pitch4', 'pitch5', 'pitch6',
                'pitch7', 'pitch8', 'pitch9', 'pitch10', 'pitch11', 'timbre0',
                'timbre1', 'timbre2', 'timbre3', 'timbre4', 'timbre5', 'timbre6',
                'timbre7', 'timbre8', 'timbre9', 'timbre10', 'timbre11']
                
    stages = []
    # Convert label into label indices using the StringIndexer
    label_stringIdx = StringIndexer(inputCol="super_genre", outputCol="label")
    # Transform all features into a vector using VectorAssembler
    assembler = VectorAssembler(inputCols=features, outputCol="features")
    stages += [label_stringIdx, assembler]

    rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=20)
    stages += [rf]

    pipeline = Pipeline(stages=stages)
    
    # Split the data
    trainingData, testData = sparkDF.randomSplit([0.8, 0.2], seed = 1234)
    print("Training Dataset Count: " + str(trainingData.count()))
    print("Test Dataset Count: " + str(testData.count()))

    pipelineModel = pipeline.fit(trainingData)

    predictions_test = pipelineModel.transform(testData)
    predictions_test.write.format('bigquery') \
    .option('table', 'features.predictions_test') \
    .save()

    predictions_test.select("prediction", "label", "features", "super_genre").show(10)
    evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction", metricName="accuracy")
    accuracy = evaluator.evaluate(predictions_test)
    print('Train F1-Score ',   evaluator.evaluate(predictions_test, 
                                      {evaluator.metricName: 'f1'}))
    print('Train Precision ',  evaluator.evaluate(predictions_test,
                                        {evaluator.metricName: 'weightedPrecision'}))
    print('Train Recall ',     evaluator.evaluate(predictions_test, 
                                        {evaluator.metricName: 'weightedRecall'}))
    print('Train Accuracy ',   evaluator.evaluate(predictions_test, 
                                      {evaluator.metricName: 'accuracy'}))