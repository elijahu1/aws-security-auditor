import pytest
from src.audit_sg import analyze_security_groups, fetch_security_groups
import boto3
from botocore.stub import Stubber

@pytest.fixture
def ec2_client():
    return boto3.client("ec2", region_name="us-east-1")

def test_analyze_security_groups_no_vulnerabilities():
    sgs = [{"GroupId": "sg-123456", "IpPermissions": []}]
    result = analyze_security_groups(sgs)
    assert len(result) == 0  # No vulnerabilities found

def test_analyze_security_groups_with_vulnerabilities():
    sgs = [
        {
            "GroupId": "sg-123456",
            "IpPermissions": [
                {
                    "FromPort": 22,
                    "ToPort": 22,
                    "IpProtocol": "tcp",
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                }
            ],
        }
    ]
    result = analyze_security_groups(sgs)
    assert len(result) == 1  # One vulnerability found
    assert result[0]["GroupId"] == "sg-123456"

def test_fetch_security_groups(ec2_client):
    # Mock AWS response
    stubber = Stubber(ec2_client)
    stubber.add_response(
        "describe_security_groups",
        {"SecurityGroups": [{"GroupId": "sg-123456", "IpPermissions": []}]},
    )
    stubber.activate()

    # Test function
    result = fetch_security_groups(ec2_client)
    assert len(result) == 1
    assert result[0]["GroupId"] == "sg-123456"

    stubber.deactivate()
