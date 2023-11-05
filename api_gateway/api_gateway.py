import requests

MICROSERVICE_ROOT_PATH = "http://localhost:5000"


"""
Find the sum of items prices of a product category
"""
def sum_of_prices(product_category):
    items = requests.get(url = f"{MICROSERVICE_ROOT_PATH}/product_items/{product_category}").json()

    return round(sum([int(i['price']) for i in items]))


"""
The table "product_items" in db1 contains items with the following fields:
    id SERIAL PRIMARY KEY,
    product_category integer NOT NULL,
    name varchar(1000) NOT NULL,
    price numeric NOT NULL

Communication with the database is processed via product microservice

"""
def list_products():
    items = requests.get(url = f"{MICROSERVICE_ROOT_PATH}/product_items").json()

    return items

"""
Retrieve the list of all items by category
"""
def get_by_category(product_category):
    items = requests.get(url = f"{MICROSERVICE_ROOT_PATH}/product_items/{product_category}").json()

    return items

"""
Delete all product category items
"""
def delete_product_category(product_category):

    return requests.delete(url = f"{MICROSERVICE_ROOT_PATH}/product/{product_category}").text

if __name__=="__main__":
    while True:
        print("Enter an option:")
        print("1. Get a list of all products")
        print("Command format: list_products")
        print("2. Get a list of products by category")
        print("Command format: get_by_category category_index")
        print("3. Get sum of all products by category")
        print("Command format: sum category_index")
        print("4. Delete product category")
        print("Command format: delete_product category_index")
        print("5. Exit")
        print("Command format: exit")

        user_input = input("Enter your choice: ")
        choice = user_input.split(' ')[0]


        if choice == "list_products":
            print(list_products())
        if choice == "get_by_category":
            category = user_input.split(' ')[1]
            print(get_by_category(category))
        if choice == "sum":
            category = user_input.split(' ')[1]
            print(sum_of_prices(category))
        if choice == "update_price":
            category = user_input.split(' ')[1]
            coef = int(user_input.split(' ')[2])
            print(f'Updated price for {update_price_product_category(category,coef)} items')
        if choice == "delete_product":
            category = user_input.split(' ')[1]
            print(delete_product_category(category))
        if choice == "exit":
            break
