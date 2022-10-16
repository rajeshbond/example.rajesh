""" Add foreigen-key to post table 

Revision ID: 36724650254d
Revises: ac5f1ce66403
Create Date: 2022-10-15 23:14:07.666419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36724650254d'
down_revision = 'ac5f1ce66403'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts1', sa.Column('owner_id',sa.Integer(),nullable = False))
    op.create_foreign_key('posts1_users_fk',
                          source_table= "posts1",
                          referent_table= "users",
                        local_cols= ['owner_id'],
                        remote_cols=['id'],
                        ondelete= 'CASCADE')


def downgrade() -> None:
    op.drop_constraint('posts1_users_fk', table_name='posts1')
    op.drop_column('posts1', 'owner_1')
    pass
