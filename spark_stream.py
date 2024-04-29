import logging
from data_ingestion.create_spark_connection import create_spark_connection
from data_ingestion.connect_to_kafka import connect_to_kafka
from data_ingestion.create_selection_df_from_kafka import create_selection_df_from_kafka
from data_ingestion.create_cassandra_connection import create_cassandra_connection
from data_loading.create_keyspace import create_keyspace
from data_loading.create_table import create_table

if __name__ == "__main__":
    # Create Spark connection
    spark_conn = create_spark_connection()

    if spark_conn is not None:
        # Connect to Kafka with Spark connection
        spark_df = connect_to_kafka(spark_conn)
        selection_df = create_selection_df_from_kafka(spark_df)
        session = create_cassandra_connection()

        if session is not None:
            create_keyspace(session)
            create_table(session)

            logging.info("Streaming is being started...")

            streaming_query = (selection_df.writeStream.format("org.apache.spark.sql.cassandra")
                               .option('checkpointLocation', '/tmp/checkpoint')
                               .option('keyspace', 'spark_streams')
                               .option('table', 'created_users')
                               .start())

            streaming_query.awaitTermination()