---
tags: [reference, python, data]
created: 2026-01-24T10:00:00
modified: 2026-02-03T14:00:00
---

# Pandas Tips

Patterns I keep coming back to for data manipulation. Assumes familiarity with DataFrames — these are the non-obvious parts. See [[Python_Tips]] for general Python patterns.

## Loading and Saving

```python
df = pd.read_csv("data.csv", usecols=["title", "abstract"])   # only load needed columns
df = pd.read_json("papers.json", lines=True)                  # JSONL format
df.to_parquet("data.parquet", index=False)                     # faster than CSV for large files
```

Parquet is much faster than CSV for repeated reads. We use it in the [[Data_Pipeline]] for intermediate data storage.

## Filtering

```python
df[df["year"] >= 2020]
df.query("year >= 2020 and venue == 'ACL'")   # query syntax is more readable for complex conditions
df[df["abstract"].str.contains("attention", case=False, na=False)]
```

The `na=False` in `str.contains` is important — without it, rows with NaN values raise an error or return NaN instead of False.

## GroupBy

```python
df.groupby("venue")["citations"].agg(["mean", "median", "count"])
df.groupby("year").size().reset_index(name="count")
```

Always reset_index after groupby if you need the result as a regular DataFrame.

## Apply vs Vectorized Operations

`apply` is slow — it's a Python loop. Prefer vectorized operations:

```python
# Slow
df["abstract_len"] = df["abstract"].apply(len)

# Fast
df["abstract_len"] = df["abstract"].str.len()
```

For complex transformations that can't be vectorized, `apply` is fine — but profile first.

## Memory Optimization

```python
df["year"] = df["year"].astype("int16")          # downcast integer types
df["venue"] = df["venue"].astype("category")     # categoricals use much less memory
```

On our 500k paper dataset, downcasting reduced memory usage from 4.2GB to 1.1GB.

## Merging

```python
merged = df1.merge(df2, on="paper_id", how="left")  # always specify how explicitly
```

Default merge is inner join — this silently drops rows. Use `how="left"` to preserve all rows from df1 and flag unmatched rows. Check `merged.shape` vs `df1.shape` after merging to catch unexpected drops.

## Useful with [[Numpy_Guide]]

Pandas operations on numeric columns delegate to NumPy under the hood. For heavy numerical operations, extract to NumPy arrays for speed:

```python
embeddings = df["embedding"].to_numpy()  # list of arrays → numpy array
```
