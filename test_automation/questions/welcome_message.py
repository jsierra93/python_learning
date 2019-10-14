from screenpy.questions import Text
from screenpy.pacing import beat

from ..user_interface import home_page


class WelcomeMessage:
    @staticmethod
    def text():
        return WelcomeMessage()

    @beat("{0} checks the welcome message...")
    def answered_by(self, the_actor):
        return Text.of(home_page.WELCOME_MESSAGE).answered_by(the_actor)
