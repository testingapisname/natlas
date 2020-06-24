"""add udpScan to agent config

Revision ID: d4685e98a91f
Revises: a1738920a0d3
Create Date: 2019-10-09 18:27:10.376631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d4685e98a91f"
down_revision = "a1738920a0d3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("agent_config", sa.Column("udpScan", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("agent_config", "udpScan")
    # ### end Alembic commands ###
