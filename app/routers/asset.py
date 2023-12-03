from fastapi import status, Response, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/assets",
    tags=['Asset']
)


@router.get("/", response_model=List[schemas.AssetResponse])
def get_assets(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
               limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    assets = db.query(models.Asset).filter(
        models.Asset.model.contains(search)).limit(limit).offset(skip).all()

    return assets


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.AssetResponse)
def create_asset(asset: schemas.AssetCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_asset = models.Asset(**asset.model_dump())
    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)

    return new_asset


@router.get("/{id}", response_model=schemas.AssetResponse)
def get_asset(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    asset = db.query(models.Asset).filter(
        models.Asset.id == id).first()

    if not asset:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Asset with id: {id} was not found")

    return asset


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_asset(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    asset = db.query(models.Asset).filter(
        models.Asset.id == id)

    if asset.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Asset with id: {id} was not found")

    asset.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.AssetResponse)
def update_asset(id: int, updated_asset: schemas.AssetCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    asset_query = db.query(models.Asset).filter(
        models.Asset.id == id)

    asset = asset_query.first()

    if asset == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Asset with id: {id} was not found")

    asset_query.update(
        updated_asset.model_dump(), synchronize_session=False)
    db.commit()

    return asset_query.first()
