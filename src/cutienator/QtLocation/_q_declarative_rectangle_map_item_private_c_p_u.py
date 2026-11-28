"""
QDeclarativeRectangleMapItemPrivateCPU binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativerectanglemapitem_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeRectangleMapItemPrivateCPU to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickItem
from . import QDeclarativeRectangleMapItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeRectangleMapItemPrivateCPU(QDeclarativeRectangleMapItemPrivate):
  """
  The cute side of Qt's QDeclarativeRectangleMapItemPrivateCPU: a plain
  Python object standing in front of one C++
  QDeclarativeRectangleMapItemPrivateCPU.

  It is built on the cute 'QDeclarativeRectangleMapItemPrivate', as Qt's
  QDeclarativeRectangleMapItemPrivateCPU is built on Qt's
  QDeclarativeRectangleMapItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeRectangleMapItemPrivateCPU that has a
  ritual and that Python can call so far, 9 names in all:
  'onLinePropertiesChanged', 'markSourceDirtyAndUpdate', 'onMapSet',
  'onGeoGeometryChanged', 'onItemGeometryChanged', 'afterViewportChanged',
  'updatePolish', 'updateMapItemPaintNode', 'contains'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeclarativeRectangleMapItemPrivateCPU::
    QDeclarativeRectangleMapItemPrivateCPU(QDeclarativeRectangleMapItem
    &rect)': takes a type Python has no way to hand over yet.
  - Qt's 'QDeclarativeRectangleMapItemPrivateCPU::
    ~QDeclarativeRectangleMapItemPrivateCPU()': the destructor: Python never
    removes a C++ QDeclarativeRectangleMapItemPrivateCPU.

  What to expect
  --------------

  - The C++ QDeclarativeRectangleMapItemPrivateCPU is created at the first
    use, not by 'QDeclarativeRectangleMapItemPrivateCPU(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeRectangleMapItemPrivateCPU.
  - Each name of Qt's QDeclarativeRectangleMapItemPrivateCPU that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'QDeclarativeRectangleMapItemPrivateCPU'

  #  A C++ QDeclarativeRectangleMapItemPrivateCPU Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeRectangleMapItemPrivateCPU'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QDeclarativeRectangleMapItemPrivateCPU::contains(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativeRectangleMapItemPrivateCPU::contains(const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK38QDeclarativeRectangleMapItemPrivateCPU8containsERK7QPo'
        'intF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK38QDeclarativeRectangleMapItemPrivateCPU8containsE'
          'RK7QPointF')
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

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
    Qt's 'QDeclarativeRectangleMapItemPrivateCPU::
    QDeclarativeRectangleMapItemPrivateCPU(QDeclarativeRectangleMapItem
    &rect)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeRectangleMapItemPrivateCPU.__init__' has no cute "
        "function yet. Qt's "
        "'QDeclarativeRectangleMapItemPrivateCPU::QDeclarativeRectangleMapIt"
        "emPrivateCPU(QDeclarativeRectangleMapItem &rect)': takes a type "
        "Python has no way to hand over yet.")

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

  def onLinePropertiesChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void QDeclarativeRectangleMapItemPrivateCPU::onLinePropertiesChanged()
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU23onLinePropertie'
        'sChangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU23onLinePro'
          'pertiesChangedEv')
    self.uglySide.call(ritual)

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void
    #      QDeclarativeRectangleMapItemPrivateCPU::markSourceDirtyAndUpdate()
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU24markSourceDirty'
        'AndUpdateEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU24markSourc'
          'eDirtyAndUpdateEv')
    self.uglySide.call(ritual)

  def onMapSet(self) -> None:
    """
    Calls Qt's 'void QDeclarativeRectangleMapItemPrivateCPU::onMapSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void QDeclarativeRectangleMapItemPrivateCPU::onMapSet()
    ritual = 'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU8onMapSetEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU8onMapSetEv')
    self.uglySide.call(ritual)

  def onGeoGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void QDeclarativeRectangleMapItemPrivateCPU::onGeoGeometryChanged()
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU20onGeoGeometryCh'
        'angedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU20onGeoGeom'
          'etryChangedEv')
    self.uglySide.call(ritual)

  def onItemGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void QDeclarativeRectangleMapItemPrivateCPU::onItemGeometryChanged()
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU21onItemGeometryC'
        'hangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU21onItemGeo'
          'metryChangedEv')
    self.uglySide.call(ritual)

  def afterViewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void QDeclarativeRectangleMapItemPrivateCPU::afterViewportChanged()
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU20afterViewportCh'
        'angedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU20afterView'
          'portChangedEv')
    self.uglySide.call(ritual)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativeRectangleMapItemPrivateCPU::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html
    """
    #  void QDeclarativeRectangleMapItemPrivateCPU::updatePolish()
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU12updatePolishEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU12updatePol'
          'ishEv')
    self.uglySide.call(ritual)

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updateMapItemPaintNode(
      self,
      oldNode: Optional[QSGNode],
      data: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
    *oldNode, QQuickItem::UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivatecpu.html

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode
    #      *QDeclarativeRectangleMapItemPrivateCPU::updateMapItemPaintNode(
    #      QSGNode *oldNode, QQuickItem::UpdatePaintNodeData *data)
    ritual = (
        'ritual_ZN38QDeclarativeRectangleMapItemPrivateCPU22updateMapItemPa'
        'intNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN38QDeclarativeRectangleMapItemPrivateCPU22updateMap'
          'ItemPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
