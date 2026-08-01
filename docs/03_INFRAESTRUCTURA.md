# ============================================================================
# DHP - INFRAESTRUCTURA
# ============================================================================

Versión: 2.0

Estado:
VALIDADA

Última actualización:
31/07/2026

Documento:
03_INFRAESTRUCTURA.md

==============================================================================
OBJETIVO
==============================================================================

Este documento describe la infraestructura técnica actual del proyecto DHP.

Recoge exclusivamente componentes realmente instalados y validados mediante
pruebas.

No incluye arquitectura futura ni hipótesis.

==============================================================================

VISIÓN GENERAL

==============================================================================

Toda la infraestructura principal del proyecto reside actualmente sobre un VPS
de Oracle Cloud.

Sobre este servidor se ejecutan los principales servicios que forman la base
del proyecto DHP.

==============================================================================

SERVIDOR PRINCIPAL

==============================================================================

Proveedor

Oracle Cloud

Sistema Operativo

Ubuntu Server 22.04 LTS

Acceso principal

SSH

Cliente habitual

Windows PowerShell

Estado

VALIDADO

==============================================================================

SERVICIOS INSTALADOS

==============================================================================

Hermes Agent

Estado

VALIDADO

Función

Agente inteligente principal del proyecto.

------------------------------------------------------------------------------

Hermes Gateway

Estado

VALIDADO

Puerto

8642

Función

API compatible con OpenAI utilizada por Open WebUI y otros clientes.

------------------------------------------------------------------------------

Open WebUI

Estado

VALIDADO

Despliegue

Docker

Puerto

3000

Función

Interfaz web principal para interactuar con Hermes.

------------------------------------------------------------------------------

Docker

Estado

VALIDADO

Función

Ejecución y aislamiento de servicios.

------------------------------------------------------------------------------

Prestashop

Estado

INSTALADO

Función

Plataforma principal de comercio electrónico.

------------------------------------------------------------------------------

PostgreSQL

Estado

INSTALADO

Función

Base de datos principal prevista para el Kernel DHP y aplicaciones asociadas.

------------------------------------------------------------------------------

Listmonk

Estado

INSTALADO

Función

Gestión de campañas de correo electrónico.

==============================================================================

ESTRUCTURA PRINCIPAL

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

ALMACENAMIENTO

==============================================================================

Open WebUI

Base de datos SQLite.

La estructura fue inspeccionada directamente durante la investigación.

Hermes

Configuración almacenada en:

~/.hermes/

Variables principales:

~/.hermes/.env

Proyecto Hermes

~/hermes-agent

==============================================================================

VALIDACIONES REALIZADAS

==============================================================================

Durante la fase de infraestructura se realizaron pruebas mediante:

Python

curl

API OpenAI

Open WebUI

Gateway Hermes

Todas finalizaron correctamente.

==============================================================================

CONFIGURACIÓN DEL PROVEEDOR IA

==============================================================================

Proveedor activo

DeepSeek

Estado

VALIDADO

La autenticación fue comprobada mediante scripts Python y pruebas HTTP.

==============================================================================

COMUNICACIÓN VALIDADA

==============================================================================

Open WebUI

↓

Gateway Hermes

↓

Proveedor DeepSeek

↓

Respuesta correcta

==============================================================================

HERRAMIENTAS DISPONIBLES EN HERMES

==============================================================================

Durante la investigación se verificó la disponibilidad de las siguientes
herramientas:

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

OBJETIVO DE ESTA INFRAESTRUCTURA

==============================================================================

Servir como plataforma estable para el desarrollo del Kernel DHP.

Toda la infraestructura deberá mantenerse desacoplada de la lógica empresarial.

==============================================================================

ESTADO GENERAL

==============================================================================

Oracle Cloud

VALIDADO

Linux

VALIDADO

Docker

VALIDADO

Hermes Agent

VALIDADO

Hermes Gateway

VALIDADO

Open WebUI

VALIDADO

DeepSeek

VALIDADO

Prestashop

INSTALADO

PostgreSQL

INSTALADO

Listmonk

INSTALADO

==============================================================================

PRÓXIMA EVOLUCIÓN

==============================================================================

La infraestructura base se considera finalizada.

Las siguientes fases del proyecto se centrarán en:

- Desarrollo del Kernel DHP.
- Integración con Hermes.
- Investigación de Skills.
- Investigación de MCP.
- Automatización empresarial.

==============================================================================

FIN DEL DOCUMENTO

==============================================================================
