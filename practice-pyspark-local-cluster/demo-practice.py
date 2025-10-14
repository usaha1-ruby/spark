from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Spark Demo") \
            .master("local[3]")\
            .getOrCreate()
    data_list = [('Ravi', 28),
                 ('David', 41),
                 ('Ali', 32)]
    df = spark.createDataFrame(data_list).toDF("Name", "Age")
    df.show()