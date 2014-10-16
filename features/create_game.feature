# -- FILE: features/anotator.feature
Feature: Create a game
 In order to create a game I want the anotator
 to be able to do create a game with home &
 away team

Scenario: Create a new game
    Given we want to create a new game
    When Dallas is home and NewYork is away
    Then a new game with home Dallas and away NewYork is created

Scenario: View a game
    Given we want to view a game
    When we have a mid DALVSNEW15
    Then an instance of the game must be returned
