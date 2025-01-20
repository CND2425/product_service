class ProductUseCases:
    def __init__(self, db_adapter):
        self.db_adapter = db_adapter


    async def create_product(self, product):
        return await self.db_adapter.create_product(product)


    async def list_products(self):
        return await self.db_adapter.list_products()


    async def show_product(self, id):
        return await self.db_adapter.show_product(id)


    async def update_product(self, id, product):
        return await self.db_adapter.update_product(id, product)

    async def delete_product(self, id):
        return await self.db_adapter.delete_product(id)