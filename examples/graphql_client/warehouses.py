# Generated by ariadne-codegen
# Source: examples/queries.graphql

from typing import Optional

from .base_model import BaseModel


class Warehouses(BaseModel):
    warehouse: Optional["WarehousesWarehouse"]


class WarehousesWarehouse(BaseModel):
    id: str


Warehouses.model_rebuild()
