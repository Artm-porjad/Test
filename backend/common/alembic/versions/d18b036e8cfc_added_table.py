"""added table

Revision ID: d18b036e8cfc
Revises: 0000000000
Create Date: 2022-10-28 00:01:40.336554

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd18b036e8cfc'
down_revision = '0000000000'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('first_tabl',
                    sa.Column('reg_nomer', sa.Integer(), nullable=False),
                    sa.Column('date_postup', sa.Date(), nullable=False),
                    sa.Column('name_doc', sa.String(), nullable=False),
                    sa.Column('story_doc', sa.String(), nullable=False),
                    sa.Column('foiv', sa.String(), nullable=False),
                    sa.Column('cur_aprf', sa.String(), nullable=False),
                    sa.Column('napr', sa.String(), nullable=False),
                    sa.Column('fed_num', sa.String(), nullable=False),
                    sa.Column('type_of_doc', sa.String(), nullable=False),
                    sa.Column('resh_doc', sa.String(), nullable=False),
                    sa.Column('status', sa.String(), nullable=False),
                    sa.Column('fin_oc', sa.Integer(), nullable=False),
                    sa.Column('exp_oc', sa.Integer(), nullable=False),
                    sa.Column('req_otv', sa.Integer(), nullable=False),
                    sa.Column('date_otv', sa.Date(), nullable=False),
                    sa.PrimaryKeyConstraint('reg_nomer')
                    )
    # ### end Alembic commands ###
    conn = op.get_bind()
    conn.execute('''
            insert into public.first_tabl (reg_nomer, date_postup, name_doc, story_doc, foiv, cur_aprf, napr, fed_num, type_of_doc, resh_doc, status, fin_oc, exp_oc, req_otv, date_otv)
            values  (111, '2022-01-11', 'ТЗ в рамках согласования Распоряжения', '-', 'Федеральный фонд обязательного медицинского страхования', 'Иванов', 'Здравоохранение', 'ГИС ГМП', 'ТЗ', 'Согласовано с учетом замечаний', 'Исполнено', 50, 100, 33, '2022-07-04'),
                    (222, '2022-01-11', 'ТЗ в рамках согласования Распоряжения', '-', 'Федеральный фонд обязательного медицинского страхования', 'Иванов', 'Здравоохранение', 'ГИС ГМП', 'ТЗ', 'Согласовано с учетом замечаний', 'Исполнено', 50, 100, 33, '2022-07-04'),
                    (33, '2022-01-11', 'ТЗ в рамках согласования Распоряжения', '-', 'Федеральный фонд обязательного медицинского страхования', 'Иванов', 'Здравоохранение', 'ГИС ГМП', 'ТЗ', 'Согласовано с учетом замечаний', 'Исполнено', 50, 100, 33, '2022-07-04');
        ''')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('first_tabl')
    # ### end Alembic commands ###
