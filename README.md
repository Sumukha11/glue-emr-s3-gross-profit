Project: Gross Profit Calculator using AWS Glue and EMR (PySpark)

Description:
This project builds a complete data processing pipeline using AWS Glue and Amazon EMR with PySpark to calculate gross profit from billing, sales, and production cost data.

Purpose:
To demonstrate the integration of AWS Glue (crawlers and catalog), S3, EMR, and PySpark for ETL and reporting purposes in a real-world financial data use case.

Process Overview:
1. Raw input files are stored in S3.
2. AWS Glue Crawlers scan and catalog the files into tables.
3. The EMR cluster is used to run a PySpark job:
   - Reads the tables using Spark SQL.
   - Joins and transforms the data to calculate gross profit.
   - Saves the final output back to S3 in CSV format.

## Key Files

- emr_cluster_setup.md: Instructions for setting up the EMR cluster and permissions
- glue_job_setup.md: Instructions for preparing the Glue-compatible PySpark job and running it
- glue_etl_job.py: PySpark job to process and transform transaction data

## Requirements

- AWS CLI configured
- IAM permissions for EC2, S3, Glue, and EMR
- Input data stored in Amazon S3 in CSV or Parquet format
