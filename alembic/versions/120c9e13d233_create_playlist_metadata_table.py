"""create playlist metadata table

Revision ID: 120c9e13d233
Revises: 
Create Date: 2022-12-03 19:19:50.845041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "120c9e13d233"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "playlist_metadata",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("playlist.id", sa.String(), nullable=True),
        sa.Column("playlist.name", sa.String(), nullable=True),
        sa.Column("playlist.description", sa.String(), nullable=True),
        sa.Column("followers.total", sa.BigInteger(), nullable=True),
        sa.Column("owner.display_name", sa.String(), nullable=True),
        sa.Column("owner.uri", sa.String(), nullable=True),
        sa.Column("tracks.limit", sa.BigInteger(), nullable=True),
        sa.Column("tracks.total", sa.BigInteger(), nullable=True),
        sa.Column("playlist.extracteddate", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("playlist_metadata")
    # ### end Alembic commands ###
