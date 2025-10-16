Feature: Bookstore Shopping Cart Management
  As a user of the bookstore website,
  I want to manage items in my shopping cart,
  So that I can purchase the correct books.

  Scenario: Add a new book to an empty cart
    Given the shopping cart is empty
    When the user adds a book titled "48 Laws of Power" with a price of 200.00 SEK
    Then the cart should contain 1 book item
    And the total number of books should be 1
    And the cart total should be 200.00 SEK
  
  Scenario: Remove a book from the cart
    Given the shopping cart contains a book titled "48 Laws of Power" with a quantity of 1 and a price of 200.00 SEK
    When the user removes the book "48 Laws of Power"
    Then the cart should contain 0 book items
    And the total number of books should be 0
    And the cart total should be 0.00 SEK

  Scenario Outline: Increase quantity when adding an existing book
    Given the shopping cart contains a book titled "The richest Man in Babylon" with a quantity of 1 and a price of 250.00 SEK
    When the user adds a book titled "The richest Man in Babylon" with a price of 250.00 SEK
    Then the cart should contain 1 book item
    And the total number of books should be 1
    And the cart total should be 500.00 SEK

    Examples:
      | book_title                    | initial_quantity | expected_quantity | expected_total |
      | 48 Laws of Power              | 3                | 4                 | 800.00         |
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