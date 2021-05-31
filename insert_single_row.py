from sqlalchemy import MetaData, insert, create_engine

# Table field name
field_name = "name"
field_price = "price"

# Input user data
value_name = "apple " + "red"
value_price = 10

connection_string = 'sqlite:///db.sqlite'
engine = create_engine(connection_string, echo=True)

with engine.connect() as connection:
  meta = MetaData()
  meta.reflect(bind=connection)
  product_table = meta.tables['product']

  # Using insert() function
  stmt_from_function = (
    insert(product_table).
    values(name= value_name, price= value_price)
  )
  print(f"statement generated using insert() function: {stmt_from_function}")
  connection.execute(stmt_from_function)
  
  # Using insert() method from table object
  stmt_from_table = product_table.insert().values(name= value_name, price= value_price)
  print(f"statement generated using insert() method from table object: {stmt_from_table}")
  connection.execute(stmt_from_table)

  # Using insert() function with values dict
  stmt_from_function = (
    insert(product_table).
    values({field_name: value_name, field_price: value_price})
  )
  connection.execute(stmt_from_function)
