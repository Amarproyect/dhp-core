"""
DHP Kernel - Dependency Resolver
"""

from __future__ import annotations

from graphlib import TopologicalSorter, CycleError

from .plugin import Plugin


class DependencyResolver:
    """
    Resuelve el orden correcto de carga de los plugins
    utilizando sus dependencias.
    """

    def resolve(self, plugins: list[Plugin]) -> list[Plugin]:

        plugin_map = {
            plugin.id: plugin
            for plugin in plugins
        }

        graph: dict[str, set[str]] = {}

        for plugin in plugins:
            graph[plugin.id] = set(plugin.metadata.dependencies)

        #
        # Comprobar dependencias inexistentes
        #
        for plugin_id, deps in graph.items():

            for dep in deps:

                if dep not in plugin_map:

                    raise RuntimeError(
                        f"El plugin '{plugin_id}' depende de "
                        f"'{dep}', pero no existe."
                    )

        try:

            order = list(
                TopologicalSorter(graph).static_order()
            )

        except CycleError as exc:

            raise RuntimeError(
                f"Dependencia circular detectada: {exc}"
            ) from exc

        return [
            plugin_map[plugin_id]
            for plugin_id in order
        ]