"""
    Fill database
"""
import requests
import mysql.connector
from createdb import *


class FillDb:
    """
        collect data from list and API and fill the database
    """
    def __init__(self):
        self.cat_list = ['boissons', 'produits-laitiers', 'viandes', 'desserts', 'poissons']
        self.nb_pages = 2
        self.connection = mysql.connector.connect(host='localhost', database='mydb',
                                                  user='root', password='Mysql93')
        self.mycursor = self.connection.cursor(buffered=True, dictionary=True)

    def get_category(self):
        """
            take CAT_LIST and fill the category table with all categories
        """
        for i in range(len(self.cat_list)):
            sql = "INSERT INTO category (category_name) VALUES(%s)"
            val = (self.cat_list[i],)
            self.mycursor.execute(sql, val)
            self.connection.commit()

    def get_product(self):
        """
            Connect to the Open Food Facts API to extract data and fill it in the product table
        """
        url_off = "https://fr.openfoodfacts.org/categorie/"
        for cat in self.cat_list:
            category_name = cat
            for page in range(1, self.nb_pages + 1):
                url_cat = url_off + cat + "/" + str(page) + ".json"
                r_prod = requests.get(url_cat)
                json_prod = r_prod.json()
                for i in range(1, 21):
                    try:
                        product_name = json_prod["products"][i]["product_name_fr"]
                        nutrigrade = json_prod["products"][i]["nutrition_grade_fr"]
                        product_url = json_prod["products"][i]['url']
                        product_store = json_prod["products"][i]["stores"]
                        barcode = json_prod["products"][i]["id"]
                        self.mycursor.execute(
                            "SELECT category_id FROM category WHERE category_name ='{}'"
                            .format(category_name))
                        select_cat = self.mycursor.fetchall()
                        for cats in select_cat:
                            category_id = cats['category_id']
                        if len(product_name) != 0:
                            sql = "INSERT INTO product (name,category_id,nutrigrade,url," \
                                  "store,barcode) VALUES (%s,%s,%s,%s,%s,%s)"
                            val = (product_name, category_id, nutrigrade, product_url,
                                   product_store, barcode,)
                            self.mycursor.execute(sql, val)
                            self.connection.commit()
                        else:
                            continue
                    except:
                        continue
                page += 1
        nutrigrade_letter = ['a', 'b', 'c', 'd', 'e']
        for number, letter in enumerate(nutrigrade_letter, 1):
            self.mycursor.execute(
                "UPDATE product SET nutrigrade = REPLACE(nutrigrade, '{}', '{}') WHERE nutrigrade "
                "LIKE '{}'".format(letter, number, letter))
            self.connection.commit()


FILLDB = FillDb()
FILLDB.get_category()
FILLDB.get_product()
