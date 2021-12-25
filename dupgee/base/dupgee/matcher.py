urls_module = __import__("{{ app_name }}.urls")
pages_module = __import__("{{ app_name }}.pages")


def match_url(path):
    for url in urls_module.urls.urls:
        if url.get("path") == path:
            return url.get("view")
    return pages_module.pages.HomepageView


def find_view(request):
    view_class = match_url(path=request.path)
    view = view_class()
    return view.dispatch(request=request)
