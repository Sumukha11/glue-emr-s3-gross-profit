# AWS Glue + EMR PySpark ETL Project

## Project Overview

This project demonstrates how to process sales transaction data using a hybrid AWS Glue + EMR-based architecture. It leverages AWS Glue Crawlers, Amazon Data Catalog, and PySpark running on Amazon EMR to perform data extraction, transformation, and loading (ETL) of business records.

The core objective is to compute gross profit by integrating and transforming datasets that include:

- Billing records
- Units sold per item
- Production costs

---

## Architecture

- **AWS S3**: Stores input data (`CSV` files) and final ETL output.
- **AWS Lake Formation**: Provides secure access control to the data catalog and S3 buckets.
- **AWS Glue Crawlers**: Crawls raw CSV files and creates external tables in the AWS Glue Data Catalog.
- **AWS Glue Data Catalog**: Central metadata repository used by EMR for querying.
- **Amazon EMR Cluster**: Executes a PySpark script via SSH that reads from Glue tables, processes data, and writes results back to S3.

---

## ETL Workflow

1. **Input Files** (stored in S3):
   - `billing_data_dairy_07_2023.csv`
   - `units_sold_07_2023.csv`
   - `production_costs_07_2023.csv`

2. **AWS Glue Crawlers**:
   - Crawlers scan these files and create tables in the Glue Data Catalog:
     - `sumukha_billing_x_processed`
     - `units_sold`
     - `production_costs`

3. **PySpark Script on EMR**:
   - Connects to Glue Catalog using Hive support
   - Performs `JOINs` and transformations to calculate gross profit:
     ```
     gross_profit = bill_amount - (units_sold * cost_per_unit_usd)
     ```
   - Writes the output to:
     - `s3://sumukha-billing-x-datalake/reports/gross-profits`

---

## Key Learnings

- Hands-on experience in hybrid ETL architecture combining AWS Glue and EMR
- Using AWS Lake Formation for secure access to S3 and Glue Data Catalog
- Creating PySpark scripts with Hive support for dynamic querying of Glue tables
- Data engineering best practices for transformation pipelines
- Writing final output back to S3 in CSV format using Spark

---
