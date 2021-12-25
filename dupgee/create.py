import os
import shutil


def move_files(files, src_prefix, dst_prefix, app_name):
    for file_name, attributes in files.items():
        file_path = os.path.join(src_prefix, file_name)
        dest_path = os.path.join(dst_prefix, file_name)
        if attributes["static"]:
            shutil.copy(file_path, dest_path)
        else:
            with open(file_path, "r") as file:
                content = file.read()
            with open(dest_path, "w") as file:
                file.write(content.replace("{{ app_name }}", app_name))


def create_project(name):
    project_path = os.path.join(os.getcwd(), name)
    project_templates_path = os.path.join(project_path, "templates")
    project_dupgee_path = os.path.join(project_path, "dupgee")

    os.mkdir(project_path)
    os.mkdir(project_templates_path)
    os.mkdir(project_dupgee_path)

    absolute_path = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.join(absolute_path, "base")
    dupgee_path = os.path.join(base_path, "dupgee")

    base_files = {
        "runner.py": {"static": False},
        "urls.py": {"static": True},
        "pages.py": {"static": True},
        "__init__.py": {"static": True},
    }

    dupgee_files = {
        "__init__.py": {"static": True},
        "parsers.py": {"static": True},
        "render.py": {"static": False},
        "response.py": {"static": True},
        "request.py": {"static": True},
        "views.py": {"static": True},
        "server.py": {"static": True},
        "utils.py": {"static": True},
        "wifi.py": {"static": True},
        "matcher.py": {"static": False},
    }

    move_files(base_files, base_path, project_path, app_name=name)
    move_files(dupgee_files, dupgee_path, project_dupgee_path, app_name=name)

    with open(os.path.join(project_templates_path, "index.html"), "w") as f:
        index_html = """<html lang="en">
    <head>
        <title>Dupgee Framework</title>
    </head>
    <body>
        <h2>{{ name }}</h2>
    </body>
</html>"""
        f.write(index_html)

    print(f"{name} project created at {project_path}")
