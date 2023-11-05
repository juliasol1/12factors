from faker import Faker

import faker_commerce

fake = Faker()
fake.add_provider(faker_commerce.Provider)
no_items=3000

with open('db_init_out.sql',"a+") as f:
    for i in range(no_items):
        product_name = fake.ecommerce_name()
        line = ''.join(product_name)
        f.write(line)
