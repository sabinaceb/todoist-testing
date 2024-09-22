Feature: Projects from Todoist

@project
Scenario Outline: GET active Projects
    When the user create a new project "<name>"
    And the user request to get all Projects
    Then the user should receive a 200 status code
    And the user delete a project

Examples:
    | name          |
    | Shopping List |

@project
Scenario Outline: POST Create new Project
    When the user create a new project "<name>"
    Then the user should receive a 200 status code
    And the user delete a project

Examples:
    | name          |
    | Shopping List |

@project
Scenario Outline: POST Create new Project - Negative Scenario
    When the user create a new project with invalid data "<name>", "<color>"
    Then the user should receive a 400 status code

Examples:
    | name            | color |
    | Shopping List 2 | rojo  |

@project
Scenario Outline: GET active Project
    When the user create a new project "<name>"
    And the user request to get a project
    Then the user should receive a 200 status code
    And the user delete a project

Examples:
    | name          |
    | Shopping List |

@project
Scenario: GET active Project - Negative Scenario
    When the user request to get a non-existing project
    Then the user should receive a 400 status code

@project
Scenario Outline: POST update Project
    When the user create a new project "<name>"
    And the user update a project "<updated_name>"
    Then the user should receive a 200 status code
    And the user delete a project

Examples:
    | name          | updated_name  |
    | Shopping List | Things To Buy |

@project
Scenario Outline: POST update Project - Negative Scenario
    When the user update a non-existing project "<name>"
    Then the user should receive a 400 status code

Examples:
    | name          |
    | Things To Buy |

@project
Scenario Outline: DELETE a Project
    When the user create a new project "<name>"
    And the user delete a project
    Then the user should receive a 204 status code

Examples:
    | name          |
    | Shopping List |

@project
Scenario Outline: DELETE a Project - Negative Scenario
    When the user delete a non-existing project
    Then the user should receive a 400 status code

Examples:
    | name          |
    | Shopping List |

@project
Scenario Outline: GET Project collaborators
    When the user create a new project "<name>"
    And the user request to get the collaborators of a project
    Then the user should receive a 200 status code
    And the user delete a project 

Examples:
    | name          |
    | Shopping List |

@project
Scenario: GET Project collaborators - Negative Scenario
    When the user request to get the collaborators of a non-existing project
    Then the user should receive a 400 status code
