import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()

DATABASE = {
    "connections": {
        "default": "sqlite://{}".format(BASE_DIR / "fin_blog.sqlite")
    },
    "apps": {
        "user": {
            "models": ["fin_blog.web.user.models"],
            "default_connection": "default",
        }

        #     "auth": {
        #         "models": ["collect.web.auth.models"],
        #         "default_connection": "default",
        #     },
        # "staff": {
        #     "models": ["collect.web.staff.models"],
        #     "default_connection": "default",
        # },
        # "task": {
        #     "models": ["collect.web.task.models"],
        #     "default_connections": "default",
        #     # }
    },
    "use_tz": True,
    "timezone": "UTC",
}
