File: EMR Cluster Setup Instructions

1. Launch EMR Cluster:
   - Cluster Type: EMR on EC2
   - Applications: Spark, Hive
   - Release: EMR 6.x (latest stable)
   - Instance Type: m5.xlarge (or any preferred)
   - Number of Instances: 1 (or more for scaling)
   - Logging: Enabled to S3 bucket (optional)
   - Permissions: Use a role with access to S3 and Glue

2. Enable Hive Support:
   - Ensure 'Enable Hive Support' is checked during cluster creation.

3. SSH into EMR Cluster:
   - Use the following command:
     ssh -i /path/to/key.pem hadoop@<EMR-Master-Public-DNS>

4. Confirm Spark is Installed:
   - Run: which pyspark
   - Output should be: /usr/bin/pyspark or similar

5. Run PySpark:
   - Run: pyspark --master yarn
   - Ensure it drops you into a PySpark shell without errors.

6. Ports Required (if accessing from outside):
   - TCP 22: SSH Access
   - TCP 8088: YARN ResourceManager (UI)
   - TCP 18080: Spark History Server
   - TCP 8888: Jupyter (if installed)
   - Add these ports to EMR security group if needed.

7. Verify Spark with Hive Support:
   - Run this in PySpark:
     from pyspark.sql import SparkSession
     spark = SparkSession.builder.enableHiveSupport().getOrCreate()
     spark.sql("show databases").show()
