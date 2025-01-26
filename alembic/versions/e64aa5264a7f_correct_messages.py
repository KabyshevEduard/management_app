"""correct messages

Revision ID: e64aa5264a7f
Revises: cf04d19dbbf5
Create Date: 2025-01-24 20:03:54.604405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e64aa5264a7f'
down_revision: Union[str, None] = 'cf04d19dbbf5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
