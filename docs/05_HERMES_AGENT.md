# ============================================================================
# DHP - HERMES AGENT
# ============================================================================

Versión: 2.0

Estado:
OPERATIVO

Última actualización:
31/07/2026

Documento:
05_HERMES_AGENT.md

==============================================================================
OBJETIVO
==============================================================================

Este documento recoge todo el conocimiento obtenido sobre Hermes Agent durante
la investigación, instalación, configuración y validación realizadas para el
proyecto DHP.

Debe servir como referencia antes de modificar Hermes o integrar nuevas
capacidades.

==============================================================================
OBJETIVO DE HERMES DENTRO DEL PROYECTO DHP
==============================================================================

Hermes NO constituye el Kernel DHP.

Hermes constituye el agente inteligente encargado de interactuar con el usuario
y utilizar las capacidades disponibles.

En la arquitectura prevista:

Usuario

↓

Hermes Agent

↓

Kernel DHP

↓

Servicios empresariales

Hermes nunca deberá contener reglas de negocio.

==============================================================================

ESTADO ACTUAL

==============================================================================

Hermes Agent se encuentra instalado correctamente.

Durante esta fase se consiguió validar completamente:

- Instalación.

- Gateway.

- API OpenAI Compatible.

- Comunicación con DeepSeek.

- Integración con Open WebUI.

Todos los componentes funcionan correctamente.

==============================================================================

MODELO ACTUAL

==============================================================================

Proveedor activo

DeepSeek

Estado

VALIDADO

La comunicación fue comprobada mediante:

Python

curl

Gateway

Open WebUI

==============================================================================

PROBLEMAS RESUELTOS

==============================================================================

INCIDENCIA 1

Error 401

Causa:

API Key truncada.

Se detectó que el fichero .env contenía una API Key de 34 caracteres en lugar
de los 35 correctos.

Resolución:

Actualización del fichero ~/.hermes/.env.

Resultado:

Problema resuelto.

------------------------------------------------------------------------------

INCIDENCIA 2

Error 402

Causa:

Saldo insuficiente.

Resolución:

Recarga del proveedor.

Resultado:

Servicio completamente operativo.

==============================================================================

VALIDACIÓN FINAL

==============================================================================

Se ejecutó una llamada mediante Python.

Resultado:

OK

Posteriormente se ejecutó la misma prueba desde Open WebUI.

Resultado:

OK

Conclusión:

Toda la cadena quedó completamente validada.

==============================================================================

HERRAMIENTAS DETECTADAS

==============================================================================

Durante la investigación Hermes informó disponer de las siguientes herramientas
nativas:

terminal

execute_code

process

read_file

write_file

patch

search_files

memory

todo

cronjob

delegate_task

session_search

skills_list

skill_view

skill_manage

Estas herramientas ya forman parte del entorno operativo.

==============================================================================

CAPACIDADES MÁS IMPORTANTES

==============================================================================

terminal

Permite ejecutar comandos Linux.

------------------------------------------------------------------------------

execute_code

Permite ejecutar código Python utilizando herramientas Hermes.

------------------------------------------------------------------------------

process

Gestión de procesos.

Consultar.

Esperar.

Finalizar.

Leer logs.

------------------------------------------------------------------------------

memory

Memoria persistente.

------------------------------------------------------------------------------

read_file

Lectura de archivos.

------------------------------------------------------------------------------

write_file

Escritura de archivos.

------------------------------------------------------------------------------

patch

Edición parcial de archivos.

==============================================================================

SKILLS

==============================================================================

Hermes utiliza Skills como mecanismo principal para ampliar capacidades.

Los Skills pueden contener:

Instrucciones.

Plantillas.

Scripts.

Workflows.

Documentación.

Herramientas existentes.

La documentación oficial recomienda utilizar Skills siempre que sea posible
antes de desarrollar nuevas Tools.

==============================================================================

TOOLS

==============================================================================

Las Tools representan capacidades nativas del agente.

Su desarrollo implica modificar la arquitectura interna de Hermes.

Solo deberán utilizarse cuando un Skill resulte insuficiente.

==============================================================================

MCP

==============================================================================

Hermes soporta Model Context Protocol.

Los servidores MCP permiten añadir nuevas capacidades de forma desacoplada.

Esta característica será objeto de una investigación específica antes de
implementar nuevas integraciones.

==============================================================================

INVESTIGACIÓN REALIZADA

==============================================================================

Durante esta fase se analizaron:

Arquitectura oficial.

Herramientas.

Skills.

Configuración.

Gateway.

API.

Autenticación.

Proveedor DeepSeek.

==============================================================================

CONCLUSIONES OBTENIDAS

==============================================================================

Conclusión 1

Hermes está diseñado para ampliarse.

------------------------------------------------------------------------------

Conclusión 2

La filosofía del proyecto prioriza:

Skills

↓

MCP

↓

Tools

------------------------------------------------------------------------------

Conclusión 3

Modificar Hermes debe constituir siempre la última opción.

==============================================================================

DECISIÓN ACTUAL DEL PROYECTO

==============================================================================

Tras la investigación realizada se adopta la siguiente decisión provisional.

Hermes será utilizado como:

Agente Inteligente.

Interfaz conversacional.

Motor de razonamiento.

Ejecutor de herramientas.

El Kernel DHP continuará siendo independiente.

==============================================================================

PRÓXIMO OBJETIVO

==============================================================================

Convertir Hermes en el entorno de desarrollo del propio proyecto DHP.

Antes de implementar nuevas funcionalidades deberán investigarse en profundidad
las capacidades oficiales disponibles mediante:

Skills.

MCP.

Plugins.

Integraciones existentes.

El objetivo consiste en reutilizar la arquitectura oficial siempre que sea
posible antes de desarrollar soluciones propias.

==============================================================================

LÍNEAS DE INVESTIGACIÓN ABIERTAS

==============================================================================

Quedan pendientes investigaciones sobre:

MCP para GitHub.

MCP para PostgreSQL.

MCP para Docker.

MCP para Filesystem.

MCP para Prestashop (si existiera).

Arquitectura interna de Skills.

Arquitectura interna de Tools.

Registro interno de capacidades.

==============================================================================

REGLA IMPORTANTE

==============================================================================

Antes de crear una nueva integración para DHP deberá comprobarse:

1. ¿Existe ya un Skill?

2. ¿Existe un MCP?

3. ¿Existe una Tool oficial?

4. Solo en caso negativo se desarrollará una integración propia.

Esta regla pretende mantener la máxima compatibilidad posible con Hermes Agent
y reducir el mantenimiento futuro del proyecto.

==============================================================================

FIN DEL DOCUMENTO

==============================================================================
