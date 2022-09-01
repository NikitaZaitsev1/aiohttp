import json
from datetime import datetime, date

from aiohttp import web
from typing import Union, Dict, Any, List
from tortoise.queryset import QuerySet, QuerySetSingle


class ModelSerialize(json.JSONEncoder):
    def default(self, value: Any) -> Any:
        if isinstance(value, datetime):
            return value.strftime("%c")
        if isinstance(value, date):
            return datetime.strftime(value, "%a %b %d %Y")
        return str(value)


class SerializeView(web.View):
    _serializer = ModelSerialize()

    def serialize(self, data: Union[Dict, List, QuerySet, QuerySetSingle]) -> str:
        if isinstance(data, QuerySet):
            data = [dict(val) for val in data]
        if not isinstance(data, Dict) or not isinstance(data, List):
            data = dict(data)
            return self._serializer.encode(data)

    def response(self, data: Union[Dict, List, QuerySet, QuerySetSingle], status: web.HTTPException) -> object:
        return web.Response(text=self.serialize(data), status=status.status_code)
