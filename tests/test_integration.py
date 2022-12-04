import pytest
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models.orm import PlaylistMetadata
from settings import Settings

settings = Settings()
DEV_DATABASE_URI = settings.dev_database_url
PLAYLIST_METADATA = "tests/dataset/112022_df_playlist_metadata.csv"
DATA_FOLDER = "tests/dataset"


@pytest.fixture(scope="module")
def db_session():
    """
    Instantiates the session with dev database.
    Before first run please make sure that the dev database is running and the migration is performed.
    alembic --name test upgrade head
    """
    # Create connection
    engine = create_engine(DEV_DATABASE_URI, echo=False)
    Session = sessionmaker(bind=engine)
    session = Session(autocommit=True)

    # Perform tests
    yield session

    # Tear down
    session.execute("""TRUNCATE TABLE playlist_metadata restart identity""")

    # Close connection
    session.close()


class DatabaseLoader(Settings):
    settings: Settings

    def get_playlist_metadata(self) -> pd.DataFrame:
        pass

    def check_data(self) -> bool:
        """
        Various checks for given dataset.
        Should log Error if data is wrong type and Warnings if the data is duplicated or there is no data
        """
        pass

    def load_to_database(self) -> bool:
        """Should log Error if data is wrong type and Warnings if the data is duplicated or there is no data"""
        pass


class TestDatabaseLoader:
    def test_load_playlist_metadata(self, db_session: Session):
        playlist_metadata = pd.read_csv(PLAYLIST_METADATA, index_col="Unnamed: 0")
        engine = create_engine(DEV_DATABASE_URI, echo=False)
        playlist_metadata.to_sql(
            "playlist_metadata",
            con=engine,
            if_exists="append",
            schema=None,
            index=False,
        )
        result = db_session.query(PlaylistMetadata.playlist_id)
        assert result.count() == 1800
