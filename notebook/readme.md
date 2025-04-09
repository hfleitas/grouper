# Notebook Resources

## Fix for .save() fails after 45 minutes. 
```
Py4JJavaError: An error occurred while calling o5704.save. : org.apache.spark.SparkException: Job aborted due to stage failure: Task 0 in stage 23.0 failed 4 times, most recent failure: Lost task 0.3 in stage 23.0 (TID 40) (vm-69326674 executor 2): com.microsoft.kusto.spark.exceptions.RetriesExhaustedException: Failed to move extents after 11 tries.
```
Solutions:
1. Add a `.option("writeMode","Queued")`.
2. Use option format & mapping for json. (preferred)


## Is it possible for the spark connector to run control commands, such as...
```
kql = ".execute database script <| \
.drop table test22 ifexists; \
.create-or-alter test22 (data:dynamic); \
.alter column test22.data policy encoding type='BigObject32';"
```
Yes, see sample [KustoControlCmd.py](KustoControlCmd.py).
