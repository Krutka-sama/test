from tortoise import fields
from tortoise.models import Model
class User(Model):
    id=fields.IntField(pk=True)
    phone=fields.CharField(max_length=64,unique=True)
    password=fields.CharField(max_length=255)