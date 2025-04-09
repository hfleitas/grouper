#!/usr/bin/env python
# coding: utf-8

# ## KustoControlCmds
# 
# New notebook

# In[ ]:


get_ipython().system('pip install azure-kusto-data==4.6.3')


# In[8]:


from datetime import timedelta

from azure.kusto.data import KustoClient, KustoConnectionStringBuilder, ClientRequestProperties
from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.helpers import dataframe_from_result_table

cluster='https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com'
token= mssparkutils.credentials.getToken('kusto')

kcsb = KustoConnectionStringBuilder.with_aad_user_token_authentication(cluster,token)

# The authentication method will be taken from the chosen KustoConnectionStringBuilder.
client = KustoClient(kcsb)

# Make sure to close the client when you're done with it.
# Either by using a context manager:
with KustoClient(kcsb) as client2:
    pass  # will be closed automatically at the end of the block

# Or by calling the close method explicitly:
client3 = KustoClient(kcsb)
# query='.show cluster'
query='.show tables'

response = client.execute_mgmt("RTIDemo", query).primary_results[0]

print(response)

client3.close()


# In[ ]:




