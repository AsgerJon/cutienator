"""
The namespace 'QNativeInterface::Private' of Qt, a package of 'cutienator.QtGui':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtGui import QNativeInterface
  QNativeInterface.Private.QXcbScreen

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
    'QXcbScreen',
    'QVsp2Screen',
    'QEvdevKeyMapper',
    'QVxKeyMapper',
    'QXcbWindow',
    'QWaylandWindow',
    'QEGLIntegration',
    'QGLXIntegration',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from ..._q_native_interface__private__q_xcb_screen import QXcbScreen
  from ..._q_native_interface__private__q_vsp2_screen import QVsp2Screen
  from ..._q_native_interface__private__q_evdev_key_mapper import QEvdevKeyMapper
  from ..._q_native_interface__private__q_vx_key_mapper import QVxKeyMapper
  from ..._q_native_interface__private__q_xcb_window import QXcbWindow
  from ..._q_native_interface__private__q_wayland_window import QWaylandWindow
  from ..._q_native_interface__private__q_e_g_l_integration import QEGLIntegration
  from ..._q_native_interface__private__q_g_l_x_integration import QGLXIntegration
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QXcbScreen': '_q_native_interface__private__q_xcb_screen',
      'QVsp2Screen': '_q_native_interface__private__q_vsp2_screen',
      'QEvdevKeyMapper': '_q_native_interface__private__q_evdev_key_mapper',
      'QVxKeyMapper': '_q_native_interface__private__q_vx_key_mapper',
      'QXcbWindow': '_q_native_interface__private__q_xcb_window',
      'QWaylandWindow': '_q_native_interface__private__q_wayland_window',
      'QEGLIntegration': '_q_native_interface__private__q_e_g_l_integration',
      'QGLXIntegration': '_q_native_interface__private__q_g_l_x_integration',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ()


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QNativeInterface.Private.QXcbScreen'. Python calls this
    for a name the package does not hold yet, and what it gives is kept here
    for the next time.

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
      module = importlib.import_module('...%s' % fileName, __name__)
      value = getattr(module, name)
    globals()[name] = value
    return value


  def __dir__() -> List[str]:
    """Names everything of the namespace, brought in or not."""
    return [*__all__]
