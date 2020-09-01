from django.db import connection


class ProductRepository():
    def __init__(self):
        pass

    @staticmethod
    def all():
        cursor = connection.cursor()
        query = """
                SELECT  
                    t1.id as id, 
                    t1.name as name, 
                    t1.description as description, 
                    t1.unit_measurement as unit_measurement, 
                    t1.quantity as quantity, 
                    t2.id as categoryId,
                    t2.name as categoryName,
                    t2.description as categoryDescription
                FROM products t1
                INNER JOIN categories t2
                    ON t1.categoryId = t2.id;
                """
        cursor.execute(query)
        objects = []

        for row in cursor.fetchall():
            from supermarket_api.models.category_model import Category
            category = Category()
            category.id = row[5]
            category.name = row[6]
            category.description = row[7]
            
            from supermarket_api.models.product_model import Product
            product = Product()
            product.id = row[0]
            product.name = row[1]
            product.description = row[2]
            product.unit_measurement = row[3]
            product.quantity = row[4]
            product.category = category

            objects.append(product)
        
        return objects

    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = """
                SELECT  
                    t1.id as id, 
                    t1.name as name, 
                    t1.description as description, 
                    t1.unit_measurement as unit_measurement, 
                    t1.quantity as quantity, 
                    t2.id as categoryId,
                    t2.name as categoryName,
                    t2.description as categoryDescription
                FROM products t1
                INNER JOIN categories t2
                    ON t1.categoryId = t2.id
                WHERE t1.id = {0};
                """.format(id)
        cursor.execute(query)
        object = None

        for row in cursor.fetchall():
            from supermarket_api.models.category_model import Category
            category = Category()
            category.id = row[5]
            category.name = row[6]
            category.description = row[7]
            
            from supermarket_api.models.product_model import Product
            product = Product()
            product.id = row[0]
            product.name = row[1]
            product.description = row[2]
            product.unit_measurement = row[3]
            product.quantity = row[4]
            product.category = category

            object = product
        
        return object

    @staticmethod
    def insert(product):
        cursor = connection.cursor()
        query = """
                INSERT INTO products(name, description, unit_measurement, quantity, categoryId)
                VALUES("{0}", "{1}", "{2}", {3}, {4});
                """.format(
                    product.name,
                    product.description,
                    product.unit_measurement,
                    product.quantity,
                    product.category.id
                )
        cursor.execute(query)

        #Recuperando el id
        query = """
                SELECT LAST_INSERT_ID();
                """
        cursor.execute(query)
        product.id = cursor.fetchall()[0][0]

    @staticmethod 
    def update(product):
        cursor = connection.cursor()
        query = """
                UPDATE products
                SET
                    name = "{1}",
                    description = "{2}",
                    unit_measurement = "{3}",
                    quantity = {4},
                    categoryId = {5}
                WHERE id = {0};
                """.format(
                    product.id,
                    product.name,
                    product.description,
                    product.unit_measurement,
                    product.quantity,
                    product.category.id
                )

        cursor.execute(query)

    @staticmethod
    def delete(product):
        cursor = connection.cursor()
        query = """
                DELETE FROM products
                WHERE id = '{0}';
                """.format(product.id)
        
        cursor.execute(query)