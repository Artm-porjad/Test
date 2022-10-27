import asyncio
import json

from sqlalchemy.ext.asyncio import AsyncEngine
from datetime import date

from sqlalchemy import insert, delete
from starlette.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from common.models.table import first_tabl, second_tabl
from utils import JsonParams


async def get_table(request):
    d = [[
        "Рег. номер МКС в СЭД",
        "Дата поступления в МКС",
        "Название документа",
        "В дополнение к или взамен (предыстория документа)",
        "ФОИВ",
        "Куратор АПРФ",
        "Направление",
        "Фед. Проект / ГИС",
        "Тип документа",
        "Решение по документу",
        "Текущий статус",
        "Финансовая оценка, тыс. руб.",
        "Экспертная оценка, тыс. руб.",
        "Реквизиты ответа в ведомство",
        "Дата ответа в ведомство",
    ]]
    engine = request.app.state.postgres
    async with AsyncSession(engine) as session:
        first_table = (await session.execute(first_tabl.select())).fetchall()
        second_table = (await session.execute(second_tabl.select())).fetchall()
        c = [[] for i in range(15)]
        for row in second_table:
            n = len(row)
            for j in range(n):
                if row[j]:
                    c[j].append(row[j])
        c[0] = []
        a = []
        for row in first_table:
            b = []
            n = len(row)
            for j in range(n):
                if j == 1 or j == 14:
                    b.append(str(row[j].day) + '.' + str(row[j].month) + '.' + str(row[j].year))
                else:
                    b.append(row[j])
            a.append(b)
        response = d + [c] + a
    return JSONResponse(response)


async def post_table(request):
    engine = request.app.state.postgres
    data = json.loads((await request.form())['data'])[2:]
    n = len(data)
    async with AsyncSession(engine) as session:
        for i in range(n):
            query = delete(first_tabl).where(first_tabl.c.reg_nomer == int(data[i][0]))
            await session.execute(query)
            if '-' in data[i][1]:
                a = data[i][1].split('-')
                data[i][1] = a[2]+'.'+a[1]+'.'+a[0]
            if '-' in data[i][14]:
                a = data[i][14].split('-')
                data[i][14] = a[2] + '.' + a[1] + '.' + a[0]
            query = first_tabl.insert().values(
                reg_nomer=int(data[i][0]),
                date_postup=date(year=int(data[i][1][-4:]), month=int(data[i][1][data[i][1].find('.')+1:data[i][1].find('.', data[i][1].find('.')+1)]), day=int(data[i][1][:data[i][1].find('.')])),
                name_doc=data[i][2],
                story_doc=data[i][3],
                foiv=data[i][4],
                cur_aprf=data[i][5],
                napr=data[i][6],
                fed_num=data[i][7],
                type_of_doc=data[i][8],
                resh_doc=data[i][9],
                status=data[i][10],
                fin_oc=int(data[i][11]),
                exp_oc=int(data[i][12]),
                req_otv=int(data[i][13]),
                date_otv=date(year=int(data[i][14][-4:]), month=int(data[i][14][data[i][14].find('.')+1:data[i][14].find('.', data[i][14].find('.')+1)]), day=int(data[i][14][:data[i][14].find('.')])),
            )
            await session.execute(query)
        await session.commit()
        print('ok')
    return JSONResponse('ok')