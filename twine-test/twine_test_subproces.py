from subprocess import Popen, PIPE


def update_pypi(package_path, pypi_user, pypi_password, repository_url):
    command = f"python -m twine upload {package_path} --username {pypi_user} --password {pypi_password} --repository-url {repository_url} --skip-existing --verbose"
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    outp = process.stdout.read()
    err_outp = process.stderr.read()
    return outp, err_outp


if __name__ == "__main__":
    PACKAGE_PATH = "test_deps"
    PYPI_USER = "pypiadmin"
    PYPI_PASSWORD = "pypiadmin"
    PYPI_REPO_URL = "http://localhost:8036"
    outp, err_outp = update_pypi(PACKAGE_PATH, PYPI_USER, PYPI_PASSWORD, PYPI_REPO_URL)
    print(outp)
    if err_outp:
        print(f"error output:\n{err_outp}")
