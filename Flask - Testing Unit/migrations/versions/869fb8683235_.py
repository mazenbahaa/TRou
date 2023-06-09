"""empty message

Revision ID: 869fb8683235
Revises: 
Create Date: 2022-03-19 04:16:05.730801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '869fb8683235'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('CompanyName', sa.String(length=100), nullable=False),
    sa.Column('Location', sa.String(length=40), nullable=False),
    sa.Column('Address', sa.String(length=150), nullable=False),
    sa.Column('Email', sa.String(length=120), nullable=False),
    sa.Column('Password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('CompanyName'),
    sa.UniqueConstraint('Email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('manager')
    # ### end Alembic commands ###
