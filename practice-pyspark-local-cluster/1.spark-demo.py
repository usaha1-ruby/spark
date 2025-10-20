from pyspark.sql import *
from lib.logger import Log4J

if __name__ == "__main__":
    spark = SparkSession.builder\
            .appName("first-spark-practice")\
            .master("local[3]")\
            .getOrCreate()

    logger = Log4J(spark)
    logger.info("Spark processing start....")
    data_list = [('Ravi', 28),
                 ('David', 41),
                 ('Ali', 32)]
    df = spark.createDataFrame(data_list).toDF("Name", "Age")
    df.show()
    logger.info("Spark processing end....")
    spark.stop()