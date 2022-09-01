from datetime import datetime
from aiohttp import web
from fin_blog.web.root.views import SerializeView
from fin_blog.web.user.models import User


#
# def serialize(data):
#     return json.dumps(data, default=str)


class UserView(SerializeView):
    async def get(self):
        data = await User.all().values()
        return self.response(data, status=web.HTTPOk)
        # return web.json_response(data, dumps=serialize)

    async def post(self):
        data = await self.request.json()
        data["birth_day"] = datetime.strptime(data["birth_day"], "%d-%m-%Y")
        new_user = await User.create(**data)
        return web.json_response(new_user, dumps=serialize)

    async def put(self):
        ...

    async def delete(self):
        ...
