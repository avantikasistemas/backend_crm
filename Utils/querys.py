from Utils.tools import Tools, CustomException
from sqlalchemy import text, func, case, extract, and_, or_, Date, cast
from datetime import datetime, date
from Models.IntranetCrmOportunidadesModel import IntranetCrmOportunidadesModel
from Models.IntranetOportunidadVisitasModel import IntranetOportunidadVisitasModel
import json
import traceback


class Querys:

    def __init__(self, db):
        self.db = db
        self.tools = Tools()
        self.query_params = dict()
        
    # Query para obtener los datos del tercero por medio del nit
    def get_terceros(self, valor: str):

        response = list()
        try:
            sql = """
                SELECT t.nit, t.nombres, tv.coordinador, tv.ejecutivo, dbo.terceros_16.descripcion AS 'tipo_cliente', dbo.terceros_2.descripcion AS 'zona',
                t.ciudad
                FROM   dbo.terceros AS t 
                INNER JOIN dbo.terceros_ventas AS tv ON t.concepto_2 = tv.concepto_2 
                INNER JOIN dbo.terceros_16 ON t.concepto_16 = dbo.terceros_16.concepto_16 
                INNER JOIN dbo.terceros_2 ON t.concepto_2 = dbo.terceros_2.concepto_2
                WHERE (t.nit LIKE :valor OR t.nombres LIKE :valor)
            """

            query = self.db.execute(text(sql), {"valor": f"%{valor}%"}).fetchall()

            if query:
                for key in query:   
                    response.append({
                        "nit": key.nit,
                        "nombres": key.nombres,
                        "coordinador": key.coordinador,
                        "ejecutivo": key.ejecutivo,
                        "tipo_cliente": key.tipo_cliente,
                        "zona": key.zona,
                        "ciudad": key.ciudad
                    })

            return response
                
        except Exception as ex:
            print(str(ex))
            raise CustomException(str(ex))
        finally:
            self.db.close()

    # Query para obtener una oportunidad por ID
    def obtener_oportunidad_por_id(self, oportunidad_id: int):
        try:
            oportunidad = self.db.query(IntranetCrmOportunidadesModel).filter(
                IntranetCrmOportunidadesModel.id == oportunidad_id,
                IntranetCrmOportunidadesModel.activo == 1
            ).first()
            
            if not oportunidad:
                raise CustomException("Oportunidad no encontrada")
            
            # Convertir a diccionario con todos los campos
            return {
                "id": oportunidad.id,
                "numero_oportunidad": oportunidad.numero_oportunidad,
                "nombre_oportunidad": oportunidad.nombre_oportunidad,
                
                # Tipo de registro
                "tipo_registro_id": oportunidad.tipo_registro_id,
                "tipo_registro_nombre": oportunidad.tipo_registro_nombre,
                
                # Origen
                "origen_id": oportunidad.origen_id,
                "origen_nombre": oportunidad.origen_nombre,
                
                # Medio de identificación
                "medio_identificacion_id": oportunidad.medio_identificacion_id,
                "medio_identificacion_nombre": oportunidad.medio_identificacion_nombre,
                
                # Empresa
                "empresa_nit": oportunidad.empresa_nit,
                "empresa_nombre": oportunidad.empresa_nombre,
                "ciudad": oportunidad.ciudad,
                "zona": oportunidad.zona,
                
                # Tiempo de ejecución
                "tiempo_ejecucion_id": oportunidad.tiempo_ejecucion_id,
                "tiempo_ejecucion_nombre": oportunidad.tiempo_ejecucion_nombre,
                
                # Tipo de proyecto
                "tipo_proyecto_id": oportunidad.tipo_proyecto_id,
                "tipo_proyecto_nombre": oportunidad.tipo_proyecto_nombre,
                
                # Tipo de contratación
                "tipo_contratacion_id": oportunidad.tipo_contratacion_id,
                "tipo_contratacion_nombre": oportunidad.tipo_contratacion_nombre,
                
                # Información adicional
                "numero_cotizacion": oportunidad.numero_cotizacion,
                "numero_pedidos": oportunidad.numero_pedidos,
                "owner": oportunidad.owner,
                
                # Campos de texto
                "descripcion": oportunidad.descripcion,
                "competencia": oportunidad.competencia,
                "proximos_pasos": oportunidad.proximos_pasos,
                
                # Campos de gestión
                "tipo_adjudicacion_id": oportunidad.tipo_adjudicacion_id,
                "tipo_adjudicacion_nombre": oportunidad.tipo_adjudicacion_nombre,
                "impuestos_adicionales": float(oportunidad.impuestos_adicionales) if oportunidad.impuestos_adicionales else None,
                "compromiso_mes": oportunidad.compromiso_mes,
                "monto": float(oportunidad.monto) if oportunidad.monto else None,
                "probabilidad_exito": float(oportunidad.probabilidad_exito) if oportunidad.probabilidad_exito else None,
                "fecha_cierre": oportunidad.fecha_cierre.isoformat() if oportunidad.fecha_cierre else None,
                "numero_oc_contrato": oportunidad.numero_oc_contrato,
                "valor_oc_contrato": float(oportunidad.valor_oc_contrato) if oportunidad.valor_oc_contrato else None,
                
                # Motivo no adjudicación
                "motivo_no_adjudicacion_id": oportunidad.motivo_no_adjudicacion_id,
                "motivo_no_adjudicacion_nombre": oportunidad.motivo_no_adjudicacion_nombre,
                
                # Estado
                "estado_id": oportunidad.estado_id,
                "estado_nombre": oportunidad.estado_nombre,
                
                # Auditoría
                "created_at": oportunidad.created_at.isoformat() if oportunidad.created_at else None,
                "updated_at": oportunidad.updated_at.isoformat() if oportunidad.updated_at else None
            }
                
        except Exception as ex:
            print(f"Error obteniendo oportunidad: {str(ex)}")
            raise CustomException(str(ex))
        finally:
            self.db.close()
    
    # Query para listar oportunidades con paginación y filtros
    def listar_oportunidades(self, filtros: dict):
        try:
            # Extraer parámetros de paginación
            pagina = filtros.get("pagina", 1)
            page_size = filtros.get("page_size", 30)
            busqueda = filtros.get("busqueda", "").strip()
            zona = filtros.get("zona", "").strip()
            estado = filtros.get("estado", "").strip()
            
            # Query base
            query = self.db.query(IntranetCrmOportunidadesModel).filter(
                IntranetCrmOportunidadesModel.activo == 1
            )
            
            # Aplicar filtros
            if busqueda:
                query = query.filter(
                    or_(
                        IntranetCrmOportunidadesModel.numero_oportunidad.ilike(f"%{busqueda}%"),
                        IntranetCrmOportunidadesModel.nombre_oportunidad.ilike(f"%{busqueda}%"),
                        IntranetCrmOportunidadesModel.empresa_nombre.ilike(f"%{busqueda}%")
                    )
                )
            
            if zona:
                query = query.filter(
                    IntranetCrmOportunidadesModel.zona.ilike(f"%{zona}%")
                )
            
            if estado:
                query = query.filter(
                    IntranetCrmOportunidadesModel.estado_nombre == estado
                )
            
            # Contar total de registros
            total_registros = query.count()
            
            # Ordenar por fecha de creación descendente
            query = query.order_by(IntranetCrmOportunidadesModel.id.desc())
            
            # Aplicar paginación
            offset = (pagina - 1) * page_size
            oportunidades = query.offset(offset).limit(page_size).all()
            
            # Convertir a diccionario
            resultado = []
            for op in oportunidades:
                resultado.append({
                    "id": op.id,
                    "numero_oportunidad": op.numero_oportunidad,
                    "nombre_oportunidad": op.nombre_oportunidad,
                    "empresa_nombre": op.empresa_nombre,
                    "zona": op.zona,
                    "owner": op.owner,
                    "estado": op.estado_nombre,
                    "monto": float(op.monto) if op.monto else None,
                    "fecha_cierre": op.fecha_cierre.isoformat() if op.fecha_cierre else None,
                    "created_at": op.created_at.isoformat() if op.created_at else None
                })
            
            return {
                "oportunidades": resultado,
                "total_registros": total_registros,
                "pagina": pagina,
                "page_size": page_size,
                "total_paginas": (total_registros + page_size - 1) // page_size
            }
                
        except Exception as ex:
            print(f"Error listando oportunidades: {str(ex)}")
            raise CustomException(str(ex))
        finally:
            self.db.close()
    
    # Query para guardar una oportunidad
    def guardar_oportunidad(self, data: dict):
        try:
            oportunidad_id = data.get("id")
            
            # Si tiene ID, es una actualización
            if oportunidad_id:
                oportunidad = self.db.query(IntranetCrmOportunidadesModel).filter(
                    IntranetCrmOportunidadesModel.id == oportunidad_id
                ).first()
                
                if not oportunidad:
                    raise CustomException("Oportunidad no encontrada")
                
                # Campos que no se deben actualizar
                campos_excluidos = ['id', 'created_at']
                
                # Actualizar campos
                for key, value in data.items():
                    if hasattr(oportunidad, key) and key not in campos_excluidos:
                        setattr(oportunidad, key, value)
                
                # Actualizar fecha de modificación
                oportunidad.updated_at = datetime.now()
                self.db.commit()
                self.db.refresh(oportunidad)
                
                return {
                    "id": oportunidad.id,
                    "numero_oportunidad": oportunidad.numero_oportunidad,
                    "nombre_oportunidad": oportunidad.nombre_oportunidad,
                    "created_at": oportunidad.created_at.isoformat() if oportunidad.created_at else None,
                    "updated_at": oportunidad.updated_at.isoformat() if oportunidad.updated_at else None
                }
            else:
                # Es una nueva oportunidad
                nueva_oportunidad = IntranetCrmOportunidadesModel(data)
                self.db.add(nueva_oportunidad)
                self.db.commit()
                self.db.refresh(nueva_oportunidad)
                
                # Generar numero_oportunidad con el ID
                numero_op = f"OP{str(nueva_oportunidad.id).zfill(5)}"
                nueva_oportunidad.numero_oportunidad = numero_op
                self.db.commit()
                self.db.refresh(nueva_oportunidad)
                
                # Devolver data completa
                return {
                    "id": nueva_oportunidad.id,
                    "numero_oportunidad": nueva_oportunidad.numero_oportunidad,
                    "nombre_oportunidad": nueva_oportunidad.nombre_oportunidad,
                    "created_at": nueva_oportunidad.created_at.isoformat() if nueva_oportunidad.created_at else None,
                    "updated_at": nueva_oportunidad.updated_at.isoformat() if nueva_oportunidad.updated_at else None
                }
                
        except Exception as ex:
            self.db.rollback()
            print(f"Error guardando oportunidad: {str(ex)}")
            raise CustomException(str(ex))
        finally:
            self.db.close()

    # Query para obtener los contactos de la cotización.            
    def get_contactos(self, nit: str):
        try:
            response = list()
            sql = """
                SELECT nit, nombre, tel_celular FROM CRM_contactos WHERE nit = :nit ORDER BY nombre ASC;
            """
            query = self.db.execute(text(sql), {"nit": nit}).fetchall()
            for row in query:
                response.append({
                    "tel_celular": row.tel_celular,
                    "nombre": row.nombre.upper(),
                    "nit": row.nit
                })
            return response

        except Exception as ex:
            raise CustomException(str(ex))
        finally:
            self.db.close()

    # Query para listar visitas de una oportunidad
    def listar_visitas_oportunidad(self, oportunidad_id: int):
        try:
            visitas = self.db.query(IntranetOportunidadVisitasModel).filter(
                IntranetOportunidadVisitasModel.oportunidad_id == oportunidad_id,
                IntranetOportunidadVisitasModel.activo == 1
            ).order_by(IntranetOportunidadVisitasModel.fecha_hora.desc()).all()
            
            resultado = []
            for visita in visitas:
                resultado.append({
                    "id": visita.id,
                    "oportunidad_id": visita.oportunidad_id,
                    "asunto": visita.asunto,
                    "tipo_id": visita.tipo_id,
                    "tipo_nombre": visita.tipo_nombre,
                    "contacto": visita.contacto,
                    "objetivo": visita.objetivo,
                    "fecha_hora": visita.fecha_hora.isoformat() if visita.fecha_hora else None,
                    "estado_id": visita.estado_id,
                    "estado_nombre": visita.estado_nombre,
                    "fecha_cierre_real": visita.fecha_cierre_real.isoformat() if visita.fecha_cierre_real else None,
                    "created_at": visita.created_at.isoformat() if visita.created_at else None
                })
            
            return resultado
                
        except Exception as ex:
            print(f"Error listando visitas: {str(ex)}")
            raise CustomException(str(ex))
        finally:
            self.db.close()
    
    # Query para guardar o actualizar una visita
    def guardar_visita(self, data: dict):
        try:
            visita_id = data.get("id")
            
            # Convertir fecha_hora de string a datetime si es necesario
            if isinstance(data.get("fecha_hora"), str):
                try:
                    # Formato: 2026-02-02T16:47
                    data["fecha_hora"] = datetime.strptime(data["fecha_hora"], "%Y-%m-%dT%H:%M")
                except ValueError:
                    try:
                        # Intentar con formato ISO completo
                        data["fecha_hora"] = datetime.fromisoformat(data["fecha_hora"])
                    except:
                        raise CustomException("Formato de fecha/hora inválido")
            
            # Si tiene ID, es una actualización
            if visita_id:
                visita = self.db.query(IntranetOportunidadVisitasModel).filter(
                    IntranetOportunidadVisitasModel.id == visita_id
                ).first()
                
                if not visita:
                    raise CustomException("Visita no encontrada")
                
                # Campos que no se deben actualizar
                campos_excluidos = ['id', 'created_at']
                
                # Verificar cambio de estado para setear fecha_cierre_real
                if data.get("estado_id") != 1 and visita.estado_id == 1:
                    data["fecha_cierre_real"] = datetime.now()
                
                # Actualizar campos
                for key, value in data.items():
                    if hasattr(visita, key) and key not in campos_excluidos:
                        setattr(visita, key, value)
                
                visita.updated_at = datetime.now()
                self.db.commit()
                self.db.refresh(visita)
                
                return {
                    "id": visita.id,
                    "oportunidad_id": visita.oportunidad_id,
                    "asunto": visita.asunto,
                    "fecha_hora": visita.fecha_hora.isoformat() if visita.fecha_hora else None,
                    "estado_nombre": visita.estado_nombre,
                    "estado_id": visita.estado_id
                }
            else:
                # Es una nueva visita
                # Verificar si el estado es diferente de "Abierto" para setear fecha_cierre_real
                if data.get("estado_id") != 1:
                    data["fecha_cierre_real"] = datetime.now()
                
                nueva_visita = IntranetOportunidadVisitasModel(data)
                self.db.add(nueva_visita)
                self.db.commit()
                self.db.refresh(nueva_visita)
                
                return {
                    "id": nueva_visita.id,
                    "oportunidad_id": nueva_visita.oportunidad_id,
                    "asunto": nueva_visita.asunto,
                    "fecha_hora": nueva_visita.fecha_hora.isoformat() if nueva_visita.fecha_hora else None,
                    "estado_nombre": nueva_visita.estado_nombre
                }
                
        except Exception as ex:
            self.db.rollback()
            print(f"Error guardando visita: {str(ex)}")
            raise CustomException(str(ex))
        finally:
            self.db.close()
