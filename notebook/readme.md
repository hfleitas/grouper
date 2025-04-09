# Notebook Resources

## Fix for .save() fails after 45 minutes. 
```
Py4JJavaError: An error occurred while calling o5704.save. : org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 23.0 failed 4 times, most recent failure: Lost task 0.3 in stage 23.0 (TID 40) (vm-69326674 executor 2): com.microsoft.kusto.spark.exceptions.RetriesExhaustedException: Failed to move extents after 11 tries.
```
Solutions:
1. Add a `.option("writeMode","Queued")`, that will fix this issue.
2. Use option format & mapping for json. (preferred)


## Is it possible for the spark connector to run control commands? 
```
kql = ".execute database script <| \
.drop table test22 ifexists; \
.create-or-alter test22 (data:dynamic); \
.alter column test22.data policy encoding type='BigObject32';"
 
kustoDf  = spark.read.format("com.microsoft.kusto.spark.synapse.datasource")\
    .option("kustoCluster", "https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com")\
    .option("kustoDatabase", "RTIDemo")\
    .option("accessToken", mssparkutils.credentials.getToken("kusto"))\
    .option("kustoQuery", kql)
 
kustoDf.load()
```

Yes, follow these steps:
1. `!pip install azure-kusto-data`
2. Once this is done using the [ConnectionStringBuilder](https://github.com/Azure/azure-kusto-python/blob/fed5aebd10c3cfbc3a14467656fb57a43cb4180e/azure-kusto-data/tests/sample.py#L26)
3. Create an admin / management client and execute the query
