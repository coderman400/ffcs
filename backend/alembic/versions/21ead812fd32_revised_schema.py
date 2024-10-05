"""revised schema

Revision ID: 21ead812fd32
Revises: 
Create Date: 2024-09-28 21:16:46.808143

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '21ead812fd32'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_groups_id', table_name='groups')
    op.drop_table('groups')
    op.add_column('courses', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('courses', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_column('courses', 'title')
    op.create_table('groups',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('slot', sa.VARCHAR(), nullable=True),
    sa.Column('professor_id', sa.INTEGER(), nullable=True),
    sa.Column('timings', sa.VARCHAR(), nullable=True),
    sa.ForeignKeyConstraint(['professor_id'], ['professors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_groups_id', 'groups', ['id'], unique=False)
    # ### end Alembic commands ###