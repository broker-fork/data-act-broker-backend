"""create FileRequest table for D file generation

Revision ID: 4d66a8d6e11b
Revises: bcdf1134f0df
Create Date: 2017-10-19 14:28:03.788883

"""

# revision identifiers, used by Alembic.
revision = '4d66a8d6e11b'
down_revision = 'bcdf1134f0df'
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
    op.create_table('file_request',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('file_request_id', sa.Integer(), nullable=False),
    sa.Column('request_date', sa.Date(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('parent_job_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('agency_code', sa.Text(), nullable=False),
    sa.Column('file_type', sa.Text(), nullable=False),
    sa.Column('is_cached_file', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['job.job_id'], name='fk_file_request_job_id'),
    sa.PrimaryKeyConstraint('file_request_id')
    )
    op.create_index(op.f('ix_file_request_agency_code'), 'file_request', ['agency_code'], unique=False)
    op.create_index(op.f('ix_file_request_end_date'), 'file_request', ['end_date'], unique=False)
    op.create_index(op.f('ix_file_request_file_type'), 'file_request', ['file_type'], unique=False)
    op.create_index(op.f('ix_file_request_parent_job_id'), 'file_request', ['parent_job_id'], unique=False)
    op.create_index(op.f('ix_file_request_request_date'), 'file_request', ['request_date'], unique=False)
    op.create_index(op.f('ix_file_request_start_date'), 'file_request', ['start_date'], unique=False)
    op.add_column('job', sa.Column('from_cached', sa.Boolean(), server_default='False', nullable=False))
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job', 'from_cached')
    op.drop_index(op.f('ix_file_request_start_date'), table_name='file_request')
    op.drop_index(op.f('ix_file_request_request_date'), table_name='file_request')
    op.drop_index(op.f('ix_file_request_parent_job_id'), table_name='file_request')
    op.drop_index(op.f('ix_file_request_file_type'), table_name='file_request')
    op.drop_index(op.f('ix_file_request_end_date'), table_name='file_request')
    op.drop_index(op.f('ix_file_request_agency_code'), table_name='file_request')
    op.drop_table('file_request')
    ### end Alembic commands ###

