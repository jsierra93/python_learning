from unittest import TestCase

from selenium.webdriver import Firefox

from screenpy import AnActor, given, when, then
from screenpy.abilities import BrowseTheWeb
from screenpy.resolutions import ContainsTheText

from ..questions.welcome_message import WelcomeMessage
from ..tasks.start import Start
from ..user_interface import home_page


class TestExample(TestCase):
    def setUp(self):
        self.actor = AnActor.named("Name me!").who_can(BrowseTheWeb.using(Firefox()))

    def test_open_homepage(self):
        "Tests that the user can visit the homepage. Extend me!"
        Actor = self.actor

        given(Actor).was_able_to(Start.on_the_homepage())
        # ... fill in your test steps here!
        then(Actor).should_see_the(
            (WelcomeMessage.text(), ContainsTheText("Welcome to ScreenPy"))
        )

    def tearDown(self):
        self.actor.exit_stage_right()
