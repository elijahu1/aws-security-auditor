import boto3
import click
import logging
import pandas as pd
import logging.config
logging.config.fileConfig('config/logging.conf')

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@click.command()
@click.option("--region", default="us-east-1", help="AWS region to audit")
@click.option("--output", default="csv", help="Output format (csv/json)")
def audit_security_groups(region, output):
    """Audit AWS EC2 security groups for overly permissive rules."""
    ec2 = boto3.client("ec2", region_name=region)
    logging.info(f"Fetching security groups in {region}...")

    try:
        sgs = ec2.describe_security_groups()["SecurityGroups"]
        logging.info(f"Found {len(sgs)} security groups.")
    except Exception as e:
        logging.error(f"Failed to fetch security groups: {e}")
        return

    # Analyze rules
    vulnerable_sgs = []
    for sg in sgs:
        for rule in sg["IpPermissions"]:
            for ip_range in rule.get("IpRanges", []):
                if ip_range["CidrIp"] == "0.0.0.0/0" and rule["FromPort"] in [22, 3389]:
                    vulnerable_sgs.append({
                        "GroupId": sg["GroupId"],
                        "Port": rule["FromPort"],
                        "Protocol": rule["IpProtocol"],
                    })

    # Output results
    if vulnerable_sgs:
        df = pd.DataFrame(vulnerable_sgs)
        if output == "csv":
            df.to_csv("reports/vulnerable_sgs.csv", index=False)
            logging.info("Report saved to reports/vulnerable_sgs.csv")
        else:
            print(df.to_json(orient="records", indent=2))
    else:
        logging.info("No vulnerable security groups found.")

if __name__ == "__main__":
    audit_security_groups()

