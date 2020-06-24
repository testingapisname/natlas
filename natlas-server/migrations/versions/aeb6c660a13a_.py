"""empty message

Revision ID: aeb6c660a13a
Revises: 271044238ee1
Create Date: 2018-06-27 01:33:47.812346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "aeb6c660a13a"
down_revision = "271044238ee1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "scope_item",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("target", sa.String(), nullable=True),
        sa.Column("blacklist", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("target"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("scope_item")
    # ### end Alembic commands ###
