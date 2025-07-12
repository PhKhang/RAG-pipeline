from fastapi import APIRouter
from ..services.llm import get_simple_response

router = APIRouter()


@router.get("/chat/stream")
def stream_llm_response():
    return {"type": "reasoning", "data": "Hello world"}


@router.get("/chat/simple")
def simple_llm_response():
    answer = get_simple_response("Who are you")
    return {
        "content": f"{answer}",
        "reasoning": "The user asked a simple question about myself",
    }
