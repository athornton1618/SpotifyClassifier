from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.ml.feature import MinMaxScaler
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LinearSVC
from pyspark.ml.classification import OneVsRest
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

if __name__ == '__main__':
    spark = SparkSession.builder.master('yarn').appName('data-processing').getOrCreate()
    bucket = "audio-features-vectorized"
    table = 'features.audio_features'
    # Load data from BigQuery.
    spark.conf.set('temporaryGcsBucket', bucket)
    sql_context = SQLContext(spark)
    sparkDF = sql_context.read.format('bigquery') \
    .option('table', table) \
    .load()
    sparkDF.printSchema()

    # VectorAssembler Transformation - Converting column to vector type
    features = ['danceability', 'energy',
                'loudness', 'mode', 'speechiness', 'acousticness',
                'instrumentalness', 'liveness', 'valence',
                'tempo', 'time_signature']
    stages = []
    # Convert label into label indices using the StringIndexer
    label_stringIdx = StringIndexer(inputCol="genre", outputCol="label")
    # Transform all features into a vector using VectorAssembler
    assembler = VectorAssembler(inputCols=features, outputCol="features")
    # Rescale each feature to range [min, max].
    scaler = MinMaxScaler(inputCol="features", outputCol="scaledFeatures")
    stages += [label_stringIdx, assembler, scaler]
    pipeline = Pipeline(stages=stages)
    pipelineModel = pipeline.fit(sparkDF)
    preppedDataDF = pipelineModel.transform(sparkDF)
    preppedDataDF.show()

    # Split the data
    trainingData, testData = preppedDataDF.randomSplit([0.7, 0.3], seed = 100)
    print("Training Dataset Count: " + str(trainingData.count()))
    print("Test Dataset Count: " + str(testData.count()))

    lsvc = LinearSVC(maxIter=10, regParam=0.1)
    # instantiate the One Vs Rest Classifier.
    ovr = OneVsRest(classifier=lsvc)
    # train the multiclass model.
    ovrModel = ovr.fit(trainingData)
    # score the model on test data.
    predictions = ovrModel.transform(testData)
    # obtain evaluator.
    evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
    # compute the classification error on test data.
    accuracy = evaluator.evaluate(predictions)
    print("Test Error = %g" % (1.0 - accuracy))