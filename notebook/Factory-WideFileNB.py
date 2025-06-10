#!/usr/bin/env python
# coding: utf-8

# ## Factory-WideFileNB
# 
# New notebook

# #### Query data from KQL DB for latest File from blobeventsdetails table

# In[1]:


kustoUri="https://trd-2y6rnwz9kguf1bqfcs.z3.kusto.fabric.microsoft.com"
database="TerniumDB"

kustoQuery = "blobeventsdetails | project subject,EventEnqueuedUtcTime,type | order by EventEnqueuedUtcTime desc | limit 1"
kustoDf  = spark.read\
            .format("com.microsoft.kusto.spark.synapse.datasource")\
            .option("accessToken", mssparkutils.credentials.getToken(kustoUri))\
            .option("kustoCluster", kustoUri)\
            .option("kustoDatabase", database) \
            .option("kustoQuery", kustoQuery).load()



# #### Exit Notebook in case of Blob Operation is not Microsoft.Storage.BlobCreated

# In[2]:


if  (kustoDf.first()['type'] != "Microsoft.Storage.BlobCreated"):
    mssparkutils.notebook.exit("NoExecutionFurther")


# #### Extract File Name

# In[3]:


#subject = kustoDf.select("subject").collect[0]
#display(kustoDf)

subject =  (kustoDf.first()['subject'])
FileList =  subject.split("/")
File = FileList.pop()
#File="20250401_162451_44_51.parquet"
#print(File)


# #### Access blob Storage 

# In[4]:


blob_account_name = "iotmonitoringsa26915"
blob_container_name = "widefile"
blob_relative_path = File  # Replace with your actual file path
# blob_sas_token = r"sp=r&st=2025-05-21T10:37:50Z&se=2025-05-30T18:37:50Z&spr=https&sv=2024-11-04&sr=c&sig=M8u1qBPe3qeZ2fvyley6iOB8cdIVXJD6yp8wtpM6NrE%3D"

# Set Spark configuration to use the SAS token
# spark.conf.set(
#   f"fs.azure.sas.{blob_container_name}.{blob_account_name}.dfs.core.windows.net",
#   blob_sas_token
# )

# Build the ABFS path
abfs_path = f"abfss://{blob_container_name}@{blob_account_name}.dfs.core.windows.net/{blob_relative_path}"



# #### Process to JSON

# In[5]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import to_json, struct

df = spark.read.parquet(abfs_path)
formatted_df = df.withColumn("Time", date_format("Time", "yyyy-MM-dd HH:mm:ss.SSSSSS"))
jsonDf = formatted_df.select(to_json(struct("*")).alias("data"))
#df = df.select("[0:0]Welder Speed Reference %","[0:1]Welder Speed Actual","[0:2]Welder Laser Power Reference","Time")
# jsonDf = df.select(to_json(struct("*")).alias("data"))


# In[12]:


#display(df)


# In[6]:


#path="abfss://3582b164-c42f-4707-98ac-a85e3bf6a734@msit-onelake.dfs.fabric.microsoft.com/daa0c241-9e58-49c3-be78-52ceb66a3c4a/Files/NarrowWidthFileActivator145.parquet"
#mssparkutils.fs.rm(path,True)


# In[7]:


#display(dfnew)


# #### Write to Eventhouse with JSON mapping in FactoryJsonMapping Table

# In[6]:


jsonDf.write.format("com.microsoft.kusto.spark.synapse.datasource").\
option("kustoCluster","https://trd-2y6rnwz9kguf1bqfcs.z3.kusto.fabric.microsoft.com").\
option("kustoDatabase","TerniumDB").\
option("kustoTable", "FactoryJsonMapping").\
option("format","json").\
option("ingestionMappingReference","jsonMapping").\
option("accessToken", mssparkutils.credentials.getToken('kusto')).\
option("tableCreateOptions", "CreateIfNotExist").mode("Append").save()


# #### Added because Instance of  Notebook execution was running even after data load in mapping Table

# In[ ]:


mssparkutils.notebook.exit("Finished")

