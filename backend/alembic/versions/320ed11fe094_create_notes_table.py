"""create notes table

Revision ID: 320ed11fe094
Revises: 
Create Date: 2023-01-24 19:53:03.959087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '320ed11fe094'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.String),
        sa.Column("completed", sa.Boolean)
    )


def downgrade() -> None:
    op.drop_table("notes")
