"""Create Asset Type table

Revision ID: 5146049d6ffd
Revises: 
Create Date: 2024-10-16 20:44:45.516643

"""
from typing import Sequence, Union
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, TIMESTAMP, func, Column


# revision identifiers, used by Alembic.
revision: str = '5146049d6ffd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "asset_types",
    Column("id", INTEGER, primary_key=True),
    Column("description", VARCHAR(50), nullable=False),
    Column("created_at", TIMESTAMP(timezone=True), server_default=func.now()),
)


def downgrade() -> None:
    op.drop_table('asset_types')
