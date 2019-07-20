"""
    User Interface
"""
from filldb import FILLDB


class Menu:
    """
        User interface that contains the menu to acces to diffents fonctions
    """
    def main_menu(self):
        """
            main user menu to access to substitute_menu and substitute_fav or quit the program
        """
        while True:
            user_input = input("""
        1- Selectionner un produit à substituer
        2- Retrouver mes produits substitués
        3- Quitter
            """)
            if user_input == "1":
                Menu.substitute_menu(self)
            if user_input == "2":
                Menu.substitute_fav(self)
            if user_input == "3":
                break

    def substitute_menu(self):
        """
            allow the user to select a product and choose a substitute if there is another healthy
        """
        product_list = []
        cat_list = FILLDB.cat_list
        select_cat = "SELECT name FROM product WHERE category_id ='{}'"
        select_product_name = "SELECT name,nutrigrade,category_id FROM product " \
                              "WHERE name='{}' AND category_id='{}'"
        select_sub_product = "SELECT name,nutrigrade,category_id,url,store, id FROM product " \
                             "WHERE nutrigrade <{} AND category_id='{}'"
        print("Sélectionnez une catégorie :")
        for index, cat in enumerate(cat_list, 1):
            print(str(index) + "- " + str(cat))
        user_input_cat = input("Choix :")
        print("Catégorie :" + cat_list[int(user_input_cat) - 1])
        FILLDB.mycursor.execute(select_cat.format(int(user_input_cat)))
        for index_product, product in enumerate(FILLDB.mycursor, 1):
            print(str(index_product) + "-" + str(product["name"]))
            product_list.append(product["name"])
        user_input_product = input("Selectionnez un produit")
        selected_product = product_list[int(user_input_product) - 1]
        FILLDB.mycursor.execute(select_product_name.format(selected_product, user_input_cat))
        myresult = FILLDB.mycursor.fetchall()
        for val in myresult:
            selected_nutrigrade = val['nutrigrade']
            selected_category = val['category_id']
            continue
        FILLDB.mycursor.execute(select_sub_product.format(selected_nutrigrade, selected_category))
        final_result = FILLDB.mycursor.fetchall()
        sub_list = []
        for result in final_result:
            sub_list.append(tuple((result['name'], result['nutrigrade'], result['url'],
                                   result['store'], result['id'])))
        sorted_result = sorted(sub_list, key=lambda result: result[1])
        try:
            print("{} peut être substitué par {} . \n Nutrigrade:{} \n url : {} \nMagasin : {}"
                  .format(selected_product, sorted_result[0][0], sorted_result[0][1],
                          sorted_result[0][2], sorted_result[0][3]))
        except:
            print("Ce produit est déjà le plus sain")
        user_input_fav = input("""Voulez-vous sauvegarder cette recherche?
        1 : Oui
        2 : Non
        """)
        if user_input_fav == "1":
            print("Produit enregistré dans les favoris")
            try:
                FILLDB.mycursor.execute("INSERT INTO favorite (product_id) VALUES ('{}')"
                                        .format(sorted_result[0][4]))
                FILLDB.connection.commit()
            except:
                FILLDB.mycursor.execute("SELECT id FROM product WHERE name ='{}'"
                                        .format(selected_product))
                selected_id = FILLDB.mycursor.fetchall()
                for ids in selected_id:
                    selected_id = ids['id']
                FILLDB.mycursor.execute("INSERT INTO favorite (product_id) VALUES ({})"
                                        .format(selected_id))
                FILLDB.connection.commit()

    def substitute_fav(self):
        """
            print healthy products found and recorded in substitute_menu
        """
        FILLDB.mycursor.execute("SELECT product_id FROM favorite")
        fav_list = []
        try:
            print("Historique de recherche : ")
            for fav in FILLDB.mycursor:
                fav_list.append(fav["product_id"])
            for prod_fav in fav_list:
                FILLDB.mycursor.execute("SELECT name FROM product WHERE id='{}'"
                                        .format(prod_fav))
                for index_fav, prod_fav_name in enumerate(FILLDB.mycursor, 1):
                    print(str(index_fav) + " - " + str(prod_fav_name['name']))
        except:
            print("Il n'y a pas encore de favoris")


MENU = Menu()
MENU.main_menu()
