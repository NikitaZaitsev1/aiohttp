import jinja2

import aiohttp_jinja2
from aiohttp import web
from tortoise.contrib.aiohttp import register_tortoise

from fin_blog.web.home import views as home_views
from fin_blog.web.user import views as user_views
from fin_blog.conf import settings


def create_app():
    app = web.Application()
    register_tortoise(app, config=settings.DATABASE, generate_schemas=True)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            [
                path / "templates"
                for path in (settings.BASE_DIR / "web").iterdir()
                if path.is_dir() and (path / "templates").exists()
            ]
        )
    )
    app.router.add_static('/static', settings.BASE_DIR / "web" / "root")
    # app['static_root_url'] = 'settings.BASE_DIR / "web" / "root" / "static"'
    app.router.add_route("*", "/", home_views.HomeView, name="home_view")
    app.router.add_route("*", "/contact", home_views.ContactView, name="contact_view")
    app.router.add_route("*", "/about", home_views.AboutView, name="about_view")

    app.router.add_route("*", "/api/v1/user", user_views.UserView, name="user_endpoint")



    return app


async def get_application():
    return create_app()


def run():
    app = create_app()
    web.run_app(app, host="127.0.0.1")


"""gunicorn fin_blog.app.server:get_application --bind localhost:8080 --worker-class aiohttp.GunicornUVLoopWebWorker"""
