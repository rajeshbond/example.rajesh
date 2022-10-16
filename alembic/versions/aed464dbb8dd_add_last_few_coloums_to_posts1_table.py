"""add last few coloums to posts1 table

Revision ID: aed464dbb8dd
Revises: 36724650254d
Create Date: 2022-10-16 06:26:30.127259

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aed464dbb8dd'
down_revision = '36724650254d'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.add_column('posts1', sa.Column(
                            "published",
                            sa.Boolean, nullable = False, server_default = 'True'
                                    )
                  )
    op.add_column('posts1', sa.Column(
                            "create_at",
                            sa.TIMESTAMP(timezone=True),
                            server_default = sa.text("Now()")
                                    )
                )

    pass


def downgrade() -> None:
    op.drop_column('posts1','published')
    op.drop_column('posts1', "create_at")
    pass
