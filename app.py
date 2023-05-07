import sys

from pyspark.sql import SparkSession

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: spark-submit app.py <input>")
        sys.exit(1)

    # TODO: Add argument parser
    input_file_path = sys.argv[1]

    spark = SparkSession.builder.appName("Spark").getOrCreate()
    df = spark.read.json(input_file_path)

    # Show example
    df.show(20)

    df.createOrReplaceTempView("df")

    # Queries
    spark.sql("SELECT * FROM df LIMIT 10").show()
    spark.sql("SELECT COUNT(*) FROM df").show()
    spark.sql("SELECT cn, COUNT(*) FROM df GROUP BY cn ORDER BY 2 DESC").show()
    spark.sql("SELECT cn, MAX(temp) AS max_temp FROM df GROUP BY cn ORDER BY 2 DESC").show()
