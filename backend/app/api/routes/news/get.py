from typing import List
from fastapi import APIRouter, HTTPException
from fastapi import Depends, Body
from starlette.status import HTTP_200_OK

from app.api.dependencies.database import get_db_repository
from app.db.repositories.news.news import NewsDBRepository

# response models
from app.models.news import NewsResponseModel


router = APIRouter()

@router.get("/get/count")
async def get_news_count(
    db_repo: NewsDBRepository = Depends(get_db_repository(NewsDBRepository)),
    ) -> int:

    return await db_repo.get_news_count()


@router.get("/get/news", response_model=NewsResponseModel, name="news:get-news", status_code=HTTP_200_OK)
async def get_news(
    start: int,
    count: int,
    db_repo: NewsDBRepository = Depends(get_db_repository(NewsDBRepository)),
    ) -> NewsResponseModel:

    count = await db_repo.get_news_count()
    news = await db_repo.select_news(start=start,count=count)

    return NewsResponseModel(news=news, count=count)