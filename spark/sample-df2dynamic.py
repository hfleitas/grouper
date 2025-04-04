%%spark
val dataFrame = List((1,"a1","b1"),(2,"a2","b2"),(3,"a3","b3")).toDF("id","col1","col2")
// val jsonDf =  dataFrame.select($"id",struct(to_json(struct($"*")).as("value")).as("data"))
val jsonDf = dataFrame.select(to_json(struct($"*")).as("data"))
display(jsonDf)

jsonDf.write.format("com.microsoft.kusto.spark.synapse.datasource").
option("kustoCluster","https://trd-wuyr5npkmn85n65q3m.z8.kusto.fabric.microsoft.com").
option("kustoDatabase","RTIDemo").
option("kustoTable", "test22").
option("accessToken", mssparkutils.credentials.getToken("kusto")).
option("tableCreateOptions", "CreateIfNotExist").mode("Append").save()
