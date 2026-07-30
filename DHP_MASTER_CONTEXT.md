# DHP_MASTER_CONTEXT
# ⚠️ IMPORTANTE PARA FUTURAS SESIONES

Antes de proponer nuevas hipótesis o repetir comprobaciones, leer completamente este archivo y las sesiones anteriores.

No volver a repetir verificaciones ya descartadas salvo que exista una evidencia nueva.

Cuando se retome el proyecto, continuar exactamente desde el apartado "Próximo paso" de la última sesión registrada.

El objetivo es mantener continuidad entre sesiones y evitar perder tiempo repitiendo investigaciones ya realizadas.

> Documento maestro del proyecto DHP.

## Estado recuperado (27/07/2026)

-   Proyecto: DHP
-   Repositorio: Amarproyect/dhp-core
-   Oracle: /opt/dhp
-   Repositorio Oracle: /opt/dhp/apps/dhp-core
-   Rama: kernel-v1
-   Git: limpio y sincronizado con origin/kernel-v1

## Hallazgos confirmados

-   El kernel DHP existe.
-   El kernel fue desarrollado antes que Hermes.
-   Hermes está instalado en /opt/dhp/sources/hermes-agent y
    \~/hermes-agent.
-   Existe configuración \~/.hermes.
-   La estructura /opt/dhp pertenece al proyecto DHP.

## Cronología

1.  Initial project structure
2.  Provider interface
3.  Base Provider
4.  Move common provider initialization
5.  Refactor Prestashop provider
6.  ProductService
7.  Product count
8.  Initial kernel foundation
9.  Service container
10. Hermes boot system
11. Dependency resolver
12. Stable kernel v1 foundation

## Arquitectura

Módulos: - kernel - providers - services - commerce - communications -
knowledge - marketing - office - models - config - core - cli

Kernel: - boot - registry - service_container - dependency_resolver -
plugin - plugin_loader - plugin_manager - lifecycle - event -
event_bus - command_bus - command_handler - command_middleware -
logger_service - resolver

## Decisiones

-   DHP es el proyecto.
-   Hermes es un componente.
-   Todo gira alrededor del kernel.

## Próximo paso

Documentar completamente el kernel e integrar Hermes sobre él.
---

# 📅 SESIÓN 2026-07-30 – Investigación Hermes + Open WebUI + DeepSeek

## Estado general

Objetivo de la sesión:

Resolver el error de autenticación (HTTP 401) que se produce cuando Open WebUI utiliza Hermes Agent con DeepSeek, aunque la misma API Key funciona correctamente mediante curl.

---

# Infraestructura

## Servidor

Oracle Cloud

Ubuntu

Proyecto:

/home/ubuntu/hermes-agent

Entorno virtual:

.venv

---

## Gateway

Servicio:

hermes-gateway

Escuchando en:

0.0.0.0:8642

Comprobación:

GET /v1/models

Resultado:

hermes-agent

Conclusión:

Gateway funcionando correctamente.

---

# Open WebUI

Configuración utilizada:

Base URL

http://172.17.0.1:8642/v1

API Type

responses

API Key

dhp-hermes-2026-OPENWEBUI

Conclusión:

Configuración correcta.

---

# DeepSeek

API Key utilizada

sk-e1be6da102b944f698970bf905e7f7c1

Comprobación mediante curl.

Resultado:

HTTP 200

Modelo devuelto:

deepseek-v4-flash

Conclusión:

La API Key es completamente válida.

---

# Configuración Hermes

Archivos utilizados

~/.hermes/config.yaml

~/.hermes/.env

Se confirmó que Hermes carga correctamente la API Key desde .env.

---

# Problema observado

Flujo:

Open WebUI

↓

Hermes Gateway

↓

Hermes Agent

↓

DeepSeek

Resultado:

HTTP 401

Authentication Fails

Your api key ****7f7c is invalid

Pero exactamente esa misma API Key funciona mediante curl.

---

# Investigaciones realizadas

## 1. Open WebUI

Descartado.

Configuración correcta.

---

## 2. Gateway

Descartado.

El Gateway responde correctamente.

---

## 3. API Key

Comprobado:

- carga correcta

- lectura correcta

- envío correcto

Los logs muestran:

****7f7c

que coincide exactamente con la API Key válida.

---

## 4. Configuración Hermes

Revisados:

config.yaml

.env

No existe ningún problema de configuración.

---

## 5. Código fuente investigado

Archivos principales revisados

agent/auxiliary_client.py

agent/chat_completion_helpers.py

agent/transports/chat_completions.py

run_agent.py

---

# Investigación del cliente OpenAI

Se comprobó completamente:

_create_openai_client()

Resultado:

Hermes crea el cliente simplemente mediante:

OpenAI(
    api_key=api_key,
    base_url=base_url
)

No modifica la API Key.

---

# Investigación de _to_openai_base_url()

Analizado completamente.

Solo modifica:

- Anthropic

- Kimi

- ZAI

Para DeepSeek devuelve exactamente:

https://api.deepseek.com/v1

Conclusión:

La base_url NO se modifica.

---

# Investigación resolve_api_key_provider()

Se comprobó todo el flujo.

Hermes:

obtiene api_key

obtiene base_url

crea cliente OpenAI

No aparecen modificaciones sospechosas.

---

# Investigación chat_completion_helpers.py

Se localizó la llamada real al proveedor.

La llamada es:

request_client.chat.completions.create(**api_kwargs)

No existe ninguna capa adicional.

---

# Versiones

Commit Hermes

4c9628eab5393e7561bbd2c1faaa1765fb14a5f9

SDK OpenAI

2.24.0

---

# Estado Git

git status

Solo aparece:

?? --helpq

Archivo sin seguimiento.

No relacionado con el problema.

---

# Hipótesis descartadas

✅ API Key incorrecta

✅ Base URL incorrecta

✅ Open WebUI

✅ Gateway

✅ Error en .env

✅ Error en config.yaml

✅ Reescritura de base_url

✅ Error al crear el cliente OpenAI

---

# Situación actual

Todo apunta a que el problema ocurre durante:

request_client.chat.completions.create(**api_kwargs)

Todavía NO conocemos el contenido exacto de:

api_kwargs

en tiempo de ejecución.

---

# Próximo paso

NO continuar haciendo grep.

NO seguir leyendo miles de líneas de código.

Instrumentar Hermes.

Añadir temporalmente logs justo antes de:

request_client.chat.completions.create(**api_kwargs)

para imprimir:

- base_url

- modelo

- provider

- últimos caracteres de la API Key

- api_kwargs completos

Con ello se podrá conocer exactamente qué petición está enviando Hermes a DeepSeek.

---

# Conclusión de la sesión

Después de varias horas de investigación se consiguió reducir el problema desde todo el proyecto Hermes a un único punto del código.

Ya no parece un problema de configuración.

Las posibilidades restantes son:

1. Un bug de Hermes en esa revisión.

2. Un bug del SDK OpenAI 2.24.0 utilizado por Hermes.

3. Parámetros incorrectos contenidos en api_kwargs.

La próxima sesión debe comenzar instrumentando esa llamada para registrar la petición real antes de enviarla a DeepSeek.

NO volver a repetir todas las comprobaciones ya realizadas.

Continuar exactamente desde este punto.
