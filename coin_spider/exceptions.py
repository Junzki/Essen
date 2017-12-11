# -*- coding:utf-8 -*-

class RequestException(Exception):
    """
    Common request excpetion.
    Raises when one HTTP request returns a failure.

    Args:
        - status_code: HTTP response status code.
        - message: Response content.
    """
    def __init__(self, status_code, message):
        super().__init__(message)

        self.status_code = str(status_code)
        self.message = str(message)


    def __str__(self):
        return '[{}] {}'.format(self.status_code, self.message)
