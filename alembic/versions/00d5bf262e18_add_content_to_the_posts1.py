"""add content to the posts1

Revision ID: 00d5bf262e18
Revises: e5069fabba05
Create Date: 2022-10-15 22:50:31.633147

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00d5bf262e18'
down_revision = 'e5069fabba05'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts1', sa.Column('content',sa.String(), nullable= False))
    pass


def downgrade() -> None:
    op.drop_column('posts1','content')
    pass
