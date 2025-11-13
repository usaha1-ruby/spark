class Log4J:
    def __init__(self, spark):
        log4j = spark._jvm.org.apache.log4j
        root_class = "personal.practice.spark"
        configs = spark.sparkContext.getConf()
        app_name = configs.get("spark.app.name")
        # best practice: organization name as the root class and suffix it with the application name.
        # log4j configuration works as long as the base name/ root class matches.
        self.logger = log4j.LogManager.getLogger(root_class + "." + app_name)

    def warn(self, msg):
        self.logger.warn(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)
