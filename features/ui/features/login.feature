Feature: Login functionallity

@login @successful_login
Scenario: Successful Login
    Given the user navigates to the login page
    When the user logs in with valid credentials
    Then the user should be redirected to the dashboard

@login @unsuccessful_login
Scenario Outline: Unsuccessful Login
    Given the user navigates to the login page
    When the user logs in with invalid credentials "<invalid_user>" "<password>"
    Then the user should see an error message

Examples:
    | invalid_user   | password |
    | email@test.com | pass     |
    | email@         | password |
    | email@test     | password |
    | email@testcom  | password |
    | emailtest.com  | password |
    