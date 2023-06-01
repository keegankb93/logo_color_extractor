from typing import Dict
from pathlib import Path
from starlite.contrib.jinja import JinjaTemplateEngine
from app.controllers.application_controller import ApplicationController
from starlite import Starlite, TemplateConfig


app = Starlite(
    route_handlers=[ApplicationController],
    template_config=TemplateConfig(
        directory=Path(__file__).parent.joinpath("app/views"),
        engine=JinjaTemplateEngine,
    ),
)

# run: /
