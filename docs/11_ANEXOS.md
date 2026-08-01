# ============================================================================
# DHP - ANEXOS TÉCNICOS
# ============================================================================

Versión: 2.0

Estado:
ACTIVO

Última actualización:
31/07/2026

Documento:
11_ANEXOS.md

==============================================================================
OBJETIVO
==============================================================================

Este documento reúne la información técnica de consulta rápida del proyecto
DHP.

No contiene decisiones de arquitectura.

No contiene visión del proyecto.

Su finalidad consiste en facilitar la administración y recuperación del entorno
sin necesidad de repetir investigaciones.

==============================================================================

SERVIDOR PRINCIPAL

==============================================================================

Proveedor

Oracle Cloud

Sistema Operativo

Ubuntu Server 22.04 LTS

Acceso habitual

SSH

Cliente utilizado

Windows PowerShell

==============================================================================

DIRECTORIOS PRINCIPALES

==============================================================================

Proyecto Hermes

~/hermes-agent

------------------------------------------------------------------------------

Configuración Hermes

~/.hermes

------------------------------------------------------------------------------

Variables de entorno

~/.hermes/.env

------------------------------------------------------------------------------

Entorno virtual

~/hermes-agent/.venv

==============================================================================

SERVICIOS INSTALADOS

==============================================================================

Hermes Agent

Estado

VALIDADO

------------------------------------------------------------------------------

Hermes Gateway

Estado

VALIDADO

Puerto

8642

------------------------------------------------------------------------------

Open WebUI

Estado

VALIDADO

Puerto

3000

Contenedor Docker

open-webui

------------------------------------------------------------------------------

Prestashop

Estado

INSTALADO

------------------------------------------------------------------------------

PostgreSQL

Estado

INSTALADO

------------------------------------------------------------------------------

Listmonk

Estado

INSTALADO

==============================================================================

FLUJO VALIDADO

==============================================================================

Usuario

↓

Open WebUI

↓

Hermes Gateway

↓

Hermes Agent

↓

DeepSeek

↓

Respuesta

==============================================================================

ENDPOINT PRINCIPAL

==============================================================================

http://127.0.0.1:8642/v1/chat/completions

==============================================================================

MODELO IA ACTUAL

==============================================================================

Proveedor

DeepSeek

Modelo

deepseek-chat

==============================================================================

COMANDOS FRECUENTES

==============================================================================

Entrar en el proyecto

cd ~/hermes-agent

------------------------------------------------------------------------------

Activar entorno virtual

source .venv/bin/activate

------------------------------------------------------------------------------

Comprobar procesos Hermes

ps -ef | grep -E "gateway|api_server|hermes" | grep -v grep

------------------------------------------------------------------------------

Comprobar puerto

ss -ltnp | grep 8642

------------------------------------------------------------------------------

Comprobar Docker

docker ps -a

==============================================================================

PRUEBA RÁPIDA DEL GATEWAY

==============================================================================

Resultado esperado

HTTP 200

Respuesta

OK

==============================================================================

HERRAMIENTAS DISPONIBLES EN HERMES

==============================================================================

terminal

execute_code

process

memory

todo

patch

read_file

write_file

search_files

delegate_task

cronjob

session_search

skills_list

skill_view

skill_manage

==============================================================================

COMPONENTES PENDIENTES DE INVESTIGACIÓN

==============================================================================

Arquitectura interna de Skills

Arquitectura interna de MCP

Plugin System

Capability Registry

Integraciones oficiales

==============================================================================

CHECKLIST DE RECUPERACIÓN

==============================================================================

□ Oracle Cloud accesible

□ SSH funcionando

□ Docker operativo

□ Hermes Agent activo

□ Gateway escuchando

□ Open WebUI operativo

□ DeepSeek respondiendo

□ API validada

==============================================================================

CHECKLIST ANTES DE PROGRAMAR

==============================================================================

□ Leer documentación

□ Revisar decisiones

□ Revisar problemas resueltos

□ Buscar Skills existentes

□ Buscar MCP existentes

□ Buscar Tools existentes

□ Solo después desarrollar código nuevo

==============================================================================

REGLA DE ORO

==============================================================================

Antes de desarrollar cualquier integración:

1.

Comprobar si existe un Skill.

2.

Comprobar si existe un MCP.

3.

Comprobar si existe una Tool oficial.

4.

Solo desarrollar una solución propia cuando no exista una alternativa oficial.

==============================================================================

FILOSOFÍA DE DESARROLLO

==============================================================================

Investigar.

↓

Diseñar.

↓

Programar.

↓

Probar.

↓

Documentar.

↓

Publicar.

Nunca alterar este orden.

==============================================================================

OBJETIVO FINAL

==============================================================================

Construir un sistema operativo empresarial capaz de administrar completamente
la empresa DHP mediante lenguaje natural, reutilizando siempre que sea posible
las capacidades oficiales de Hermes Agent y manteniendo una arquitectura
modular, desacoplada y preparada para evolucionar durante años.

==============================================================================

FIN DEL DOCUMENTO

==============================================================================
