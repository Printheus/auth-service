from fastapi import Body, FastAPI, HTTPException
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError


from .core.models import Base
from .core.database import engine, get_db
from .core.utils import verify_access_token


#views
from .basic.views import router as basic_router


async def create_all():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)


app = FastAPI()
app.add_event_handler("startup", create_all)

app.include_router(basic_router)


@app.post("/verify")
def verify_token(token: str = Body(embed=True)) -> dict:
    try:
        payload = verify_access_token(token)
        
        if isinstance(payload, dict):
            return {"access_token": token, "payload": payload}
        else:
            raise HTTPException(status_code=401, detail="Invalid token")
            
    except ExpiredSignatureError as e:
        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        ) from e
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=401,
            detail=f"Invalid token: {e}"
        ) from e