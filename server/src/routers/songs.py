from typing import Annotated

from dependencies import get_current_active_user
from fastapi import APIRouter, Depends
from schemas import Prompt, User

router = APIRouter(prefix="/prompt", tags=["songs"])


@router.post("/new/")
async def make_a_prompt(
    current_user: Annotated[User, Depends(get_current_active_user)],
    prompt: Prompt,
) -> dict[str, str]:
    return {"result": prompt.prompt}