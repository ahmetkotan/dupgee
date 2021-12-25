import ujson

from .render import render_html


class BaseResponse:
    content_type = ""
    content = ""
    status = ""

    def render(self):
        return self.content

    def get_content(self):
        return self.render()

    def get_status_code(self):
        return self.status or 200

    @classmethod
    def get_content_type(cls):
        return cls.content_type or "text/html"


class HttpResponse(BaseResponse):
    def __init__(self, html, status=200):
        self.content = html
        self.status = status


class TemplateResponse(BaseResponse):
    context = {}
    template_name = ""

    def __init__(self, context, template_name, status=200):
        self.context = context
        self.template_name = template_name
        self.status = status

    def render(self):
        return render_html(context=self.context, template_name=self.template_name)


class JsonResponse(BaseResponse):
    content_type = "application/json"
    data = {}

    def __init__(self, data, status=200):
        self.data = data
        self.status = status

    def render(self):
        return ujson.dumps(self.data)
