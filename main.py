from databricks.connect import DatabricksSession
from databricks.sdk.core import Config

config = Config(profile = "dbconnect-v2")
spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)