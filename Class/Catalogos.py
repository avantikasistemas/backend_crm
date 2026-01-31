import traceback
from Utils.tools import Tools, CustomException
from Utils.querys import Querys


class Catalogos:

    def __init__(self, db):
        self.db = db
        self.tools = Tools()
        self.querys = Querys(self.db)

    def get_tipo_registros(self):
        """
        Obtiene todos los tipos de registro activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_tipo_registros", "nombre")
            return self.tools.output(200, "Tipos de registro obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo tipos de registro: {e}")
            return self.tools.output(500, "Error obteniendo tipos de registro.", {})

    def get_origenes(self):
        """
        Obtiene todos los orígenes activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_origenes", "nombre")
            return self.tools.output(200, "Orígenes obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo orígenes: {e}")
            return self.tools.output(500, "Error obteniendo orígenes.", {})

    def get_medios_identificacion(self):
        """
        Obtiene todos los medios de identificación activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_medios_identificacion", "nombre")
            return self.tools.output(200, "Medios de identificación obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo medios de identificación: {e}")
            return self.tools.output(500, "Error obteniendo medios de identificación.", {})

    def get_tiempos_ejecucion(self):
        """
        Obtiene todos los tiempos de ejecución activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_tiempos_ejecucion", "id")
            return self.tools.output(200, "Tiempos de ejecución obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo tiempos de ejecución: {e}")
            return self.tools.output(500, "Error obteniendo tiempos de ejecución.", {})

    def get_tipos_proyecto(self):
        """
        Obtiene todos los tipos de proyecto activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_tipos_proyecto", "nombre")
            return self.tools.output(200, "Tipos de proyecto obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo tipos de proyecto: {e}")
            return self.tools.output(500, "Error obteniendo tipos de proyecto.", {})

    def get_tipos_contratacion(self):
        """
        Obtiene todos los tipos de contratación activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_tipos_contratacion", "nombre")
            return self.tools.output(200, "Tipos de contratación obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo tipos de contratación: {e}")
            return self.tools.output(500, "Error obteniendo tipos de contratación.", {})

    def get_tipos_adjudicacion(self):
        """
        Obtiene todos los tipos de adjudicación activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_tipos_adjudicacion", "nombre")
            return self.tools.output(200, "Tipos de adjudicación obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo tipos de adjudicación: {e}")
            return self.tools.output(500, "Error obteniendo tipos de adjudicación.", {})

    def get_motivos_no_adjudicacion(self):
        """
        Obtiene todos los motivos de no adjudicación activos
        """
        try:
            data = self.querys.get_catalogo_generico("intranet_crm_motivos_no_adjudicacion", "nombre")
            return self.tools.output(200, "Motivos de no adjudicación obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo motivos de no adjudicación: {e}")
            return self.tools.output(500, "Error obteniendo motivos de no adjudicación.", {})

    def get_todos_catalogos(self):
        """
        Obtiene todos los catálogos en una sola petición
        """
        try:
            data = self.querys.get_todos_catalogos()
            return self.tools.output(200, "Catálogos obtenidos exitosamente.", data)
                
        except CustomException as ce:
            return self.tools.output(400, str(ce), {})
        except Exception as e:
            print(f"Error obteniendo catálogos: {e}")
            return self.tools.output(500, "Error obteniendo catálogos.", {})    
    def get_estados(self):
        """Obtiene el catálogo de estados de oportunidades."""
        try:
            estados = self.querys.get_catalogo_generico("intranet_crm_estados", "id")
            return self.tools.output(200, "Estados obtenidos exitosamente.", estados)
        except Exception as e:
            print(f"Error obteniendo estados: {e}")
            return self.tools.output(500, "Error obteniendo estados.", [])