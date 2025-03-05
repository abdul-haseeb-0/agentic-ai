### Install:
- poetry add alembic
- poetry add psycopg2-binary
---

### New setup
- run in cmd -> poetry run alembic init <FOLDER_NAME> # like alembic
- Replace db URI with sqlalchemy.url in alembic.ini.
- Create sqlalcemy base model
- Replace None in target_metadata in env with base model like target_metadata = base.metadata

### With Every changes run these commands:
- poetry run alembic revision --autogenerate -m "commit"
 It will create file in versions.
- poetry run alembic upgrade head
 It will add changes to db


Alembic is only used to create table, to add data we have to use 