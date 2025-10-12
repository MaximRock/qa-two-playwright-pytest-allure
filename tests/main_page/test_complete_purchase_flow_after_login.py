import pytest

from pages.checkout_page_toolshop import CheckoutPageToolshop
from pages.main_page_toolshop import MainPageToolshop
from pages.product_page_toolshop import ProductPageToolshop


@pytest.mark.usefixtures("auth_user")
class TestCompletePurchaseFlowAfterLogin:
    """Тесты для проверки полного цикла покупки после авторизации пользователя."""

    @pytest.fixture
    def data_test(self, get_generated_file, full_name_translit) -> dict[str, str]:
        """
        Фикстура подготовки тестовых данных для покупки.
        Args:
            get_generated_file: Фикстура сгенерированных данных пользователя
            full_name_translit: Фикстура транслитерированного имени пользователя
        Returns:
            dict: Словарь с тестовыми данными для выполнения покупки
        """
        user_data = get_generated_file
        full_name = f"{user_data['first_name']} {user_data['last_name']}"
        holder_name = full_name_translit
        return {
            "search": "Nuts",
            "product": "M4 Nuts",
            "quantity": "5",
            "text_logged_in": (
                f"Hello {full_name}, "
                "you are already logged in. You can proceed to checkout."
            ),
            "user_data": user_data,
            "credit_card": "credit_card",
            "holder_name": holder_name,
            "payment_massage": "Payment was successful",
        }

    def test_complete_purchase_flow_after_login(
        self,
        data_test,
        main_page_toolshop: MainPageToolshop,
        product_page_toolshop: ProductPageToolshop,
        checkout_page_toolshop: CheckoutPageToolshop,
    ) -> None:
        """
        Тест полного цикла покупки после авторизации пользователя.

        Steps:
        1. Перейти на главную страницу
        2. Проверить отображение баннера
        3. Выполнить поиск товара
        4. Проверить результат поиска
        5. Перейти на страницу товара
        6. Проверить название товара
        7. Добавить несколько единиц товара в корзину
        8. Проверить отображение иконки корзины
        9. Проверить количество товаров в корзине
        10. Перейти в корзину
        11. Проверить URL корзины
        12. Начать оформление заказа
        13. Проверить авторизацию и продолжить
        14. Проверить данные плательщика
        15. Выбрать способ оплаты
        16. Заполнить данные кредитной карты
        17. Заполнить имя владельца карты
        18. Подтвердить заказ
        19. Проверить сообщение об успешной оплате

        Args:
            data_test: Фикстура с тестовыми данными
            main_page_toolshop: Фикстура главной страницы
            product_page_toolshop: Фикстура страницы товара
            checkout_page_toolshop: Фикстура страницы оформления заказа
        """
        main_page_toolshop.navbar.click_home_link()
        main_page_toolshop.banner.check_banner()
        main_page_toolshop.search(search_value=data_test["search"])
        main_page_toolshop.check_search_result(serch_result=data_test["product"])
        main_page_toolshop.click_product()
        product_page_toolshop.check_product_name(product_name=data_test["product"])
        product_page_toolshop.add_multiple_items(items=int(data_test["quantity"]))
        main_page_toolshop.navbar.check_icon_cart_visible()
        main_page_toolshop.navbar.check_quantity_icon_cart(
            text_quantity=data_test["quantity"]
        )
        main_page_toolshop.navbar.click_on_cart()
        checkout_page_toolshop.check_cart_url()
        checkout_page_toolshop.click_proceed_to_checkout_cart()
        checkout_page_toolshop.is_logged_in(text=data_test["text_logged_in"])
        checkout_page_toolshop.invoice_fields(data=data_test["user_data"])
        checkout_page_toolshop.choose_payment_method(
            payment_method=data_test["credit_card"]
        )
        checkout_page_toolshop.fill_credit_card(data=data_test["user_data"])
        checkout_page_toolshop.fill_card_holder_name(
            holder_name=data_test["holder_name"]
        )
        checkout_page_toolshop.click_confirm_button()
        checkout_page_toolshop.check_payment_success_message(
            text=data_test["payment_massage"]
        )
