from supermarket_api.repositories.product_repository import ProductRepository


class Product:
    objects = ProductRepository()
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.category = None
        self.unit_measurement = None
        self.quantity = None
    
    def save(self):
        if self.id is not None:
            self.objects.update(self)    
        else:
            self.objects.insert(self)
    
    def delete(self):
        self.objects.delete(self)

            