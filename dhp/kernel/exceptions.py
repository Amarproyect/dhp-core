"""
DHP Kernel Exceptions

Excepciones base del Kernel.
Todo el resto del framework heredará de ellas.
"""


class KernelError(Exception):
    """Excepción base del Kernel."""


class PluginError(KernelError):
    """Error relacionado con plugins."""


class PluginNotFoundError(PluginError):
    """Plugin no encontrado."""


class DuplicatePluginError(PluginError):
    """Ya existe un plugin con ese ID."""


class InvalidPluginError(PluginError):
    """Plugin inválido."""


class PluginAlreadyStartedError(PluginError):
    """El plugin ya estaba iniciado."""


class PluginNotStartedError(PluginError):
    """El plugin no está iniciado."""


class CapabilityError(KernelError):
    """Error relacionado con capabilities."""


class CapabilityNotFoundError(CapabilityError):
    """Capability no encontrada."""


class DuplicateCapabilityError(CapabilityError):
    """Capability registrada dos veces."""


class RegistryError(KernelError):
    """Errores del Registry."""


class EventBusError(KernelError):
    """Errores del EventBus."""