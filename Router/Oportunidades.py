from fastapi import APIRouter, Request, Depends, Query
from sqlalchemy.orm import Session
from Class.Oportunidades import Oportunidades
from Utils.decorator import http_decorator
from Config.db import get_db

oportunidades_router = APIRouter()

# ===================================================
# ENDPOINTS DE OPORTUNIDADES
# ===================================================

@oportunidades_router.post('/terceros', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def buscar_terceros(request: Request, db: Session = Depends(get_db)):
    """Busca terceros por NIT o nombre para el campo empresa"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).buscar_terceros(data)
    return response

@oportunidades_router.post('/guardar', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def guardar_oportunidad(request: Request, db: Session = Depends(get_db)):
    """Guarda una nueva oportunidad"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).guardar_oportunidad(data)
    return response

@oportunidades_router.post('/listar', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def listar_oportunidades(request: Request, db: Session = Depends(get_db)):
    """Lista oportunidades con paginación y filtros"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).listar_oportunidades(data)
    return response

@oportunidades_router.post('/obtener', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def obtener_oportunidad(request: Request, db: Session = Depends(get_db)):
    """Obtiene una oportunidad por ID"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).obtener_oportunidad(data)
    return response

@oportunidades_router.post('/contactos', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def buscar_contactos(request: Request, db: Session = Depends(get_db)):
    """Busca contactos por NIT de empresa"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).buscar_contactos(data)
    return response

@oportunidades_router.post('/visitas/listar', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def listar_visitas(request: Request, db: Session = Depends(get_db)):
    """Lista visitas de una oportunidad"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).listar_visitas(data)
    return response

@oportunidades_router.post('/visitas/guardar', tags=["OPORTUNIDADES"], response_model=dict)
@http_decorator
def guardar_visita(request: Request, db: Session = Depends(get_db)):
    """Guarda o actualiza una visita"""
    data = getattr(request.state, "json_data", {})
    response = Oportunidades(db).guardar_visita(data)
    return response
