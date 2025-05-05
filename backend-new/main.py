from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from app.utils import (
    verify_access_token, 
    ExpiredSignatureError, 
    InvalidTokenError,
)
from app.routers import auth

app = FastAPI()
app.include_router(auth.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return "Fuck off"


@app.post("/verify")
def verify_token(token: str = Body(embed=True)) -> dict:
    try:
        payload = verify_access_token(token)

        if isinstance(payload, dict):
            return {"access_token": token, "payload": payload}
        else:
            raise HTTPException(status_code=401, detail="Invalid token")

    except ExpiredSignatureError as e:
        raise HTTPException(status_code=401, detail="Token has expired") from e
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Invalid token: {e}") from e
