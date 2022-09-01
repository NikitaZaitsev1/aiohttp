import pathlib
from setuptools import setup, find_packages

BASE_DIR = pathlib.Path(__file__).parent.absolute()


def get_version():
    with open(BASE_DIR / "VERSION") as file:
        return file.readline().strip()


def get_license():
    with open(BASE_DIR / "LICENSE") as file:
        return file.read().strip()


def get_description():
    with open(BASE_DIR / "README.md") as file:
        return file.read().strip()


def get_packages():
    with open(BASE_DIR / "requirements.txt") as file:
        return [package.strip() for package in file.readlines()]


setup(
    name="fin_blog",
    version=get_version(),
    author="Nikita Zaitsev",
    author_email="nikniks77@gmail.com",
    url="",
    license=get_license(),
    packages=find_packages(".", include=["fin_blog"]),
    package_dir={"": "."},
    include_package_data=True,
    description="Finance blog",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    install_requires=get_packages(),
    python_require=">=3.8",
    zip_sefe=True,
    entry_points={"console_scripts": ["fin_blog = fin_blog.app:run"]},
    classifiers=[
        "Development Status :: 3 - Alpha"
        if "dev" in get_version()
        else "Development Status :: 4 Beta"
        if "rc" in get_version()
        else "Development Status :: 5 Production/Stable"
    ],
)
