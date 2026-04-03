import pytest
from aqueduct_sdk import ApiClient, Configuration


def test_client_creates_with_api_key():
    config = Configuration()
    config.api_key["X-API-Key"] = "test-key"
    client = ApiClient(configuration=config)
    assert client is not None


def test_client_creates_with_bearer():
    config = Configuration()
    config.access_token = "test-bearer"
    client = ApiClient(configuration=config)
    assert client is not None


def test_configuration_has_host():
    config = Configuration()
    # Default host should be set from spec servers block
    assert config.host is not None
    assert "aqueduct" in config.host.lower() or "localhost" in config.host.lower() or len(config.host) > 0
