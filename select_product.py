from sqlalchemy import MetaData, select, create_engine

# Table field name
field_name = "name"
field_price = "price"

# Input user data
value_name = "banana"
value_price = 10

connection_string = 'sqlite:///db.sqlite'
engine = create_engine(connection_string, echo=True)

with engine.connect() as connection:
  meta = MetaData()
  meta.reflect(bind=connection)
  product_table = meta.tables['product']

  stmt = (
    select(product_table)
    .where(product_table.columns[field_name] == value_name)
  )
  result = connection.execute(stmt)
  
  for row in result:
    print(row)
