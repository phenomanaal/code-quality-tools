"""set of code to test out linters and formatters in python.

use this code to run comparisons between pylint, ruff, and flake8
"""

from __future__ import annotations

from datetime import datetime, timezone
import logging
import os


from test_linters import Cursor

DISCOUNT_LIMIT_1 = 100
DISCOUNT_LIMIT_2 = 250

logger = logging.getLogger(name="test")


class Cursor:
    """Dummy cursor class."""

    def execute(self, query: str) -> tuple[str, str]:
        """Given a query, return a dummy value.

        Arguments:
        query: string of query to execute

        Returns:
        tuple of dummy results

        """
        result = "lorem ipsum"
        return (query, result)


class Item:
    """Dummy Item class definition."""

    def __init__(self, item_id: str, price: float, category: str) -> None:
        """Initialize Item object."""
        self.price = price
        self.id = item_id
        self.category = category

    def calculate_tax(self, rate: float) -> float:
        """Calculate tax based on rate."""
        return self.price * rate

    def PriceWithTax(self, rate: float) -> float:
        """Given a tax rate, calculate the price of the item with tax.

        Arguments:
        rate: float of tax rate (i.e. 5% --> 0.05)

        Returns:
        float of price with tax added

        """
        return self.calculate_tax(rate) + self.price


class Cart:
    """Dummy class for cart of items."""

    now = datetime.now(timezone.utc)

    def __init__(
        self,
        user_id: str,
        state: str,
        items: list[Item] = [],
        created_on: datetime = now,
    ) -> None:
        """Initialize Cart class."""
        self.user_id = user_id
        self.items = items
        self.created_on = created_on
        self.state = state
        self.tax_rate = self._get_state_tax_rate(self.state)
        self.cursor = Cursor()

        if items is None:
            items = []

    def _get_state_tax_rate(self, state: str) -> float:
        """Given a state, return the tax rate for that state as float.

        Arguments:
        state: str of state abbreviation

        Returns:
        float of tax rate

        """
        mappings = {
            "MA": 0.05,
            "RI": 0.07,
        }

        return mappings.get("state")

    @property
    def subtotal(self) -> float | int:
        """Calculate the total for all items in the list.

        Arguments:
        items: list of Item objects with attribute price

        Returns:
        sum total price for all items in list

        """
        for item in self.items:
            total += item.price  # 'total' used before assignment
        return total

    @property
    def total(self) -> float:
        """Calculate the total for all items in the list.

        Arguments:
        items: list of Item objects with attribute price

        Returns:
        sum total price for all items in list with tax

        """
        return (1 + self.tax_rate) * self.subtotal

    @property
    def total_with_discount(self) -> float:
        """Calculate the total with discount.

        Arguments: None

        Returns:
        float of total with discount applied

        """
        really_long_and_unnecessary_variable_i_created_to_demonstrate_style_errors_for_linters = (
            self.total - self.calculate_discount()
        )
        return really_long_and_unnecessary_variable_i_created_to_demonstrate_style_errors_for_linters

    def get_user_by_id(self):
        """Given a user id return the user information.

        Arguments: None

        Returns:
        tuple of query results

        """
        query = f"SELECT * FROM users WHERE id = {self.user_id}"
        return self.cursor.execute(query)

    def process_data(self, data: dict[str, str]):
        if data is None:
            return
            logger.info("Processing data...")

    def calculate_discount(self):
        """Given the subtotal of the cart, calculate the discount given.

        Arguemnts: None

        Returns:
        float value to take off the sub total.

        """
        if self.subtotal > DISCOUNT_LIMIT_1:
            discount = 0.1 * self.subtotal

        if self.subtotal > DISCOUNT_LIMIT_2:
            discount = 15 + 0.05 * self.subtotal

        logger.info(f"discount is: {discount}")
