# ============================================================================
# DHP - HISTORIAL DE SESIONES
# ============================================================================

Versión: 2.0

Estado:
ACTIVO

Última actualización:
31/07/2026

Documento:
09_SESIONES.md

==============================================================================
OBJETIVO
==============================================================================

Este documento registra cronológicamente los hitos más importantes del
desarrollo del proyecto DHP.

No pretende sustituir al historial de Git.

Su finalidad consiste en comprender la evolución del proyecto, las decisiones
adoptadas y el contexto de cada fase importante.

Cada nueva etapa relevante deberá añadirse al final de este documento.

==============================================================================

SESIÓN 001

ORIGEN DEL PROYECTO

==============================================================================

Objetivo

Definir la visión del proyecto.

Resultado

Se decidió construir un sistema operativo empresarial basado en inteligencia
artificial en lugar de un simple chatbot.

Decisiones principales

- Kernel independiente.

- Arquitectura modular.

- Desacoplamiento completo del modelo LLM.

==============================================================================

SESIÓN 002

DISEÑO CONCEPTUAL DEL KERNEL

==============================================================================

Objetivo

Diseñar la arquitectura principal del sistema.

Resultado

Se definieron los componentes fundamentales:

Core.

Runtime.

Providers.

Connectors.

Plugin Manager.

Capability Registry.

Event Bus.

==============================================================================

SESIÓN 003

ESTUDIO DE TECNOLOGÍAS

==============================================================================

Objetivo

Evaluar las tecnologías disponibles.

Se investigaron:

Hermes Agent.

Open WebUI.

Prestashop.

Docker.

Oracle Cloud.

GitHub.

PostgreSQL.

Listmonk.

Conclusión

Hermes Agent se seleccionó como plataforma principal para el desarrollo del
proyecto debido a su arquitectura extensible.

==============================================================================

SESIÓN 004

DESPLIEGUE DE INFRAESTRUCTURA

==============================================================================

Objetivo

Preparar el entorno de desarrollo.

Trabajos realizados

- Oracle Cloud.

- Ubuntu.

- Docker.

- Prestashop.

- Hermes Agent.

- Open WebUI.

- GitHub.

Resultado

Infraestructura estable.

==============================================================================

SESIÓN 005

INVESTIGACIÓN DE HERMES

==============================================================================

Objetivo

Comprender la arquitectura oficial de Hermes.

Investigaciones realizadas

Skills.

Tools.

MCP.

Sistema de memoria.

Ejecución de código.

Gestión de procesos.

Conclusión

La estrategia del proyecto cambió.

Se decidió reutilizar la arquitectura oficial siempre que fuera posible antes
de desarrollar componentes propios.

==============================================================================

SESIÓN 006

DEPURACIÓN DE DEEPSEEK

==============================================================================

Objetivo

Resolver definitivamente los errores de autenticación.

Problemas encontrados

401 Authentication Failed.

402 Insufficient Balance.

Investigación

Variables.

Python.

curl.

Gateway.

SDK OpenAI.

Open WebUI.

Conclusiones

La API Key estaba truncada.

Posteriormente se detectó falta de saldo.

Resultado

Proveedor completamente operativo.

==============================================================================

SESIÓN 007

VALIDACIÓN GLOBAL

==============================================================================

Objetivo

Validar toda la infraestructura.

Pruebas realizadas

Python.

curl.

Gateway.

Open WebUI.

Resultado

Open WebUI

↓

Hermes Gateway

↓

Hermes Agent

↓

DeepSeek

↓

Respuesta correcta.

Esta sesión marca el final de la Fase 1 del proyecto.

==============================================================================

SESIÓN 008

DOCUMENTACIÓN TÉCNICA

==============================================================================

Objetivo

Crear una documentación permanente del proyecto.

Resultado

Se decide organizar toda la documentación en documentos independientes dentro
del repositorio GitHub.

Se crean:

00_LEEME_PRIMERO.md

01_VISION_DHP.md

02_ESTADO_PROYECTO.md

03_INFRAESTRUCTURA.md

04_KERNEL_DHP.md

05_HERMES_AGENT.md

06_DECISIONES.md

