import argparse
import sys

from pyspark.sql import *
from lib.logger import Log4J
from lib.utils import get_spark_app_config, create_dataframe_from_file

if __name__ == "__main__":
    conf = get_spark_app_config()
    spark = SparkSession.builder\
            .config(conf=conf)\
            .getOrCreate()

    logger = Log4J(spark)
    logger.info("Spark processing started....")

    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", nargs=1, type=str)
    args = parser.parse_args()

    # print(len(args.file_path))
    df = create_dataframe_from_file(spark, args.file_path)
    df.show()

    logger.info("Spark processing end....")
    spark.stop()