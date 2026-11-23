
from sqlalchemy import create_engine, URL, text

print("Starting MySQL Connection...")

connection_url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="Harikaran@123.com",
    host="localhost",
    port=3306,
    database="india_analytics"
)

engine = create_engine(connection_url)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE()"))
        print("MySQL Connected Successfully!")
        print("Database Name:", result.scalar())

except Exception as e:
    print("Connection Failed:", e)
