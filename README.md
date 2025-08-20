# PetiteSakura - Automation Project

**PetiteSakura** is a Python-based automation project designed to interact with external APIs like **Google APIs**, **OpenAI**, and more. The project leverages **FastAPI** for the backend, ensures secure handling of credentials, and integrates modern best practices for deployment and continuous integration (CI/CD). It also includes **data science**, **machine learning**, and **AI** workflows.

## Key Features

-   **OAuth & Service Account Authentication**: Secure management of credentials using OAuth or Service Account tokens.
-   **API Integrations**: Integrates with **Google APIs** (Drive, Sheets, Docs, etc.) and **OpenAI**.
-   **FastAPI Backend**: REST API for various automation tasks.
-   **CI/CD Setup**: GitHub Actions for continuous integration and deployment.
-   **Environment Management**: Uses `.env`, `.env.local`, and `.env.sample` for secure configuration.
-   **Data Science & AI Workflows**: Supports data analytics, machine learning, and AI-based tasks.

## Folder Structure

Here’s an overview of the project structure, which is organized for scalability, security, and collaboration. New contributors should follow this structure for clarity and consistency:

``` bash
petitesakura/
├── backend/                        # Backend (FastAPI or other backend)
│   ├── app/                          # FastAPI application source code
│   │   ├── __init__.py              # Initializes the application module
│   │   ├── main.py                  # Entry point for the FastAPI app
│   │   ├── api/                     # API routes (e.g., v1, v2)
│   │   │   ├── v1/                  # Version 1 of the APIs
│   │   │   └── v2/                  # Future version APIs
│   │   ├── models/                  # Pydantic models for validation
│   │   ├── services/                # Core business logic services
│   │   │   └── ai_services.py       # AI services for model inference, etc.
│   │   ├── api_clients/             # External API clients (Google, OpenAI)
│   │   ├── credentials/             # Securely store credentials (e.g., Google API)
│   ├── Dockerfile                   # Dockerfile for backend containerization
│   ├── requirements.txt             # Backend dependencies
│   ├── .env                         # Environment variables
│   ├── .env.sample                  # Sample env file
│   ├── .env.local                   # Local development environment variables
│   └── tests/                       # Backend tests
│       ├── unit/                    # Unit tests
│       └── integration/             # Integration tests
├── frontend/                        # Frontend (React/Vue)
│   ├── public/                      # Static files (e.g., images, CSS, JS)
│   ├── src/                         # Source code for frontend components
│   ├── package.json                 # Frontend dependencies
│   ├── Dockerfile                   # Dockerfile for frontend containerization
│   └── .env                         # Frontend-specific environment variables
├── data_science/                    # Data science, analytics, ML work
│   ├── data/                        # Data files (raw and processed data)
│   │   ├── raw/                     # Raw data (should not be modified directly)
│   │   └── processed/               # Cleaned and processed data
│   ├── analytics/                   # Scripts and notebooks for exploratory data analysis
│   │   ├── scripts/                 # EDA and data exploration scripts
│   │   └── notebooks/               # Jupyter notebooks for analysis
│   ├── machine_learning/            # Traditional machine learning models
│   │   ├── models/                  # Saved machine learning models
│   │   ├── scripts/                 # Scripts for training and tuning ML models
│   │   └── notebooks/               # Notebooks for machine learning models
│   ├── ai/                          # Advanced AI models (Deep Learning, NLP, etc.)
│   │   ├── models/                  # Saved AI models (e.g., deep learning models)
│   │   ├── scripts/                 # Scripts for training AI models
│   │   ├── notebooks/               # Notebooks for prototyping AI models
│   │   ├── experiments/             # Logs and metrics from AI model experiments
│   │   ├── requirements.txt         # Dependencies for AI-related work (e.g., TensorFlow, PyTorch)
│   │   └── tests/                   # AI model evaluation and metrics tests
│   ├── requirements.txt             # Data science dependencies
│   ├── .env                         # Data-science-specific environment variables
│   └── tests/                       # Unit and integration tests for data processing
├── docker/                          # Docker-related configuration
│   ├── compose.yml                  # Multi-container Docker setup for backend, frontend, and databases
├── .gitignore                       # Git ignore file
├── LICENSE                          # License for the project
├── README.md                        # Project documentation
└── requirements.txt                 # Root-level dependencies for the entire project
```

