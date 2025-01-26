"""correct

Revision ID: 7470952274ea
Revises: 96600c68b177
Create Date: 2025-01-24 19:29:22.472085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7470952274ea'
down_revision: Union[str, None] = '96600c68b177'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
