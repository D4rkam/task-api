from sqlalchemy import Table, Column, Integer, String, Boolean
from config.db import engine, meta
# Diseño de la Entity TASK
tasks = Table("tasks", meta,
Column("id", Integer, primary_key=True),
Column("title", String(255), nullable=False),
Column("content", String(255), nullable=False),
Column("done", Boolean, default=False))

meta.create_all(engine)