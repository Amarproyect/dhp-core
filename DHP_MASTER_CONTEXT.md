# DHP_MASTER_CONTEXT

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
