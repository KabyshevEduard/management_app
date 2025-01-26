"""correct

Revision ID: 607e9b0d58c0
Revises: 7470952274ea
Create Date: 2025-01-24 19:47:34.153209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '607e9b0d58c0'
down_revision: Union[str, None] = '7470952274ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
