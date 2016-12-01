"""Add sanity check to tas

Revision ID: 9dded6e6bf79
Revises: 180c6e439a69
Create Date: 2016-11-02 17:34:03.314917

"""

# revision identifiers, used by Alembic.
revision = '9dded6e6bf79'
down_revision = '180c6e439a69'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tas_lookup_sanity_check', 'tas_lookup', ['account_num', 'allocation_transfer_agency', 'agency_identifier', 'beginning_period_of_availability', 'ending_period_of_availability', 'availability_type_code', 'main_account_code', 'sub_account_code'])
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tas_lookup_sanity_check', 'tas_lookup', type_='unique')
    ### end Alembic commands ###
