"""
QSSGSceneDesc::Material binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DAssetUtils/6.12.0/QtQuick3DAssetUtils/private/qssgscenedesc_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGSceneDesc::Material to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGSceneDesc
from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject


class Material(QSSGSceneDesc.Node):
  """
  The cute side of Qt's QSSGSceneDesc::Material: a plain Python object
  standing in front of one C++ QSSGSceneDesc::Material.

  It is built on the cute 'QSSGSceneDesc::Node', as Qt's
  QSSGSceneDesc::Material is built on Qt's QSSGSceneDesc::Node, and has
  everything that class has.

  C++ hands a QSSGSceneDesc::Material around as a copy, so every C++
  QSSGSceneDesc::Material behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGSceneDesc::Material yet. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGSceneDesc::Material::~Material()': the destructor: Python
    removes its C++ QSSGSceneDesc::Material by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QSSGSceneDesc::Material is created at the first use, not by
    'QSSGSceneDesc::Material(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGSceneDesc::Material back gives a copy the ritual
    made for Python, in a new cute QSSGSceneDesc::Material.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGSceneDesc::Material'

  #  Qt's '~QSSGSceneDesc::Material()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGSceneDesc::Material behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGSceneDesc8MaterialD1Ev'

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

  @overload(QSSGRenderGraphObject.Type)
  def __init__(self, rt: QSSGRenderGraphObject.Type) -> None:
    """
    Notes what was given, for Qt's
    'QSSGSceneDesc::Material::Material(Node::RuntimeType rt)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgscenedesc-material.html#Material

    Parameters
    ----------

    rt : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  QSSGSceneDesc::Material::Material(Node::RuntimeType rt)
    self._noteCreation(Material, lambda: Rituals.call(
        'ritual_ZN13QSSGSceneDesc8MaterialC1EN21QSSGRenderGraphObject4TypeE',
        rt.value,
    ))

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
