"""empty message

Revision ID: 951f34a42fe5
Revises: 213a14197060
Create Date: 2025-11-07 19:50:51.281832

"""
from alembic import op
import sqlalchemy as sa


revision = '951f34a42fe5'
down_revision = '213a14197060'
branch_labels = None
depends_on = None


def upgrade():
    # contato_usuario
    with op.batch_alter_table('contato_usuario', schema=None) as batch_op:
        # adiciona a coluna correta
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=False))

        # cria UNIQUE corretamente
        batch_op.create_unique_constraint(
            'uq_contato_usuario_usuario_id',
            ['usuario_id']
        )

        # cria FOREIGN KEY com nome correto
        batch_op.create_foreign_key(
            'fk_contato_usuario',
            'usuario',
            ['usuario_id'],
            ['id']
        )

        # remove a coluna antiga
        batch_op.drop_column('fk_contato_usuario')

    # venda
    with op.batch_alter_table('venda', schema=None) as batch_op:
        batch_op.add_column(sa.Column('usuario_id', sa.Integer(), nullable=True))

        batch_op.create_foreign_key(
            'fk_venda_usuario',
            'usuario',
            ['usuario_id'],
            ['id']
        )

        batch_op.drop_column('fk_venda_usuario')


def downgrade():
    # venda
    with op.batch_alter_table('venda', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fk_venda_usuario', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_venda_usuario', type_='foreignkey')
        batch_op.create_foreign_key(
            'fk_venda_usuario',
            'usuario',
            ['fk_venda_usuario'],
            ['id']
        )
        batch_op.drop_column('usuario_id')

    # contato_usuario
    with op.batch_alter_table('contato_usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fk_contato_usuario', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_contato_usuario', type_='foreignkey')
        batch_op.create_foreign_key(
            'fk_contato_usuario',
            'usuario',
            ['fk_contato_usuario'],
            ['id']
        )
        batch_op.drop_constraint('uq_contato_usuario_usuario_id', type_='unique')
        batch_op.drop_column('usuario_id')
