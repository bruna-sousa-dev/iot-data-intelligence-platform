from fastapi import FastAPI

from .configs.settings import ConfigAppFastAPI
from .routers import health_router

app = FastAPI(
    title=ConfigAppFastAPI.PROJECT_NAME,
    description=ConfigAppFastAPI.PROJECT_DESCRIPTION,
    version=ConfigAppFastAPI.PROJECT_VERSION,
)

app.include_router(health_router)
