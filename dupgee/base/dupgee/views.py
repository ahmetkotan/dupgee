class View:
    def dispatch(self, request):
        http_method_function = getattr(self, request.method.lower(), None)
        if http_method_function is None:
            from .response import JsonResponse
            return JsonResponse({"detail": "This method is not allowed."})
        return http_method_function(request=request)
