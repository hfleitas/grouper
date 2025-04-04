#!/usr/bin/env python
# coding: utf-8

# ## WideFile
# 
# New notebook

# #### Process file column(s) to JSON Dataframe

# In[ ]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import to_json, struct
import pandas as pd
df = pd.read_parquet("https://rtainaday.blob.core.windows.net/sample/20250401_162451_44_51.parquet?sp=r&st=2025-04-03T19:39:37Z&se=2029-04-04T03:39:37Z&spr=https&sv=2024-11-04&sr=b&sig=BIUY%2F4hJpVGhBpUt6QrqeJX3zWIw24Pq1axHJd44R6U%3D")

dataFrame = spark.createDataFrame(df)
display(dataFrame.count())

#print(f"First 10 columns: {dataFrame.columns[:10]}")
#selectedDf = dataFrame.select(
#    'Time',
#    '[0:0]Welder Speed Reference %',
#    '[0:1]Welder Speed Actual',
#    '[0:2]Welder Laser Power Reference',
#    '[0:3]Welder Laser Power Actual',
#    '[0:4]Welder Laser Position Focus Reference',
#    '[0:5]Welder Laser Position Focus Aactual',
#    '[0:6]Welder Laser Head Pressure Reference %',
#    '[0:7]Welder Laser Head Pressure Actual',
#    '[0:8]Welder Planishing Pressure Reference')

jsonDf = dataFrame.select(to_json(struct("*")).alias("data"))
# display(jsonDf.head(1))


# In[ ]:


jsonDf.write.format("com.microsoft.kusto.spark.synapse.datasource").\
option("kustoCluster","https://bwattscluster.eastus.kusto.windows.net").\
option("kustoDatabase","Demo").\
option("kustoTable", "test22").\
option("format","json").\
option("ingestionMappingReference","jsonMapping").\
option("accessToken", mssparkutils.credentials.getToken('kusto')).\
option("tableCreateOptions", "CreateIfNotExist").mode("Append").save()


# #### Write JSON

# In[ ]:


jsonDf.write.format("com.microsoft.kusto.spark.synapse.datasource").\
option("kustoCluster","https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com").\
option("kustoDatabase","RTIDemo").\
option("kustoTable", "test23").\
option("accessToken", mssparkutils.credentials.getToken('kusto')).\
option("tableCreateOptions", "CreateIfNotExist").mode("Append").save()


# #### Check destination table

# In[76]:


kustoDf  = spark.read.format("com.microsoft.kusto.spark.synapse.datasource")\
    .option("kustoCluster", "https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com")\
    .option("kustoDatabase", "RTIDemo")\
    .option("accessToken", mssparkutils.credentials.getToken("kusto"))\
    .option("kustoQuery", "test23 | summarize count() by ingestion_time()").load()

display(kustoDf)


# In[ ]:


row_count = jsonDf.count()
print(f"Total number of rows: {row_count}")

