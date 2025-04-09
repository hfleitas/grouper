#!/usr/bin/env python
# coding: utf-8

# ## KustoControlCmds
# 
# New notebook

# In[ ]:


get_ipython().system('pip install azure-kusto-data==4.6.3')


# In[ ]:


from azure.kusto.data import KustoClient, KustoConnectionStringBuilder, ClientRequestProperties

token = mssparkutils.credentials.getToken('kusto')
eventhouse = 'https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com'
database = 'RTIDemo'
query = '.show tables'

kcsb = KustoConnectionStringBuilder.with_aad_user_token_authentication(eventhouse,token)
client = KustoClient(kcsb)
response = client.execute_mgmt(database, query).primary_results[0]

print(response)

client.close()

