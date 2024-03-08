from pyspark.sql import types
from pyspark.sql import functions as F
import pyspark.pandas as ps

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    spark = kwargs['spark']

    df = spark.createDataFrame(data)

    #modify df
    df =  df.withColumn("Date_Rptd", F.to_date(df["Date_Rptd"], "MM/dd/yyyy hh:mm:ss a")) \
            .withColumn("DATE_OCC", F.to_date(df["DATE_OCC"], "MM/dd/yyyy hh:mm:ss a")) \
            .withColumn('Vict_Sex', F.when(~F.col('Vict_Sex').isin(['M', 'F']), 'Other')
                                        .otherwise(F.when(F.col('Vict_Sex') == 'M', 'Male')
                                        .otherwise(F.when(F.col('Vict_Sex') == 'F', 'Female'))) ) \
            .withColumn('TIME_OCC', F.when(F.length(F.col('TIME_OCC')) < 4, F.concat(F.lit("0"), F.col('TIME_OCC')))
                                        .otherwise(F.col('TIME_OCC'))) \
            .withColumn("TIME_OCC", F.concat(F.col("TIME_OCC")[0:2], F.lit(":"), F.col("TIME_OCC")[3:4]))

    #print("Schema:")
    #print(df.printSchema())
    pandas_df = df.toPandas()
    #print("Dataframe:")
    return pandas_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
