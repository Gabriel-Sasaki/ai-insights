# AI Insights

AI Insights is a project developed as part of a technical challenge. This repository contains a FastAPI-based API that processes natural language questions using LangChain paired with relational database insights.

## Table of Contents

- [Endpoints](#endpoints)
- [Technical Requirements](#technical-requirements)
- [Project Setup](#project-setup)
    - [Cloning the Repository](#cloning-the-repository)
    - [Database Setup](#database-setup)
    - [Installing Dependencies](#installing-dependencies)
    - [Configuration](#configuration)
    - [Running the Application](#running-the-application)
- [Additional Notes](#additional-notes)
- [Links](#links)

## Endpoints

1. **GET /sales-insights?question={question}**
     - Receives a natural language question (e.g., "What was the best-selling product last week?").
     - The API processes the query using LangChain with your chosen LLM (e.g., GPT-4o), querying the sales table from the database.
     - Ensures that the question is limited to data available in the database to force the use of Retrieval Augmented Generation (RAG). 

2. **GET /top-products**
     - Returns the top 5 best-selling products for the last month.

## Technical Requirements

- **Framework:** FastAPI for creating the API.
- **Database:** A relational database of your choice. Use the provided SQL script to create the database schema.
- **Database Connection:** Connect to the selected relational database.
- **LLM Integration:** Use LangChain to process incoming questions in the first endpoint, leveraging a Free or Preferred LLM.
- **ORM:** Use SQLAlchemy to interact with the database.
- **Documentation:** Document the code thoroughly and provide instructions on how to execute the application.
- **RAG Enforcement:** Implement a limitation in the questions to enforce that no answer is returned without querying the database directly.

## Project Setup

### Cloning the Repository

Clone the project via HTTPS or SSH:

**HTTPS**

```bash
git clone https://github.com/Gabriel-Sasaki/ai-insights
```

**SSH**

```bash
git clone git@github.com:Gabriel-Sasaki/ai-insights.git
```

### Database Setup

Use the provided `script_dump.sql` file to create the database. This script sets up the necessary tables and inserts initial data required for the project.

### Installing Dependencies

Install all project dependencies by running:

```bash
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root with the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: The URL connection string for your relational database.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Running the Application

Start the FastAPI server with:

```bash
uvicorn app.main:app
```

Once the application is running, access the interactive API documentation via [Swagger UI](http://127.0.0.1:8000/docs/).

## Additional Notes

- Ensure your database is properly configured and running before starting the application.
- Review the environment settings to match your development environment.
- All endpoints are documented within the Swagger UI, allowing for in-browser API testing.
- The project emphasizes data integrity: all LLM processing in the `/sales-insights` endpoint is grounded in actual database records using RAG strategies with an AI Agent.

## Links

- [Project Repository](https://github.com/Gabriel-Sasaki/ai-insights)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)

