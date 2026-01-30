from Config.db import BASE
from sqlalchemy import Column, String, BigInteger, Text, Integer, DateTime, Date, Numeric
from datetime import datetime

class IntranetCrmOportunidadesModel(BASE):

    __tablename__= "intranet_crm_oportunidades"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    numero_oportunidad = Column(String(50))
    
    # Tipo de registro
    tipo_registro_id = Column(Integer)
    tipo_registro_nombre = Column(String(100))
    
    nombre_oportunidad = Column(String(300))
    
    # Origen
    origen_id = Column(Integer)
    origen_nombre = Column(String(100))
    
    # Medio de identificación
    medio_identificacion_id = Column(Integer)
    medio_identificacion_nombre = Column(String(200))
    
    # Empresa (tercero)
    empresa_nit = Column(String(50))
    empresa_nombre = Column(String(300))
    ciudad = Column(String(200))
    zona = Column(String(200))
    
    # Tiempo de ejecución
    tiempo_ejecucion_id = Column(Integer)
    tiempo_ejecucion_nombre = Column(String(100))
    
    # Tipo de proyecto
    tipo_proyecto_id = Column(Integer)
    tipo_proyecto_nombre = Column(String(100))
    
    # Tipo de contratación
    tipo_contratacion_id = Column(Integer)
    tipo_contratacion_nombre = Column(String(200))
    
    numero_cotizacion = Column(String(100))
    numero_pedidos = Column(String(100))
    owner = Column(String(200))
    
    descripcion = Column(Text)
    competencia = Column(String(500))
    proximos_pasos = Column(String(500))
    
    # Campos de gestión
    tipo_adjudicacion_id = Column(Integer)
    tipo_adjudicacion_nombre = Column(String(50))
    impuestos_adicionales = Column(Numeric(5, 2))
    compromiso_mes = Column(Integer, default=0)
    monto = Column(Numeric(18, 2))
    probabilidad_exito = Column(Numeric(5, 2))
    fecha_cierre = Column(Date)
    numero_oc_contrato = Column(String(100))
    valor_oc_contrato = Column(Numeric(18, 2))
    
    # Motivo no adjudicación
    motivo_no_adjudicacion_id = Column(Integer)
    motivo_no_adjudicacion_nombre = Column(String(300))
    
    # Estado del pipeline de gestión
    estado_id = Column(Integer)
    estado_nombre = Column(String(100))
    
    activo = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, data: dict):
        self.numero_oportunidad = data.get("numero_oportunidad")
        
        self.tipo_registro_id = data.get("tipo_registro_id")
        self.tipo_registro_nombre = data.get("tipo_registro_nombre")
        
        self.nombre_oportunidad = data.get("nombre_oportunidad")
        
        self.origen_id = data.get("origen_id")
        self.origen_nombre = data.get("origen_nombre")
        
        self.medio_identificacion_id = data.get("medio_identificacion_id")
        self.medio_identificacion_nombre = data.get("medio_identificacion_nombre")
        
        self.empresa_nit = data.get("empresa_nit")
        self.empresa_nombre = data.get("empresa_nombre")
        self.ciudad = data.get("ciudad")
        self.zona = data.get("zona")
        
        self.tiempo_ejecucion_id = data.get("tiempo_ejecucion_id")
        self.tiempo_ejecucion_nombre = data.get("tiempo_ejecucion_nombre")
        
        self.tipo_proyecto_id = data.get("tipo_proyecto_id")
        self.tipo_proyecto_nombre = data.get("tipo_proyecto_nombre")
        
        self.tipo_contratacion_id = data.get("tipo_contratacion_id")
        self.tipo_contratacion_nombre = data.get("tipo_contratacion_nombre")
        
        self.numero_cotizacion = data.get("numero_cotizacion")
        self.numero_pedidos = data.get("numero_pedidos")
        self.owner = data.get("owner")
        
        self.descripcion = data.get("descripcion")
        self.competencia = data.get("competencia")
        self.proximos_pasos = data.get("proximos_pasos")
        
        # Campos de gestión
        self.tipo_adjudicacion_id = data.get("tipo_adjudicacion_id")
        self.tipo_adjudicacion_nombre = data.get("tipo_adjudicacion_nombre")
        self.impuestos_adicionales = data.get("impuestos_adicionales")
        self.compromiso_mes = data.get("compromiso_mes", 0)
        self.monto = data.get("monto")
        self.probabilidad_exito = data.get("probabilidad_exito")
        self.fecha_cierre = data.get("fecha_cierre")
        self.numero_oc_contrato = data.get("numero_oc_contrato")
        self.valor_oc_contrato = data.get("valor_oc_contrato")
        
        self.motivo_no_adjudicacion_id = data.get("motivo_no_adjudicacion_id")
        self.motivo_no_adjudicacion_nombre = data.get("motivo_no_adjudicacion_nombre")
        
        self.estado_id = data.get("estado_id")
        self.estado_nombre = data.get("estado_nombre")
        
        self.activo = data.get("activo", 1)
