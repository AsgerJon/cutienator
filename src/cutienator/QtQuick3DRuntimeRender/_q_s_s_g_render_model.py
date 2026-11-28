"""
QSSGRenderModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderModel to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSSGRenderNode


class QSSGRenderModel(QSSGRenderNode):
  """
  The cute side of Qt's QSSGRenderModel: a plain Python object standing in
  front of one C++ QSSGRenderModel.

  It is built on the cute 'QSSGRenderNode', as Qt's QSSGRenderModel is built
  on Qt's QSSGRenderNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderModel that has a ritual and that Python
  can call so far, 4 names in all: 'instanceCount', 'instancing',
  'hasLightmap', 'usesBoneTexture'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QSSGRenderModel is created at the first use, not by
    'QSSGRenderModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderModel.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def instanceCount(self) -> int:
    """
    Calls Qt's 'int QSSGRenderModel::instanceCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendermodel.html#instanceCount
    """
    #  int QSSGRenderModel::instanceCount() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderModel13instanceCountEv')

  def instancing(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderModel::instancing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendermodel.html#instancing
    """
    #  bool QSSGRenderModel::instancing() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderModel10instancingEv')

  def hasLightmap(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderModel::hasLightmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendermodel.html#hasLightmap
    """
    #  bool QSSGRenderModel::hasLightmap() const
    return self.uglySide.call('ritual_ZNK15QSSGRenderModel11hasLightmapEv')

  def usesBoneTexture(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderModel::usesBoneTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendermodel.html#usesBoneTexture
    """
    #  bool QSSGRenderModel::usesBoneTexture() const
    return self.uglySide.call(
        'ritual_ZNK15QSSGRenderModel15usesBoneTextureEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderModel::QSSGRenderModel()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendermodel.html#QSSGRenderModel
    """
    #  QSSGRenderModel::QSSGRenderModel()
    self._noteCreation(QSSGRenderModel, lambda: Rituals.call(
        'ritual_ZN15QSSGRenderModelC1Ev',
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
