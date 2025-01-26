"""correct

Revision ID: 4bb8d84ad02f
Revises: 607e9b0d58c0
Create Date: 2025-01-24 19:57:49.334976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4bb8d84ad02f'
down_revision: Union[str, None] = '607e9b0d58c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
