"""
QDeclarativeCircleMapItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativecirclemapitem_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeCircleMapItemPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtPositioning import QGeoCoordinate
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QPointF = WAIT['QPointF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeCircleMapItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDeclarativeCircleMapItemPrivate: a plain Python
  object standing in front of one C++ QDeclarativeCircleMapItemPrivate.

  What exists
  -----------

  Every function of Qt's QDeclarativeCircleMapItemPrivate that has a ritual
  and that Python can call so far, 11 names in all:
  'onLinePropertiesChanged', 'markSourceDirtyAndUpdate', 'onMapSet',
  'onGeoGeometryChanged', 'onItemGeometryChanged', 'updatePolish',
  'afterViewportChanged', 'updateMapItemPaintNode', 'contains',
  'updateCirclePath', 'crossEarthPole'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeclarativeCircleMapItemPrivate::QDeclarativeCircleMapItemPrivate(
    QDeclarativeCircleMapItem &circle)': takes a type Python has no way to
    hand over yet.
  - Qt's
    'QDeclarativeCircleMapItemPrivate::~QDeclarativeCircleMapItemPrivate()':
    the destructor: Python never removes a C++
    QDeclarativeCircleMapItemPrivate.
  - Qt's 'void QDeclarativeCircleMapItemPrivate::includeOnePoleInPath(
    QList<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal
    distance, const QGeoProjectionWebMercator &p)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QDeclarativeCircleMapItemPrivate::calculatePeripheralPointsSimple(
    QList<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal
    distance, const QGeoProjectionWebMercator &p, int steps)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QDeclarativeCircleMapItemPrivate::calculatePeripheralPointsGreatCircle(
    QList<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal
    distance, const QGeoProjectionWebMercator &p, int steps)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDeclarativeCircleMapItemPrivate is created at the first use, not
    by 'QDeclarativeCircleMapItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeCircleMapItemPrivate.
  - Each name of Qt's QDeclarativeCircleMapItemPrivate that has no cute
    function yet, '__init__', 'calculatePeripheralPointsGreatCircle',
    'calculatePeripheralPointsSimple', 'includeOnePoleInPath', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGeoCoordinate, float)
  def crossEarthPole(center: QGeoCoordinate, distance: float) -> int:
    """
    Calls Qt's 'int QDeclarativeCircleMapItemPrivate::crossEarthPole(const
    QGeoCoordinate &center, qreal distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    distance : float
      Passed on as it is.
    """
    #  int QDeclarativeCircleMapItemPrivate::crossEarthPole(const
    #      QGeoCoordinate &center, qreal distance)
    return Rituals.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate14crossEarthPoleERK14QG'
        'eoCoordinated',
        CuteMixin._valueOf(center), distance,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeCircleMapItemPrivate'

  #  A C++ QDeclarativeCircleMapItemPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeCircleMapItemPrivate'

  #  The functions Qt calls itself that QDeclarativeCircleMapItemPrivate is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'onLinePropertiesChanged': (
          ('_ZN32QDeclarativeCircleMapItemPrivate23onLinePropertiesChangedE'
           'v',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'markSourceDirtyAndUpdate': (
          ('_ZN32QDeclarativeCircleMapItemPrivate24markSourceDirtyAndUpdate'
           'Ev',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onMapSet': (
          ('_ZN32QDeclarativeCircleMapItemPrivate8onMapSetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onGeoGeometryChanged': (
          ('_ZN32QDeclarativeCircleMapItemPrivate20onGeoGeometryChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onItemGeometryChanged': (
          ('_ZN32QDeclarativeCircleMapItemPrivate21onItemGeometryChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updatePolish': (
          ('_ZN32QDeclarativeCircleMapItemPrivate12updatePolishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'afterViewportChanged': (
          ('_ZN32QDeclarativeCircleMapItemPrivate20afterViewportChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateMapItemPaintNode': (
          ('_ZN32QDeclarativeCircleMapItemPrivate22updateMapItemPaintNodeEP'
           '7QSGNodePN10QQuickItem19UpdatePaintNodeDataE',
           ('address', 'address', 'QtQuick:QSGNode'),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address',
                'QtQuick:QQuickItem.UpdatePaintNodeData'),
           )),
      ),
      'contains': (
          ('_ZNK32QDeclarativeCircleMapItemPrivate8containsERK7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
  }

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
    Calls Qt's 'bool QDeclarativeCircleMapItemPrivate::contains(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativeCircleMapItemPrivate::contains(const QPointF &point)
    #      const
    return self.uglySide.call(
        'ritual_ZNK32QDeclarativeCircleMapItemPrivate8containsERK7QPointF',
        self._valueOf(point, 'QPointF'),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDeclarativeCircleMapItemPrivate::QDeclarativeCircleMapItemPrivate(
    QDeclarativeCircleMapItem &circle)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeCircleMapItemPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QDeclarativeCircleMapItemPrivate::QDeclarativeCircleMapItemPrivate"
        "(QDeclarativeCircleMapItem &circle)': takes a type Python has no "
        "way to hand over yet.")

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
    QDeclarativeCircleMapItemPrivate::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html
    """
    #  void QDeclarativeCircleMapItemPrivate::onLinePropertiesChanged()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate23onLinePropertiesChang'
        'edEv',
    )

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeCircleMapItemPrivate::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html
    """
    #  void QDeclarativeCircleMapItemPrivate::markSourceDirtyAndUpdate()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate24markSourceDirtyAndUpd'
        'ateEv',
    )

  def onMapSet(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItemPrivate::onMapSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html#onMapSet
    """
    #  void QDeclarativeCircleMapItemPrivate::onMapSet()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate8onMapSetEv',
    )

  def onGeoGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeCircleMapItemPrivate::onGeoGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html
    """
    #  void QDeclarativeCircleMapItemPrivate::onGeoGeometryChanged()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate20onGeoGeometryChangedE'
        'v',
    )

  def onItemGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeCircleMapItemPrivate::onItemGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html
    """
    #  void QDeclarativeCircleMapItemPrivate::onItemGeometryChanged()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate21onItemGeometryChanged'
        'Ev',
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItemPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html#updatePolish
    """
    #  void QDeclarativeCircleMapItemPrivate::updatePolish()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate12updatePolishEv',
    )

  def afterViewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeCircleMapItemPrivate::afterViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html
    """
    #  void QDeclarativeCircleMapItemPrivate::afterViewportChanged()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate20afterViewportChangedE'
        'v',
    )

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
    *QDeclarativeCircleMapItemPrivate::updateMapItemPaintNode(QSGNode
    *oldNode, QQuickItem::UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html

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
    #      *QDeclarativeCircleMapItemPrivate::updateMapItemPaintNode(QSGNode
    #      *oldNode, QQuickItem::UpdatePaintNodeData *data)
    address = self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate22updateMapItemPaintNod'
        'eEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def updateCirclePath(self) -> None:
    """
    Calls Qt's 'void QDeclarativeCircleMapItemPrivate::updateCirclePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativecirclemapitemprivate.html
    """
    #  void QDeclarativeCircleMapItemPrivate::updateCirclePath()
    self.uglySide.call(
        'ritual_ZN32QDeclarativeCircleMapItemPrivate16updateCirclePathEv',
    )

  @staticmethod
  def calculatePeripheralPointsGreatCircle(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeCircleMapItemPrivate::calculatePeripheralPointsGreatCircle(
    QList<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal
    distance, const QGeoProjectionWebMercator &p, int steps)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeCircleMapItemPrivate.calculatePeripheralPointsGreatCir"
        "cle' has no cute function yet. Qt's 'void "
        "QDeclarativeCircleMapItemPrivate::calculatePeripheralPointsGreatCir"
        "cle(QList<QDoubleVector2D> &path, const QGeoCoordinate &center, "
        "qreal distance, const QGeoProjectionWebMercator &p, int steps)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def calculatePeripheralPointsSimple(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeCircleMapItemPrivate::calculatePeripheralPointsSimple(
    QList<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal
    distance, const QGeoProjectionWebMercator &p, int steps)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeCircleMapItemPrivate.calculatePeripheralPointsSimple' "
        "has no cute function yet. Qt's 'void "
        "QDeclarativeCircleMapItemPrivate::calculatePeripheralPointsSimple(Q"
        "List<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal "
        "distance, const QGeoProjectionWebMercator &p, int steps)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def includeOnePoleInPath(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeCircleMapItemPrivate::includeOnePoleInPath(
    QList<QDoubleVector2D> &path, const QGeoCoordinate &center, qreal
    distance, const QGeoProjectionWebMercator &p)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeCircleMapItemPrivate.includeOnePoleInPath' has no "
        "cute function yet. Qt's 'void "
        "QDeclarativeCircleMapItemPrivate::includeOnePoleInPath(QList<QDoubl"
        "eVector2D> &path, const QGeoCoordinate &center, qreal distance, "
        "const QGeoProjectionWebMercator &p)': takes a type Python has no "
        "way to hand over yet.")
