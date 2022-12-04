from typing import Union
from models.commons import DataType
from settings import Settings
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
import logging

logger = logging.getLogger()


class SpotifyDailyTop50Extraction:
    def __init__(self):
        settings = Settings()
        self.playlist_metadata = pd.DataFrame()
        self.data_folder = settings.data_folder
        self.database_url = settings.database_url
        self.playlist_metadata_pattern = settings.playlist_metadata_pattern
        self.playlist_tracks_metadata_pattern = (
            settings.playlist_tracks_metadata_pattern
        )
        self.tracks_metadata_pattern = settings.tracks_metadata_pattern

    def get_playlist_metadata(self) -> pd.DataFrame:
        playlist_metadata: Path = self.find_dataset(DataType.PlaylistMetadata)
        if playlist_metadata:
            if self.check_playlist_metadata(playlist_metadata):
                self.playlist_metadata = pd.read_csv(
                    playlist_metadata, index_col="Unnamed: 0"
                )
        return self.playlist_metadata

    def check_playlist_metadata(self, file: Path) -> bool:
        """
        Various checks for given dataset.
        Should log Error if data is wrong type and Warnings if the data is duplicated or there is no data
        """
        df = pd.read_csv(file)
        is_empty = df.empty
        if is_empty:
            logger.warning("Dataset is empty")
        df_columns = df.columns.to_list()
        required_columns = {"Unnamed: 0", "playlist.id", "playlist.name"}
        contains_defined_columns = required_columns.issubset(set(df_columns))
        if not contains_defined_columns:
            logger.warning("Dataset does not contain required columns")

        return all([not is_empty, contains_defined_columns])

    def load_to_database(self) -> bool:
        # TODO: Validate data
        if not self.playlist_metadata.empty:
            engine = create_engine(self.database_url, echo=False)
            self.playlist_metadata.to_sql(
                "playlist_metadata",
                con=engine,
                if_exists="append",
                schema=None,
                index=False,
            )
            return True
        return False

    def find_dataset(self, dataset_type: DataType) -> Union[Path, None]:
        """Find first dataset matching the pattern"""
        directory = Path(self.data_folder)
        pattern = None

        if dataset_type == DataType.PlaylistMetadata:
            pattern = self.playlist_metadata_pattern
        elif dataset_type == DataType.PlaylistTracksMetadata:
            pattern = self.playlist_tracks_metadata_pattern
        elif dataset_type == DataType.TracksMetadata:
            pattern = self.tracks_metadata_pattern
        else:
            NotImplementedError()

        lookup = directory.rglob(f"*{pattern}")
        results = list(lookup)
        if results:
            return results[0]

        return None
