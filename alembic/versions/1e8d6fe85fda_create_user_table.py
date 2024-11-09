"""Create User Table

Revision ID: 1e8d6fe85fda
Revises: 5146049d6ffd
Create Date: 2024-10-16 21:11:28.633496

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, TIMESTAMP, func, Column


# revision identifiers, used by Alembic.
revision: str = '1e8d6fe85fda'
down_revision: Union[str, None] = '5146049d6ffd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "users",
    Column("id", INTEGER, primary_key=True),
    Column("email", VARCHAR(50), nullable=False, unique=True),
    Column("password", VARCHAR(100), nullable=False),
    Column("created_at", TIMESTAMP(timezone=True), server_default=func.now()),
)

def downgrade() -> None:
    op.drop_table('users')
