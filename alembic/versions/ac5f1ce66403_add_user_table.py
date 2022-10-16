"""Add user table 

Revision ID: ac5f1ce66403
Revises: 00d5bf262e18
Create Date: 2022-10-15 23:00:04.783132

"""
from http import server
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac5f1ce66403'
down_revision = '00d5bf262e18'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable= False),
                    sa.Column('email',sa.String(), nullable= False),
                    sa.Column('password', sa.String(), nullable= False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default = sa.text('now()'),nullable= False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
