"""Initial migration1

Revision ID: 2dfbec93134e
Revises: 
Create Date: 2024-10-03 11:21:29.311972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2dfbec93134e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=256), nullable=False),
    sa.Column('isbn', sa.String(length=256), nullable=False),
    sa.Column('is_lent', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('members')
    op.drop_table('books')
    # ### end Alembic commands ###
