"""Add Course

Revision ID: 6566a427d78b
Revises: c010c72ebc7a
Create Date: 2024-01-12 09:23:22.939563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6566a427d78b'
down_revision = 'c010c72ebc7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('photo_url', sa.String(length=50), nullable=True),
    sa.Column('pass_mark', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    # ### end Alembic commands ###