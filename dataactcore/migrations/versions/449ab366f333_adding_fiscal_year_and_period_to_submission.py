"""adding fiscal year and period to submission

Revision ID: 449ab366f333
Revises: a0a4f1ef56ae
Create Date: 2016-08-11 13:21:49.526346

"""

# revision identifiers, used by Alembic.
revision = '449ab366f333'
down_revision = '5a9051f9bfc5'
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
    op.add_column('submission', sa.Column('reporting_fiscal_period', sa.Integer(), server_default='0', nullable=False))
    op.add_column('submission', sa.Column('reporting_fiscal_year', sa.Integer(), server_default='0', nullable=False))
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'reporting_fiscal_year')
    op.drop_column('submission', 'reporting_fiscal_period')
    ### end Alembic commands ###
