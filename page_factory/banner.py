from page_factory.component import Component


class Banner(Component):
    """Компонент баннера для страниц приложения."""

    @property
    def type_of(self) -> str:
        """Возвращает тип компонента для использования в логировании и
        сообщениях об ошибках.
        Returns:
            str: Тип компонента - 'banner'
        """
        return "banner"
