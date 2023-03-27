
from src.infra.elasticsearch.elastic_search_repository import ElasticLogRepository
from src.presentation.controllers.log_controller import LogController
from src.presentation.protocols.controller import Controller


def log_controller_factory() -> Controller:
    log_repository = ElasticLogRepository()
    log_controller_factory = LogController(log_repository)
    
    return log_controller_factory
    