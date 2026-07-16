"""update order model"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision = "312c6c13f9eb"
down_revision = "01892cd95ebe"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Step 1: Nullable column add karo
    op.add_column(
        "order",
        sa.Column("order_date", sa.DateTime(), nullable=True)
    )

    # Step 2: Existing rows ko value do
    op.execute("""
        UPDATE `order`
        SET order_date = NOW()
        WHERE order_date IS NULL
    """)

    # Step 3: Ab NOT NULL bana do
    op.alter_column(
        "order",
        "order_date",
        existing_type=sa.DateTime(),
        nullable=False
    )

def downgrade() -> None:
    op.drop_column("order", "order_date")