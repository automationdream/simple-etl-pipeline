from pydantic import BaseSettings, PostgresDsn, DirectoryPath


class Settings(BaseSettings):
    database_url: PostgresDsn = (
        "postgresql://potatoes:tomatoes@127.0.0.1:5432/simple-etl"
    )
    dev_database_url: PostgresDsn = (
        "postgresql://potatoes:tomatoes@127.0.0.1:5433/dev-etl"
    )
    playlist_metadata_pattern: str = "df_playlist_metadata.csv"
    playlist_tracks_metadata_pattern: str = "df_playlist_tracks_metadata.csv"
    tracks_metadata_pattern: str = "df_tracks_metadata.csv"
    data_folder: DirectoryPath = "dataset"
    kaggle_datasets_url: str = "bwandowando/daily-spotify-top-50-of-60-countries"


settings = Settings()
