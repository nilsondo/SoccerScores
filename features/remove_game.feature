Feature: Remove a game

Scenario: Removing a game
    Given we want to remove a game
    When having mid DALVSNEW15
    Then the instance of the game must be removed
