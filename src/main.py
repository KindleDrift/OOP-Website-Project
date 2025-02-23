from fasthtml.common import *
from classes.hotel import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Hello, World!", "Lorem ipsum dolor sit amet, consectetur adipiscing elit,")


serve()