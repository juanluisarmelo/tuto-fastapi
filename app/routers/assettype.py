from fastapi import status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/assetTypes",
    tags=['Asset Types']
)


@router.get("/", response_model=List[schemas.AssetTypeResponse])
def get_asset_types(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    asset_types = db.query(models.AssetType).all()

    return asset_types


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.AssetTypeResponse)
def create_asset_type(asset_type: schemas.AssetTypeCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_asset_type = models.AssetType(description=asset_type.description)
    db.add(new_asset_type)
    db.commit()
    db.refresh(new_asset_type)

    return new_asset_type


@router.get("/{id}", response_model=schemas.AssetTypeResponse)
def get_asset_type(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    asset_type = db.query(models.AssetType).filter(
        models.AssetType.id == id).first()

    if not asset_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Asset type with id: {id} was not found")

    return asset_type


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_asset_type(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    asset_type = db.query(models.AssetType).filter(
        models.AssetType.id == id)

    if asset_type.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Asset type with id: {id} was not found")

    asset_type.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.AssetTypeResponse)
def update_asset_type(id: int, updated_asset_type: schemas.AssetTypeCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    asset_type_query = db.query(models.AssetType).filter(
        models.AssetType.id == id)

    asset_type = asset_type_query.first()

    if asset_type == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Asset type with id: {id} was not found")

    asset_type_query.update(
        updated_asset_type.model_dump(), synchronize_session=False)
    db.commit()

    return asset_type_query.first()
