import traceback
from Utils.tools import Tools, CustomException
from Utils.querys import Querys


class Oportunidades:

    def __init__(self, db):
        self.db = db
        self.tools = Tools()
        self.querys = Querys(self.db)

    def buscar_terceros(self, data: dict):
        """
        Busca terceros por NIT o nombre
        """
        try:
            valor = data.get("valor", "")
            terceros = self.querys.get_terceros(valor)
            return self.tools.output(200, "Terceros encontrados exitosamente.", terceros)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error buscando terceros: {e}")
            return self.tools.output(500, "Error buscando terceros.", {})

    def guardar_oportunidad(self, data: dict):
        """
        Guarda una nueva oportunidad en la base de datos
        """
        try:
            oportunidad = self.querys.guardar_oportunidad(data)
            return self.tools.output(201, "Oportunidad guardada exitosamente.", oportunidad)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error guardando oportunidad: {e}")
            return self.tools.output(500, "Error guardando oportunidad.", {})

    def listar_oportunidades(self, filtros: dict):
        """
        Lista oportunidades con paginación y filtros
        """
        try:
            resultado = self.querys.listar_oportunidades(filtros)
            return self.tools.output(200, "Oportunidades listadas exitosamente.", resultado)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error listando oportunidades: {e}")
            return self.tools.output(500, "Error listando oportunidades.", {})

    def obtener_oportunidad(self, data: dict):
        """
        Obtiene una oportunidad por ID
        """
        try:
            oportunidad_id = data.get("id")
            if not oportunidad_id:
                raise CustomException("ID de oportunidad requerido")
            
            oportunidad = self.querys.obtener_oportunidad_por_id(oportunidad_id)
            return self.tools.output(200, "Oportunidad obtenida exitosamente.", oportunidad)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo oportunidad: {e}")
            return self.tools.output(500, "Error obteniendo oportunidad.", {})

    def buscar_contactos(self, data: dict):
        """
        Busca contactos por NIT
        """
        try:
            nit = data.get("nit", "")
            if not nit:
                raise CustomException("NIT requerido")
            
            contactos = self.querys.get_contactos(nit)
            return self.tools.output(200, "Contactos encontrados exitosamente.", contactos)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error buscando contactos: {e}")
            return self.tools.output(500, "Error buscando contactos.", {})

    def listar_visitas(self, data: dict):
        """
        Lista visitas de una oportunidad
        """
        try:
            oportunidad_id = data.get("oportunidad_id")
            if not oportunidad_id:
                raise CustomException("ID de oportunidad requerido")
            
            visitas = self.querys.listar_visitas_oportunidad(oportunidad_id)
            return self.tools.output(200, "Visitas listadas exitosamente.", visitas)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error listando visitas: {e}")
            return self.tools.output(500, "Error listando visitas.", {})

    def guardar_visita(self, data: dict):
        """
        Guarda o actualiza una visita
        """
        try:
            visita = self.querys.guardar_visita(data)
            codigo = 201 if not data.get("id") else 200
            mensaje = "Visita creada exitosamente." if not data.get("id") else "Visita actualizada exitosamente."
            return self.tools.output(codigo, mensaje, visita)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error guardando visita: {e}")
            return self.tools.output(500, "Error guardando visita.", {})
    
    def listar_visitas_global(self, filtros: dict):
        """
        Lista todas las visitas con paginación y filtros (vista global)
        """
        try:
            resultado = self.querys.listar_visitas_global(filtros)
            return self.tools.output(200, "Visitas listadas exitosamente.", resultado)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error listando visitas globales: {e}")
            return self.tools.output(500, "Error listando visitas globales.", {})
    
    def listar_visitas_clientes(self, filtros: dict):
        """
        Lista visitas de clientes con paginación y filtros
        """
        try:
            resultado = self.querys.listar_visitas_clientes(filtros)
            return self.tools.output(200, "Visitas de clientes listadas exitosamente.", resultado)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error listando visitas de clientes: {e}")
            return self.tools.output(500, "Error listando visitas de clientes.", {})
    
    def guardar_visita_cliente(self, data: dict):
        """
        Guarda o actualiza una visita de cliente
        """
        try:
            visita = self.querys.guardar_visita_cliente(data)
            codigo = 201 if not data.get("id") else 200
            mensaje = "Visita de cliente creada exitosamente." if not data.get("id") else "Visita de cliente actualizada exitosamente."
            return self.tools.output(codigo, mensaje, visita)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error guardando visita de cliente: {e}")
            return self.tools.output(500, "Error guardando visita de cliente.", {})
