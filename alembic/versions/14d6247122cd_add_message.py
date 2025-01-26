"""Add message

Revision ID: 14d6247122cd
Revises: b9af2771e114
Create Date: 2025-01-19 13:53:19.384864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14d6247122cd'
down_revision: Union[str, None] = 'b9af2771e114'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
