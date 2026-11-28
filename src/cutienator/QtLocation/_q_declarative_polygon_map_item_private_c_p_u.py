"""
QDeclarativePolygonMapItemPrivateCPU binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePolygonMapItemPrivateCPU to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickItem
from . import QDeclarativePolygonMapItemPrivate

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


class QDeclarativePolygonMapItemPrivateCPU(QDeclarativePolygonMapItemPrivate):
  """
  The cute side of Qt's QDeclarativePolygonMapItemPrivateCPU: a plain Python
  object standing in front of one C++ QDeclarativePolygonMapItemPrivateCPU.

  It is built on the cute 'QDeclarativePolygonMapItemPrivate', as Qt's
  QDeclarativePolygonMapItemPrivateCPU is built on Qt's
  QDeclarativePolygonMapItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePolygonMapItemPrivateCPU that has a
  ritual and that Python can call so far, 10 names in all:
  'onLinePropertiesChanged', 'markSourceDirtyAndUpdate',
  'afterViewportChanged', 'onMapSet', 'onGeoGeometryChanged',
  'onGeoGeometryUpdated', 'onItemGeometryChanged', 'updatePolish',
  'updateMapItemPaintNode', 'contains'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeclarativePolygonMapItemPrivateCPU::
    ~QDeclarativePolygonMapItemPrivateCPU()': the destructor: Python never
    removes a C++ QDeclarativePolygonMapItemPrivateCPU.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 leans on 'QDeclarativeGeoMapItemUtils.

  What to expect
  --------------

  - The C++ QDeclarativePolygonMapItemPrivateCPU is created at the first use,
    not by 'QDeclarativePolygonMapItemPrivateCPU(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePolygonMapItemPrivateCPU.
  - Each name of Qt's QDeclarativePolygonMapItemPrivateCPU that has no cute
    function yet, '__init__', 'regenerateCache', 'updateCache', holds a
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
  __qt_class__ = 'QDeclarativePolygonMapItemPrivateCPU'

  #  A C++ QDeclarativePolygonMapItemPrivateCPU Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePolygonMapItemPrivateCPU'

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
    Calls Qt's 'bool QDeclarativePolygonMapItemPrivateCPU::contains(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativePolygonMapItemPrivateCPU::contains(const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK36QDeclarativePolygonMapItemPrivateCPU8containsERK7QPoin'
        'tF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK36QDeclarativePolygonMapItemPrivateCPU8containsERK'
          '7QPointF')
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
    Qt's 'QDeclarativePolygonMapItemPrivateCPU::
    QDeclarativePolygonMapItemPrivateCPU(QDeclarativePolygonMapItem
    &polygon)': leans on
    'QDeclarativeGeoMapItemUtils::greaterCirclePath(QList<QGeoCoordinate>
    const&, QDeclarativeGeoMapItemUtils::greaterCirclePathForm, int)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDeclarativePolygonMapItemPrivateCPU.__init__' has no cute "
        "function yet. Qt's "
        "'QDeclarativePolygonMapItemPrivateCPU::QDeclarativePolygonMapItemPr"
        "ivateCPU(QDeclarativePolygonMapItem &polygon)': leans on "
        "'QDeclarativeGeoMapItemUtils::greaterCirclePath(QList<QGeoCoordinat"
        "e> const&, QDeclarativeGeoMapItemUtils::greaterCirclePathForm, "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

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
    QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::onLinePropertiesChanged()
    ritual = (
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU23onLinePropertiesC'
        'hangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU23onLinePrope'
          'rtiesChangedEv')
    self.uglySide.call(ritual)

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::markSourceDirtyAndUpdate()
    ritual = (
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU24markSourceDirtyAn'
        'dUpdateEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU24markSourceD'
          'irtyAndUpdateEv')
    self.uglySide.call(ritual)

  def afterViewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::afterViewportChanged()
    ritual = (
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU20afterViewportChan'
        'gedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU20afterViewpo'
          'rtChangedEv')
    self.uglySide.call(ritual)

  def onMapSet(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItemPrivateCPU::onMapSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html#onMapSet
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::onMapSet()
    self.uglySide.call(
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU8onMapSetEv',
    )

  def onGeoGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryChanged()
    self.uglySide.call(
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU20onGeoGeometryChan'
        'gedEv',
    )

  def onGeoGeometryUpdated(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::onGeoGeometryUpdated()
    self.uglySide.call(
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU20onGeoGeometryUpda'
        'tedEv',
    )

  def onItemGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::onItemGeometryChanged()
    ritual = (
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU21onItemGeometryCha'
        'ngedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU21onItemGeome'
          'tryChangedEv')
    self.uglySide.call(ritual)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItemPrivateCPU::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html
    """
    #  void QDeclarativePolygonMapItemPrivateCPU::updatePolish()
    ritual = (
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU12updatePolishEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU12updatePolis'
          'hEv')
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
    *QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
    *oldNode, QQuickItem::UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivatecpu.html

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
    #  QSGNode *QDeclarativePolygonMapItemPrivateCPU::updateMapItemPaintNode(
    #      QSGNode *oldNode, QQuickItem::UpdatePaintNodeData *data)
    ritual = (
        'ritual_ZN36QDeclarativePolygonMapItemPrivateCPU22updateMapItemPain'
        'tNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN36QDeclarativePolygonMapItemPrivateCPU22updateMapIt'
          'emPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @staticmethod
  def regenerateCache(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativePolygonMapItemPrivateCPU::regenerateCache()':
    leans on
    'QDeclarativeGeoMapItemUtils::greaterCirclePath(QList<QGeoCoordinate>
    const&, QDeclarativeGeoMapItemUtils::greaterCirclePathForm, int)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDeclarativePolygonMapItemPrivateCPU.regenerateCache' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativePolygonMapItemPrivateCPU::regenerateCache()': leans on "
        "'QDeclarativeGeoMapItemUtils::greaterCirclePath(QList<QGeoCoordinat"
        "e> const&, QDeclarativeGeoMapItemUtils::greaterCirclePathForm, "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def updateCache(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativePolygonMapItemPrivateCPU::updateCache()': leans on
    'QDeclarativeGeoMapItemUtils::greaterCirclePath(QList<QGeoCoordinate>
    const&, QDeclarativeGeoMapItemUtils::greaterCirclePathForm, int)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDeclarativePolygonMapItemPrivateCPU.updateCache' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativePolygonMapItemPrivateCPU::updateCache()': leans on "
        "'QDeclarativeGeoMapItemUtils::greaterCirclePath(QList<QGeoCoordinat"
        "e> const&, QDeclarativeGeoMapItemUtils::greaterCirclePathForm, "
        "int)', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")
