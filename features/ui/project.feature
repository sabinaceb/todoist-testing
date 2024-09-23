Feature: Create a new project functionallity

Background:
    Given the user navigates to the login page
    When the user logs in with valid credentials

@project
Scenario: Create a new project
    When the user tap the new project button
    When the user create a project
    Then the user validates the project data
