CREATE TABLE IF NOT EXISTS kafka_table
(
  Day          String,
  TickTime      String,
  Speed          String
)
ENGINE=Kafka('localhost:9092', 'v8', 'group', 'JSONEachRow');



CREATE TABLE table_kafka
(
  Day          String,
  TickTime      String,
  Speed          String
)
Engine=MergeTree() order by (Day, TickTime, Speed)

CREATE MATERIALIZED VIEW table_kafka_consumer
TO table_kafka
AS SELECT *
FROM kafka_table;


SELECT * from table_kafka
