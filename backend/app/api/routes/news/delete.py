from fastapi import APIRouter, HTTPException
from fastapi import Depends, Body
from starlette.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from app.api.dependencies.database import get_db_repository
from app.db.repositories.news.news import NewsDBRepository

from app.api.dependencies.auth import is_superuser, is_verified

router = APIRouter()

@router.delete("/delete", response_model=None, name="news:delete", status_code=HTTP_200_OK)
async def create_news(
    id: int,
    db_repo: NewsDBRepository = Depends(get_db_repository(NewsDBRepository)),
    is_superuser = Depends(is_superuser),
    is_verified = Depends(is_verified),
    ) -> None:

    if not is_superuser:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not superuser!")
    if not is_verified:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Email not verified!")

    await db_repo.delete_news(id=id)
