from pathlib import Path

import ETL
from models.commons import DataType


def test_find_dataset():
    top50 = ETL.SpotifyDailyTop50Extraction()
    top50.data_folder = "tests/dataset"
    playlist_metadata = top50.find_dataset(DataType.PlaylistMetadata)
    assert playlist_metadata == Path("tests/dataset/112022_df_playlist_metadata.csv")
