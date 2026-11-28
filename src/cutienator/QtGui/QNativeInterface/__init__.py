"""
The namespace 'QNativeInterface' of Qt, a package of 'cutienator.QtGui':
what Qt writes inside it, under the names C++ has for it.

  from cutienator.QtGui import QNativeInterface
  QNativeInterface.QWaylandApplication

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
    'QWaylandApplication',
    'QWaylandScreen',
    'QX11Application',
    'QEGLContext',
    'QGLXContext',
    'Private',
)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, List

  from .._q_native_interface__q_wayland_application import QWaylandApplication
  from .._q_native_interface__q_wayland_screen import QWaylandScreen
  from .._q_native_interface__q_x11_application import QX11Application
  from .._q_native_interface__q_e_g_l_context import QEGLContext
  from .._q_native_interface__q_g_l_x_context import QGLXContext
  from . import Private
else:
  #  Where each class is: the file in the folder of the part
  #  that is brought in the first time the class is asked for.
  __class_files__ = {
      'QWaylandApplication': '_q_native_interface__q_wayland_application',
      'QWaylandScreen': '_q_native_interface__q_wayland_screen',
      'QX11Application': '_q_native_interface__q_x11_application',
      'QEGLContext': '_q_native_interface__q_e_g_l_context',
      'QGLXContext': '_q_native_interface__q_g_l_x_context',
  }
  #  The namespaces right inside this one, each a package.
  __space_packages__ = ('Private',)


  def __getattr__(name: str) -> Any:
    """
    Brings in a class or a namespace of this namespace the first time it is
    asked for, as by 'QNativeInterface.QWaylandApplication'. Python calls
    this for a name the package does not hold yet, and what it gives is kept
    here for the next time.

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
