"""empty message

Revision ID: 213a14197060
Revises: 39067c42c04c
Create Date: 2025-11-07 19:44:35.832029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213a14197060'
down_revision = '39067c42c04c'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('contato_usuario', schema=None) as batch_op:
        batch_op.create_unique_constraint(
            'uq_contato_usuario_usuario_id',
            ['usuario_id']
        )


def downgrade():
    with op.batch_alter_table('contato_usuario', schema=None) as batch_op:
        batch_op.drop_constraint(
            'uq_contato_usuario_usuario_id',
            type_='unique'
        )