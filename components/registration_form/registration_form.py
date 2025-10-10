from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.select import Select


class RegistrationForm:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.country_select: Select = Select(
            page,
            locator="div>div>select",
            name="Select option",
        )
        self.input_password: Input = Input(
            page,
            locator="input[data-test='password']",
            name="Password input",
        )
        self.first_name_input: Input = Input(
            page,
            locator="input[data-test='first-name']",
            name="First name input",
        )
        self.last_name_input: Input = Input(
            page,
            locator="input[data-test='last-name']",
            name="Last name input",
        )
        self.date_of_birth_input: Input = Input(
            page,
            locator="input[data-test='dob']",
            name="Date of birth input",
        )
        self.street_input: Input = Input(
            page,
            locator="input[data-test='street']",
            name="Street input",
        )
        self.postal_code_input: Input = Input(
            page,
            locator="input[data-test='postal_code']",
            name="Postal code input",
        )
        self.city_input: Input = Input(
            page,
            locator="input[data-test='city']",
            name="City input",
        )
        self.region_input: Input = Input(
            page,
            locator="input[data-test='state']",
            name="Region input",
        )
        self.phone_input: Input = Input(
            page,
            locator="input[data-test='phone']",
            name="Phone input",
        )
        self.email_input: Input = Input(
            page,
            locator="input[data-test='email']",
            name="Email input",
        )
        self.first_name_empty_error: Input = Input(
            page,
            locator="[data-test='first-name-error']",
            name="First name error",
        )
        self.last_name_empty_error: Input = Input(
            page,
            locator="[data-test='last-name-error']",
            name="Last name error",
        )
        self.date_of_birth_empty_error: Input = Input(
            page,
            locator="[data-test='dob-error'] div:last-of-type",
            name="Date of birth error",
        )
        self.street_empty_error: Input = Input(
            page,
            locator="[data-test='street-error']",
            name="Street error",
        )
        self.postal_code_empty_error: Input = Input(
            page,
            locator="[data-test='postal_code-error']",
            name="Postal code error",
        )
        self.city_empty_error: Input = Input(
            page,
            locator="[data-test='city-error']",
            name="City error",
        )
        self.region_empty_error: Input = Input(
            page,
            locator="[data-test='state-error']",
            name="Region error",
        )
        self.country_empty_error: Input = Input(
            page,
            locator="[data-test='country-error']",
            name="Country error",
        )
        self.phone_empty_error: Input = Input(
            page,
            locator="[data-test='phone-error']",
            name="Phone error",
        )
        self.email_empty_error: Input = Input(
            page,
            locator="[data-test='email-error']",
            name="Email error",
        )
        self.password_empty_error: Input = Input(
            page,
            locator="[data-test='password-error'] div:first-child",
            name="Password error",
        )

    def fill_all_fields_except(self, data: dict, exclude_field=None) -> None:
        field_mapping = {
            "first_name": (self.first_name_input, "fill"),
            "last_name": (self.last_name_input, "fill"),
            "date_of_birth": (self.date_of_birth_input, "fill"),
            "street_name": (self.street_input, "fill"),
            "postcode": (self.postal_code_input, "fill"),
            "city": (self.city_input, "fill"),
            "region": (self.region_input, "fill"),
            "country": (self.country_select, "select"),
            "phone": (self.phone_input, "fill"),
            "email": (self.email_input, "fill"),
            "password": (self.input_password, "fill"),
        }

        if exclude_field and exclude_field in field_mapping:
            locator, method = field_mapping[exclude_field]
            if method == "fill":
                locator.clear()
            elif method == "select":
                locator.select_option("")

        for field_name, value in data.items():
            if field_name != exclude_field and field_name in field_mapping:
                locator, method = field_mapping[field_name]
                if method == "fill":
                    locator.fill(value)
                elif method == "select":
                    locator.select_option(value)

    def check_error_text(self, error_field):
        error_mapping = {
            "first_name": (self.first_name_empty_error, " First name is required "),
            "last_name": (self.last_name_empty_error, " Last name is required "),
            "date_of_birth": (
                self.date_of_birth_empty_error,
                " Date of Birth is required ",
            ),
            "street_name": (self.street_empty_error, " Street is required "),
            "postcode": (self.postal_code_empty_error, " Postcode is required "),
            "city": (self.city_empty_error, " City is required "),
            "region": (self.region_empty_error, " State is required "),
            "country": (self.country_empty_error, " Country is required "),
            "phone": (self.phone_empty_error, " Phone is required. "),
            "email": (self.email_empty_error, " Email is required "),
            "password": (self.password_empty_error, " Password is required "),
        }

        if error_field not in error_mapping:
            raise ValueError(f"Field {error_field} not found in error mapping.")

        locator, error_text = error_mapping[error_field]
        locator.should_to_have_text(error_text)
