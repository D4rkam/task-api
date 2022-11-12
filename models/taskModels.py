from sqlalchemy import Table, Column, Integer, String, Date
from config.db import engine, meta


# Diseño de la Entity TASK
tasks = Table("tasks", meta,
Column("id", Integer, primary_key=True),
Column("title", String(255), nullable=False),
Column("content", String(255), nullable=False),
Column("type", String(255), nullable=False),
Column("created", Date(), nullable=False))

meta.create_all(engine)



