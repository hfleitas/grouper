## Step 3

1. Run queryset [timeseriesanalytics-sample.kql](./kql/timeseriesanalytics-sample.kql) by adding the Help cluster URI in your queryset connections pane and select the Samples db.
2. See more [Time Series Analysis](https://learn.microsoft.com/kusto/query/time-series-analysis?view=microsoft-fabric).
3. Adjust queries over your data as necessary.

### Next (Phase 2)

1. Proceed to visuals by using RTI Dashboard (recommended) or Power BI, then building alerts or custom actions by using Reflex (Data Activator) item.
2. Ingest historical data if needed, depending on volume consider using `creationTime` parameter. See [supported ingestion properties](https://learn.microsoft.com/kusto/management/data-ingestion/ingest-from-query?view=microsoft-fabric#supported-ingestion-properties).
3. Consider implement continous ingestion using Eventhouse Get Data UI from Azure Storage, instead of Eventstream + Notebook, granted platform capabilities when zstd compression is supported or files are in standard parquet compression. 
