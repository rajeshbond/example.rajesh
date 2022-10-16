"""Creating posts1 table 

Revision ID: e5069fabba05
Revises: 
Create Date: 2022-10-15 22:37:17.397774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5069fabba05'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts1',sa.Column('id',sa.Integer(),nullable = False,primary_key= True),
                    sa.Column('title',sa.String(),nullable = False))
    
    pass


def downgrade() -> None:
    op.drop_table('posts1')
    pass
