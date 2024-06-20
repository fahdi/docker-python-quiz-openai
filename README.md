This project sets up a Dockerized environment with a Python application and an SQL database to manage multiple-choice questions (MCQs) and their answers. The application also integrates with OpenAI's API to generate MCQs.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Prerequisites

- Docker and Docker Compose installed on your machine.
- An OpenAI API key. You can get one from [OpenAI](https://beta.openai.com/signup/).

## Project Structure

```
docker_mcq_project_with_openai/
│
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── README.md
```

- **Dockerfile**: Defines the Docker image for the Python application.
- **docker-compose.yml**: Configures Docker services, including the Python application and the MySQL database.
- **app.py**: The main Python application that handles MCQs and integrates with OpenAI.
- **requirements.txt**: Lists the Python dependencies for the project.
- **README.md**: This file.

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd docker_mcq_project_with_openai
   ```

2. Replace `your_openai_api_key_here` in `docker-compose.yml` with your actual OpenAI API key.

3. Build and start the Docker containers:

   ```sh
   docker-compose up --build
   ```

This command will build the Docker images and start the containers. Your application should be accessible at `http://localhost:5000`.

## Usage

### Adding an MCQ Manually

You can add an MCQ manually by sending a POST request to the `/add_mcq` endpoint with the following JSON payload:

```json
{
  "question": "What is the capital of France?",
  "answer": "Paris"
}
```

### Generating an MCQ Using OpenAI

You can generate an MCQ using OpenAI by sending a POST request to the `/generate_mcq` endpoint with the following JSON payload:

```json
{
  "prompt": "Generate an MCQ about world geography."
}
```

### Retrieving All MCQs

You can retrieve all MCQs by sending a GET request to the `/mcqs` endpoint.

## API Endpoints

### 1. Add MCQ

- **URL**: `/add_mcq`
- **Method**: `POST`
- **Request Payload**:
  ```json
  {
    "question": "Question text",
    "answer": "Answer text"
  }
  ```
- **Response**:
  ```json
  {
    "message": "MCQ added successfully"
  }
  ```

### 2. Generate MCQ

- **URL**: `/generate_mcq`
- **Method**: `POST`
- **Request Payload**:
  ```json
  {
    "prompt": "Prompt for generating MCQ"
  }
  ```
- **Response**:
  ```json
  {
    "message": "MCQ generated and added successfully"
  }
  ```

### 3. Get All MCQs

- **URL**: `/mcqs`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "question": "Question text",
      "answer": "Answer text"
    },
    ...
  ]
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

