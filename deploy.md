# Deployment Workflow Documentation

This document explains the GitHub Actions workflow defined in `.github/workflows/deploy.yml` for deploying the backend application to AWS Elastic Beanstalk.

## Workflow Overview

The workflow is triggered on every push to the `master` branch. It automates the process of building, packaging, and deploying the backend application to AWS Elastic Beanstalk.

### Steps in the Workflow

1. **Checkout Code**
   - Uses the `actions/checkout@v3` action to clone the repository into the workflow runner.
   - This ensures the latest code is available for the deployment process.

2. **Configure AWS Credentials**
   - Uses the `aws-actions/configure-aws-credentials@v2` action to set up AWS credentials.
   - The credentials are securely stored in GitHub Secrets and include:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_REGION`
     - `ECR_REPOSITORY_URL`
     - `S3_BUCKET_NAME`
   - This step is essential for authenticating with AWS services and accessing the required resources.

3. **Login to Amazon ECR**
   - Logs in to Amazon Elastic Container Registry (ECR) using the AWS CLI.
   - Retrieves a temporary authentication token and uses it to authenticate Docker with ECR.
   - This step ensures the workflow can push Docker images to the ECR repository.

4. **Build and Push Docker Image**
   - Builds a Docker image using the `Dockerfile.prod` file.
   - Tags the image with a unique timestamp-based tag (`IMAGE_TAG`).
   - Pushes the tagged image to the ECR repository specified in the `ECR_REPOSITORY_URL` secret.
   - The `IMAGE_TAG` is stored in the GitHub Actions environment for use in subsequent steps.

5. **Create Application Bundle**
   - Packages the application into a ZIP file (`app.zip`).
   - This bundle is required for creating a new application version in Elastic Beanstalk.

6. **Create Elastic Beanstalk Application Version**
   - Uploads the application bundle to an S3 bucket specified in the `S3_BUCKET_NAME` secret.
   - Creates a new application version in Elastic Beanstalk using the uploaded bundle.
   - The application version is identified by the `IMAGE_TAG`.

7. **Deploy Docker Image to Elastic Beanstalk**
   - Updates the Elastic Beanstalk environment to use the newly created application version.
   - This step ensures the latest Docker image is deployed to the Elastic Beanstalk environment.

## Why This Workflow?

- **Automation**: Automates the entire deployment process, reducing manual effort and the risk of errors.
- **Consistency**: Ensures a consistent deployment process by using a predefined workflow.
- **Security**: Uses GitHub Secrets to securely store sensitive information like AWS credentials.
- **Scalability**: Leverages AWS Elastic Beanstalk to manage the application infrastructure, allowing for easy scaling.

## Prerequisites

- AWS credentials (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`) must be stored as GitHub Secrets.
- The ECR repository URL (`ECR_REPOSITORY_URL`) and S3 bucket name (`S3_BUCKET_NAME`) must also be stored as GitHub Secrets.
- The `Dockerfile.prod` file must be correctly configured for building the production Docker image.

## Notes

- The workflow assumes that the Elastic Beanstalk application and environment are already set up.
- Ensure the S3 bucket specified in `S3_BUCKET_NAME` exists and is accessible.
- The `Dockerfile.prod` should include all necessary configurations for running the application in production.
- Ensure the application version specified in Elastic Beanstalk matches the version being deployed to avoid errors like "Incorrect application version."