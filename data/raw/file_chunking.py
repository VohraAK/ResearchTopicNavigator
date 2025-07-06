import os
import json
import pprint
import pandas as pd

from config import CHUNK_SIZE

chunks = pd.read_json("./data/raw/arxiv-metadata-oai-snapshot.json", chunksize=CHUNK_SIZE, lines=True)

for i, chunk in enumerate(chunks):
    # save each chunk as a CSV file
    save = chunk.to_csv(f"./data/raw/arXiv_{i+1}.csv")
