import inspect
import models
import sqlalchemy
from utils import Base

def get_default_bool(c):
    if c.default:
        return True
    else:
        return False


def get_fk_bool(c):
    if c.foreign_keys:
        return True
    else:
        return False


def sqlalchemy_type_to_python(t: object) -> str:
    if isinstance(t, sqlalchemy.String):
        return "str"
    if isinstance(t, sqlalchemy.Integer):
        return "int"
    if isinstance(t, sqlalchemy.DateTime):
        return "datetime.datetime"
    if isinstance(t, sqlalchemy.Float):
        return "float"
    if isinstance(t, sqlalchemy.Float):
        return "float"

api_tables = [
    j
    for i, j in inspect.getmembers(models)
    if isinstance(j, sqlalchemy.orm.decl_api.DeclarativeMeta) and j != Base
]
 
for table in api_tables:
    columns = []
    for c in table.__table__.columns:

        col = {
            "name": c.name,
            "type": sqlalchemy_type_to_python(c.type),
            "is_pk": c.primary_key,
            "is_nullable": c.nullable,
            "is_fk": get_fk_bool(c),
            "has_default": get_default_bool(c),
        }

        if c.foreign_keys:
            _keys = [fk for fk in c.foreign_keys]
            k = _keys[0]
            foreign_key_target_full_name = k.target_fullname.split(".")
            col["_ftable"] = foreign_key_target_full_name[0]
            col["_fcol"] = foreign_key_target_full_name[1]

        columns.append(col)
    print(columns)