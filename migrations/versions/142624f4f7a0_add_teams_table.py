"""add teams table

Revision ID: 142624f4f7a0
Revises: bcb16e8d296b
Create Date: 2022-12-05 22:26:34.032944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '142624f4f7a0'
down_revision = 'bcb16e8d296b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('candidates', schema=None) as batch_op:
        batch_op.add_column(sa.Column('team_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'teams', ['team_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('candidates', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('team_id')

    op.drop_table('teams')
    # ### end Alembic commands ###
