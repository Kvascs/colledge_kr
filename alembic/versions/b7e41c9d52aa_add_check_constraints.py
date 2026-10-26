"""add check constraints to movies

Revision ID: b7e41c9d52aa
Revises: a08ab2f2c2a3
Create Date: 2026-10-26 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'b7e41c9d52aa'
down_revision: Union[str, Sequence[str], None] = 'a08ab2f2c2a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # SQLite не умеет добавлять ограничения через ALTER TABLE, поэтому batch-режим
    with op.batch_alter_table('movies') as batch_op:
        batch_op.create_check_constraint(
            'check_movie_rating_range', 'rating >= 0 AND rating <= 10')
        batch_op.create_check_constraint(
            'check_movie_year_1888', 'year >= 1888')


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('movies') as batch_op:
        batch_op.drop_constraint('check_movie_year_1888', type_='check')
        batch_op.drop_constraint('check_movie_rating_range', type_='check')
