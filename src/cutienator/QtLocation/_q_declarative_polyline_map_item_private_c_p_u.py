"""
QDeclarativePolylineMapItemPrivateCPU binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePolylineMapItemPrivateCPU to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickItem
from . import QDeclarativePolylineMapItemPrivate

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


class QDeclarativePolylineMapItemPrivateCPU(QDeclarativePolylineMapItemPrivate):
  """
  The cute side of Qt's QDeclarativePolylineMapItemPrivateCPU: a plain Python
  object standing in front of one C++ QDeclarativePolylineMapItemPrivateCPU.

  It is built on the cute 'QDeclarativePolylineMapItemPrivate', as Qt's
  QDeclarativePolylineMapItemPrivateCPU is built on Qt's
  QDeclarativePolylineMapItemPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePolylineMapItemPrivateCPU that has a
  ritual and that Python can call so far, 12 names in all:
  'onLinePropertiesChanged', 'markSourceDirtyAndUpdate', 'regenerateCache',
  'updateCache', 'afterViewportChanged', 'onMapSet', 'onGeoGeometryChanged',
  'onGeoGeometryUpdated', 'onItemGeometryChanged', 'updatePolish',
  'updateMapItemPaintNode', 'contains'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeclarativePolylineMapItemPrivateCPU::
    QDeclarativePolylineMapItemPrivateCPU(QDeclarativePolylineMapItem
    &poly)': takes a type Python has no way to hand over yet.
  - Qt's 'QDeclarativePolylineMapItemPrivateCPU::
    ~QDeclarativePolylineMapItemPrivateCPU()': the destructor: Python never
    removes a C++ QDeclarativePolylineMapItemPrivateCPU.

  What to expect
  --------------

  - The C++ QDeclarativePolylineMapItemPrivateCPU is created at the first
    use, not by 'QDeclarativePolylineMapItemPrivateCPU(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePolylineMapItemPrivateCPU.
  - Each name of Qt's QDeclarativePolylineMapItemPrivateCPU that has no cute
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
  __qt_class__ = 'QDeclarativePolylineMapItemPrivateCPU'

  #  A C++ QDeclarativePolylineMapItemPrivateCPU Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePolylineMapItemPrivateCPU'

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
    Calls Qt's 'bool QDeclarativePolylineMapItemPrivateCPU::contains(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativePolylineMapItemPrivateCPU::contains(const QPointF
    #      &point) const
    ritual = (
        'ritual_ZNK37QDeclarativePolylineMapItemPrivateCPU8containsERK7QPoi'
        'ntF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK37QDeclarativePolylineMapItemPrivateCPU8containsER'
          'K7QPointF')
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
    Qt's 'QDeclarativePolylineMapItemPrivateCPU::
    QDeclarativePolylineMapItemPrivateCPU(QDeclarativePolylineMapItem
    &poly)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativePolylineMapItemPrivateCPU.__init__' has no cute "
        "function yet. Qt's "
        "'QDeclarativePolylineMapItemPrivateCPU::QDeclarativePolylineMapItem"
        "PrivateCPU(QDeclarativePolylineMapItem &poly)': takes a type "
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
    QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::onLinePropertiesChanged()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU23onLineProperties'
        'ChangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU23onLineProp'
          'ertiesChangedEv')
    self.uglySide.call(ritual)

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::markSourceDirtyAndUpdate()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU24markSourceDirtyA'
        'ndUpdateEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU24markSource'
          'DirtyAndUpdateEv')
    self.uglySide.call(ritual)

  def regenerateCache(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItemPrivateCPU::regenerateCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::regenerateCache()
    self.uglySide.call(
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU15regenerateCacheE'
        'v',
    )

  def updateCache(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItemPrivateCPU::updateCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::updateCache()
    self.uglySide.call(
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU11updateCacheEv',
    )

  def afterViewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::afterViewportChanged()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU20afterViewportCha'
        'ngedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU20afterViewp'
          'ortChangedEv')
    self.uglySide.call(ritual)

  def onMapSet(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItemPrivateCPU::onMapSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::onMapSet()
    ritual = 'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU8onMapSetEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU8onMapSetEv')
    self.uglySide.call(ritual)

  def onGeoGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryChanged()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeometryCha'
        'ngedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeome'
          'tryChangedEv')
    self.uglySide.call(ritual)

  def onGeoGeometryUpdated(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::onGeoGeometryUpdated()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeometryUpd'
        'atedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU20onGeoGeome'
          'tryUpdatedEv')
    self.uglySide.call(ritual)

  def onItemGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::onItemGeometryChanged()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU21onItemGeometryCh'
        'angedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU21onItemGeom'
          'etryChangedEv')
    self.uglySide.call(ritual)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItemPrivateCPU::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html
    """
    #  void QDeclarativePolylineMapItemPrivateCPU::updatePolish()
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU12updatePolishEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU12updatePoli'
          'shEv')
    self.uglySide.call(ritual)

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updateMapItemPaintNode(
      self,
      oldNode: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNode(QSGNode
    *oldNode, QQuickItem::UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitemprivatecpu.html

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode
    #      *QDeclarativePolylineMapItemPrivateCPU::updateMapItemPaintNode(
    #      QSGNode *oldNode, QQuickItem::UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN37QDeclarativePolylineMapItemPrivateCPU22updateMapItemPai'
        'ntNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QDeclarativePolylineMapItemPrivateCPU22updateMapI'
          'temPaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
