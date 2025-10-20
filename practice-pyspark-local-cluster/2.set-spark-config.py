from pyspark.sql import *
from lib.logger import Log4J
from lib.utils import get_spark_app_config

if __name__ == "__main__":
    conf = get_spark_app_config()
    spark = SparkSession.builder\
            .config(conf=conf)\
            .getOrCreate()

    logger = Log4J(spark)
    logger.info("Spark processing start....")
    data_list = [('Ravi', 28),
                 ('David', 41),
                 ('Ali', 32)]
    df = spark.createDataFrame(data_list).toDF("Name", "Age")
    df.show()

    conf_out_put = spark.sparkContext.getConf()
    logger.info(conf_out_put.toDebugString())

    logger.info("Spark processing end....")
    spark.stop()