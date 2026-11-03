"""rename visa_options Category to category

Revision ID: 4beed23c0704
Revises: 43eb44323b9a
Create Date: 2026-11-03 04:05:59.949101

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4beed23c0704'
down_revision: Union[str, Sequence[str], None] = '43eb44323b9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
       op.alter_column("visa_options", "Category", new_column_name="category")


def downgrade() -> None:
       op.alter_column("visa_options", "category", new_column_name="Category")
