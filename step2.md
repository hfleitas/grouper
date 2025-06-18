# Step 2

1. Create [Eventstream](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/create-manage-an-eventstream).
2. Add source [azure storage blob event](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-source-azure-blob-storage).
3. Add destination [Reflex](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-get-data-eventstreams) to trigger Fabric item Notebook.
4. Create a new [Notebook](./notebook/Factory-WideFileNB.py) similar to previous Notebook that takes blob URI paramater.
5. Test by uploading a new file to the blob container folder and monitor the eventstream payload.
6. Run queryset to sample or count new rows by using a filter such as `| where ingestion_time()>=ago(5m)`.

   All the above steps have been detailed in the [document](./step2details/blob_events_processing_and_incremental_file_read.docx).

## 🎯 Completed Step 2
- Proceed to [step3.md](step3.md).
