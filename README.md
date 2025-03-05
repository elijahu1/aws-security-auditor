
---

```markdown
# 🛡️ AWS Security Group Auditor

Welcome to the **AWS Security Group Auditor**! This is a simple yet powerful CLI tool to help you audit your AWS EC2 security groups for overly permissive rules, like open SSH (port 22) or RDP (port 3389) access to the world (`0.0.0.0/0`). It’s perfect for DevOps engineers, security teams, or anyone who wants to keep their AWS infrastructure secure.

---

## 🚀 Features

- **Identify Risky Rules**: Find security groups with `0.0.0.0/0` on critical ports.
- **Generate Reports**: Export results in CSV or JSON format.
- **Easy Automation**: Run it manually or schedule it with cron jobs.
- **Lightweight**: Built with Python and Bash, so it’s easy to customize.

---

## 🛠️ Installation

### Prerequisites
Before you start, make sure you have the following installed:
- **Python 3.11+**: [Download Python](https://www.python.org/downloads/)
- **AWS CLI**: [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **Git**: [Install Git](https://git-scm.com/downloads)

### Step 1: Clone the Repository
First, clone this repository to your local machine:
```bash
git clone https://github.com/elijahu1/aws-security-auditor.git
cd aws-security-auditor
```

### Step 2: Set Up a Virtual Environment
Create a virtual environment to keep dependencies isolated:
```bash
python -m venv .venv
```

Activate the virtual environment:
- **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```

### Step 3: Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### Step 4: Configure AWS Credentials
Make sure your AWS credentials are set up. Run:
```bash
aws configure
```
You’ll need to provide:
- **AWS Access Key ID**
- **AWS Secret Access Key**
- **Default region** (e.g., `us-east-1`)
- **Default output format** (e.g., `json`)

---

## 🖥️ Usage

### Option 1: Run with Python
You can run the tool directly using Python:
```bash
python src/audit_sg.py --region us-east-1 --output csv
```
- `--region`: The AWS region to audit (default: `us-east-1`).
- `--output`: The output format (`csv` or `json`).

### Option 2: Use the Bash Wrapper
For easier automation, use the Bash wrapper script:
1. Make the script executable:
   ```bash
   chmod +x scripts/run_audit.sh
   ```
2. Run the script:
   ```bash
   ./scripts/run_audit.sh us-east-1 csv
   ```

---

## 📂 Output

The tool generates a report in the `reports/` directory:
- **CSV Format**: `reports/vulnerable_sgs.csv`
- **JSON Format**: Printed to the terminal.

Example CSV Output:
```
GroupId,Port,Protocol
sg-123456,22,tcp
sg-789012,3389,tcp
```

---

## 🤖 Automation

### Schedule with Cron
To run the tool daily at 2 AM, add a cron job:
1. Open your crontab:
   ```bash
   crontab -e
   ```
2. Add the following line:
   ```bash
   0 2 * * * /path/to/aws-security-auditor/scripts/run_audit.sh us-east-1 csv
   ```

---

## IAM Permissions
Ensure your IAM role or user has the following permissions:
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

## 🧪 Testing

To ensure everything is working correctly, run the tests:
```bash
make test
```

---

## 🛠️ Development

### Directory Structure
Here’s what the project looks like:
```
aws-security-auditor/
├── src/                  # Python source code
├── tests/                # Unit tests
├── scripts/              # Bash scripts
├── config/               # Configuration files
├── logs/                 # Log files
├── reports/              # Generated reports
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

### Common Tasks
- **Run Tests**:
  ```bash
  make test
  ```
- **Format Code**:
  ```bash
  make format
  ```
- **Clean Up**:
  ```bash
  make clean
  ```

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve this tool:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it as you see fit.

---

## 🙏 Credits

- Built with ❤️ by [Eli]
- Inspired by the need for better AWS security practices.

---

Happy auditing! 🎉
```

---

