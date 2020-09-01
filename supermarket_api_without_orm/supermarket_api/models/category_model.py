from supermarket_api.repositories.category_repository import CategoryRepository

class Category:
    objects = CategoryRepository()
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
    
    def save(self):
        if self.id is not None:
            self.objects.update(self)
        else:
            self.objects.insert(self)
    
    def delete(self):
        self.objects.delete(self)

