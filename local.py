from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Initialize Spark
spark = SparkSession.builder \
    .appName("Local Gross Profit Calculator") \
    .master("local[*]") \
    .getOrCreate()

# Load CSVs
billing_df = spark.read.csv("s3_files/billing_data_dairy_07_2023.csv", header=True, inferSchema=True)
units_df = spark.read.csv("s3_files/units_sold_07_2023.csv", header=True, inferSchema=True)
cost_df = spark.read.csv("s3_files/production_costs_07_2023.csv", header=True, inferSchema=True)

# Optional: Explore data
billing_df.printSchema()
billing_df.show(5)

# JOIN data (based on assumed key 'product_id')
df_joined = billing_df \
    .join(units_df, on="product_id") \
    .join(cost_df, on="product_id")

# Compute Gross Profit
df_final = df_joined.withColumn(
    "gross_profit",
    (col("units_sold") * col("selling_price")) - (col("units_sold") * col("production_cost"))
)

# Save to CSV locally
df_final.select("product_id", "units_sold", "selling_price", "production_cost", "gross_profit") \
    .coalesce(1) \
    .write \
    .option("header", True) \
    .csv("output/gross_profit_report")

print("✅ Gross profit report saved in ./output/")
spark.stop()
