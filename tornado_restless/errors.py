#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""

"""
from __future__ import unicode_literals
from tornado.web import HTTPError
from builtins import super


class IllegalArgumentError(ValueError, HTTPError):
    """
        An exception occuring when there was a problem in parsing arguments or model data
    """

    def __init__(self, log_message, status_code=400, *args, **kwargs):
        ValueError.__init__(self, log_message)
        HTTPError.__init__(self, status_code, log_message, *args, **kwargs)


class ProcessingException(HTTPError):
    """
        Raised when a pre or postprocessors encouters a problem.

        No more processing will be done and the processing of the query is halted
    """

    def __init__(self, log_message, status_code=400, *args, **kwargs):
        HTTPError.__init__(self, status_code, log_message, *args, **kwargs)


class DictConvertionError(HTTPError):
    """
        Raised from convert.to_dict when it can't convert an instance to plain dict
    """

    def __init__(self, instance_type, log_message=None, status_code=400, *args, **kwargs):
        super().__init__(status_code, log_message, *args, **kwargs)
        self.instance_type = instance_type


try:
    from tornado.web import MethodNotAllowedError
except ImportError:
    class MethodNotAllowedError(HTTPError):
        """An exception occuring when the method is not supported by the handler

        Takes in addition to `HTTPError` arguments method and stores it value

        :arg string method: The name of the method that was called
        """

        def __init__(self, method=None, log_message=None, status_code=405, *args, **kwargs):
            super().__init__(status_code, log_message, *args, **kwargs)
            self.method = method
