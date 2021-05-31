from sqlalchemy import MetaData, insert, select, create_engine

# Table field name
field_name = "name"
field_price = "price"

connection_string = 'sqlite:///db.sqlite'
engine = create_engine(connection_string, echo=True)

with engine.connect() as connection:
  meta = MetaData()
  meta.reflect(bind=connection)
  
  product_table = meta.tables['product']
  stmt = insert(product_table)
  
  values = [
      {field_name: 'hazelnut', field_price: 5},
      {field_name: 'banana', field_price: 8}
  ]

  print(stmt)  
  connection.execute(stmt, values)
