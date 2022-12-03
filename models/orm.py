from sqlalchemy import Column, String, BigInteger, Integer, DateTime

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PlaylistMetadata(Base):
    __tablename__ = "playlist_metadata"
    id = Column("id", Integer, primary_key=True)
    playlist_id = Column("playlist.id", String)
    name = Column("playlist.name", String)
    description = Column("playlist.description", String)
    followers_total = Column("followers.total", BigInteger)
    owner_display_name = Column("owner.display_name", String)
    owner_uri = Column("owner.uri", String)
    tracks_limit = Column("tracks.limit", BigInteger)
    tracks_total = Column("tracks.total", BigInteger)
    playlist_extracted_date = Column("playlist.extracteddate", DateTime)
