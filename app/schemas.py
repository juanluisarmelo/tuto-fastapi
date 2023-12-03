from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class AssetTypeCreate(BaseModel):
    description: str


class AssetTypeResponse(BaseModel):
    id: int
    description: str
    created_at: datetime

    class Config:
        orm_mode = True


class AssetBase(BaseModel):
    model: str
    serial_number: str
    asset_tag: Optional[str] = None
    name: Optional[str] = None
    note: Optional[str] = None


class AssetCreate(AssetBase):
    asset_type_id: int


class AssetResponse(AssetBase):
    id: int
    created_at: datetime
    asset_type_id: int
    asset_type: AssetTypeResponse

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
