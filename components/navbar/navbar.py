from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.link import Link


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.sign_in_link: Link = Link(
            page,
            locator="//a[text()='Sign in']",
            name="Sign in",
        )
        self.navbar_toggler: Button = Button(
            page,
            locator="button.navbar-toggler[data-bs-target='#navbarSupportedContent']",
            name="navbar-toggler",
        )
        self.home_link: Link = Link(
            page,
            locator="a[data-test='nav-home']",
            name="Link to home page",
        )
        self.nav_menu: Link = Link(
            page,
            locator="[data-test='nav-menu']",
            name="Link to menu page",
        )
        self.nav_cart: Link = Link(
            page,
            locator="a[data-test='nav-cart']",
            name="Link to menu cart",
        )
        self.cart_quantity: Link = Link(
            page,
            locator="[data-test='cart-quantity']",
            name="Cart cart-quantity",
        )

    def visit_login_page(self) -> None:
        if self.navbar_toggler:
            self.navbar_toggler.click()
            self.sign_in_link.wait_for_link(state="visible")
            self.sign_in_link.click()
        else:
            self.sign_in_link.click()

    def click_home_link(self) -> None:
        if self.navbar_toggler:
            self.navbar_toggler.click()
            self.home_link.wait_for_link(state="visible")
            self.home_link.click()
        else:
            self.home_link.click()

    def check_user_login(self, user_text) -> None:
        if self.navbar_toggler:
            self.navbar_toggler.click()
            self.nav_menu.should_to_have_text(text=user_text)
        else:
            self.nav_menu.should_to_have_text(text=user_text)

    def click_on_cart(self) -> None:
        self.nav_cart.click()

    def check_icon_cart_visible(self) -> None:
        self.nav_cart.should_be_visible()

    def check_quantity_icon_cart(self, text_quantity: str) -> None:
        self.cart_quantity.should_to_have_text(text=text_quantity)
