from fastapi import APIRouter
from app.services.generator import generate_news
from app.database.db import cursor, conn

router = APIRouter()

@router.get("/news/random")
def random_news(category: str, sentiment: str):
    headline = generate_news(category, sentiment)

    cursor.execute(
        "INSERT INTO news (headline, category, sentiment) VALUES (?, ?, ?)",
        (headline, category, sentiment)
    )
    conn.commit()

    return {
        "headline": headline,
        "category": category,
        "sentiment": sentiment
    }

@router.get("/news/history")
def history():
    cursor.execute("SELECT headline, category, sentiment FROM news")
    return cursor.fetchall()
