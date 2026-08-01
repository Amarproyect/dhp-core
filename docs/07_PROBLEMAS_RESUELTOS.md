# ============================================================================
# DHP - PROBLEMAS RESUELTOS
# ============================================================================

Versión: 2.0

Estado:
ACTIVO

Última actualización:
31/07/2026

Documento:
07_PROBLEMAS_RESUELTOS.md

==============================================================================
OBJETIVO
==============================================================================

Este documento recoge los problemas importantes resueltos durante el desarrollo
del proyecto.

Antes de volver a investigar una incidencia deberá comprobarse si ya aparece
documentada aquí.

==============================================================================

INCIDENCIA 001

CONFIGURACIÓN INICIAL DE HERMES

==============================================================================

Estado

RESUELTA

Descripción

Durante la instalación inicial aparecieron numerosos problemas de
configuración relacionados con proveedores, autenticación y estructura interna.

Resultado

Hermes quedó completamente operativo.

==============================================================================

INCIDENCIA 002

ERROR 401 DEEPSEEK

==============================================================================

Estado

RESUELTA

Síntoma

Authentication Failed

Investigación

Se comprobó:

Proveedor.

Gateway.

Python.

OpenAI SDK.

Variables de entorno.

Fichero .env.

Conclusión

La API Key almacenada tenía únicamente 34 caracteres.

La clave correcta tenía 35.

Causa raíz

Clave truncada.

Resolución

Actualización del fichero:

~/.hermes/.env

Resultado

Incidencia completamente resuelta.

==============================================================================

INCIDENCIA 003

ERROR 402

==============================================================================

Estado

RESUELTA

Síntoma

Insufficient Balance

Investigación

Se verificó:

Gateway.

SDK OpenAI.

curl.

Proveedor.

Conclusión

Saldo insuficiente.

Resolución

Recarga del proveedor.

Resultado

Servicio operativo.

==============================================================================

INCIDENCIA 004

OPEN WEBUI

==============================================================================

Estado

RESUELTA

Síntoma

Open WebUI aparentemente no funcionaba.

Investigación

Docker.

Variables.

Gateway.

SQLite.

Configuración OpenAI.

Conclusión

La infraestructura era correcta.

El problema estaba relacionado con la autenticación del proveedor.

Resultado

Open WebUI funcionando correctamente.

==============================================================================

INCIDENCIA 005

API GATEWAY

==============================================================================

Estado

RESUELTA

Se verificó mediante curl.

Resultado

HTTP 200

Compatible OpenAI.

==============================================================================

INCIDENCIA 006

PRUEBAS PYTHON

==============================================================================

Estado

RESUELTA

Se desarrollaron scripts específicos para validar:

Gateway.

Proveedor.

SDK.

Autenticación.

Todos finalizaron correctamente.

==============================================================================

INCIDENCIA 007

EDICIÓN DEL FICHERO .ENV

==============================================================================

Estado

RESUELTA

Problema

La edición manual mediante nano provocó dificultades para modificar la API Key.

Resolución

Se decidió utilizar scripts en Python para actualizar automáticamente el
fichero ~/.hermes/.env.

Resultado

Proceso mucho más fiable y repetible.

==============================================================================

INCIDENCIA 008

DESCONEXIONES SSH

==============================================================================

Estado

RESUELTA

Descripción

Durante varias sesiones se produjeron desconexiones del cliente SSH desde
PowerShell.

Conclusión

No se detectó ningún problema en Oracle Cloud.

La solución consiste simplemente en reconectar la sesión SSH.

==============================================================================

INCIDENCIA 009

VALIDACIÓN COMPLETA DEL FLUJO

==============================================================================

Estado

RESUELTA

Se verificó correctamente el siguiente flujo:

Open WebUI

↓

Hermes Gateway

↓

Hermes Agent

↓

DeepSeek

↓

Respuesta correcta

Resultado

Infraestructura completamente validada.

==============================================================================

INCIDENCIA 010

HERRAMIENTAS DE HERMES

==============================================================================

Estado

RESUELTA

Se verificó el conjunto real de herramientas disponibles.

También se investigó:

Skills.

Tools.

MCP.

Esta investigación modificó la estrategia inicial del proyecto.

==============================================================================

LECCIONES APRENDIDAS

==============================================================================

Siempre validar con pruebas reales.

Nunca asumir que un error proviene del código sin comprobar primero:

Variables.

Configuración.

Proveedor.

Autenticación.

Conectividad.

==============================================================================

METODOLOGÍA DE RESOLUCIÓN

==============================================================================

Toda incidencia futura deberá seguir este proceso:

1.

Reproducir el problema.

2.

Identificar la causa raíz.

3.

Aplicar una solución mínima.

4.

Validar mediante pruebas reales.

5.

Documentar la incidencia.

==============================================================================

INCIDENCIAS ABIERTAS

==============================================================================

Actualmente

NINGUNA

La infraestructura base del proyecto se considera estable.

==============================================================================

FIN DEL DOCUMENTO

==============================================================================
