from playwright.sync_api import Page

from components.authentication.login_form_component import LoginFormComponent
from components.base_component import BaseComponent


class CreateExerciseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
