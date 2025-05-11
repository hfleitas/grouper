# Step 1

1. Login to your [Fabric Workspace](https://app.fabric.microsoft.com/).
2. Create an Eventhouse if one does not already exist and run queryset [test22.kql](./kql/test22.kql).
3. Download the following [Notebook](./notebook/WideFile.py) and import it to your Fabric workspace.
4. Paste into the first codecell your parquet file https SAS URI.
5. Paste the Eventhouse query URI and database name.
6. Click Run All till both code cells complete successfully.
7. Return to the queryset test22.kql and get a count of records in the table, it should match that of your file.
8. Run queryset [function.kql](./kql/function.kql). You may adjust the function as needed to pull out the desired key-value or fields as necessary.
9. Rerun the Notebook.
10. Check the count on the target table of the update policy and sample a few rows to verify they appear as expected.
11. Lower the Eventhouse caching policy on the raw/bronze table (test22) to zero or as necessary.
12. Verify OneLake availability is enabled for both tables of the update policy.
13. Lower the mirroring policy as needed, either for the entire database or per table.
