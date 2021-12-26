from dupgee.views import View
from dupgee.response import TemplateResponse, JsonResponse, HttpResponse


class HomepageView(View):
    template_name = "index.html"

    def get(self, request):
        name = request.parameters.get("name", "Dupgee")
        context = {"name": name}
        return TemplateResponse(context=context, template_name=self.template_name)


class BasicView(View):
    message = "<h2>basic page</h2>"

    def get(self, request):
        return HttpResponse(html=self.message)


class ApiView(View):
    data = {"detail": "ok"}

    def post(self, request):
        request.data.update(self.data)
        return JsonResponse(request.data, status=201)
