from cookiecutter.main import cookiecutter

GITHUB_REPO = "gh:katzy687/cookiecutter-pypackage-minimal"

ec = {"package_name": "natti-test"}
response = cookiecutter(template=GITHUB_REPO, no_input=True, extra_context=ec)
pass