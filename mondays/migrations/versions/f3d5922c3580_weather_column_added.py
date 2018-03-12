"""weather column added

Revision ID: f3d5922c3580
Revises: e4bf96b3c9ab
Create Date: 2018-03-12 11:32:42.647924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3d5922c3580'
down_revision = 'e4bf96b3c9ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('days', sa.Column('weather', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('days', 'weather')
    # ### end Alembic commands ###
