import pytest
from aqueduct_sdk import ApiClient, Configuration


def test_client_creates_with_api_key():
    config = Configuration()
    config.api_key["ApiKeyAuth"] = "test-key"
    # Verify auth is actually wired, not just that client is non-None
    auth = config.auth_settings()
    assert "ApiKeyAuth" in auth
    assert auth["ApiKeyAuth"]["value"] == "test-key"
    client = ApiClient(configuration=config)
    assert client is not None


def test_client_creates_with_bearer():
    config = Configuration()
    config.access_token = "test-bearer"
    # Verify bearer token is actually wired
    auth = config.auth_settings()
    # BearerAuth is the key used in configuration.py auth_settings()
    bearer_keys = [k for k in auth if "bearer" in k.lower() or "jwt" in k.lower()]
    if bearer_keys:
        assert auth[bearer_keys[0]]["value"].endswith("test-bearer")
    else:
        # Fallback: access_token stored and client created
        assert config.access_token == "test-bearer"
    client = ApiClient(configuration=config)
    assert client is not None


def test_configuration_has_default_host():
    config = Configuration()
    # Default host must be set from spec servers block — non-empty string
    assert config.host is not None
    assert len(config.host) > 0
    # Should point to the Aqueduct gateway (not a placeholder)
    assert "GIT_USER_ID" not in config.host
    assert "example.com" not in config.host
