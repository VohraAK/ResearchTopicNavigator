import os
import pandas as pd

PROCESSED_FIELDS = ["id", "title", "authors_parsed", "abstract"]

# df = pd.read_csv("data/raw/arXiv_10.csv")
# cleaned_df = df[PROCESSED_FIELDS]

# print(cleaned_df.info())

for chunk_i in range(1, 57):
    df = pd.read_csv(f"data/raw/arXiv_{chunk_i}.csv")
    cleaned_df = df[PROCESSED_FIELDS]
    cleaned_df.to_csv(f"data/processed/processed_arXiv_{chunk_i}.csv")
