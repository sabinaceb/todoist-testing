# SQA Challenge project

## Description
This is a project done as part of the QA Team Onboarding Chanllenge.
The idea is to generate a complete framework that allos to automate the webapp [`Todoist`](https://todoist.com/home).
The Test Automation Framework should be able to exercise the `FrontEnd` and `BackEnd`.

General goals for the whole project

- Required Items
  - Implement a [design pattern](#design-patterns) and [structured folders](#project-structure) for frontend automation.
  - Use different levels of documentation.
    - [README.md](#).
    - [Comments inside code](#docstrings).
  - Use best practices for element selectors.
    - Avoid absolute selectors.
    - Unique selectors.
    - Use different selectors supported.
  - Use [Eslint-like](#linters) for static analysis and assure code standards.
  - Coding best practices.
    - Naming conventions for method, classes and tests.
    - Avoid hardcoded data.
    - Avoid magic numbers.
    - Descriptive name for test scripts.
    - Avoid explicit waits. (if possible).
    - Hooks.
  - Best practiced for Assertions.
    - Single assertion per test.
    - Avoid assertions on the page objects.
  - Proper Data management
    - Usage of data providers
    - Usage of env/config files (when possible) for sensible data.
  - Implement an [automated reporter](#).
  - Configure a [CI tools](#) to build on demand.
  - Set up [Slack notifications](#) once a new build is done.
  - Implement [BrowserStack](#) for cross platform/browser testing.
  - Include a [.gitignore](#) file.

---
### Design Patterns
This project was designed with the following Design Patterns
> - [Factory](https://www.geeksforgeeks.org/factory-method-for-designing-pattern/)
> - [POM](https://www.geeksforgeeks.org/page-object-model-pom/)
> - [BDD](https://www.geeksforgeeks.org/behavioral-driven-development-bdd-in-software-engineering/) (Behavior-Driven Development)

---
### Project Structure
```md
.
├── Collections # POSTMAN Collections and Test Environments
├── README.md
├── config.py
├── factories # Path for Factory Patterns
├── features # Path for BDD Feature and Steps
│   ├── api
│   │   ├── environment.py
│   │   ├── *.feature
│   │   └── steps
│   │       └── *_steps.py
│   └── ui
│       ├── environment.py
│       ├── *.feature
│       └── steps
│           └── *_steps.py
├── pages # Path for POM's
│   └── *_page.py 
├── pyproject.toml # Poetry file where all depencencies and execution scripts are declared
├── *reports
└── todoist_client # Path for TODOIST API Clients
    ├── __init__.py
    └── *_client.py
```

---

### Docstrings

This project follows [PEP 257 Docstrings](https://peps.python.org/pep-0257/) Conventions

---
### Linters

This project follows [PEP 8 - Coding Styles](https://peps.python.org/pep-0008/), making use of the following tools
> - [Flake8](https://flake8.pycqa.org/en/latest/)
> - [Black](https://pypi.org/project/black/)
> - [MyPy](https://pypi.org/project/mypy/)

---
## Getting Started
The challenge project was based on Python Programming Language making use of the following Frameworks
> - [Selenium](https://www.selenium.dev/documentation/)
> - [Behave](https://behave.readthedocs.io/en/latest/)

All of this to interact on a well structured format with the web application making use of BDD practices.
This project is being managed by [`Poetry`](https://python-poetry.org/) as the Test Runner

### Setting things up
- Make sure to have Python version `3.11`
- Install Poetry
```bash
pip install poetry
``` 
#### Set your Environment Variables
> This project uses `dotenv` to manage local environment variables from file.
> Poetry takes care of those variables making use of the `dotenv - loadenv` dependency

- Environment Variables

Make sure to set a `.env` file under the Project root with the following data.
Don't forget to replace the data with valid information according to your personal account.
```txt
USERNAME_ENV="test@email.com"
PASSWORD_ENV="password"

TODOIST_API_TOKEN="abcdefghijk01234567890"
```
- Install project dependencies
```bash
poetry install
```

## Running Tests
As mentioned above we described Poetry not only as dependency and packaging manager, but as well as our Test Runner linking the Framework dependency.

### Running UI Test Automation
```bash
poetry run behave feature/ui
```

### Running API Test Automation
```bash
poetry run behave feature/api
```

### Running from Tags
Behave allows to integrate tags identifiers within the Gherkin Scenarios
To execute particular scenarios within the test context make use of the flag argument as follows
```bash
poetry run behave feature/api --flags=<flag_name>
```

## Test Coverage

- FrontEnd
    1. Successful login
    2. Unsuccessful login
    3. Create a new task
    4. Create a new project
- BackEnd
    1. Project
        1. Get all projects
        2. Create a new project
        3. Update a project
        4. Delete a project
    2. Task
        1. Get active tasks
        2. Create a new task
        3. Get an active task
        4. Update a task
        5. Delete a task



## REPORTS
Cómo acceder o generar reportes de pruebas (por ejemplo, Allure, HTML reports, etc.).
Comandos para visualizar reportes.


## CI/CD
Explicación de cómo está configurado el pipeline de integración continua, si es relevante.
Herramientas de CI/CD que se están utilizando (Jenkins, GitHub Actions, GitLab CI, etc.).


## CONTRIBUTIONS
Instrucciones para contribuir al proyecto.
Guías de estilo de código, PRs, issues, etc.


## CONTACT
- sabina.cebreroz@wizeline.com
- sabinaceb@gmail.com