# API Gateway for Unified Threat Detection and Response System (UTDRS)

This is the API Gateway component for the UTDRS, providing centralized authentication, routing, and API documentation.

## Features

- Authentication and authorization with JWT
- User management
- Alert handling
- Event processing
- Integration with other UTDRS components
- MongoDB integration for data storage
- Comprehensive API documentation
- Docker-ready for deployment on Render

## Getting Started

### Prerequisites

- Docker and Docker Compose (for local development)
- MongoDB database (can use MongoDB Atlas)

### Local Development

1. **Clone the repository**

```bash
git clone <repository-url>
cd api-gateway
```

2. **Configure environment variables**

Copy the example environment file and update it with your settings:

```bash
cp .env.example .env
# Edit .env with your MongoDB connection details and other settings
```

3. **Run using Docker Compose**

```bash
docker-compose up
```

The API will start running at `http://localhost:8000`, and you can access the API documentation at `http://localhost:8000/api/v1/docs`.

## Deployment on Render

### Option 1: Using the Render Dashboard

1. Create a new Web Service on Render
2. Select "Build and deploy from a Git repository"
3. Connect your GitHub/GitLab repository
4. Select "Docker" as the runtime
5. Configure environment variables:
   - `MONGODB_URI`: Your MongoDB connection string
   - `JWT_SECRET`: A secret key for JWT token generation
   - `DEBUG`: Set to "false" for production

### Option 2: Using render.yaml

1. Push your code to a Git repository
2. In the Render dashboard, select "Blueprint" and connect to your repository
3. Render will automatically detect the `render.yaml` file and set up the service

## API Routes

- **/api/v1/auth** - Authentication endpoints
- **/api/v1/alerts** - Alert management
- **/api/v1/events** - Event query and creation
- **/api/v1/assets** - Asset management
- **/api/v1/detection** - Detection configuration
- **/api/v1/simulation** - Simulation controls

## Project Structure

- **api/** - API routes, controllers, and middleware
- **core/** - Business logic, models, and data access
- **utils/** - Utility functions and helpers
- **tests/** - Test files
- **Dockerfile** - Docker configuration
- **docker-compose.yml** - Docker Compose configuration
- **render.yaml** - Render deployment configuration
