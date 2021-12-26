from dupgee.utils import path

from .pages import HomepageView, ApiView, BasicView


urls = [
    path(pattern="/", view=HomepageView),
    path(pattern="/api", view=ApiView),
    path(pattern="/basic", view=BasicView),
]
