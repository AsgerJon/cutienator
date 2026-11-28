"""
QQuickFramePrivate stands in for the class 'QQuickFramePrivate' of Qt, which
has no cute class yet.
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickframe_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFramePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from ..cute import UnsupportedMeta


class QQuickFramePrivate(metaclass=UnsupportedMeta):
  """
  Qt's class 'QQuickFramePrivate' of QtQuickTemplates2: writing its cute
  class raised RuntimeError: The compiler refuses the ritual file of
  'QQuickFramePrivate' as it would be written, for what no code taken from
  Qt's source is to blame: line 7: static_cast from 'QObject *' to
  'QQuickPane *', which are not related by inheritance, is not allowed
  """

  #  The class of Qt this class stands in for.
  __qt_class__ = 'QQuickFramePrivate'
