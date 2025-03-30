
import os
import sys

def get_env():
    # Try getting from Glue args if available
    try:
        from awsglue.utils import getResolvedOptions
        args = getResolvedOptions(sys.argv, ['APP_ENV'])
        return args.get('APP_ENV', 'local')
    except Exception:
        return os.getenv('APP_ENV', 'local')


ENV = get_env()


def get_spark_context():
    print("Env: ", ENV)
    if ENV == "glue":
        import sys
        from awsglue.utils import getResolvedOptions
        from pyspark.context import SparkContext
        from awsglue.context import GlueContext
        from awsglue.job import Job

        ## @params: [JOB_NAME]
        args = getResolvedOptions(sys.argv, ['JOB_NAME'])

        sc = SparkContext()
        glueContext = GlueContext(sc)
        return glueContext.spark_session, glueContext
    else:
        from pyspark.sql import SparkSession
        spark = SparkSession.builder.appName("Example") \
            .config("spark.hadoop.io.native.lib.available", "false") \
            .config("spark.hadoop.native.lib", "false") \
            .getOrCreate()

        hadoopConf = spark._jsc.hadoopConfiguration()
        hadoopConf.set("fs.s3a.access.key", "")
        hadoopConf.set("fs.s3a.secret.key", "")
        hadoopConf.set("fs.s3a.endpoint", "s3.amazonaws.com")
        hadoopConf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        return spark, None