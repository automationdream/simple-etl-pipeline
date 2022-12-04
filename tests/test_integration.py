import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from models.orm import PlaylistMetadata
from settings import Settings
import ETL

settings = Settings()
DEV_DATABASE_URI = settings.dev_database_url


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


class TestDatabaseLoader:
    def test_get_playlist_metadata(self):
        top50 = ETL.SpotifyDailyTop50Extraction()
        # need to override for test directory
        top50.data_folder = "tests/dataset"
        top50.get_playlist_metadata()
        assert top50.playlist_metadata.shape[0] == 1800

    def test_load_playlist_metadata(self, db_session: Session):
        top50 = ETL.SpotifyDailyTop50Extraction()
        top50.data_folder = "tests/dataset"
        # need to override for test database
        top50.database_url = settings.dev_database_url
        top50.get_playlist_metadata()
        top50.load_to_database()
        # Check
        result = db_session.query(PlaylistMetadata.playlist_id)
        assert result.count() == 1800

    def test_extract_datasets(self):
        top50 = ETL.SpotifyDailyTop50Extraction()
        top50.data_folder = "tests/dataset"
        assert top50.get_datasets() == 3
