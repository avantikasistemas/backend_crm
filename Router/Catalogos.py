from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from Class.Catalogos import Catalogos
from Utils.decorator import http_decorator
from Config.db import get_db

catalogos_router = APIRouter()

# ===================================================
# ENDPOINTS DE CATÁLOGOS
# ===================================================

@catalogos_router.post("/tipo-registros", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_tipo_registros(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los tipos de registro activos"""
    response = Catalogos(db).get_tipo_registros()
    return response

@catalogos_router.post("/origenes", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_origenes(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los orígenes activos"""
    response = Catalogos(db).get_origenes()
    return response

@catalogos_router.post("/medios-identificacion", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_medios_identificacion(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los medios de identificación activos"""
    response = Catalogos(db).get_medios_identificacion()
    return response

@catalogos_router.post("/tiempos-ejecucion", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_tiempos_ejecucion(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los tiempos de ejecución activos"""
    response = Catalogos(db).get_tiempos_ejecucion()
    return response

@catalogos_router.post("/tipos-proyecto", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_tipos_proyecto(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los tipos de proyecto activos"""
    response = Catalogos(db).get_tipos_proyecto()
    return response

@catalogos_router.post("/tipos-contratacion", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_tipos_contratacion(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los tipos de contratación activos"""
    response = Catalogos(db).get_tipos_contratacion()
    return response

@catalogos_router.post("/tipos-adjudicacion", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_tipos_adjudicacion(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los tipos de adjudicación activos"""
    response = Catalogos(db).get_tipos_adjudicacion()
    return response

@catalogos_router.post("/motivos-no-adjudicacion", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_motivos_no_adjudicacion(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los motivos de no adjudicación activos"""
    response = Catalogos(db).get_motivos_no_adjudicacion()
    return response

@catalogos_router.post("/todos", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_todos_catalogos(request: Request, db: Session = Depends(get_db)):
    """Obtiene todos los catálogos en una sola petición"""
    response = Catalogos(db).get_todos_catalogos()
    return response

@catalogos_router.post("/estados", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_estados(request: Request, db: Session = Depends(get_db)):
    """Obtiene el catálogo de estados de oportunidades"""
    response = Catalogos(db).get_estados()
    return response

@catalogos_router.post("/resultados-visitas", tags=["CATALOGOS"], response_model=dict)
@http_decorator
def get_resultados_visitas(request: Request, db: Session = Depends(get_db)):
    """Obtiene el catálogo de resultados de visitas"""
    response = Catalogos(db).get_resultados_visitas()
    return response
