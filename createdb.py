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
                    CREATE TABLE pizza (
                    pizza_id INT (11) NOT NULL,
                    nom VARCHAR (255) NOT NULL,
                    taille VARCHAR (255) NOT NULL,
                    PRIMARY KEY (pizza_id)
                    );
                    
                    CREATE TABLE ingredient (
                    ingredient_id VARCHAR (255) NOT NULL,
                    pizza_id INT (11) NOT NULL,
                    nom VARCHAR (255) NOT NULL,
                    PRIMARY KEY (ingredient_id)
                    );
    
    
                    CREATE TABLE adresse (
                    adresse_id INT (11) NOT NULL,
                    rue VARCHAR (255) NOT NULL,
                    adresse VARCHAR (255) NOT NULL,
                    ville VARCHAR (255) NOT NULL,
                    code_postal INT (11) NOT NULL,
                    commentaire VARCHAR (255) NOT NULL,
                    PRIMARY KEY (adresse_id)
                    );
    
    
                    CREATE TABLE pizzeria (
                    pizzeria_id INT (11) NOT NULL,
                    name VARCHAR (255) NOT NULL,
                    adresse_id INT (11) NOT NULL,
                    PRIMARY KEY (pizzeria_id)
                    );
    
    
                    CREATE TABLE stock (
                    pizzeria_id INT (11) NOT NULL,
                    dose INT (11) NOT NULL,
                    ingredient_id VARCHAR (255) NOT NULL,
                    PRIMARY KEY (pizzeria_id)
                    );
    
    
                    CREATE TABLE client (
                    client_id INT (11) NOT NULL,
                    civilite VARCHAR (255) NOT NULL,
                    nom VARCHAR (255) NOT NULL,
                    prenom VARCHAR (255) NOT NULL,
                    mot_de_passe VARCHAR (255) NOT NULL,
                    telephone INT (11) NOT NULL,
                    email VARCHAR (255) NOT NULL,
                    adresse_id INT (11) NOT NULL,
                    PRIMARY KEY (client_id)
                    );
    
    
                    CREATE TABLE employe (
                    employe_id INT (11) AUTO_INCREMENT NOT NULL,
                    login VARCHAR (255) NOT NULL,
                    mot_de_passe VARCHAR (255) NOT NULL,
                    fonction VARCHAR (255) NOT NULL,
                    pizzeria_id INT (11) NOT NULL,
                    PRIMARY KEY (employe_id)
                    );
    
    
                    CREATE TABLE commande (
                    commande_id INT (11) NOT NULL,
                    date DATE NOT NULL,
                    horaire TIME NOT NULL,
                    statut VARCHAR (255) NOT NULL,
                    mode_de_payement VARCHAR (255) NOT NULL,
                    client_id INT (11) NOT NULL,
                    pizzeria_id INT (11) NOT NULL,
                    adresse_id INT (11) NOT NULL,
                    PRIMARY KEY (commande_id)
                    );
    
    
                    CREATE TABLE quantite_commande (
                    commande_id INT (11) NOT NULL,
                    pizza_id INT (11) NOT NULL,
                    quantite INT (11) NOT NULL,
                    PRIMARY KEY (commande_id, pizza_id)
                    );
                    """)

    def create_category_table(self):
        """
            Category table creation
        """
        self.cursor.execute("""
                    CREATE TABLE Category (
                    category_id INT (11)(11) AUTO_INCREMENT NOT NULL,
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
                    favorite_id INT (11)(11) AUTO_INCREMENT NOT NULL,
                    product_id INT (11)(16) NOT NULL,
                    PRIMARY KEY (favorite_id)
                    );
                    """)

    def db_setting(self):
        """
            Foreign key setting
        """
        self.cursor.execute("""
                    ALTER TABLE product ADD CONSTRAINT (11) category_product_fk
                    FOREIGN KEY (category_id)
                    REFERENCES category (category_id)
                    ON DELETE NO ACTION
                    ON UPDATE NO ACTION;
                    """)
        self.cursor.execute("""
                    ALTER TABLE favorite ADD CONSTRAINT (11) product_favorite_fk
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
        # self.create_category_table()
        # self.create_favorite_table()
        # self.db_setting()


def main():
    """
        main
    """
    connection = mysql.connector.connect(host='localhost',
                                         database='mydb',
                                         user='root',
                                         password='mdp')
    create = DbCreation(connection)
    create.table_creation()


print("Mise à jour de la base de donnée, veuillez patienter...")
main()
