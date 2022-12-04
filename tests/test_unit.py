from pathlib import Path

import ETL
from models.commons import DataType


def test_find_dataset():
    top50 = ETL.SpotifyDailyTop50Extraction()
    top50.data_folder = "tests/dataset"
    playlist_metadata = top50.find_dataset(DataType.PlaylistMetadata)
    assert playlist_metadata == Path("tests/dataset/112022_df_playlist_metadata.csv")


def test_check_data():
    top50 = ETL.SpotifyDailyTop50Extraction()
    top50.data_folder = "tests/dataset"
    playlist_metadata = top50.find_dataset(DataType.PlaylistMetadata)
    if playlist_metadata:
        valid = top50.check_playlist_metadata(playlist_metadata)
        assert valid


def test_unzip_files():
    top50 = ETL.SpotifyDailyTop50Extraction()
    top50.data_folder = "tests/dataset"
    unzipped = top50.unzip_files(Path(top50.data_folder))
    assert unzipped == 3
