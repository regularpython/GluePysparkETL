

from src.framework.engine.spark_context_factory import get_spark_context
from src.services.s3_to_s3_service import S3ToS3Service


spark, context = get_spark_context()
print('Hello Sairam')
etl = S3ToS3Service(spark)
etl.read()
etl.transform()
etl.load()
