from django.db import connection

class CategoryRepository():
    def __init__(self):
        pass

    @staticmethod
    def all():
        cursor = connection.cursor()
        query = """
                SELECT id,name, description
                FROM categories;
                """
        cursor.execute(query)
        objects = []

        for row in cursor.fetchall():
            from supermarket_api.models.category_model import Category
            category = Category()
            category.id = row[0]
            category.name = row[1]
            category.description = row[2]
            objects.append(category)
        
        return objects

    @staticmethod
    def get(id):
        cursor = connection.cursor()
        query = """
                SELECT id, name, description
                FROM categories
                WHERE id = {0};
                """.format(id)

        cursor.execute(query)
        object = None

        for row in cursor.fetchall():
            from supermarket_api.models.category_model import Category
            category = Category()
            category.id = row[0]
            category.name = row[1]
            category.description = row[2]
            object = category
        
        return object

    @staticmethod
    def insert(category):
        #Guardando el elemento
        cursor = connection.cursor()
        query = """
                INSERT INTO categories(name, description)
                VALUES('{0}', '{1}');
                """.format(category.name, category.description)
        cursor.execute(query)

        #Recuperando el id
        query = """
                SELECT LAST_INSERT_ID();
                """
        cursor.execute(query)
        category.id = cursor.fetchall()[0][0]

    @staticmethod
    def update(category):
        cursor = connection.cursor()
        query = """
                UPDATE categories
                SET name = '{1}', description='{2}'
                WHERE id = '{0}';
                """.format(category.id, category.name, category.description)
        
        cursor.execute(query)
    
    @staticmethod
    def delete(category):
        cursor = connection.cursor()
        query = """
                DELETE FROM categories
                WHERE id = '{0}';
                """.format(category.id)
        
        cursor.execute(query)
        


