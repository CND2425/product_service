from fastapi import APIRouter, Depends
from app.dependencies import get_db_adapter
from app.core.use_cases import ProductUseCases
from pydantic import BaseModel
from app.core.models import ProductModel, ProductCollection
from app.core.models import UpdateProductModel
from fastapi import FastAPI, Body, HTTPException, status
from bson import ObjectId
from fastapi.responses import Response

#TODO: auslagern in zwei Router

# Router erstellen
router = APIRouter()

@router.post(
    "/products/",
    response_description="Add new product",
    response_model=ProductModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_product(product: ProductModel = Body(...), db_adapter=Depends(get_db_adapter)):
    """
        Insert a new product record.

        A unique `id` will be created and provided in the response.
    """
    product_use_cases = ProductUseCases(db_adapter)
    return await product_use_cases.create_product(product)


@router.get(
    "/products/",
    response_description="List all products",
    response_model=ProductCollection,
    response_model_by_alias=False,
)
async def list_products(db_adapter=Depends(get_db_adapter)):
    """
        List all of the product data in the database.

        The response is unpaginated and limited to 1000 results.
    """
    product_use_cases = ProductUseCases(db_adapter)
    return await product_use_cases.list_products()


@router.get(
    "/products/{id}",
    response_description="Get a single product",
    response_model=ProductModel,
    response_model_by_alias=False,
)
async def show_product(id: str, db_adapter=Depends(get_db_adapter)):
    """
        Get the record for a specific product, looked up by `id`.
    """
    product_use_cases = ProductUseCases(db_adapter)
    if (
        product := await product_use_cases.show_product(id)
    ) is not None:
        return product

    raise HTTPException(status_code=404, detail=f"Product {id} not found")


@router.put(
    "/products/{id}",
    response_description="Update a product",
    response_model=ProductModel,
    response_model_by_alias=False,
)
async def update_product(id: str, product: UpdateProductModel = Body(...), db_adapter=Depends(get_db_adapter)):
    """
    Update individual fields of an existing product record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.
    """
    product_use_cases = ProductUseCases(db_adapter)
    update_result = await product_use_cases.update_product(id, product)
    if update_result is not None:
        return update_result
    else:
        raise HTTPException(status_code=404, detail=f"Product {id} not found")


@router.delete(
    "/products/{id}",
    response_description="Delete a product"
)
async def delete_product(id: str, db_adapter=Depends(get_db_adapter)):
    """
    Remove a single product record from the database.
    """
    product_use_cases = ProductUseCases(db_adapter)
    delete_result = await product_use_cases.delete_product(id)
    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Product {id} not found")

@router.get("/")
async def root():
    """
    Test-Endpunkt, um sicherzustellen, dass die API läuft.
    """
    return {"message": "Product Service is running"}
