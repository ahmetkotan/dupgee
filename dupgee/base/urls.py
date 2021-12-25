from dupgee.utils import path

from .pages import HomepageView, ApiView


urls = [
    path(pattern="/", view=HomepageView),
    path(pattern="/api", view=ApiView)
]
