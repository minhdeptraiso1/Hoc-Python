"""
===============================================================================
                      BIG DATA PIPELINE — Spark + Kafka

Real-time data pipeline

Kafka → Spark Streaming → xử lý → xuất output

Dùng cho hệ thống IoT, Logs, Event Streaming
===============================================================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

print("\n===== SPARK STREAMING + KAFKA =====")

spark = SparkSession.builder \
    .appName("KafkaSparkPipeline") \
    .getOrCreate()

# =================== READ FROM KAFKA =====================

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "sensor-topic") \
    .load()

schema = StructType().add("sensor", StringType()).add("value", StringType())

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# =================== TRANSFORM ===========================

processed = json_df.withColumn("value_num", col("value").cast("float"))

# =================== WRITE TO SINK =======================

query = processed.writeStream \
    .format("console") \
    .start()

query.awaitTermination()
