from aiohttp import web
from aiohttp_jinja2 import template


@template("home.html")
class HomeView(web.View):
    async def get(self):
        print(self.request.headers)
        # return web.Response(body="Home")
        # return web.json_response({"status":"ok"}, status=200)
        return {"header": "Home Page"}


@template("contact.html")
class ContactView(web.View):
    async def get(self):
        print(self.request.headers)
        return {"header": "Contact"}

@template("about.html")
class AboutView(web.View):
    async def get(self):
        print(self.request.headers)
        return {"header": "About"}
