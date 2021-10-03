import logging
from typing import Optional


class LoggingManager:
    """
    Class responsible for common logging setup.
    """

    def __init__(
            self,
            *,
            log_level: int = logging.INFO,
            formatter: Optional[logging.Formatter] = None
    ) -> None:
        """
        Constructor.

        :param log_level: Default log level set for logging.
        :param formatter: Default formatter set for logging.
        """

        self.log_level = log_level
        self.formatter = formatter

    def setup_logging(self) -> None:
        """
        Set up the logging with the default parameters.
        """
        try:
            root_logger = logging.getLogger()
            root_logger.setLevel(self.log_level)

            for handler in root_logger.handlers:
                handler.setLevel(self.log_level)
                if self.formatter:
                    handler.setFormatter(self.formatter)

            root_logger.info("Set up logging")
        except:
            # We don't want this to ever fail. If it fails though, it should fail as loud as it can without disruption.
            logging.exception("Failed to set up logging")
