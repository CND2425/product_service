from app.core.models import ProductCollection
from bson import ObjectId
from pymongo import ReturnDocument


class MongoDBAdapter:
    def __init__(self, collection):
        self.collection = collection

    async def create_product(self, product):
        new_product = await self.collection.insert_one(
            product.model_dump(by_alias=True, exclude=["id"])
        )
        created_product = await self.collection.find_one(
            {"_id": new_product.inserted_id}
        )
        return created_product


    async def list_products(self):
        return ProductCollection(products=await self.collection.find().to_list(1000))


    async def show_product(self, id):
        return await self.collection.find_one({"_id": ObjectId(id)})

    #TODO: optimieren und aufteilen
    async def update_product(self, id, product):
        product_data = {
            k: v for k, v in product.model_dump(by_alias=True).items() if v is not None
        }

        if len(product_data) >= 1:
            update_result = await self.collection.find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": product_data},
                return_document=ReturnDocument.AFTER,
            )
            return update_result

        # The update is empty, but we should still return the matching document:
        if (existing_product := await self.collection.find_one({"_id": id})) is not None:
            return existing_product

    async def delete_product(self, id):
        return await self.collection.delete_one({"_id": ObjectId(id)})

