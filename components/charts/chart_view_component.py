from playwright.sync_api import Page

from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
