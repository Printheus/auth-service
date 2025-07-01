# auth-service
Authentication service

## Backend Env


|       ENV         |   DEFAULT         | REQUIRED |
|       ---         |   -------         | -------- |
|DATABASE_NAME      |"mydb"             |          |
|DATABASE_USERNAME  |"auth"             |          |
|DATABASE_PASSWORD  |-                  |TRUE      |
|DATABASE_HOST      |127.0.0.1          |          |
|PRIVATE_KEY        |"./private_key.pem"|          |
|PUBLIC_KEY         |./public_key.pem   |          |


## frontend Env


|           ENV         |   DEFAULT         | REQUIRED |
|           ---         |   -------         | -------- |
|VITE_API_BASE_URL      | -                 | TRUE     |
|VITE_API_DASHBOARD_URL | -                 | TRUE     |