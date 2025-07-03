import os
import json
import pprint
import pandas as pd

from config import CHUNK_SIZE

chunks = pd.read_json("./arxiv-metadata-oai-snapshot.json", chunksize=CHUNK_SIZE, lines=True)

for i, chunk in enumerate(chunks):
    # save each chunk as a CSV file
    save = chunk.to_csv(f"arXiv_{i+1}.csv")
