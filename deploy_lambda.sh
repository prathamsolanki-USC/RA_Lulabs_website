#!/bin/bash

# AWS Lambda + API Gateway Deployment Script
# This script deploys your genomic query interface to AWS

set -e

echo "🚀 Starting AWS Lambda + API Gateway deployment..."

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI not found. Please install it first."
    exit 1
fi

# Check if AWS credentials are configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "❌ AWS credentials not configured. Please run 'aws configure' first."
    exit 1
fi

# Check if SAM CLI is installed
if ! command -v sam &> /dev/null; then
    echo "❌ AWS SAM CLI not found. Installing..."
    # Install SAM CLI (macOS)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install aws-sam-cli
    else
        echo "Please install AWS SAM CLI manually: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html"
        exit 1
    fi
fi

echo "✅ Prerequisites check passed"

# Create deployment package
echo "📦 Creating deployment package..."

# Create a temporary directory for the package
rm -rf lambda_package
mkdir lambda_package

# Copy Lambda function files
cp lambda_function.py lambda_package/
cp lambda_requirements.txt lambda_package/

# Install dependencies
cd lambda_package
pip install -r lambda_requirements.txt -t .
rm lambda_requirements.txt

# Create ZIP file
zip -r ../genomic-query-lambda.zip .
cd ..

# Clean up
rm -rf lambda_package

echo "✅ Deployment package created: genomic-query-lambda.zip"

# Deploy using SAM
echo "🚀 Deploying to AWS using SAM..."

# Build SAM application
sam build

# Deploy SAM application
sam deploy --guided

echo "✅ Deployment completed successfully!"

# Get the API Gateway URL
echo "🌐 Getting API Gateway URL..."
API_URL=$(aws cloudformation describe-stacks \
    --stack-name genomic-query-interface \
    --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' \
    --output text)

echo "🎉 Your API is now live at: $API_URL"
echo ""
echo "📋 Available endpoints:"
echo "  GET  $API_URL/          - Home page"
echo "  GET  $API_URL/api/health - Health check"
echo "  POST $API_URL/api/query  - Genomic data query"
echo ""
echo "🧪 Test your API:"
echo "  curl $API_URL/api/health"
echo "  curl -X POST $API_URL/api/query \\"
echo "    -H 'Content-Type: application/json' \\"
echo "    -d '{\"selections\":{\"species\":\"HS\"},\"files_required\":[\"pri_crssant\"],\"limit\":5}'"
