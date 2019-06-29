"""Company related

Revision ID: f3c19cddc5a7
Revises: 47b770328f68
Create Date: 2019-06-29 23:02:15.729491

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f3c19cddc5a7'
down_revision = '47b770328f68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('company')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('create_at', mysql.DATETIME(), nullable=True),
    sa.Column('update_at', mysql.DATETIME(), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('desc', mysql.TEXT(), nullable=True),
    sa.Column('addr', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('website', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('logo', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('slogan', mysql.VARCHAR(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='company_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###