from fasthtml.common import *

class Hotel:
    pass


class User:
    pass


app, rt = fast_app()

@rt("/")
def get():
    return Titled("Hello, World!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit,")


serve()