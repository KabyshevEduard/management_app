"""correct messages

Revision ID: cf04d19dbbf5
Revises: 4bb8d84ad02f
Create Date: 2025-01-24 20:01:36.844335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf04d19dbbf5'
down_revision: Union[str, None] = '4bb8d84ad02f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
