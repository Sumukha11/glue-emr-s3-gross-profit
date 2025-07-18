File: AWS Glue Job and Crawler Setup

1. Create Input S3 Buckets:
   - Store your CSV files for billing, units sold, and production costs.
   - Example:
     s3://sumukha-billing-x/input/bills.csv
     s3://sumukha-billing-x/input/units_sold.csv
     s3://sumukha-billing-x/input/production_costs.csv

2. Create Glue Database:
   - Navigate to AWS Glue > Databases > Add database
   - Name: sumukha-billing

3. Create Glue Crawlers:
   - One for each input directory
   - Source: S3
   - Target: Glue Data Catalog
   - Database: sumukha-billing
   - Output Tables: 
     sumukha_billing_x_processed
     units_sold
     production_costs

4. Run Crawlers:
   - This will automatically infer schema and create tables.

5. Tables Created:
   - sumukha_billing_x_processed
   - units_sold
   - production_costs

6. Validate Tables:
   - You can use Athena or Spark to preview the data.
