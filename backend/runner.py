import os
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=os.environ.get("PORT", 8000),
        root_path=os.environ.get("PREFIX")
        )