"""Correct

Revision ID: 96600c68b177
Revises: 2d241beb5c5d
Create Date: 2025-01-19 21:15:47.598183

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '96600c68b177'
down_revision: Union[str, None] = '2d241beb5c5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
