"""add content column to posts table

Revision ID: 21ef658b9995
Revises: b6ba577173c7
Create Date: 2024-08-16 11:42:23.629379

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "21ef658b9995"
down_revision: Union[str, None] = "b6ba577173c7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts_v2", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts_v2", "content")
    pass
