"""Making HistoricDuns table

Revision ID: 06d5bc68c29a
Revises: 653d47c65df8
Create Date: 2019-07-24 20:46:56.121706

"""

# revision identifiers, used by Alembic.
revision = '06d5bc68c29a'
down_revision = '653d47c65df8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historic_duns',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('duns_id', sa.Integer(), nullable=False),
    sa.Column('awardee_or_recipient_uniqu', sa.Text(), nullable=True),
    sa.Column('legal_business_name', sa.Text(), nullable=True),
    sa.Column('dba_name', sa.Text(), nullable=True),
    sa.Column('activation_date', sa.Date(), nullable=True),
    sa.Column('registration_date', sa.Date(), nullable=True),
    sa.Column('expiration_date', sa.Date(), nullable=True),
    sa.Column('last_sam_mod_date', sa.Date(), nullable=True),
    sa.Column('address_line_1', sa.Text(), nullable=True),
    sa.Column('address_line_2', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('zip', sa.Text(), nullable=True),
    sa.Column('zip4', sa.Text(), nullable=True),
    sa.Column('country_code', sa.Text(), nullable=True),
    sa.Column('congressional_district', sa.Text(), nullable=True),
    sa.Column('business_types_codes', sa.ARRAY(sa.Text()), nullable=True),
    sa.Column('ultimate_parent_unique_ide', sa.Text(), nullable=True),
    sa.Column('ultimate_parent_legal_enti', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('duns_id')
    )
    op.create_index(op.f('ix_historic_duns_awardee_or_recipient_uniqu'), 'historic_duns', ['awardee_or_recipient_uniqu'], unique=False)
    # ### end Alembic commands ###


def downgrade_data_broker():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_historic_duns_awardee_or_recipient_uniqu'), table_name='historic_duns')
    op.drop_table('historic_duns')
    # ### end Alembic commands ###

