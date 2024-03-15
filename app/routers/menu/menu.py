""" describe """
from typing import Annotated
from fastapi import APIRouter, Header, Request
from fastapi.responses import HTMLResponse


from app.utils import Template, log


router = APIRouter()
template = Template()

@router.get("/gnb", )
async def get_gnb(request: Request) -> HTMLResponse:
    """endpoint"""  
    return Template().TemplateResponse(
            "menu/menu_gnb.html",
        context={'request': request, 'datetime': ""}
    )

@router.get("/sidebar", response_class=HTMLResponse)
async def get_sidebar(request: Request) -> HTMLResponse:
    """sidebar"""
    return Template().TemplateResponse(
        "menu/menu_sidebar.html",
        context={'request': request, "datetime": "value"}
    )
    
@router.get("/breadcrumbs", response_class=HTMLResponse)
async def get_breadcombs(request: Request, hx_current_url: Annotated[str | None, Header()] = None) -> HTMLResponse:
    """breadcombs"""
    # get path string from request
    log.info(f"current_url: {hx_current_url}")
    return Template().TemplateResponse(
        "menu/menu_breadcombs.html",
        context={'request': request, "datetime": "value"}
    )