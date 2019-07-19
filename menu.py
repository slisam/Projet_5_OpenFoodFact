from filldb import *


class Menu :
    '''User interface to interact with the program'''
    def main_menu(self):
        '''Main user menu'''
        while True :
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
            else:
                print("Veuillez rentrer un chiffre compris entre 1 et 2" )


    def substitute_menu(self):
        '''First menu : Substitution '''
        try :
        product_list = []
        cat_list = FillDb.cat_list
        select_cat = "SELECT name FROM product WHERE category_id ='{}'"
        select_product_name = "SELECT name,nutrigrade,category_id FROM product WHERE name='{}' AND category_id='{}'"
        select_sub_product = "SELECT name,nutrigrade,category_id,url,store, id FROM product WHERE nutrigrade <{} AND category_id='{}'"
        print("Sélectionnez une catégorie :")
        for index, cat in enumerate(cat_list, 1):
            print(str(index) + "- " + str(cat))
        user_input_cat = input("Choix :")
        print("Catégorie :" + cat_list[int(user_input_cat) - 1])
        FillDb.mycursor.execute(select_cat.format(int(user_input_cat)))
        for index_product, product in enumerate(FillDb.mycursor, 1):
            print(str(index_product) + "-" + str(product["name"]))
            product_list.append(product["name"])
        user_input_product = input("Selectionnez un produit")
        selected_product = product_list[int(user_input_product) - 1]
        print(selected_product)
        FillDb.mycursor.execute(select_product_name.format(selected_product,user_input_cat))
        myresult = FillDb.mycursor.fetchall()
        for x in myresult:
            selected_nutrigrade = x['nutrigrade']
            selected_category = x['category_id']
            continue
        FillDb.mycursor.execute(select_sub_product.format(selected_nutrigrade, selected_category))
        final_result = FillDb.mycursor.fetchall()
        sub_list = []
        for y in final_result:
            sub_list.append(tuple((y['name'], y['nutrigrade'], y['url'], y['store'], y['id'])))
        sorted_result = sorted(sub_list, key=lambda y: y[1])
        try :
            print("{} peut être substitué par {} . \n Nutrigrade:{} \n url : {} \nMagasin : {}".format(
                selected_product, sorted_result[0][0], sorted_result[0][1],
                sorted_result[0][2], sorted_result[0][3]))
        except:
            print("Ce produit est déjà le plus sain")
        user_input_fav = input("""Voulez-vous sauvegarder cette recherche?
        1 : Oui
        2 : Non
        """)
        if user_input_fav == "1" :
            print(sorted_result)
            try:
            # FillDb.mycursor.execute("Select id from product where name='{}'".format(sorted_result[0][0]))
            # sub_product = FillDb.mycursor.fetchall()
                print(sorted_result[0][4])
                FillDb.mycursor.execute("INSERT INTO favorite (product_id) VALUES ('{}')".format(sorted_result[0][4]))
                FillDb.connection.commit()
            except:
                FillDb.mycursor.execute("SELECT id FROM product WHERE name ='{}'".format(selected_product))
                selected_id = FillDb.mycursor.fetchall()
                for id in selected_id :
                    selected_id = id['id']
                FillDb.mycursor.execute("INSERT INTO favorite (product_id) VALUES ({})".format(selected_id))
                FillDb.connection.commit()
        except:
             print("Veuillez rentrer un chiffre compris entre 1 et " + str(len(cat_list)))
             pass

    def substitute_fav(self):
        '''second menu : favorite menu '''
        FillDb.mycursor.execute("SELECT product_id FROM favorite")
        fav_list =[]
        try :
            print("Historique de recherche : ")
            for fav in FillDb.mycursor :
                # fav_list.append(fav["product_id"])
                # FillDb.mycursor.execute("SELECT product_id FROM favorite".format(fav["product_id"]))
                # product_name_fav = FillDb.mycursor.fetchall()
                fav_list.append(fav["product_id"])
            for prod_fav in fav_list:
                FillDb.mycursor.execute("SELECT name FROM product WHERE id='{}'".format(prod_fav))
                for index_fav, prod_fav_name in enumerate(FillDb.mycursor, 1):
                    print(str(index_fav) + " - " + str(prod_fav_name['name']))
        except:
            print("Il n'y a pas encore de favoris")


menu = Menu()
menu.main_menu()

# except:
#     print("Veuillez rentrer un numéro compris entre 1 et " + str(len(cat_list)))