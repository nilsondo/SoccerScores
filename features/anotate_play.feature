Feature: Annotate play

Scenario: Annotating a play
    Given add a play minute 1 type 0 spec 0 team home and description gol
    When we add all these plays to the match DALVSNEW15
    Then all these plays should have been added
