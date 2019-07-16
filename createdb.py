import mysql.connector

class DbCreation:
    def __init__(self, connection):
        self.db = connection
        self.cursor = self.db.cursor()

    def clean_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS product, category, favorite, store")
        print("Database cleaned")

    def create_product_table(self):
        self.cursor.execute("""
                    CREATE TABLE product (
                    id INT(11) AUTO_INCREMENT NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    category_id INT(11),
                    nutrigrade VARCHAR(45) NOT NULL,
                    url VARCHAR(250),
                    store VARCHAR(255) NOT NULL,
                    favorite_id INT(11),
                    barcode BIGINT,
                    PRIMARY KEY (id)
                    );
                    """)
        print("Product table created")

    def create_category_table(self):
        self.cursor.execute("""
            		CREATE TABLE Category (
                    category_id INT(11) AUTO_INCREMENT NOT NULL,
                    category_name VARCHAR(255) NOT NULL,
                    PRIMARY KEY (category_id)
                    );
                    """)
        print("Category table created")

    def create_favorite_table(self):
        self.cursor.execute("""
                    CREATE TABLE favorite (
                    favorite_id INT(11) AUTO_INCREMENT NOT NULL,
                    product_id INT(16) NOT NULL,
                    PRIMARY KEY (favorite_id)
                    );
                    """)
        print("Favorite table created")

    def db_setting(self):
        self.cursor.execute("""
                    ALTER TABLE product ADD CONSTRAINT category_product_fk
                    FOREIGN KEY (category_id)
                    REFERENCES category (category_id)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION;
                    """)
        self.cursor.execute("""
                    ALTER TABLE favorite ADD CONSTRAINT product_favorite_fk
                    FOREIGN KEY (product_id)
                    REFERENCES product (id)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION;
                    """)

    def table_creation(self):
        self.clean_table()
        self.create_product_table()
        self.create_category_table()
        self.create_favorite_table()
        self.db_setting()


def main():
    connection = mysql.connector.connect(host='localhost',
                                   database='mydb',
                                   user='root',
                                   password='Mysql93')
    create = DbCreation(connection)
    create.table_creation()
    print(connection)


main()