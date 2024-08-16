"""auto vote

Revision ID: 1f91195c65ed
Revises: fa11a35a25d1
Create Date: 2024-08-16 11:55:08.191440

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f91195c65ed'
down_revision: Union[str, None] = 'fa11a35a25d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
