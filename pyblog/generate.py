import yaml

from .page import Page


def generate_index_html():
    with open("config.yaml", "r") as file:
        metadata = yaml.safe_load(file)
    landing_page = Page(metadata, "templates/index.html")
    landing_page.inject_templates()
    landing_page.generate_html()
