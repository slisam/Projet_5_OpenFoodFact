"""
database creation
"""
import mysql.connector


class DbCreation:
    """
        database creation
    """
    def __init__(self, connection):
        self.database = connection
        self.cursor = self.database.cursor()

    def clean_table(self):
        """
            clean tables if already exist
        """
        self.cursor.execute("DROP TABLE IF EXISTS product, category, favorite, store")

    def create_product_table(self):
        """
            Product table creation
        """
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

    def create_category_table(self):
        """
            Category table creation
        """
        self.cursor.execute("""
                    CREATE TABLE Category (
                    category_id INT(11) AUTO_INCREMENT NOT NULL,
                    category_name VARCHAR(255) NOT NULL,
                    PRIMARY KEY (category_id)
                    );
                    """)

    def create_favorite_table(self):
        """
            Favorite table creation
        """
        self.cursor.execute("""
                    CREATE TABLE favorite (
                    favorite_id INT(11) AUTO_INCREMENT NOT NULL,
                    product_id INT(16) NOT NULL,
                    PRIMARY KEY (favorite_id)
                    );
                    """)

    def db_setting(self):
        """
            Foreign key setting
        """
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
        """
            cleaning and table creation
        """
        self.clean_table()
        self.create_product_table()
        self.create_category_table()
        self.create_favorite_table()
        self.db_setting()


def main():
    """
        main
    """
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='Mysql93')
    create = DbCreation(connection)
    create.table_creation()


print("Mise à jour de la base de donnée, veuillez patienter...")
main()
