from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db


@router.get('/', response_model=list[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_by_id(id: int, request: schemas.Blog, db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_by_id(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)

@router.put('/0/{MachineName}',status_code=status.HTTP_202_ACCEPTED)
def update_MachineName(MachineName:str,NewName:str,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_MachineName(MachineName , NewName , db)

@router.get('/0/{MachineName}',status_code=200,response_model=list[schemas.ShowBlog])
def show_byMachineName(MachineName:str,db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show_byMachineName(MachineName,db)