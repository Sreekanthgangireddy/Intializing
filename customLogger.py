import logging

class LogGen:
    _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    # @staticmethod
    # def loggen():
    #     import pdb
    #     pdb.set_trace()
    #     logging.basicConfig(filename=".\\Logs\\Automation.log",format="%(asctime)s:%(levelname)s:%(message)s",datefmt='%m/%d/%Y %I:%M:%S %p')
    #     logger = logging.getLogger(__name__)
    #     logger.setLevel(logging.INFO)
    #     logger.info('Hi this is shadak')
    #     return logger
    def loggen(self):
        file_handler = logging.FileHandler("C:/myProject/pythonProject/Logs/automation.log")
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter(self._log_format))
        return file_handler

    def get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.addHandler(self.loggen())
        # logger.addHandler(get_stream_handler())
        return logger