from screenpy import Target


url = "https://screenpy-docs.readthedocs.io/en/latest/"

WELCOME_MESSAGE = Target.the("welcome message").located_by(
    "#welcome-to-screenpy-s-documentation>h1"
)
