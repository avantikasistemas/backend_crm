from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from Config.db import BASE


class IntranetVisitasClientesModel(BASE):
    __tablename__ = "intranet_visitas_clientes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_nit = Column(String(50), nullable=False)
    cliente_nombre = Column(String(300), nullable=False)
    asunto = Column(String(500), nullable=False)
    tipo_id = Column(Integer, nullable=False)
    tipo_nombre = Column(String(200), nullable=False)
    contacto = Column(String(300))
    objetivo = Column(Text)
    fecha_hora = Column(DateTime, nullable=False)
    estado_id = Column(Integer, nullable=False)
    estado_nombre = Column(String(50), nullable=False)
    fecha_cierre_real = Column(DateTime)
    activo = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, nullable=False, server_default=func.getdate())
    updated_at = Column(DateTime, nullable=False, server_default=func.getdate())
    
    def __init__(self, data: dict):
        self.cliente_nit = data.get("cliente_nit")
        self.cliente_nombre = data.get("cliente_nombre")
        self.asunto = data.get("asunto")
        self.tipo_id = data.get("tipo_id")
        self.tipo_nombre = data.get("tipo_nombre")
        self.contacto = data.get("contacto")
        self.objetivo = data.get("objetivo")
        self.fecha_hora = data.get("fecha_hora")
        self.estado_id = data.get("estado_id")
        self.estado_nombre = data.get("estado_nombre")
        self.fecha_cierre_real = data.get("fecha_cierre_real")
        self.activo = data.get("activo", 1)
