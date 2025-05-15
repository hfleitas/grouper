# Step 2

1. Create Eventstream.
2. Add source azure storage blob event.
3. Add destination Reflex to trigger Fabric item Notebook.
4. Create a new Notebook similar to previous Notebook that takes blob URI paramater.
5. Test by uploading a new file to the blob container folder and monitor the eventstream payload.
6. Run queryset to sample or count new rows by using a filter such as `| where ingestion_time()>=ago(5m)`.

## 🎯 Completed Step 2
- Proceed to [step3.md](step3.md).
