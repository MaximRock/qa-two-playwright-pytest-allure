from page_factory.component import Component


class Banner(Component):
    @property
    def type_of(self) -> str:
        return "banner"
