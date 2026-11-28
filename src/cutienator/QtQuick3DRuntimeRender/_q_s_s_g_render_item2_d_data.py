"""
QSSGRenderItem2DData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderItem2DData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGRenderItem2DData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderItem2DData: a plain Python object standing
  in front of one C++ QSSGRenderItem2DData.

  What exists
  -----------

  Every function of Qt's QSSGRenderItem2DData that has a ritual and that
  Python can call so far, 1 name in all: 'releaseAll'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderItem2DData::QSSGRenderItem2DData(const
    QSSGGlobalRenderNodeDataPtr &globalNodeData)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSSGRenderItem2DData::~QSSGRenderItem2DData()': the destructor:
    Python never removes a C++ QSSGRenderItem2DData.
  - Qt's 'ModelViewProjections
    QSSGRenderItem2DData::getModelViewProjection(QSSGRenderNodeHandle h)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'ModelViewProjections
    QSSGRenderItem2DData::getModelViewProjection(const QSSGRenderItem2D
    &item) const': takes a type Python has no way to hand over yet.
  - Qt's 'Item2DRenderer QSSGRenderItem2DData::getItem2DRenderer(const
    QSSGRenderItem2D &item) const': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QSSGGlobalRenderNodeDataPtr
    &QSSGRenderItem2DData::globalNodeData() const': gives a type Python has
    no way to take yet.
  - Qt's 'void QSSGRenderItem2DData::releaseRenderData(const QSSGRenderItem2D
    &item)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 4 forbidden; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QSSGRenderItem2DData is created at the first use, not by
    'QSSGRenderItem2DData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderItem2DData.
  - Each name of Qt's QSSGRenderItem2DData that has no cute function yet,
    '__init__', 'getItem2DRenderer', 'getModelViewProjection',
    'globalNodeData', 'releaseRenderData', 'updateItem2DData', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderItem2DData'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QSSGRenderItem2DData::QSSGRenderItem2DData(const
    QSSGGlobalRenderNodeDataPtr &globalNodeData)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderItem2DData.__init__' has no cute function yet. Qt's "
        "'QSSGRenderItem2DData::QSSGRenderItem2DData(const "
        "QSSGGlobalRenderNodeDataPtr &globalNodeData)': takes a type Python "
        "has no way to hand over yet.")

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

  def releaseAll(self) -> None:
    """
    Calls Qt's 'void QSSGRenderItem2DData::releaseAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderitem2ddata.html#releaseAll
    """
    #  void QSSGRenderItem2DData::releaseAll()
    self.uglySide.call('ritual_ZN20QSSGRenderItem2DData10releaseAllEv')

  @staticmethod
  def getItem2DRenderer(*__, **_) -> Never:
    """
    Qt's 'Item2DRenderer QSSGRenderItem2DData::getItem2DRenderer(const
    QSSGRenderItem2D &item) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderItem2DData.getItem2DRenderer' has no cute function yet. "
        "Qt's 'Item2DRenderer QSSGRenderItem2DData::getItem2DRenderer(const "
        "QSSGRenderItem2D &item) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def getModelViewProjection(*__, **_) -> Never:
    """
    - Qt's 'ModelViewProjections
      QSSGRenderItem2DData::getModelViewProjection(QSSGRenderNodeHandle h)
      const': takes a type Python has no way to hand over yet.
    - Qt's 'ModelViewProjections
      QSSGRenderItem2DData::getModelViewProjection(const QSSGRenderItem2D
      &item) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderItem2DData.getModelViewProjection' has no cute function "
        "yet. Qt's 'ModelViewProjections "
        "QSSGRenderItem2DData::getModelViewProjection(QSSGRenderNodeHandle "
        "h) const': takes a type Python has no way to hand over yet. Qt's "
        "'ModelViewProjections "
        "QSSGRenderItem2DData::getModelViewProjection(const "
        "QSSGRenderItem2D &item) const': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def globalNodeData(*__, **_) -> Never:
    """
    Qt's 'const QSSGGlobalRenderNodeDataPtr
    &QSSGRenderItem2DData::globalNodeData() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderItem2DData.globalNodeData' has no cute function yet. "
        "Qt's 'const QSSGGlobalRenderNodeDataPtr "
        "&QSSGRenderItem2DData::globalNodeData() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def releaseRenderData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderItem2DData::releaseRenderData(const QSSGRenderItem2D
    &item)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderItem2DData.releaseRenderData' has no cute function yet. "
        "Qt's 'void QSSGRenderItem2DData::releaseRenderData(const "
        "QSSGRenderItem2D &item)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def updateItem2DData(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderItem2DData::updateItem2DData(QSSGItem2DsView &items,
    QSSGRenderer *renderer, const QSSGRenderCameraDataList
    &renderCameraData)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'const QSSGRenderItem2D'.
    """
    raise NotImplementedError(
        "'QSSGRenderItem2DData.updateItem2DData' has no cute function yet. "
        "Qt's 'void QSSGRenderItem2DData::updateItem2DData(QSSGItem2DsView "
        "&items, QSSGRenderer *renderer, const QSSGRenderCameraDataList "
        "&renderCameraData)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'const QSSGRenderItem2D'.")
