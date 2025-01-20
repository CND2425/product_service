from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from typing import Optional, List
from bson import ObjectId

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.pip install -r requirements.txt
PyObjectId = Annotated[str, BeforeValidator(str)]


class ProductModel(BaseModel):
    """
    Container for a single product record.
    """

    # The primary key for the ProductModel, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    description: str = Field(...)
    price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    stock_status: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Laptop",
                "description": "A high-performance laptop",
                "price": 999.99,
                "stock_quantity": 50,
                "stock_status": "inStock",
            }
        },
    )


class UpdateProductModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None
    stock_status: Optional[str] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "name": "Laptop",
                "description": "An updated laptop description",
                "price": 899.99,
                "stock_quantity": 40,
            }
        },
    )


class ProductCollection(BaseModel):
    """
    A container holding a list of `ProductModel` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    products: List[ProductModel]