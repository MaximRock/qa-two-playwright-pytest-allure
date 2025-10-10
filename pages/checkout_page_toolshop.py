from playwright.sync_api import Page, expect

from components.registration_form.registration_form import RegistrationForm
from page_factory.button import Button
from page_factory.input import Input
from page_factory.paragraph import Paragraph
from page_factory.select import Select
from pages.base_page import BasePage


class CheckoutPageToolshop(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.form: RegistrationForm = RegistrationForm(page)
        self.checkout_url: str = self.urls["checkout"]
        self.cart_proceed_to_checkout: Button = Button(
            page,
            locator="button[data-test='proceed-1']",
            name="Button proceed to checkout cart",
        )
        self.logged_in: Paragraph = Paragraph(
            page,
            locator="p.ng-star-inserted",
            name="Paragraph Signed in",
        )
        self.sign_in_proceed_to_checkout: Button = Button(
            page,
            locator="button[data-test='proceed-2']",
            name="Button proceed to checkout sign in",
        )
        self.country_input: Input = Input(
            page,
            locator="input[data-test='country']",
            name="Country input",
        )
        self.billing_address_proceed_to_checkout: Button = Button(
            page,
            locator="button[data-test='proceed-3']",
            name="Button proceed to checkout billing address",
        )
        self.payment_method: Select = Select(
            page,
            locator="select[data-test='payment-method']",
            name="Select payment method",
        )
        self.credit_card_number: Input = Input(
            page,
            locator="input[data-test='credit_card_number']",
            name="Input credit card number",
        )
        self.expiration_date: Input = Input(
            page,
            locator="input[data-test='expiration_date']",
            name="Input expiration date",
        )
        self.cvv: Input = Input(
            page,
            locator="input[data-test='cvv']",
            name="Input cvv",
        )
        self.card_holder_name: Input = Input(
            page,
            locator="input[data-test='card_holder_name']",
            name="Input card holder name",
        )
        self.button_confirm: Button = Button(
            page,
            locator="//button[text()=' Confirm ']",
            name="Button confirm",
        )
        self.payment_success_message: Paragraph = Paragraph(
            page,
            locator="[data-test='payment-success-message']",
            name="Paragraph payment success message",
        )

    def check_cart_url(self) -> None:
        self.get_current_page(url=self.checkout_url)

    def click_proceed_to_checkout_cart(self) -> None:
        self.cart_proceed_to_checkout.click()

    def is_logged_in(self, text: str) -> None:
        self.logged_in.must_contain_text(text=text)
        self.sign_in_proceed_to_checkout.click()

    def invoice_fields(self, data: dict) -> None:
        field_mapping: dict[str, Input] = {
            "street_name": self.form.street_input,
            "city": self.form.city_input,
            "region": self.form.region_input,
            "country": self.country_input,
            "postcode": self.form.postal_code_input,
        }

        for field_name, value in data.items():
            if field_name in field_mapping:
                locator: Input = field_mapping[field_name]
                locator.should_have_value(value=value)

        self.billing_address_proceed_to_checkout.click()

    def choose_payment_method(self, payment_method: str) -> None:
        option_mapping: dict[str, str] = {
            "bank_transfer": "Bank Transfer",
            "cash_on_delivery": "Cash on Delivery",
            "credit_card": "Credit Card",
            "buy_now_pay_later": "Buy Now Pay Later",
            "gift_card": "Gift Card",
            }

        for option, value in option_mapping.items():
            if payment_method == option:
                self.payment_method.select_option(value=value)
                break

    def fill_credit_card(self, data: dict, exlude_field=None) -> None:
        credit_card_mapping: dict[str, Input] = {
            "cart_number": self.credit_card_number,
            "expiration_date": self.expiration_date,
            "cvv": self.cvv,
        }

        if exlude_field and exlude_field in credit_card_mapping:
            locator: Input = credit_card_mapping[exlude_field]
            locator.clear()

        for field_name, value in data.items():
            if field_name != exlude_field and field_name in credit_card_mapping:
                locator: Input = credit_card_mapping[field_name]
                locator.fill(value=value)

    def fill_card_holder_name(self, holder_name: str) -> None:
        self.card_holder_name.fill(value=holder_name)

    def click_confirm_button(self) -> None:
        self.button_confirm.click()

    def check_payment_success_message(self, text: str) -> None:
        self.payment_success_message.should_to_have_text(text=text)
