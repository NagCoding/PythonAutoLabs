import pytest
from utilities.config_loader import Config
import logging

# Setup logging once for all tests
def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,  # show INFO and above
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="common", help = "Environment : common/sit/preprod")


@pytest.fixture(scope="session")

def config(request):
    env = request.config.getoption("--env")
    logger.info(f"Running tests with environment: {env}")  # <-- log it here
    return Config(env=env)



