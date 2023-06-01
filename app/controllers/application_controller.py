from typing import Any, Annotated, Dict
from starlite import Template, MediaType
from starlite.datastructures import UploadFile
from starlite.controller import Controller
from starlite.handlers import get, post
from starlite.enums import RequestEncodingType
from starlite.params import Body
from lib.image_color_parser import ImageColorParser


class ApplicationController(Controller):
    path = "/"

    @get()
    def hello_world(self) -> Template:
        """Handler function that returns a greeting dictionary."""
        return Template(name="app.html.jinja2", context={"hello": "world"})

    @post("/submit")
    def submit(self, data: UploadFile = Body(media_type=RequestEncodingType.MULTI_PART)) -> Template:
        """Handler function that returns a greeting dictionary."""
        processed_image = ImageColorParser(data)
        colors = processed_image.get_common_colors(5)
        return Template(name="submit.html.jinja2", context={"colors": colors})
