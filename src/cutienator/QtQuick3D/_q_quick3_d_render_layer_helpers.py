"""
QQuick3DRenderLayerHelpers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DRenderLayerHelpers to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuick3DRenderLayerHelpers(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DRenderLayerHelpers: a plain Python object
  standing in front of one C++ QQuick3DRenderLayerHelpers.

  C++ hands a QQuick3DRenderLayerHelpers around as a copy, so every C++
  QQuick3DRenderLayerHelpers behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQuick3DRenderLayerHelpers yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuick3DRenderLayerHelpers::updateLayerNodeHelper(const
    QQuick3DViewport &view3D, const
    std::shared_ptr<QSSGRenderContextInterface> &rci, QSSGRenderLayer
    &layerNode, bool &aaIsDirty, bool &temporalIsDirty)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQuick3DRenderLayerHelpers::~QQuick3DRenderLayerHelpers()': the
    destructor: Python removes its C++ QQuick3DRenderLayerHelpers by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QQuick3DRenderLayerHelpers is created at the first use, not by
    'QQuick3DRenderLayerHelpers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DRenderLayerHelpers back gives a copy the
    ritual made for Python, in a new cute QQuick3DRenderLayerHelpers.
  - Each name of Qt's QQuick3DRenderLayerHelpers that has no cute function
    yet, 'updateLayerNodeHelper', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DRenderLayerHelpers'

  #  Qt's '~QQuick3DRenderLayerHelpers()'. Naming it makes this a value
  #  class: Python owns every C++ QQuick3DRenderLayerHelpers behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuick3DRenderLayerHelpersD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def updateLayerNodeHelper(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DRenderLayerHelpers::updateLayerNodeHelper(const
    QQuick3DViewport &view3D, const
    std::shared_ptr<QSSGRenderContextInterface> &rci, QSSGRenderLayer
    &layerNode, bool &aaIsDirty, bool &temporalIsDirty)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DRenderLayerHelpers.updateLayerNodeHelper' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DRenderLayerHelpers::updateLayerNodeHelper(const "
        "QQuick3DViewport &view3D, const "
        "std::shared_ptr<QSSGRenderContextInterface> &rci, QSSGRenderLayer "
        "&layerNode, bool &aaIsDirty, bool &temporalIsDirty)': takes a type "
        "Python has no way to hand over yet.")
