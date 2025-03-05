import pytest
from src.audit_sg import analyze_security_groups, fetch_security_groups
import boto3
from botocore.stub import Stubber

@pytest.fixture
def ec2_client():
    """Fixture to create a mock EC2 client."""
    return boto3.client("ec2", region_name="us-east-1")

def test_analyze_security_groups_empty_input():
    result = analyze_security_groups([])
    assert len(result) == 0  # No vulnerabilities found

def test_analyze_security_groups_invalid_rule():
    sgs = [{"GroupId": "sg-123456", "IpPermissions": [{"FromPort": 22, "ToPort": 22, "IpProtocol": "tcp"}]}]
    result = analyze_security_groups(sgs)
    assert len(result) == 0  # No vulnerabilities found (no IpRanges)

def test_fetch_security_groups_error(ec2_client):
    # Mock AWS response
    stubber = Stubber(ec2_client)
    stubber.add_client_error("describe_security_groups", service_error_code="AccessDenied")
    stubber.activate()

    with pytest.raises(Exception):
        fetch_security_groups(ec2_client)

    stubber.deactivate()
