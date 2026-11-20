# Lab 1: DevOps Foundations & Continuous Integration

## Objective
To establish a basic DevOps workflow using Git, GitHub, Docker, Jenkins, and Python.

## Environment
- OS: Ubuntu 24.04 LTS (WSL2)
- Version Control: Git
- Repository Hosting: GitHub
- IDE: Visual Studio Code
- CI/CD: Jenkins (Docker)
- Application: Python 3

## Implementation

1. Created a Git repository for the sample Python application.
2. Implemented a Python greeting application.
3. Created unit tests using Python unittest.
4. Created a custom Jenkins Docker image with Python installed.
5. Configured a Jenkins pipeline using a Jenkinsfile.
6. Connected Jenkins to the GitHub repository.
7. Executed the pipeline successfully.
8. Installed Docker CLI in the custom Jenkins image.
9. Configured Jenkins to communicate with the Docker daemon.
10. Created a Dockerfile for the Python application.
11. Updated Jenkinsfile to build a Docker image and deploy a container.
12. Verified the deployed container and application logs.

## Jenkins Pipeline Stages

| Stage | Description | Result |
|---|---|---|
| Checkout | Loads pipeline configuration from GitHub | Success |
| Build | Compiles Python application | Success |
| Test | Executes automated unit tests | Success |
| Docker Build | Builds application Docker image | Success |
| Deploy | Runs application container | Success |

## Observations

- Git successfully tracked project changes.
- GitHub hosted the project repository.
- Jenkins successfully executed the pipeline.
- Both automated unit tests passed.
- The application executed successfully during the Deploy stage.

## Conclusion

Successfully established a basic CI/CD workflow using Git, GitHub, Docker, and Jenkins. The pipeline automated application compilation, testing, and execution.

## Docker Deployment

- Docker image: lab1-python-app:latest
- Container name: lab1-python-app
- Base image: python:3.13-slim
- Deployment method: Docker container
- Application output: Hello, Student! Welcome to DevOps Lab 1.

## Final Observation

The updated Jenkins pipeline successfully automated Docker image creation and container deployment. The application ran successfully inside the deployed container.
