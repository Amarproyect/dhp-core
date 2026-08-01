# ============================================================================
# DHP - DECISIONES DE ARQUITECTURA
# ============================================================================

Versión: 2.0

Estado:
VIGENTE

Última actualización:
31/07/2026

Documento:
06_DECISIONES.md

==============================================================================
OBJETIVO
==============================================================================

Este documento recoge todas las decisiones importantes tomadas durante el
desarrollo del proyecto.

Su finalidad consiste en impedir que futuras sesiones vuelvan a debatir
cuestiones ya resueltas.

Una decisión únicamente podrá modificarse si existe una evidencia técnica clara
que la contradiga.

==============================================================================

DECISIÓN 001

EL KERNEL ES EL NÚCLEO DEL PROYECTO

==============================================================================

Estado

VIGENTE

Descripción

El Kernel DHP constituye el centro de toda la arquitectura.

Nunca deberá depender del modelo de inteligencia artificial utilizado.

La IA únicamente actuará como consumidor del Kernel.

==============================================================================

DECISIÓN 002

EL LLM NO CONTIENE LÓGICA DE NEGOCIO

==============================================================================

Estado

VIGENTE

Toda la lógica empresarial deberá implementarse dentro del Kernel.

Nunca dentro de:

Hermes

OpenAI

Claude

DeepSeek

Gemini

Copilot

==============================================================================

DECISIÓN 003

DESACOPLAMIENTO TOTAL

==============================================================================

Todo componente deberá poder sustituirse.

Ejemplos.

Cambiar Prestashop.

Cambiar PostgreSQL.

Cambiar Hermes.

Cambiar proveedor IA.

Sin necesidad de reescribir el Kernel.

==============================================================================

DECISIÓN 004

HERMES NO SUSTITUYE AL KERNEL

==============================================================================

Tras la investigación realizada se concluye que:

Hermes constituye un agente.

El Kernel constituye la lógica empresarial.

Ambos sistemas deberán colaborar.

Nunca fusionarse.

==============================================================================

DECISIÓN 005

REUTILIZAR HERMES

==============================================================================

Antes de desarrollar código propio deberá comprobarse siempre:

Existe un Skill.

Existe un MCP.

Existe una Tool.

Solo en caso negativo se desarrollará una solución específica para DHP.

==============================================================================

DECISIÓN 006

NO HACER FORKS INNECESARIOS

==============================================================================

No modificar Hermes salvo necesidad demostrada.

Se priorizará mantener la compatibilidad con futuras versiones oficiales.

==============================================================================

DECISIÓN 007

DOCUMENTAR TODO

==============================================================================

Toda decisión importante deberá quedar registrada.

Toda investigación relevante deberá documentarse.

Toda incidencia importante deberá documentarse.

==============================================================================

DECISIÓN 008

INFRAESTRUCTURA ÚNICA

==============================================================================

Oracle Cloud constituye actualmente el servidor principal del proyecto.

Sobre él residen:

Hermes.

Open WebUI.

Docker.

Prestashop.

PostgreSQL.

Listmonk.

Git.

==============================================================================

DECISIÓN 009

HERMES COMO ENTORNO DE DESARROLLO

==============================================================================

Una vez validada la infraestructura se decide convertir Hermes en el asistente
principal para construir DHP.

Antes de ampliar el Kernel deberá investigarse cómo aprovechar al máximo:

Skills.

MCP.

Tools.

==============================================================================

DECISIÓN 010

MEMORIA DEL PROYECTO

==============================================================================

El conocimiento del proyecto nunca deberá depender exclusivamente de las
conversaciones.

Toda la información importante deberá mantenerse en GitHub mediante
documentación estructurada.

==============================================================================

DECISIÓN 011

HECHOS VS HIPÓTESIS

==============================================================================

Toda la documentación deberá distinguir claramente entre:

Hechos demostrados.

Hipótesis.

Investigaciones.

Decisiones.

Trabajo pendiente.

==============================================================================

DECISIÓN 012

VALIDACIÓN OBLIGATORIA

==============================================================================

Ninguna integración se considerará finalizada hasta existir una prueba real.

Ejemplos.

HTTP 200.

Respuesta correcta.

Prueba mediante Python.

Prueba mediante curl.

Prueba desde Open WebUI.

==============================================================================

DECISIÓN 013

FILOSOFÍA GENERAL

==============================================================================

No construir un chatbot.

Construir un empleado digital.

Toda decisión futura deberá respetar esta filosofía.

==============================================================================

FIN DEL DOCUMENTO

==============================================================================
