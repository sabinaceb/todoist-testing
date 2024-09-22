TITLE: SQA Challenge project


DESCRIPTION: Todoist website automation (FrontEnd and BackEnd)
- FrontEnd
    1. Successful login
    2. Unsuccessful login
    3. Create a new task
    4. Create a new project
- BackEnd
    1. Proyect
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
Tools: Selenium, Behave, Python
Testing Coverage: Feature Testing (FE y BE)


STRUCTURE:
- factories
    1. page_factory.py: Design pattern
- features: Behave
    1. login.feature
    2. new_project.feature
    3. new_task.feature
    - steps
        1. login_steps.py
        2. new_project_steps.py
        3. new_task_steps.py
    - environment.py: Hooks
- pages: POM
    1. login_page.py
    2. new_project_page.py
    3. new_task_page.py
- .env: sensible test data
- .gitignore: Files to be ignored for Git


PRE-REQUIREMENTS
- Install:
    - poetry
        pip install poetry
    - Python version manager
        brew update
        brew install pyenv
    - Python
        pyenv instal 3.11.8
    - Selenium
        poetry add selenium
    - Behave
        poetry add behave


INSTALATION
~ git clone https://github.com/tu_proyecto.git
~ cd tu_proyecto
~ npm install


CONFIGURATION
Cómo configurar variables de entorno, archivos config.json, o archivos .env.
Descripción de archivos de configuración importantes (URLs de prueba, credenciales, etc.).


EXECUTION
- All
    poetry run behave
- By tag
    poetry run behave --tags=@task


REPORTS
Cómo acceder o generar reportes de pruebas (por ejemplo, Allure, HTML reports, etc.).
Comandos para visualizar reportes.


CI/CD
Explicación de cómo está configurado el pipeline de integración continua, si es relevante.
Herramientas de CI/CD que se están utilizando (Jenkins, GitHub Actions, GitLab CI, etc.).


CONTRIBUTIONS
Instrucciones para contribuir al proyecto.
Guías de estilo de código, PRs, issues, etc.


CONTACT
sabina.cebreroz@wizeline.com
