from functools import wraps
import logging as logger

# Configure logger
logger.basicConfig(level=logger.ERROR)  # Set level to DEBUG or lower to capture all logs
logger = logger.getLogger(__name__)

def retry(retries=3, exceptions=None):
    """
    Decorator to handle Selenium exceptions and retry the test.

    :param retries: Number of times to retry the function.
    :param exceptions: specified exceptions that should be handled.
    """
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.error(f"Locator issue, maybe it was not shown or found by driver (Attempt {attempt}/{retries})")

                    if AttributeError in exceptions:
                        logger.error(f">>> Check the code attentively please <<< (Attempt {attempt}/{retries})")

                    attempt += 1

                    if attempt == retries:
                        raise Exception(f"Exception was thrown for all of retries of function {func}: {exceptions}")

                    raise e

            return func(*args, **kwargs)
        return wrapper
    return decorator
