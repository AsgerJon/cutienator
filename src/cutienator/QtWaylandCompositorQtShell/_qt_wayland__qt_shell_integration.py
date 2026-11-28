"""
QtShellIntegration stands in for the class 'QtWayland::QtShellIntegration' of
Qt, which has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositorQtShell/6.12.0/QtWaylandCompositorQtShell/private/qwaylandqtshellintegration_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtWayland::QtShellIntegration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class QtShellIntegration(metaclass=UnsupportedMeta):
  """
  Qt's class 'QtWayland::QtShellIntegration' of QtWaylandCompositorQtShell:
  cutienator ships no ritual file of it
  (QtWaylandCompositorQtShellRituals/qt_wayland__qt_shell_integration.cpp)
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QtWayland::QtShellIntegration'
