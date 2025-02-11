import logging
from abc import ABC, abstractmethod

logging.getLogger(__name__)

class CustomErrorHandler(ABC, Exception):
    def __init__(self, 
                 message: str, 
                 code = None, 
                 details: str = None):
        """
        This is base class for handle error of llms.
        """
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details

    def __str__(self, message):
        pass

    @abstractmethod
    def asknowledge():
        pass

class LoaderHandle(CustomErrorHandler):

    def __init__(self, message, code=None, details = None):
        super().__init__(message, code, details)


class RAGHandle(CustomErrorHandler):

    def __init__(self, message, code=None, details = None):
        super().__init__(message, code, details)