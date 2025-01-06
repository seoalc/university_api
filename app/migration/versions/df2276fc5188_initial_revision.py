"""Initial revision

Revision ID: df2276fc5188
Revises: 37939b3e94f3
Create Date: 2025-01-06 11:48:37.551907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df2276fc5188'
down_revision: Union[str, None] = '37939b3e94f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('majors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('major_name', sa.String(length=100), nullable=False),
    sa.Column('major_description', sa.Text(), nullable=False),
    sa.Column('count_students', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('major_name')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.String(length=15), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('enrollment_year', sa.Integer(), nullable=False),
    sa.Column('course', sa.Integer(), nullable=False),
    sa.Column('special_notes', sa.String(length=255), nullable=True),
    sa.Column('major_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['major_id'], ['majors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    op.drop_table('majors')
    # ### end Alembic commands ###
