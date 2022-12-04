from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    database_url: PostgresDsn = (
        "postgresql://potatoes:tomatoes@127.0.0.1:5432/simple-etl"
    )
    dev_database_url: PostgresDsn = (
        "postgresql://potatoes:tomatoes@127.0.0.1:5433/dev-etl"
    )
    playlist_metadata = "df_playlist_metadata"
    playlist_tracks_metadata = "df_playlist_tracks_metadata"
    tracks_metadata = "df_tracks_metadata"


settings = Settings()
