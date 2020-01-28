""" Adding business_types for duns

Revision ID: c3db0b20bdef
Revises: 6a7dfeb64b27
Create Date: 2020-01-22 18:58:55.987646

"""

# revision identifiers, used by Alembic.
revision = 'c3db0b20bdef'
down_revision = '6a7dfeb64b27'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('duns', sa.Column('business_types', sa.ARRAY(sa.Text()), nullable=True))
    op.add_column('historic_duns', sa.Column('business_types', sa.ARRAY(sa.Text()), nullable=True))
    # ### end Alembic commands ###


def downgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('duns', 'business_types')
    op.drop_column('historic_duns', 'business_types')
    # ### end Alembic commands ###
