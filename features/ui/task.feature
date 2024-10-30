Feature: Create a new task functionallity

Background:
    Given the user navigates to the login page
    When the user logs in with valid credentials

@task
Scenario Outline: Create a new task
    When the user click the add task button
    When the user creates "<number>" tasks

Examples:
    | number |         
    | 10     |