## Step 3

1. Run queryset [timeseriesanalytics-sample.kql](./kql/timeseriesanalytics-sample.kql) by adding the Help cluster URI in your queryset connections pane and select the Samples db.
2. See more [Time Series Analysis](https://learn.microsoft.com/kusto/query/time-series-analysis?view=microsoft-fabric).
3. Example of [Time Series Analysis](./kql/timeseriesanalytics-PLTCM.kql) over sample PLTCM data
4. Adjust queries over your data as necessary.

### Next (Phase 2)

1. Proceed to visuals by using [RTI Dashboard](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-real-time-create) (recommended) or Power BI, then building [alerts or custom actions](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-create-activators) by using Reflex (Data Activator) item.
2. Ingest historical data if needed, depending on volume consider using `creationTime` parameter. See [supported ingestion properties](https://learn.microsoft.com/kusto/management/data-ingestion/ingest-from-query?view=microsoft-fabric#supported-ingestion-properties). [Example](https://learn.microsoft.com/en-us/kusto/management/data-ingestion/ingest-into-command?view=microsoft-fabric)
3. Consider implement continous ingestion using Eventhouse [Get Data UI from Azure Storage](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/get-data-azure-storage?tabs=continuous-ingestion), instead of Eventstream + Notebook, granted platform capabilities when zstd compression is supported or files are in standard parquet compression. 
