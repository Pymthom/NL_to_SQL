
# NL_to_SQL

## Project Overview

This repository contains a collection of projects focused on generating SQL queries from natural language text. It explores three distinct approaches using different Large Language Models (LLMs) to achieve this task:

1.  **Phi-3 Serverless Deployment**: Utilizes the Phi-3 model, deployed as a serverless API in Azure, to convert natural language queries into SQL.
    
2.  **Phi-3 on Local Ollama**: Demonstrates how to run the Phi-3 model locally using Ollama for natural language to SQL conversion.
    
3.  **LangChain and GPT-4**: A standard approach using the LangChain framework with the GPT-4 model from Azure OpenAI to generate SQL queries.
    

The projects are designed to demonstrate various methods for handling natural language to SQL conversion, including querying a database and handling different response scenarios.

## Features

-   **Multiple LLM Integrations**: Supports Phi-3 (serverless and local) and GPT-4 models.
    
-   **Database Querying**: Includes Python code to execute the generated SQL queries against a database.
    
-   **Error Handling**: Built-in mechanisms to handle different response scenarios and potential errors.
    

## Installation

To get started with this project, you'll need Python and a virtual environment.

1.  **Clone the repository:**
    
    ```
    git clone [https://github.com/Pymthom/NL_to_SQL.git](https://github.com/Pymthom/NL_to_SQL.git)
    cd NL_to_SQL
    
    
    ```
    
2.  **Create and activate a virtual environment:**
    
    -   **Windows (Command Prompt):**
        
        ```
        python -m venv venv
        venv\Scripts\activate
        
        
        ```
        
    -   **Windows (PowerShell):**
        
        ```
        python -m venv venv
        # If you encounter an error, run Set-ExecutionPolicy RemoteSigned as an administrator first.
        venv\Scripts\activate
        
        
        ```
        
    -   **macOS / Linux:**
        
        ```
        python3 -m venv venv
        source venv/bin/activate
        
        
        ```
        
3.  **Install the dependencies:** The project uses a variety of libraries, depending on the specific approach you choose.
    
    ```
    pip install langchain_openai openai pyodbc fastapi "uvicorn[standard]" pydantic azure-identity langchain_community
    
    
    ```
    

## Usage

Each project is a separate Python script. You can run them locally to see them in action. Ensure your virtual environment is activated before running the scripts.

-   **To run the Phi-3 Serverless project:**
    
    ```
    python NLToSql-Phi3_ServerlessDeployment.py
    
    
    ```
    
-   **To run the Phi-3 Local Ollama project:**
    
    ```
    python NLToSQL-phi3_local.py
    
    
    ```
    
-   **To run the LangChain with GPT-4 project:**
    
    ```
    python NLToSql_GPT4.py
    
    
    ```
    

## Dependencies

The key dependencies for this project include:

-   `langchain_openai`
    
-   `openai`
    
-   `pyodbc`
    
-   `fastapi`
    
-   `uvicorn`
    
-   `pydantic`
    
-   `azure-identity`
    
-   `langchain_community`
    

These dependencies are listed in the installation step.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please refer to the repository's `CONTRIBUTING.md` and Contributor License Agreement (CLA) for more details.

_This README was generated based on the content of the `Pymthom/NL_to_SQL` GitHub repository._