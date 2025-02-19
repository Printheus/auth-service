from fastapi import FastAPI
from .core.models import Base
from .core.database import engine, get_db

#views
from .basic.views import router as basic_router


async def create_all():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)


app = FastAPI()
app.add_event_handler("startup", create_all)

app.include_router(basic_router)
