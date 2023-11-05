import psycopg2
from flask import Flask, jsonify, request


HOST = "db"
PORT = 5432
DATABASE = "postgres"
USERNAME = "postgres"
PASSWORD = "postgres"
conn = None


app = Flask(__name__)

"""
The table "products" in db contains items with the following fields
    id SERIAL PRIMARY KEY,
    product_id integer NOT NULL,
    name varchar(1000) NOT NULL,
    price numeric NOT NULL
Return: List of all product items
"""
@app.route('/product_items')
def get_product_items():
    try:
        conn = psycopg2.connect(
            host=HOST,
            port=PORT,
            database=DATABASE,
            user=USERNAME,
            password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"""SELECT * FROM product_items """)
        items = cur.fetchall()
        # convert arrays into objects
        items = [{"id":i[0], "product_id": i[1], "name": i[2], "price": i[3] } for i in items]

        return jsonify(items), 200

    except Exception as e:
        return jsonify(e.messages), 400

    finally:
        cur.close()
        conn.close()
"""
This method list its items filtered by product_id
Request parameters:
    product_id
Return: List of product items
"""
@app.route('/product_items/<product_id>')
def get_filtered_product_items(product_id):
    try:
        conn = psycopg2.connect(
            host=HOST,
            port=PORT,
            database=DATABASE,
            user=USERNAME,
            password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"""SELECT * FROM product_items WHERE product_id={product_id}""")
        items = cur.fetchall()
        # convert arrays into objects
        items = [{"id":i[0], "product_id": i[1], "name": i[2], "price": i[3] } for i in items]

        return jsonify(items), 200

    except Exception as e:
        return jsonify(e.messages), 400

    finally:
        cur.close()
        conn.close()

"""
Update price of item from "product_items" table.
Request paramaters:
    - id
    - price

"""
@app.route('/update_product_price', methods=['PUT'])
def update_product_price():
    params = request.json
    try:
        conn = psycopg2.connect(
            host=HOST,
            port=PORT,
            database=DATABASE,
            user=USERNAME,
            password=PASSWORD)

        cur = conn.cursor()
        cur.execute(f"""UPDATE product_items SET price = {params['price']}
                    WHERE product_items.id = {params['id']})""")
        conn.commit()

        return "The product price was successefully updated", 200

    except Exception as e:
        return jsonify(e.messages), 400
    finally:
        cur.close()
        conn.close()



"""
Delete items for a product from "product_items" table.
Request paramaters:
    - product_id
"""
@app.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        conn = psycopg2.connect(
            host=HOST,
            port=PORT,
            database=DATABASE,
            user=USERNAME,
            password=PASSWORD)

        cur = conn.cursor()

        cur.execute(f"""DELETE FROM product_items WHERE product_id = {product_id}""")
        conn.commit()

        return f"Product {product_id} was successefully deleted", 200

    except Exception as e:
        return jsonify(e.messages), 400
    finally:
        cur.close()
        conn.close()


app.run(host="0.0.0.0", port=5000)
