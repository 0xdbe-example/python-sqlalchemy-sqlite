# Python SQLalchemy with sqlite

Prototype using SQL Expression Language and avoid SQL injection

## Create database

```
sqlite3 db.sqlite

sqlite> CREATE TABLE "product" (
    id INTEGER NOT NULL,
    name VARCHAR,
    price INTEGER,
    PRIMARY KEY(id)
  );
  
sqlite> .quit
```

## Install

```
pipenv install sqlalchemy
```

## Run

```
pipenv run python insert_single_row.py
pipenv run python insert_multi_row.py
```

## Check

```
sqlite3 db.sqlite
sqlite> SELECT * FROM product;
sqlite> .quit
```
