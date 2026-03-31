import pandas as pd
from notebooks.config import DATASET_PATH, CHUNK_SIZE

def load_dataset():

    print("Loading EyeT4 dataset in chunks (ALL columns)")
    chunks = []

    for chunk in pd.read_csv(
        DATASET_PATH,
        chunksize=CHUNK_SIZE,
        low_memory=False
    ):
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)

    print("Dataset loaded successfully")
    print("Total rows:", len(df))
    print("Total columns:", len(df.columns))
    print("Column names:")
    print(list(df.columns))

    return df


if __name__ == "__main__":
    df = load_dataset()
    print(df.head())