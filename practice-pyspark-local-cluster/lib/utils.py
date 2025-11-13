import configparser
from pyspark import SparkConf
from pyspark.sql import SparkSession, DataFrame


def get_spark_app_config():
    conf = SparkConf()
    config_parser = configparser.ConfigParser()
    config_parser.read("spark.conf")

    for key, val in config_parser.items("SPARK_APP_CONFIGS"):
        conf.set(key, val)

    return conf

def create_dataframe_from_file(spark_session: SparkSession, file_path: str) -> DataFrame:
    return spark_session.read.format('csv') \
                    .option('header', 'true') \
                    .option('inferSchema', 'true') \
                    .load(file_path)