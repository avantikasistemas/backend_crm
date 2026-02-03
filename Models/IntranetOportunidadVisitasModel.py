from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from Config.db import BASE


class IntranetOportunidadVisitasModel(BASE):
    __tablename__ = "intranet_oportunidad_visitas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    oportunidad_id = Column(Integer, nullable=False)
    asunto = Column(String(500), nullable=False)
    tipo_id = Column(Integer, nullable=False)
    tipo_nombre = Column(String(200), nullable=False)
    contacto = Column(String(300))
    objetivo = Column(Text)
    fecha_hora = Column(DateTime, nullable=False)
    estado_id = Column(Integer, nullable=False)
    estado_nombre = Column(String(50), nullable=False)
    fecha_cierre_real = Column(DateTime)
    comentarios = Column(String(150))
    resultado_id = Column(Integer)
    activo = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, nullable=False, server_default=func.getdate())
    updated_at = Column(DateTime, nullable=False, server_default=func.getdate())
    
    def __init__(self, data: dict):
        self.oportunidad_id = data.get("oportunidad_id")
        self.asunto = data.get("asunto")
        self.tipo_id = data.get("tipo_id")
        self.tipo_nombre = data.get("tipo_nombre")
        self.contacto = data.get("contacto")
        self.objetivo = data.get("objetivo")
        self.fecha_hora = data.get("fecha_hora")
        self.estado_id = data.get("estado_id")
        self.estado_nombre = data.get("estado_nombre")
        self.fecha_cierre_real = data.get("fecha_cierre_real")
        self.comentarios = data.get("comentarios")
        self.resultado_id = data.get("resultado_id")
        self.activo = data.get("activo", 1)
