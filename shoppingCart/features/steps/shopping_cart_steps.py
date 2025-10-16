# steps/bookstore_steps.py
from behave import given, when, then, step
from CartClass import ShoppingCart
# --- GIVEN steps ---

@given('the shopping cart is empty')
def step_impl(context):
    """Initializes a new, empty shopping cart."""
    context.cart = ShoppingCart()

@given('the shopping cart contains a book titled "{title}" with a quantity of {quantity:d} and a price of ${price:f}')
def step_impl(context, title, quantity, price):
    """Initializes a cart with a specific book item."""
    context.cart = ShoppingCart()
    context.cart.items[title] = {'price': price, 'quantity': quantity}

@given('the shopping cart contains multiple items:')
def step_impl(context):
    """Initializes a cart with multiple items from a Gherkin table."""
    context.cart = ShoppingCart()
    for row in context.table:
        title = row['title']
        price = float(row['price'])
        quantity = int(row['quantity'])
        context.cart.items[title] = {'price': price, 'quantity': quantity}

# --- WHEN steps ---

@when('the user adds a book titled "{title}" with a price of ${price:f}')
def step_impl(context, title, price):
    """Calls the add_book method."""
    context.cart.add_book(title, price)

@when('the user removes the book "{title}"')
def step_impl(context, title):
    """Calls the remove_book method."""
    context.cart.remove_book(title)

@when('the user empties the cart')
def step_impl(context):
    """Calls the empty_cart method."""
    context.cart.empty_cart()

# --- THEN steps ---

@then('the cart should contain {expected_items:d} book item\w*')
def step_impl(context, expected_items):
    """Verifies the number of unique items in the cart."""
    assert context.cart.total_items == expected_items, \
        f"Expected {expected_items} unique items, but found {context.cart.total_items}"

@then('the total number of books should be {expected_books:d}')
def step_impl(context, expected_books):
    """Verifies the total quantity of all books."""
    assert context.cart.total_books == expected_books, \
        f"Expected {expected_books} total books, but found {context.cart.total_books}"

@then('the cart total should be ${expected_total:f}')
def step_impl(context, expected_total):
    """Verifies the calculated total sum."""
    actual_total = context.cart.total_sum
    # Use a small tolerance for floating point comparison
    assert abs(actual_total - expected_total) < 0.001, \
        f"Expected total ${expected_total:.2f}, but found ${actual_total:.2f}"