import re


def load_template(template_name):
    template_path = "/{{ app_name }}/templates/{0}".format(template_name)
    with open(template_path, "r") as f:
        return f.read().strip()


def render_html(context, template_name):
    content = load_template(template_name=template_name)

    for variable, value in context.items():
        pattern = r"{{\s*%s\s*}}" % variable
        content = re.sub(pattern, value, content)

    return content