07_PROBLEMAS_RESUELTOS.md

08_ROADMAP.md

09_SESIONES.md

10_RECUPERACION.md

11_ANEXOS.md

12_MASTER_MANUAL.md

Objetivo

Eliminar la dependencia exclusiva de las conversaciones como fuente de
conocimiento del proyecto.

==============================================================================

ESTADO ACTUAL

==============================================================================

Infraestructura

COMPLETADA

Documentación

EN DESARROLLO

Investigación Hermes

PENDIENTE

Kernel

PENDIENTE

Integraciones empresariales

PENDIENTES

==============================================================================

SESIÓN 009

AUDITORÍA, OPTIMIZACIÓN DE COSTE Y CORRECCIÓN DEL KERNEL DHP

==============================================================================

Fecha

05/08/2026

Objetivo

Auditar el repo dhp-core, reducir el coste de tokens de la plataforma
Hermes/DeepSeek y corregir desalineaciones del código con la tienda real
de PrestaShop.

Trabajos realizados

Auditoría estructurada del repo dhp-core (árbol completo, contenido por
carpetas, export a docs/auditoria_arbol.txt).

Consolidación de memoria del agente: MEMORY -19%, perfil de usuario -31%
y skill prestashop-read -36% (sin perder información crítica).

Diagnóstico de caché de DeepSeek: la caché KV funciona (hit 96-99% con
prefijo idéntico); el coste alto del 02/08 se debió a clientes que creaban
sesión nueva por request (historial completo reenviado como cache miss).

Harness de sesión estable creado y verificado en scripts/harness_sesion_estable.py:
header X-Hermes-Session-Id persistente por conversación + body solo con el
mensaje nuevo; dos requests idénticos reutilizan la misma sesión y la caché
(probe: 2304 hit / 87 miss).

Corrección del provider PrestaShop (dhp/providers/prestashop.py): endpoint
legacy /webservice/dispatcher.php + Host hardcodeado sustituido por el Web
Service oficial /api de PS 8.1.7 con display selectivo.

Optimización de product_service (dhp/services/product_service.py): list()
pasó de N+1 (625 llamadas HTTP) a 1 llamada con display=[campos], verificado
contra los 624 productos reales en 0.3s.

Actualización de pyproject.toml: dependencias reales declaradas (requests,
python-dotenv).

Problemas encontrados

El proveedor usaba el endpoint legacy de PrestaShop 1.x (dispatcher.php),
incompatible con el WS moderno de PS 8.1.7 (solo devolvía ids).

list() realizaba N+1: 1 llamada de lista + 1 por producto (625 en total).

pyproject.toml declaraba dependencies=[] pese a importar requests y
python-dotenv.

El cliente del 02/08 creaba una sesión por request: 9 llamadas de 300k+
tokens sin caché (~59% del coste del día).

Soluciones

Provider: endpoint /api/{resource}, normalización de la URL base (/api),
sin Host hardcodeado, display selectivo opcional.

ProductService: list() con display=[id,reference,name,price,ean13,active]
en una sola llamada y mapeo directo a Product; se conserva la tolerancia a
errores por item y la interfaz pública.

pyproject: dependencies = ["requests", "python-dotenv"].

Harness de referencia para clientes externos: sesión estable por conversación
con X-Hermes-Session-Id (UUID v4 persistido) y body mínimo.

Decisiones tomadas

El Kernel se mantiene desacoplado; el provider solo cambia su implementación
interna, no su interfaz.

La caché de DeepSeek es automática por prefijo; la continuidad de sesión se
gestiona en el cliente (header) o en Open WebUI (previous_response_id).

Estado final

Provider, product_service y pyproject corregidos y verificados con datos
reales (1 request, 624 productos, 0.3s). Harness de sesión estable
documentado y funcionando. Sin incidencias abiertas.

==============================================================================

==============================================================================

REGLA PARA FUTURAS SESIONES

==============================================================================

Toda sesión importante deberá registrar:

Fecha.

Objetivo.

Trabajos realizados.

Problemas encontrados.

Soluciones.

Decisiones tomadas.

Estado final.

==============================================================================

FIN DEL DOCUMENTO

==============================================================================
