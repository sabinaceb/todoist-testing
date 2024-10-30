Feature: Tasks from Todoist

@tasks
Scenario Outline: GET active Tasks
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    And the user request to get all Tasks
    Then the user should receive a 200 status code
    And the user close an active task

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:59 | en       | 4        |

@tasks
Scenario Outline: POST Create new Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    Then the user should receive a 200 status code
    And the user close an active task

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:59 | en       | 4        |

@tasks
Scenario Outline: POST Create new Task - Negative Scenario
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    Then the user should receive a 400 status code

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | date           | en       | 4        |

@tasks
Scenario Outline: GET active Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    And the user request to get an active task
    Then the user should receive a 200 status code
    And the user close an active task

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:59 | en       | 4        |

@tasks
Scenario: GET active Task - Negative Scenario
    When the user request to get a non-existing active task
    Then the user should receive a 400 status code

@tasks
Scenario Outline: POST update Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    And the user update an active task "<updated_content>"
    Then the user should receive a 200 status code
    And the user close an active task


Examples:
    | content   | due_string     | due_lang | priority | updated_content |
    | Buy Milk  | today at 23:59 | en       | 4        | Buy Coffee      |

@tasks
Scenario Outline: POST update Task - Negative Scenario
    And the user update a non-existing active task "<content>"
    Then the user should receive a 400 status code

Examples:
    | content    |
    | Buy Coffee |

@tasks
Scenario Outline: POST close Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    And the user close an active task
    Then the user should receive a 204 status code

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:50 | en       | 4        |

@tasks
Scenario: POST close Task - Negative Scenario
    And the user close a non-existing active task
    Then the user should receive a 400 status code

@tasks
Scenario Outline: POST reopen Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    And the user close an active task
    And the user reopen a specific task
    Then the user should receive a 204 status code
    And the user close an active task

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:50 | en       | 4        |

@tasks
Scenario: POST reopen Task - Negative Scenario
    And the user reopen a non-existing task
    Then the user should receive a 400 status code

@tasks
Scenario Outline: DELETE a Task
    When the user create a new task "<content>", "<due_string>", "<priority>", "<due_lang>"
    And the user delete an active task
    Then the user should receive a 204 status code

Examples:
    | content   | due_string     | due_lang | priority |
    | Buy Milk  | today at 23:50 | en       | 4        |

@tasks
Scenario: DELETE a Task - Negative Scenario
    And the user delete a non-existing active task
    Then the user should receive a 400 status code
