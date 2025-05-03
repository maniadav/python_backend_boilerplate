# Running the Backend with Docker

## Development Mode
To run the backend in development mode with auto-reload:

1. Using Docker Compose:
   ```bash
   docker-compose up dev
   ```
2. Alternatively, using Docker directly:
   ```bash
   docker build -f Dockerfile.dev -t flask-backend-boilerplate-dev .
   docker run -p 8000:8000 -v $(pwd):/app -e FLASK_ENV=development flask-backend-boilerplate-dev
   ```
3. The API will be available at `http://localhost:8000`.

## Production Mode
To run the backend in production mode:

1. Using Docker Compose:
   ```bash
   docker-compose up web
   ```
2. Alternatively, using Docker directly:
   ```bash
   docker build -f Dockerfile.prod -t flask-backend-boilerplate-prod .
   docker run -p 8000:8000 -e FLASK_ENV=production flask-backend-boilerplate-prod
   ```
3. The API will be available at `http://localhost:8000`.


# Running the Backend with Terraform

## Terraform Configuration
The Terraform configuration (`main.tf`) defines the following AWS resources:

1. **VPC (Virtual Private Cloud):**
   - Provides network isolation for the backend.
   - CIDR block: `10.0.0.0/16`.

2. **Public Subnet:**
   - Hosts the EC2 instance.
   - CIDR block: `10.0.1.0/24`.
   - Allows public IP assignment for the instance.

3. **Security Group:**
   - Allows inbound traffic on port `8000` for the API.
   - Allows all outbound traffic.

4. **EC2 Instance:**
   - Runs the Python backend in a Docker container.
   - Uses Amazon Linux 2 AMI.
   - Installs Docker and starts the container with the backend image.

5. **Output:**
   - Displays the public IP of the EC2 instance after deployment.

## How It Exposes the API
- The EC2 instance is launched in the public subnet with a public IP.
- The security group allows inbound traffic on port `8000`, exposing the API to the internet.
- Docker runs the backend container, binding it to port `8000` on the instance.

## Steps to Deploy with Terraform

1. **Initialize Terraform:**
   ```bash
   terraform init
   ```

2. **Preview the Infrastructure:**
   ```bash
   terraform plan
   ```

3. **Apply the Configuration:**
   ```bash
   terraform apply
   ```
   Confirm the changes when prompted.

4. **Access the API:**
   - After deployment, Terraform will output the public IP of the EC2 instance.
   - Access the API at `http://<public-ip>:8000`.

## Notes
- Ensure your AWS credentials are configured on your system before running Terraform.
- Replace `<your-docker-image>` in the `main.tf` file with the name of your Docker image.
