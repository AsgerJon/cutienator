"""
The namespace 'QtWayland' of Qt, a package of 'cutienator.QtWaylandCompositor':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtWaylandCompositor import QtWayland
  QtWayland.ServerBuffer

A class is brought in the first time it is asked for.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.PackageGenerator. Changes made here are
#  lost.
from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

__all__ = (
    'ServerBuffer',
    'ClientBufferIntegrationFactory',
    'HardwareLayerIntegrationFactory',
    'ServerBufferIntegrationFactory',
    'ClientBufferIntegrationPlugin',
    'HardwareLayerIntegrationPlugin',
    'ServerBufferIntegrationPlugin',
    'HardwareLayerIntegration',
    'QWaylandTextureOrphanage',
    'ServerBufferIntegration',
    'IviSurfaceIntegration',
    'XdgPopupIntegration',
    'XdgToplevelIntegration',
    'WlShellIntegration',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._qt_wayland__server_buffer import ServerBuffer
  from .._qt_wayland__client_buffer_integration_factory import ClientBufferIntegrationFactory
  from .._qt_wayland__hardware_layer_integration_factory import HardwareLayerIntegrationFactory
  from .._qt_wayland__server_buffer_integration_factory import ServerBufferIntegrationFactory
  from .._qt_wayland__client_buffer_integration_plugin import ClientBufferIntegrationPlugin
  from .._qt_wayland__hardware_layer_integration_plugin import HardwareLayerIntegrationPlugin
  from .._qt_wayland__server_buffer_integration_plugin import ServerBufferIntegrationPlugin
  from .._qt_wayland__hardware_layer_integration import HardwareLayerIntegration
  from .._qt_wayland__q_wayland_texture_orphanage import QWaylandTextureOrphanage
  from .._qt_wayland__server_buffer_integration import ServerBufferIntegration
  from .._qt_wayland__ivi_surface_integration import IviSurfaceIntegration
  from .._qt_wayland__xdg_popup_integration import XdgPopupIntegration
  from .._qt_wayland__xdg_toplevel_integration import XdgToplevelIntegration
  from .._qt_wayland__wl_shell_integration import WlShellIntegration
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'ServerBuffer': '_qt_wayland__server_buffer',
      'ClientBufferIntegrationFactory': '_qt_wayland__client_buffer_integration_factory',
      'HardwareLayerIntegrationFactory': '_qt_wayland__hardware_layer_integration_factory',
      'ServerBufferIntegrationFactory': '_qt_wayland__server_buffer_integration_factory',
      'ClientBufferIntegrationPlugin': '_qt_wayland__client_buffer_integration_plugin',
      'HardwareLayerIntegrationPlugin': '_qt_wayland__hardware_layer_integration_plugin',
      'ServerBufferIntegrationPlugin': '_qt_wayland__server_buffer_integration_plugin',
      'HardwareLayerIntegration': '_qt_wayland__hardware_layer_integration',
      'QWaylandTextureOrphanage': '_qt_wayland__q_wayland_texture_orphanage',
      'ServerBufferIntegration': '_qt_wayland__server_buffer_integration',
      'IviSurfaceIntegration': '_qt_wayland__ivi_surface_integration',
      'XdgPopupIntegration': '_qt_wayland__xdg_popup_integration',
      'XdgToplevelIntegration': '_qt_wayland__xdg_toplevel_integration',
      'WlShellIntegration': '_qt_wayland__wl_shell_integration',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QtWayland.ServerBuffer'. Python calls this for a name
    the package does not hold yet, and what it gives is kept here for the
    next time.

    Raises
    ------

    AttributeError
      The namespace has nothing of that name.
    """
    if name in __space_packages__:
      value = importlib.import_module('.%s' % name, __name__)
    else:
      try:
        fileName = __class_files__[name]
      except KeyError:
        infoSpec = """module '%s' has no attribute '%s'"""
        raise AttributeError(infoSpec % (__name__, name)) from None
      module = importlib.import_module('..%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
