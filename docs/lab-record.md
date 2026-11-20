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

## Jenkins Pipeline Stages

| Stage | Description | Result |
|---|---|---|
| Checkout | Jenkins loads the pipeline from GitHub | Success |
| Build | Python application syntax compilation | Success |
| Test | Automated unit tests | Success |
| Deploy | Executes the sample application | Success |

## Observations

- Git successfully tracked project changes.
- GitHub hosted the project repository.
- Jenkins successfully executed the pipeline.
- Both automated unit tests passed.
- The application executed successfully during the Deploy stage.

## Conclusion

Successfully established a basic CI/CD workflow using Git, GitHub, Docker, and Jenkins. The pipeline automated application compilation, testing, and execution.
