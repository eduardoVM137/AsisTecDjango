# AsisTecDjango

## Descripción General
**AsisTecDjango** es un sistema de asistencia desarrollado en Django diseñado para gestionar y automatizar procesos relacionados con el registro, monitoreo y control de asistencia de personal o estudiantes(Ajustable a otros entornos mas). El sistema incluye una interfaz amigable, registro eficiente de asistencia y la capacidad de visualizar métricas clave mediante un dashboard interactivo en Power BI.

## Funcionalidades Principales
- Registro de asistencia en tiempo real.
- Administración de usuarios (administradores y empleados/estudiantes).
- Generación de reportes en formato PDF e importacion de datos.
- Generación de horarios en formato PDF en base la informacion proporcionada.
- Integración con un dashboard en Power BI para la visualización de datos.

## Estructura del Proyecto
- **Backend**: Django 4.0.
- **Frontend**: Bootstrap 5 y plantillas Django.
- **Base de Datos**: SQLite (configurable para PostgreSQL o MySQL).
- **Dashboard**: Power BI integrado en una pestaña del sistema.

## Dashboard: Métricas Clave
El dashboard de Power BI está diseñado para ofrecer una visión detallada del uso y la eficiencia del sistema. Incluye las siguientes métricas:

### Métricas de Asistencia
1. **Porcentaje de Asistencia**: Total de asistencias registradas frente al total de días laborales.
2. **Usuarios con Mayor Asistencia**: Ranking de usuarios con mejor registro de asistencia.
3. **Asistencias Tardías**: Cantidad de asistencias marcadas fuera del horario establecido.
4. **Tendencia de Asistencia Mensual**: Comparación de asistencia mes a mes.
5. **otros mas**: Mas metricas disponibles en la plataforma...

 

## Cómo Ejecutar el Proyecto
1. **Requisitos**:
   - Python 3.9 o superior.
   - Django 4.0 instalado.
   - Power BI configurado para la integración.
2. **Pasos de Instalación**:
   1. Clonar el repositorio:
      ```bash
      git clone https://github.com/eduardoVM137/AsisTecDjango.git
      ```
   2. Instalar dependencias:
      ```bash
      pip install -r requirements.txt
      ```
   3. Migrar la base de datos:
      ```bash
      python manage.py migrate
      ```
   4. Ejecutar el servidor:
      ```bash
      python manage.py runserver
      ```
3. **Acceso al Dashboard**:
   - Navegar a la pestaña `Dashboard` en la aplicación para visualizar las métricas integradas.
 

## Conclusión
**AsisTecDjango** es una solución integral para el control de asistencia, complementada con visualización de datos en Power BI. Este proyecto refleja habilidades en desarrollo backend, integración de dashboards y análisis de datos para la toma de decisiones.

--- 


https://app.powerbi.com/reportEmbed?reportId=6b4aaeb9-5a60-444f-9452-5a38132a353c&autoAuth=true&ctid=725ab307-b77c-4f66-9168-376b1c7f9990
