"""borrar admin

Revision ID: 5e387f050906
Revises: 6142b3b5c36c
Create Date: 2024-02-19 02:38:55.015816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '5e387f050906'
down_revision: Union[str, None] = '6142b3b5c36c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('administrador')
    op.add_column('usuario', sa.Column('es_administrador', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'es_administrador')
    op.create_table('administrador',
    sa.Column('idAdministrador', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('correoAdministrador', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('contraseñaAdministrador', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('es_administrador', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('idAdministrador'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###