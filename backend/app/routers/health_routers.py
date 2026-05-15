from fastapi import APIRouter, status

from ..configs import ConfigAppFastAPI
from ..schemas import HealthCheckResponse

health_router = APIRouter(prefix=ConfigAppFastAPI.API_PREFIX)


@health_router.get(
    '/health',
    response_model=HealthCheckResponse,
    status_code=status.HTTP_200_OK,
)
def health_check():
    return {
        'status': 'ok',
        'service': ConfigAppFastAPI.PROJECT_NAME,
        'version': ConfigAppFastAPI.PROJECT_VERSION,
    }
