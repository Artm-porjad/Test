from starlette.applications import Starlette
from sqlalchemy.ext.asyncio import create_async_engine
from starlette.routing import Route, Mount

from website.tables import get_table, post_table
from common.envars import DATABASE_URL
import utils


class Application(Starlette):
    """ Web application
    """

    def __init__(self):
        Starlette.__init__(self, routes=[
            Mount('/api', routes=[
                Route('/test', get_table, methods=["GET"]),
                Route('/test1', post_table, methods=["POST"]),
            ], )
        ])
        self.state.postgres = create_async_engine(DATABASE_URL)