Folder and File Breakdown:

-   `backend/`: Contains the FastAPI app and related services. Includes API routes, business logic, and API client integrations (Google, OpenAI).

-   `frontend/`: Contains the frontend code (React/Vue), static assets, and dependencies.

-   `data_science/`: Organizes data science workflows, including analytics, machine learning, and AI work.

    -   `analytics/`: Contains scripts and notebooks for data exploration and analysis (EDA).

    -   `machine_learning/`: Holds traditional ML models and their training scripts.

    -   `ai/`: Dedicated to advanced AI models (e.g., deep learning, NLP). Includes model training scripts, saved models, and experiment logs.

-   `docker/`: Configuration files for Docker containerization, including `compose.yml` for multi-container setups.

-   `.gitignore`: Ensures sensitive or unnecessary files (like .env, node_modules, etc.) are not committed.

-   `LICENSE`: The project’s licensing information.

-   `requirements.txt`: Root-level and backend-level dependency files.

## Setup Instructions

### 1. Clone the repository

``` bash
git clone https://github.com/mohitshrestha/petitesakura.git
cd petitesakura
```

### 2. Install dependencies

Install dependencies for the backend, frontend, and data science environments.

For Python-based environments: You can use uv or pip to install dependencies:

``` bash
uv pip install python-dotenv httpx fastapi uvicorn google-auth google-auth-oauthlib google-api-python-client
```

``` bash
uv pip install -r requirements.txt`
```

Or, for pip-based environments:

``` bash
pip install -r requirements.txt`
```

For the frontend (React/Vue), you can install dependencies via npm or yarn:

``` bash
cd frontend
npm install
```

### 3. Set Up Environment Variables

Create a `.env` file based on the `.env.sample` file. This file should contain your sensitive data, such as API credentials and database connection strings:

``` bash
cp .env.sample .env
```

### 4. Running the Application

-   To run the backend locally using FastAPI:

``` bash
uvicorn backend.app.main:app --reload
```

Visit the backend API at `http://localhost:8000`.

-   Alternatively, run the backend using Docker:

1.  Build the Docker image:

``` bash
docker build -t petitesakura .
```

2.  Run the Docker container:

``` bash
docker run -p 8000:8000 petitesakura
```

-   Alternatively, run the backend using Docker Compose:

1.  Build and start all services:

``` bash
docker-compose up --build
```

The backend should now be accessible at `http://localhost:8000`.

### 5. Running Frontend

For the frontend, navigate to the `frontend` directory and start the development server:

``` bash
cd frontend
npm run start
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

To run tests for the backend: (unit tests, integration tests):

``` bash
pytest backend/tests/
```

For data science-specific tests (unit and integration):

``` bash
pytest data_science/tests/
```

Ensure your environment variables are properly set before running the tests, especially those related to external APIs (like Google APIs and OpenAI).

## Contributing

We follow the following standards for collaborative development:

-   **Version Control**: All code changes must be versioned and reviewed before merging.

-   **Environment Variables**: Always use environment variables (or a secure secrets manager) for sensitive data (e.g., API keys, database credentials).

-   **Testing**: Write tests for new features, and ensure that they pass before merging pull requests.

-   **CI/CD**: Ensure your pull request passes the CI pipeline (GitHub Actions) before merging.

-   **Code Style**: Adhere to the project’s style guide and provide clear documentation for your code.

-   **Security**: Never hard-code sensitive information in the source code. Always use environment variables, and ensure tokens (OAuth, API keys) are kept secure.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Additional Notes

-   **Security**: Never hard-code sensitive information (e.g., API keys) directly into the codebase. Use environment variables or secure secrets management tools like `dotenv` or `HashiCorp Vault`.

-   **Token Management**: Ensure OAuth tokens (`token.json`) and service account credentials are securely stored and are protected from unauthorized access.