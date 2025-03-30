from src.framework.etl_abstract import ETLAbstract


class S3ToS3Service(ETLAbstract):

    def __init__(self, spark):
        self.spark = spark
        self.df = None

    def read(self):
        self.df = self.spark .read.csv("s3a://pyspark-test-regularpython/source/", header=True, inferSchema=True)


    def transform(self):
        self.df = self.df.drop("Model", "Model Variant", "Variant Title", "Available Colors")


    def load(self):
        self.df.write.csv("s3a://pyspark-test-regularpython/destination/", header=True, mode="overwrite")
