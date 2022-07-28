from twine.commands.upload import upload
from twine.settings import Settings


def twine_upload(package_dist_path, pypi_user, pypi_password, repository_url):
    my_settings = Settings(repository_url=repository_url, username=pypi_user, password=pypi_password,
                           skip_existing=True, verbose=False)
    upload(my_settings, [package_dist_path])


if __name__ == "__main__":
    PACKAGE_PATH = "test_deps/*"
    # PACKAGE_PATH = "cloudshell-cm-ansible-1.5.6.3.zip"
    PYPI_USER = "pypiadmin"
    PYPI_PASSWORD = "pypiadmin"
    PYPI_REPO_URL = "http://localhost:8036"
    res = twine_upload(PACKAGE_PATH, PYPI_USER, PYPI_PASSWORD, PYPI_REPO_URL)
    pass