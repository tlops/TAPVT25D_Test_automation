Feature: Bookstore Shopping Cart Management
  As a user of the bookstore website,
  I want to manage items in my shopping cart,
  So that I can purchase the correct books.

  Scenario: Add a new book to an empty cart
    Given the shopping cart is empty
    When the user adds a book titled "Power" with a price of $200.00
    Then the cart should contain 1 book item
    And the total number of books should be 1
    And the cart total should be $200.00 
  
  Scenario: Remove a book from the cart
    Given the shopping cart contains a book titled "Power" with a quantity of 1 and a price of $200.00 
    When the user removes the book "Power"
    Then the cart should contain 0 book items
    And the total number of books should be 0
    And the cart total should be $0.00 

  Scenario Outline: Increase quantity when adding an existing book
    Given the shopping cart contains a book titled "<book_title>" with a quantity of 1 and a price of $250.00
    When the user adds a book titled "<book_title>" with a price of $250.00
    Then the cart should contain 1 book item
    And the total number of books should be <expected_quantity> 
    And the cart total should be $<expected_total>

    Examples:
      | book_title                    | initial_quantity | expected_quantity | expected_total |
      | 48 Laws of Power              | 3                | 4                 | 1000.00         |
      | The richest Man in Babylon    | 1                | 2                 | 500.00         |

  Scenario: Empty the entire shopping cart
    Given the shopping cart contains multiple items:
      | title           | price   | quantity |
      | Alchemist       | 300.00  | 2        |
      | The Odyssey     | 150.00  | 1        |
    When the user empties the cart
    Then the cart should contain 0 book items
    And the total number of books should be 0
    And the cart total should be $0.00
