from settings import Settings
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path


class SpotifyDailyTop50Extraction:
    def __init__(self):
        settings = Settings()
        self.playlist_metadata = pd.DataFrame()
        self.data_folder = settings.data_folder
        self.database_url = settings.database_url

    def get_playlist_metadata(self) -> pd.DataFrame:
        # TODO: FIND playlist_metadata
        playlist_metadata: Path = Path(self.data_folder).joinpath(
            "112022_df_playlist_metadata.csv"
        )
        self.playlist_metadata = pd.read_csv(playlist_metadata, index_col="Unnamed: 0")
        return self.playlist_metadata

    def check_data(self) -> bool:
        """
        Various checks for given dataset.
        Should log Error if data is wrong type and Warnings if the data is duplicated or there is no data
        """
        pass

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
