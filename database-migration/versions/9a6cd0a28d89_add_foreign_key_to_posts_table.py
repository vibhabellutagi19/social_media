"""add foreign key to posts table

Revision ID: 9a6cd0a28d89
Revises: 1d0b47a774ff
Create Date: 2024-08-16 11:50:13.367415

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9a6cd0a28d89"
down_revision: Union[str, None] = "1d0b47a774ff"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts_v2", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts_v2",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_fk", table_name="posts_v2")
    op.drop_column("posts_v2", "owner_id")
    pass
