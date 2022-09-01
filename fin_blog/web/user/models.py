import asyncio
from hashlib import sha3_256, sha3_512
from random import randrange

from tortoise import models, fields


class User(models.Model):
    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=120, unique=True)
    created = fields.DatetimeField(auto_now_add=True)
    last_login = fields.DatetimeField(auto_now=True)
    password = fields.TextField()
    is_active = fields.BooleanField(default=False)
    birth_day = fields.DateField()
    bio = fields.TextField()
    avatar = fields.TextField()
    friends = fields.ManyToManyField(
        "user.User",
        related_name="followers",
        on_delete=fields.SET_NULL,
    )

    class Meta:
        table = "users"

    async def set_password(self):
        salt = self.username + str(randrange(1000000, 9999999))
        salt = sha3_256(salt.encode("utf-8")).hexdigest()
        tmp = sha3_256(self.password.encode("utf-8")).hexdigest()
        data = "".join([s + t for s, t in zip(salt, tmp)])
        self.password = sha3_512(data.encode("utf-8")).hexdigest() + salt

    async def check_password(self, password):
        salt = self.password[-64:]
        tmp = sha3_256(password.encode("utf-8")).hexdigest()
        data = "".join([s + t for s, t in zip(salt, tmp)])
        hashed_pass = sha3_512(data.encode("utf-8")).hexdigest()
        if hashed_pass == self.password[:-64]:
            return True
        await asyncio.sleep(3)
        return False
