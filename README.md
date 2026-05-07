# Sentiment Analysis Service (MLOps Assignment)

## Project Overview
This is a microservice-based Sentiment Analysis application built using **Flask**. It integrates a pre-trained **Hugging Face Transformer model** for NLP tasks. The project demonstrates a complete MLOps lifecycle, including containerization with **Docker** and automated **CI/CD pipelines** via GitHub Actions.

## Deliverables
- **Python Scripts**: `app.py` (API), `model.py` (Inference logic), `cli.py` (Testing tool)
- **Containerization**: `Dockerfile` for environment consistency.
- **Automation**: `.github/workflows/ci-cd.yml` for automated build and validation.
- **Dependency Management**: `requirements.txt` for reproducible environments.

## Key Features
1. **Sentiment Prediction**: A REST API endpoint `/predict` that accepts text input and returns sentiment labels (Positive/Negative).
2. **Automated CI/CD**: Every code push triggers a GitHub Actions workflow to build the Docker image and perform a health check.
3. **Cloud-Ready Infrastructure**: The service is containerized to ensure it runs identically across local development and cloud production environments.

## Getting Started

### Local Execution
1. Install dependencies:
   ```bash
   pip install -r requirements.txt