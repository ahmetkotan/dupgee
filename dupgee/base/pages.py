from dupgee.views import View
from dupgee.response import TemplateResponse, JsonResponse


class HomepageView(View):
    template_name = "index.html"

    def get(self, request):
        context = {"name": "Dupgee"}
        return TemplateResponse(context=context, template_name=self.template_name)


class ApiView(View):
    data = {"detail": "ok"}

    def post(self, request):
        request.data.update(self.data)
        return JsonResponse(request.data, status=201)
