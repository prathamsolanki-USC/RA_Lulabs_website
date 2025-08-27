#!/bin/bash

# Set variables
AWS_REGION="us-east-2"
AWS_ACCOUNT_ID="288206953496"
ECR_REPO_NAME="ecr_genomic_website"
IMAGE_TAG="latest"
SERVICE_NAME="genomic-query-website-container"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}🚀 Starting deployment process...${NC}"

# Step 1: Build Docker image
echo -e "${YELLOW}📦 Building Docker image...${NC}"
docker build -t $ECR_REPO_NAME:$IMAGE_TAG .

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Docker build failed!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Docker image built successfully${NC}"

# Step 2: Tag image for ECR
echo -e "${YELLOW}🏷️  Tagging image for ECR...${NC}"
docker tag $ECR_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:$IMAGE_TAG

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Image tagging failed!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Image tagged successfully${NC}"

# Step 3: Login to ECR
echo -e "${YELLOW}🔐 Logging into ECR...${NC}"
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ ECR login failed!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Logged into ECR successfully${NC}"

# Step 4: Push image to ECR
echo -e "${YELLOW}⬆️  Pushing image to ECR...${NC}"
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:$IMAGE_TAG

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Image push failed!${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Image pushed to ECR successfully${NC}"

# Step 5: Get ECR image URI
ECR_IMAGE_URI="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO_NAME:$IMAGE_TAG"

echo -e "${GREEN}🎉 Deployment script completed successfully!${NC}"
echo -e "${YELLOW}📋 Next steps:${NC}"
echo -e "1. Go to AWS App Runner Console"
echo -e "2. Click 'Create service'"
echo -e "3. Select 'Container registry' as source"
echo -e "4. Select 'Amazon ECR' as provider"
echo -e "5. Use this Container image URI: ${GREEN}$ECR_IMAGE_URI${NC}"
echo -e "6. Set Port: 8000"
echo -e "7. Set CPU: 1 vCPU, Memory: 2 GB"
echo -e "8. Click 'Create service'"

echo -e "${GREEN}🔗 ECR Image URI: $ECR_IMAGE_URI${NC}"
