

from src.infra.elasticsearch.elastic_search_repository import ElasticLogRepository
from src.presentation.decorator.log_controller_decorator import LogControllerDecorator
from src.presentation.protocols.controller import Controller


def log_controller_factory(controller: Controller) -> Controller:
    log_repository = ElasticLogRepository()
    log_controller_factory = LogControllerDecorator(controller, log_repository)
    
    return log_controller_factory
    