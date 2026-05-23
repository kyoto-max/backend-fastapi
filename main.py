from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from database import engine, Base, get_db
import models
import schemas

app = FastAPI(title="FastAPI + PostgreSQL REST API")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# 1. CREATE
@app.post("/items/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    db_item = models.Item(title=item.title, description=item.description)
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item

# 2. READ ALL
@app.get("/items/", response_model=List[schemas.ItemResponse])
async def read_items(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Item).offset(skip).limit(limit))
    items = result.scalars().all()
    return items

# 3. READ ONE
@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
async def read_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    db_item = result.scalar_one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# 4. UPDATE
@app.put("/items/{item_id}", response_model=schemas.ItemResponse)
async def update_item(item_id: int, updated_item: schemas.ItemCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    db_item = result.scalar_one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db_item.title = updated_item.title
    db_item.description = updated_item.description
    
    await db.commit()
    await db.refresh(db_item)
    return db_item

# 5. DELETE
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.Item).where(models.Item.id == item_id))
    db_item = result.scalar_one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    await db.delete(db_item)
    await db.commit()
    return None