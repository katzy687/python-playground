import logging
from logging import StreamHandler
from logging import Logger, LogRecord
from cloudshell.api.cloudshell_api import CloudShellAPISession


class CsConsoleHandler(StreamHandler):
    def __init__(self, api, res_id):
        """
        add handler that will output text to console
        :param CloudShellAPISession api:
        :param str res_id:
        """
        super(CsConsoleHandler, self).__init__()
        self._api = api
        self._res_id = res_id

    def emit(self, record):
        """

        :param LogRecord record:
        :return:
        """
        self.format(record)
        if record.levelno == logging.INFO:
            if not getattr(record, "no_console", False):
                api.WriteMessageToReservationOutput(reservationId=self._res_id, message=record.message)
        elif record.levelno == logging.DEBUG:
            message = "<H2>{}</H2>".format(record.message)
            api.WriteMessageToReservationOutput(reservationId=self._res_id, message=message)

    @staticmethod
    def my_method(a):
        return a


class CustomLogger(Logger):
    def __init__(self):
        super(CustomLogger, self).__init__("test")


api = CloudShellAPISession("localhost", "admin", "admin", "Global")
SANDBOX_ID = "c8cab453-a1df-45f1-87fb-8c116dedcf3c"
logger = Logger("test")
logger.setLevel(logging.DEBUG)
cs_handler = CsConsoleHandler(api, SANDBOX_ID)
cs_handler.name = CsConsoleHandler.__name__
logger.addHandler(cs_handler)
cs_handler.setFormatter(logger.handlers[0].formatter)
print("handler name: " + cs_handler.name)
logger.info("hello there from info", extra={"no_console": True})
print(CsConsoleHandler.my_method("hey"))