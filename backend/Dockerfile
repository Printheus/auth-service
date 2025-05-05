FROM docker.arvancloud.ir/python:3.12-bullseye

WORKDIR /app

COPY req.pip ./

RUN pip install -r req.pip

WORKDIR /app/auth_service

CMD ["uvicorn", "auth_service.main:app", "--reload", "--port=8000"]
