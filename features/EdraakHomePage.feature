Feature: Marketing home page

  Scenario: All clickable buttons are redirected the user to correct page
    Test approach: the test will press command [contrl] from keyboard then click the button to open the new new page in new tab, so the home page will load one time instead of several times
    When the user visits the Home Page
    And the user clicks the Close Cookies container
    And the user opens a specific page by clicks the following elements
      | Element to click               | Expected Page |
      | Explore button                 | Explore page  |
      | Discover Programs button       | Explore page  |
      | Explore Specializations button | Explore page  |
      | First Course Card              | Programs page |
      | Show All Partners button       | Partners page |
      | Visit K12 Platform button      | K12 page      |


  Scenario: Popular Courses Oreder
    When the user visits the Home Page
    And the user clicks the Close Cookies container
    And the user clicks the Business and Entrepreneurship
    Then the following elements should be displayed with specific text
    | Elements           | Expected Text                              |
    | First Course Card  | Safe Investments During An Economic Crisis |
    | Second Course Card | Operations Management                      |
    | Third Course Card  | Accounting for Non-Accountants             |
    When the user clicks the Persona Development
    Then the following elements should be displayed with specific text
    | Elements           | Expected Text      |
    | First Course Card  | Mind Mapping       |
    | Second Course Card | Business Etiquette |
    | Third Course Card  | Leadership Skills  |
    When the user clicks the Science And Technology
    Then the following elements should be displayed with specific text
    | Elements           | Expected Text                    |
    | First Course Card  | Advanced Excel                   |
    | Second Course Card | Building Website Using Wordpress |
    | Third Course Card  | Data Science & Machine Learning  |