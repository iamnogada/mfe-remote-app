""" User endpoint router """
from datetime import datetime


from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse,JSONResponse


from app.utils import Template, log


router = APIRouter()

@router.get("", response_class=HTMLResponse)
async def get_user(request: Request) -> HTMLResponse:
    """user"""
    return Template().TemplateResponse(
        "user/user.html",
        context={'request': request, "datetime": "value"}
    )
