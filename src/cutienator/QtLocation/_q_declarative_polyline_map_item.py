"""
QDeclarativePolylineMapItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativepolylinemapitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePolylineMapItem to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick import QQuickItem
from . import QDeclarativeGeoMapItemBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtPositioning import QGeoCoordinate, QGeoPath, QGeoShape
  from ..QtQuick import QSGNode
  from . import QDeclarativeGeoMap, QDeclarativeMapLineProperties, QGeoMap
  from . import QGeoMapViewportChangeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoMap = WAIT['QGeoMap']
  QGeoMapViewportChangeEvent = WAIT['QGeoMapViewportChangeEvent']
  QGeoPath = WAIT['QGeoPath']
  QGeoShape = WAIT['QGeoShape']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativePolylineMapItem(QDeclarativeGeoMapItemBase):
  """
  The cute side of Qt's QDeclarativePolylineMapItem: a plain Python object
  standing in front of one C++ QDeclarativePolylineMapItem.

  It is built on the cute 'QDeclarativeGeoMapItemBase', as Qt's
  QDeclarativePolylineMapItem is built on Qt's QDeclarativeGeoMapItemBase,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePolylineMapItem that has a ritual and
  that Python can call so far, 23 names in all: 'metaObject', 'tr', 'setMap',
  'updateMapItemPaintNode', 'pathLength', 'addCoordinate',
  'insertCoordinate', 'replaceCoordinate', 'coordinateAt',
  'containsCoordinate', 'removeCoordinate', 'path', 'setPath', 'contains',
  'geoShape', 'setGeoShape', 'line', 'pathChanged',
  'updateAfterLinePropertiesChanged', 'afterViewportChanged',
  'geometryChange', 'setPathFromGeoList', 'updatePolish'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePolylineMapItem::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativePolylineMapItem::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePolylineMapItem::~QDeclarativePolylineMapItem()': the
    destructor: Python never removes a C++ QDeclarativePolylineMapItem.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePolylineMapItem is created at the first use, not by
    'QDeclarativePolylineMapItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePolylineMapItem.
  - Qt tells when it has removed the C++ QDeclarativePolylineMapItem. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QDeclarativePolylineMapItem::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativePolylineMapItem::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QDeclarativePolylineMapItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePolylineMapItem'

  #  A C++ QDeclarativePolylineMapItem Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePolylineMapItem'

  #  The functions Qt calls itself that QDeclarativePolylineMapItem is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setPath': (
          'void QDeclarativePolylineMapItem::setPath(const '
          'QList<QGeoCoordinate> &)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativePolylineMapItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePolylineMapItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativePolylineMapItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def pathLength(self) -> int:
    """
    Calls Qt's 'int QDeclarativePolylineMapItem::pathLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#pathLength
    """
    #  int QDeclarativePolylineMapItem::pathLength() const
    return self.uglySide.call(
        'ritual_ZNK27QDeclarativePolylineMapItem10pathLengthEv',
    )

  @overload(int)
  def coordinateAt(self, index: int) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativePolylineMapItem::coordinateAt(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#coordinateAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativePolylineMapItem::coordinateAt(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativePolylineMapItem12coordinateAtEi', index,
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QDeclarativePolylineMapItem::path()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QDeclarativePolylineMapItem::path() const
    address = self.uglySide.call(
        'ritual_ZNK27QDeclarativePolylineMapItem4pathEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QDeclarativePolylineMapItem::contains(const QPointF
    &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativePolylineMapItem::contains(const QPointF &point) const
    ritual = 'ritual_ZNK27QDeclarativePolylineMapItem8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK27QDeclarativePolylineMapItem8containsERK7QPointF')
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  def geoShape(self) -> QGeoShape:
    """
    Calls Qt's 'const QGeoShape &QDeclarativePolylineMapItem::geoShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#geoShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  const QGeoShape &QDeclarativePolylineMapItem::geoShape() const
    ritual = 'ritual_ZNK27QDeclarativePolylineMapItem8geoShapeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QDeclarativePolylineMapItem8geoShapeEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativeGeoMap, QGeoMap)
  @overload(QDeclarativeGeoMap, NoneType)
  @overload(NoneType, QGeoMap)
  @overload(NoneType, NoneType)
  def setMap(
      self,
      quickMap: Optional[QDeclarativeGeoMap],
      map: Optional[QGeoMap],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::setMap(QDeclarativeGeoMap
    *quickMap, QGeoMap *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#setMap

    Parameters
    ----------

    quickMap : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    map : Optional[QGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePolylineMapItem::setMap(QDeclarativeGeoMap *quickMap,
    #      QGeoMap *map)
    ritual = (
        'ritual_ZN27QDeclarativePolylineMapItem6setMapEP18QDeclarativeGeoMa'
        'pP7QGeoMap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativePolylineMapItem6setMapEP18QDeclarativ'
          'eGeoMapP7QGeoMap')
    self.uglySide.call(
        ritual, self._addressOf(quickMap), self._addressOf(map),
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, value: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::setPath(const
    QList<QGeoCoordinate> &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#setPath

    Parameters
    ----------

    value : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativePolylineMapItem::setPath(const QList<QGeoCoordinate>
    #      &value)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem7setPathERK5QListI14QGeoCoor'
        'dinateE',
        self._valueOf(value),
    )

  @overload(QGeoPath)
  def setPath(self, path: QGeoPath) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::setPath(const QGeoPath
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#setPath

    Parameters
    ----------

    path : QGeoPath
      Passed on as a value: Qt reads the C++ QGeoPath, which stays Python's
      own.
    """
    #  void QDeclarativePolylineMapItem::setPath(const QGeoPath &path)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem7setPathERK8QGeoPath',
        self._valueOf(path),
    )

  @overload(QGeoShape)
  def setGeoShape(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::setGeoShape(const QGeoShape
    &shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#setGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativePolylineMapItem::setGeoShape(const QGeoShape &shape)
    ritual = (
        'ritual_ZN27QDeclarativePolylineMapItem11setGeoShapeERK9QGeoShape')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativePolylineMapItem11setGeoShapeERK9QGeoS'
          'hape')
    self.uglySide.call(ritual, self._valueOf(shape))

  @overload(QList[QGeoCoordinate])
  def setPathFromGeoList(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::setPathFromGeoList(const
    QList<QGeoCoordinate> &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativePolylineMapItem::setPathFromGeoList(const
    #      QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem18setPathFromGeoListERK5QLis'
        'tI14QGeoCoordinateE',
        self._valueOf(path),
    )

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativePolylineMapItem::QDeclarativePolylineMapItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePolylineMapItem::QDeclarativePolylineMapItem(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativePolylineMapItem, lambda: Rituals.call(
        'ritual_ZN27QDeclarativePolylineMapItemC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updateMapItemPaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QDeclarativePolylineMapItem::updateMapItemPaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html

    Parameters
    ----------

    a0 : Optional[QSGNode]
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
    #  QSGNode *QDeclarativePolylineMapItem::updateMapItemPaintNode(QSGNode
    #      *a0, UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN27QDeclarativePolylineMapItem22updateMapItemPaintNodeEP7Q'
        'SGNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativePolylineMapItem22updateMapItemPaintNo'
          'deEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QGeoCoordinate)
  def addCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::addCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#addCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativePolylineMapItem::addCoordinate(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem13addCoordinateERK14QGeoCoor'
        'dinate',
        self._valueOf(coordinate),
    )

  @overload(int, QGeoCoordinate)
  def insertCoordinate(self, index: int, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::insertCoordinate(int index,
    const QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#insertCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativePolylineMapItem::insertCoordinate(int index, const
    #      QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem16insertCoordinateEiRK14QGeo'
        'Coordinate',
        index, self._valueOf(coordinate),
    )

  @overload(int, QGeoCoordinate)
  def replaceCoordinate(
      self,
      index: int,
      coordinate: QGeoCoordinate,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::replaceCoordinate(int
    index, const QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#replaceCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativePolylineMapItem::replaceCoordinate(int index, const
    #      QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem17replaceCoordinateEiRK14QGe'
        'oCoordinate',
        index, self._valueOf(coordinate),
    )

  @overload(QGeoCoordinate)
  def containsCoordinate(self, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QDeclarativePolylineMapItem::containsCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QDeclarativePolylineMapItem::containsCoordinate(const
    #      QGeoCoordinate &coordinate)
    return self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem18containsCoordinateERK14QGe'
        'oCoordinate',
        self._valueOf(coordinate),
    )

  @overload(QGeoCoordinate)
  def removeCoordinate(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::removeCoordinate(const
    QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#removeCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativePolylineMapItem::removeCoordinate(const
    #      QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem16removeCoordinateERK14QGeoC'
        'oordinate',
        self._valueOf(coordinate),
    )

  @overload(int)
  def removeCoordinate(self, index: int) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::removeCoordinate(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#removeCoordinate

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QDeclarativePolylineMapItem::removeCoordinate(int index)
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem16removeCoordinateEi', index,
    )

  def line(self) -> Optional[QDeclarativeMapLineProperties]:
    """
    Calls Qt's 'QDeclarativeMapLineProperties
    *QDeclarativePolylineMapItem::line()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#line

    Returns
    -------

    Optional[QDeclarativeMapLineProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeMapLineProperties *QDeclarativePolylineMapItem::line()
    address = self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem4lineEv',
    )
    from . import QDeclarativeMapLineProperties
    return QDeclarativeMapLineProperties._cuteAt(address)

  def pathChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::pathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#pathChanged
    """
    #  void QDeclarativePolylineMapItem::pathChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem11pathChangedEv',
    )

  def updateAfterLinePropertiesChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolylineMapItem::updateAfterLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html
    """
    #  void QDeclarativePolylineMapItem::updateAfterLinePropertiesChanged()
    self.uglySide.call(
        'ritual_ZN27QDeclarativePolylineMapItem32updateAfterLinePropertiesC'
        'hangedEv',
    )

  @overload(QGeoMapViewportChangeEvent)
  def afterViewportChanged(self, event: QGeoMapViewportChangeEvent) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::afterViewportChanged(const
    QGeoMapViewportChangeEvent &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html

    Parameters
    ----------

    event : QGeoMapViewportChangeEvent
      Passed on as a value: Qt reads the C++ QGeoMapViewportChangeEvent,
      which stays Python's own.
    """
    #  void QDeclarativePolylineMapItem::afterViewportChanged(const
    #      QGeoMapViewportChangeEvent &event)
    ritual = (
        'ritual_ZN27QDeclarativePolylineMapItem20afterViewportChangedERK26Q'
        'GeoMapViewportChangeEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativePolylineMapItem20afterViewportChanged'
          'ERK26QGeoMapViewportChangeEvent')
    self.uglySide.call(ritual, self._valueOf(event))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDeclarativePolylineMapItem::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN27QDeclarativePolylineMapItem14geometryChangeERK6QRectFS2'
        '_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QDeclarativePolylineMapItem14geometryChangeERK6QR'
          'ectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolylineMapItem::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolylinemapitem.html#updatePolish
    """
    #  void QDeclarativePolylineMapItem::updatePolish()
    ritual = 'ritual_ZN27QDeclarativePolylineMapItem12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QDeclarativePolylineMapItem12updatePolishEv'
    self.uglySide.call(ritual)
