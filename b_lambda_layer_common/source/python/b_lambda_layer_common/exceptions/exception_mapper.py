import logging
from typing import Union, Dict, Any, Type

logger = logging.getLogger(__name__)

try:
    from b_lambda_layer_common.exceptions.container.not_reached_error import NotReachedError
    from b_lambda_layer_common.exceptions.container.dependency_error import DependencyError
    from b_lambda_layer_common.exceptions.container.already_exists_error import AlreadyExistsError
    from b_lambda_layer_common.exceptions.container.bad_request_error import BadRequestError
    from b_lambda_layer_common.exceptions.container.conflict_error import ConflictError
    from b_lambda_layer_common.exceptions.container.failed_rollback_error import FailedRollbackError
    from b_lambda_layer_common.exceptions.container.forbidden_error import ForbiddenError
    from b_lambda_layer_common.exceptions.container.internal_error import InternalError
    from b_lambda_layer_common.exceptions.container.malformed_permission_error import MalformedPermissionError
    from b_lambda_layer_common.exceptions.container.misconfigured_error import MisconfiguredError
    from b_lambda_layer_common.exceptions.container.not_found_error import NotFoundError
    from b_lambda_layer_common.exceptions.container.unauthorized_error import UnauthorizedError
    from b_lambda_layer_common.exceptions.http_exception import HttpException
except ImportError as ex:
    logger.exception(f'Failed import.')
    from .container.not_reached_error import NotReachedError
    from .container.dependency_error import DependencyError
    from .container.already_exists_error import AlreadyExistsError
    from .container.bad_request_error import BadRequestError
    from .container.conflict_error import ConflictError
    from .container.failed_rollback_error import FailedRollbackError
    from .container.forbidden_error import ForbiddenError
    from .container.internal_error import InternalError
    from .container.malformed_permission_error import MalformedPermissionError
    from .container.misconfigured_error import MisconfiguredError
    from .container.not_found_error import NotFoundError
    from .container.unauthorized_error import UnauthorizedError
    from .http_exception import HttpException


class ExceptionMapper:
    __EXCEPTION_MAP: Dict[str, Type[HttpException]] = {
        AlreadyExistsError.identifier(): AlreadyExistsError,
        BadRequestError.identifier(): BadRequestError,
        ConflictError.identifier(): ConflictError,
        DependencyError.identifier(): DependencyError,
        FailedRollbackError.identifier(): FailedRollbackError,
        ForbiddenError.identifier(): ForbiddenError,
        InternalError.identifier(): InternalError,
        MalformedPermissionError.identifier(): MalformedPermissionError,
        MisconfiguredError.identifier(): MisconfiguredError,
        NotFoundError.identifier(): NotFoundError,
        NotReachedError.identifier(): NotReachedError,
        UnauthorizedError.identifier(): UnauthorizedError
    }

    @staticmethod
    def map_and_raise(exception: Union[str, Dict[str, Any], Exception]) -> None:
        logger.info(
            f'Trying to map error...\n'
            f'{exception=}'
        )

        if isinstance(exception, str):
            try:
                raise ExceptionMapper.__EXCEPTION_MAP[exception]()
            except (KeyError, TypeError):
                pass
        elif isinstance(exception, dict):
            try:
                ex_class = ExceptionMapper.__EXCEPTION_MAP[exception['identifier']]
                raise ex_class(exception['message'])
            except (KeyError, TypeError):
                pass
        elif isinstance(exception, Exception):
            raise exception

        raise ValueError('Appropriate exception could not be found.')
