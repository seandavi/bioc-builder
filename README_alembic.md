# Alembic

- https://alembic.sqlalchemy.org/en/latest/tutorial.html

```
alembic init alembic
```

Edit ini file to change url.

```
sqlalchemy.url = driver://user:pass@localhost/dbname
```

To do autogeneration, need to edit `env.py` and supply sqlalchemy 
metadata to target_metadata.

