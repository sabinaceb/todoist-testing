Feature: Tasks from Todoist

Scenario: GET active Tasks
    When the user request to get all Tasks
    Then the user should receive a 200 status code


Scenario Outline: POST Create new Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    Then the user should receive a 200 status code
    And the user close an active task
    Then the user should receive a 204 status code

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:59 | en       | 4        |


Scenario Outline: POST Create new Task - Negative Scenario
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    Then the user should receive a 400 status code

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | date           | en       | 4        |


Scenario: GET active Task
    When the user request to get an active task
    Then the user should receive a 200 status code


Scenario: GET active Task - Negative Scenario
    When the user request to get a non-existing active task
    Then the user should receive a 400 status code


Scenario Outline: POST update Task
    And the user update an active task "<content>"
    Then the user should receive a 200 status code

Examples:
    | content    |
    | Buy Coffee |


Scenario Outline: POST update Task - Negative Scenario
    And the user update a non-existing active task "<content>"
    Then the user should receive a 400 status code

Examples:
    | content    |
    | Buy Coffee |


Scenario Outline: POST close Task
    And the user close an active task
    Then the user should receive a 204 status code
    And the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:50 | en       | 4        |


Scenario: POST close Task - Negative Scenario
    And the user close a non-existing active task
    Then the user should receive a 400 status code


Scenario: POST reopen Task
    And the user reopen a specific task
    Then the user should receive a 204 status code


Scenario: POST reopen Task - Negative Scenario
    And the user reopen a non-existing task
    Then the user should receive a 400 status code


Scenario Outline: DELETE a Task
    And the user delete an active task
    Then the user should receive a 204 status code
    And the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    Then the user should receive a 200 status code

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:50 | en       | 4        |



Scenario: DELETE a Task - Negative Scenario
    And the user delete a non-existing active task
    Then the user should receive a 400 status code



# PROJECTS
# Feature: Projects from Todoist

Scenario: GET active Projects
    When the user request to get all Projects
    Then the user should receive a 200 status code


Scenario Outline: POST Create new Project
    When the user create a new project "<name>"
    Then the user should receive a 200 status code
    When the user delete a project
    Then the user should receive a 204 status code

Examples:
    | name          |
    | Shopping List |


Scenario Outline: POST Create new Project - Negative Scenario
    When the user create a new project with invalid data "<name>", "<color>"
    Then the user should receive a 400 status code

Examples:
    | name            | color |
    | Shopping List 2 | rojo  |


Scenario: GET active Project
    When the user request to get a project
    Then the user should receive a 200 status code


Scenario: GET active Project - Negative Scenario
    When the user request to get a non-existing project
    Then the user should receive a 400 status code


Scenario Outline: POST update Project
    And the user update a project "<name>"
    Then the user should receive a 200 status code

Examples:
    | name          |
    | Things To Buy |


Scenario Outline: POST update Project - Negative Scenario
    And the user update a non-existing project "<name>"
    Then the user should receive a 400 status code

Examples:
    | name          |
    | Things To Buy |


Scenario Outline: DELETE a Project
    And the user delete a project
    Then the user should receive a 204 status code
    When the user create a new project "<name>"
    Then the user should receive a 200 status code

Examples:
    | name          |
    | Shopping List |


Scenario Outline: DELETE a Project - Negative Scenario
    And the user delete a non-existing project
    Then the user should receive a 400 status code

Examples:
    | name          |
    | Shopping List |


Scenario: GET Project collaborators
    And the user request to get the collaborators of a project
    Then the user should receive a 200 status code


Scenario: GET Project collaborators - Negative Scenario
    And the user request to get the collaborators of a non-existing project
    Then the user should receive a 400 status code