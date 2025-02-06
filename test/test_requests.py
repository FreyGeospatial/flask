import logging
import time
import requests


LOGGER = logging.getLogger(__name__)


def test_sync():
    """
    Test function
    """
    count = 0
    start = time.time()
    while count < 2_000:
        response = requests.get("http://127.0.0.1:5000/hello", verify=False)
        (
            LOGGER.info(f"Call Number {count}: {response.text}")
            if count % 100 == 0
            else None
        )
        assert response.text == "Hello, World!"
        count += 1
    end = time.time()
    LOGGER.info(f"{end - start} seconds")


def test_async():
    """
    will add async test to see performance increase
    """
    assert True
    # response = requests.get("http://127.0.0.1:5000/hello")


# test_sync()
