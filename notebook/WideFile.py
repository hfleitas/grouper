#!/usr/bin/env python
# coding: utf-8

# ## WideFile
# 
# New notebook

# #### Process to JSON

# In[6]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import to_json, struct
import pandas as pd
df = pd.read_parquet("https://rtainaday.blob.core.windows.net/sample/20250401_162451_44_51.parquet?sp=r&st=2025-04-03T19:39:37Z&se=2029-04-04T03:39:37Z&spr=https&sv=2024-11-04&sr=b&sig=BIUY%2F4hJpVGhBpUt6QrqeJX3zWIw24Pq1axHJd44R6U%3D")

dataFrame = spark.createDataFrame(df)
jsonDf = dataFrame.select(to_json(struct("*")).alias("data"))


# #### Write to Eventhouse with JSON mapping

# In[10]:


jsonDf.write.format("com.microsoft.kusto.spark.synapse.datasource").\
option("kustoCluster","https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com").\
option("kustoDatabase","RTIDemo").\
option("kustoTable", "test22").\
option("format","json").\
option("ingestionMappingReference","jsonMapping").\
option("accessToken", mssparkutils.credentials.getToken('kusto')).\
option("tableCreateOptions", "CreateIfNotExist").mode("Append").save()

