# AWS Security Group Auditor

AWS Security Group Auditor is a lightweight CLI tool for auditing AWS EC2 security groups to detect overly permissive firewall rules such as SSH (22) or RDP (3389) exposed to the public internet (`0.0.0.0/0`).

The tool helps DevOps engineers, cloud engineers, and security teams quickly identify risky configurations and generate simple reports for remediation.

---

## Features

* Detects security groups exposing sensitive ports to the internet
* Generates CSV or JSON audit reports
* Simple CLI interface
* Easy automation via cron or CI pipelines
* Lightweight and easy to customize

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/elijahu1/aws-security-auditor.git
cd aws-security-auditor
```

Create a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure AWS credentials:

```bash
aws configure
```

Run the audit:

```bash
python src/audit_sg.py --region us-east-1 --output csv
```

---

## Usage

### Python CLI

```bash
python src/audit_sg.py --region us-east-1 --output csv
```

Options:

* `--region` — AWS region to scan
* `--output` — output format (`csv` or `json`)

---

### Bash Wrapper

Make the script executable:

```bash
chmod +x scripts/run_audit.sh
```

Run the audit:

```bash
./scripts/run_audit.sh us-east-1 csv
```

---

### Docker

Build the container:

```bash
docker build -t aws-security-auditor .
```

Run the container:

```bash
docker run aws-security-auditor
```

---

## Output

Audit reports are written to the `reports/` directory.

Example CSV output:

```
GroupId,Port,Protocol
sg-123456,22,tcp
sg-789012,3389,tcp
```

---

## Automation

Example cron job (run daily at 2 AM):

```bash
0 2 * * * /path/to/aws-security-auditor/scripts/run_audit.sh us-east-1 csv
```

---

## IAM Permissions

The following permission is required:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:DescribeSecurityGroups",
      "Resource": "*"
    }
  ]
}
```

---

## Development

Project structure:

```
aws-security-auditor/
├── src/
├── tests/
├── scripts/
├── config/
├── reports/
├── .github/
├── requirements.txt
├── Dockerfile
├── Makefile
├── LICENSE
├── CONTRIBUTING.md
└── README.md
```

Run tests:

```bash
make test
```

Format code:

```bash
make format
```

Clean build artifacts:

```bash
make clean
```

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

See `CONTRIBUTING.md` for more details.

---

## License

This project is licensed under the GNU Affero General Public License v3.0.

See the LICENSE file for full details.

---

## Author

Created by Elijah U.

