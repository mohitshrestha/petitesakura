# PetiteSakura - Automation Project

**PetiteSakura** is a Python-based automation project that integrates with external APIs (such as Google APIs, OpenAI, and more). It provides a secure and efficient way to interact with these APIs while managing sensitive credentials, implementing modern best practices for security, and ensuring smooth deployment and continuous integration through GitHub Actions.

This project includes backend services using **FastAPI**, authentication with **OAuth** and **Service Accounts**, and API integrations like **Google Drive** and **OpenAI**.

## Key Features

-   **OAuth & Service Account Authentication**: Securely manage credentials with OAuth or Service Account tokens.
-   **API Integrations**: Includes integrations with Google APIs (Drive, Sheets, Docs, etc.) and OpenAI.
-   **FastAPI Backend**: REST API for handling various automation tasks.
-   **CI/CD Setup**: GitHub Actions for continuous integration and deployment.
-   **Environment Management**: `.env`, `.env.local`, and `.env.sample` for secure and flexible configuration.

## Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/mohitshrestha/petitesakura.git
cd petitesakura
```

### 2. Install dependencies

You can use uv or pip to install dependencies:

``` bash
uv install fastapi httpx google-auth google-auth-oauthlib google-api-python-client python-dotenv uvicorn
```

Or, for pip-based environments:

``` bash
pip install -r requirements.txt`
```

### 3. Set up your environment variables (e.g., Google API credentials, OpenAI API key):

Create a .env file based on the .env.sample provided. This file should contain sensitive data like API credentials, database URLs, and secret keys. `bash    cp .env.sample .env`

### 4. Run the FastAPI app:

``` bash
uvicorn backend.app.main:app --reload
```

You can now access your API at http://localhost:8000.

### 5. Run using Docker (Optional)

You can also run the app using Docker. This will set up the environment with all necessary dependencies in a container.

1.  Build the Docker image:

    ``` bash
    docker build -t petitesakura .
    ```

2.  Run the Docker container:

    ``` bash
    docker run -p 8000:8000 petitesakura
    ```

    You can now access the API in your browser at http://localhost:8000.

## Folder Structure

Here's an overview of the project structure:

``` bash
petitesakura/
├── backend/                        # Backend (FastAPI or other backend)
│   ├── app/                         # FastAPI application
│   │   ├── __init__.py
│   │   ├── main.py                  # Entry point for FastAPI app
│   │   ├── api/                     # API routes (v1, v2)
│   │   │   ├── v1/                  # Version 1 of APIs
│   │   │   └── v2/                  # Version 2 of APIs (future versions)
│   │   ├── models/                  # Pydantic models for validation
│   │   ├── services/                # Core business logic services
│   │   ├── api_clients/             # API clients (Google, OpenAI)
│   │   │   ├── google_api.py        # Google API client for various services
│   │   │   └── openai_api.py        # Client for OpenAI APIs
│   │   ├── credentials/             # Folder for storing credentials securely
│   │   │   ├── __init__.py
│   │   │   └── google_credentials.py # Google credentials loading utility
│   ├── Dockerfile                   # Dockerfile to containerize backend
│   ├── requirements.txt             # Backend dependencies (including FastAPI, HTTPX)
│   ├── .env                         # Environment variables (not committed)
│   ├── .env.sample                  # Sample env file (committed, without secrets)
│   ├── .env.local                   # Local environment variables for development
│   └── tests/                       # Backend test cases (unit, integration)
│
├── frontend/                        # Frontend (React or Vue)
│   ├── public/                      # Static files (images, CSS, JS)
│   ├── src/                         # Source code for frontend
│   ├── package.json                 # Frontend dependencies
│   ├── Dockerfile                   # Dockerfile for frontend containerization
│   └── .env                          # Frontend-specific environment variables
│
├── docker/                          # Docker-related configuration files
│   ├── docker-compose.yml           # Multi-container Docker setup (Backend, Frontend, DB, etc.)
├── .gitignore                       # Git ignore file (ignore .env files, etc.)
├── LICENSE                          # License for the project
└── README.md                        # Project documentation (guidelines for contributors)
```

## Environment Variables

The project requires several environment variables to run properly. These variables should be set in the `.env` file. Here are the key variables:

-   Google API Credentials:

    -   `GOOGLE_CLIENT_SECRET_PATH`: Path to the OAuth client secret JSON file.

    -   `GOOGLE_SERVICE_ACCOUNT_PATH`: Path to the Google service account JSON file.

    -   `GOOGLE_TOKEN_PATH`: Path to the OAuth token file (generated after authentication).

-   Database Configuration:

    -   `DATABASE_URL`: Database connection string (e.g., for PostgreSQL).

-   Secret Key:

    -   `SECRET_KEY`: Used for cryptographic operations (make sure to set this to a secure value in production).

-   OpenAI API Key:

    -   `OPENAI_API_KEY`: Your OpenAI API key for GPT-related integrations.

## Running Tests

To run the backend tests (unit tests, integration tests):

``` bash
pytest backend/tests/
```

Ensure that your environment variables are set before running the tests.

## Contributing

We follow the following standards for collaborative development:

-   All code changes should be versioned and reviewed.

-   Use environment variables for sensitive data (credentials, API keys).

-   Tests should be written for all new features and bug fixes.

-   Pull requests should pass the CI pipeline before merging.

-   Ensure your code adheres to the project's style guide and is well-documented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Notes

-   Security: Never hard-code sensitive information (like API keys) directly into your codebase. Always use environment variables or a secure secrets manager.

-   Token Management: OAuth tokens (`token.json`) should be stored securely. Ensure that the path to the `token.json` file is set in `.env` and protected from public access.