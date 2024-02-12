# Create External Table
CREATE OR REPLACE EXTERNAL TABLE `eloquent-region-411618.green_taxi.external_green_tripdata`
OPTIONS (
  format = 'Parquet',
  uris = ['gs://mage-zoomcamp-bucket-awaawa/green_taxi_data/488bf1e1848849f6ad5cf6c77242fff3-0.parquet']
);

# Create Table
CREATE OR REPLACE TABLE `eloquent-region-411618.green_taxi.green_tripdata_non_partitioned` AS
SELECT * FROM `eloquent-region-411618.green_taxi.external_green_tripdata`;

# Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
SELECT COUNT(DISTINCT PULocationID)
FROM `green_taxi.external_green_tripdata`

SELECT COUNT(DISTINCT PULocationID)
FROM `green_taxi.green_tripdata_non_partitioned`

# Records having fare_amount of 0
SELECT COUNT(*)
FROM `green_taxi.green_tripdata_non_partitioned`
WHERE fare_amount = 0;

# Create Table partitioned on lpep_pickup_datetime and clustered on PUlocationID
CREATE OR REPLACE TABLE `green_taxi.green_trip_data_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM `green_taxi.green_tripdata_non_partitioned`;

# Query to get distinct PUlocationID between 2 dates
SELECT DISTINCT PULocationID
FROM `green_taxi.green_trip_data_partitioned_clustered`
WHERE lpep_pickup_datetime >= '2022-06-01' AND lpep_pickup_datetime <= '2022-06-30';


# Question 8
Retrieved directly from metadata or possibly cached query