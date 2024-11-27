from app.schemas.healthcheck import HealthCheck

def get_root():
    return {"status": "OK"}


def get_health() -> HealthCheck:
    return HealthCheck(status="OK")