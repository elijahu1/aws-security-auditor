#!/bin/bash

set -e  # Exit on error

# Parse arguments
REGION=${1:-us-east-1}
OUTPUT=${2:-csv}

# Validate AWS credentials
if ! aws sts get-caller-identity &> /dev/null; then
    echo "ERROR: AWS credentials not configured!"
    exit 1
fi

# Run Python script
echo "Starting security group audit for region: $REGION"
python src/audit_sg.py --region "$REGION" --output "$OUTPUT"

echo "Audit complete. Check reports/ for output."
