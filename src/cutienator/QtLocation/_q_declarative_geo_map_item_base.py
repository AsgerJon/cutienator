"""
QDeclarativeGeoMapItemBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitembase_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoMapItemBase to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem
from . import QLocation, QGeoMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF
  from ..QtPositioning import QGeoCoordinate, QGeoShape
  from ..QtQuick import QSGNode
  from . import QDeclarativeGeoMap, QGeoCameraData
  from . import QGeoMapViewportChangeEvent
  from ..QtQuickShapes import QQuickShape
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoMapViewportChangeEvent = WAIT['QGeoMapViewportChangeEvent']
  QGeoShape = WAIT['QGeoShape']
  QPointF = WAIT['QPointF']
  QQuickShape = WAIT['QQuickShape']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMapItemBase(QQuickItem):
  """
  The cute side of Qt's QDeclarativeGeoMapItemBase: a plain Python object
  standing in front of one C++ QDeclarativeGeoMapItemBase.

  It is built on the cute 'QQuickItem', as Qt's QDeclarativeGeoMapItemBase is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMapItemBase that has a ritual and
  that Python can call so far, 32 names in all: 'metaObject', 'tr', 'setMap',
  'setPositionOnMap', 'quickMap', 'map', 'geoShape', 'setGeoShape',
  'autoFadeIn', 'setAutoFadeIn', 'referenceSurface', 'setReferenceSurface',
  'lodThreshold', 'setLodThreshold', 'zoomForLOD', 'updatePaintNode',
  'updateMapItemPaintNode', 'itemType', 'mapItemOpacity',
  'setShapeTriangulationScale', 'mapItemOpacityChanged',
  'addTransitionFinished', 'removeTransitionFinished',
  'referenceSurfaceChanged', 'lodThresholdChanged', 'afterChildrenChanged',
  'afterViewportChanged', 'polishAndUpdate', 'zoomLevelOpacity',
  'isPolishScheduled', 'baseCameraDataChanged', 'visibleAreaChanged'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoMapItemBase::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoMapItemBase::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QDeclarativeGeoMapItemBase::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoMapItemBase::~QDeclarativeGeoMapItemBase()': the
    destructor: Python never removes a C++ QDeclarativeGeoMapItemBase.
  - Qt's 'void
    QDeclarativeGeoMapItemBase::setParentGroup(QDeclarativeGeoMapItemGroup
    &parentGroup)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 41 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMapItemBase is created at the first use, not by
    'QDeclarativeGeoMapItemBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMapItemBase.
  - Qt tells when it has removed the C++ QDeclarativeGeoMapItemBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoMapItemBase that has no cute function
    yet, 'quickChildren', 'setParentGroup', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QDeclarativeGeoMapItemBase::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#tr

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
    #  QString QDeclarativeGeoMapItemBase::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMapItemBase'

  #  A C++ QDeclarativeGeoMapItemBase Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMapItemBase'

  #  The functions Qt calls itself that QDeclarativeGeoMapItemBase is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setMap': (
          ('_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMapP7Q'
           'GeoMap',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtLocation:QDeclarativeGeoMap'),
               ('address', 'address', 'QtLocation:QGeoMap'),
           )),
      ),
      'setPositionOnMap': (
          ('_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCoord'
           'inateRK7QPointF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'geoShape': (
          ('_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv',
           ('address', 'value', 'QtPositioning:QGeoShape'),
           ()),
      ),
      'setGeoShape': (
          ('_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoShape'),
           )),
      ),
      'updateMapItemPaintNode': (
          ('_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QSGNo'
           'dePN10QQuickItem19UpdatePaintNodeDataE',
           ('address', 'address', 'QtQuick:QSGNode'),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address',
                'QtQuick:QQuickItem.UpdatePaintNodeData'),
           )),
      ),
      'afterChildrenChanged': (
          ('_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'afterViewportChanged': (
          ('_ZN26QDeclarativeGeoMapItemBase20afterViewportChangedERK26QGeoM'
           'apViewportChangeEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoMapViewportChangeEvent'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoMapItemBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoMapItemBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def quickMap(self) -> Optional[QDeclarativeGeoMap]:
    """
    Calls Qt's 'QDeclarativeGeoMap *QDeclarativeGeoMapItemBase::quickMap()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#quickMap

    Returns
    -------

    Optional[QDeclarativeGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoMap *QDeclarativeGeoMapItemBase::quickMap() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase8quickMapEv',
    )
    from . import QDeclarativeGeoMap
    return QDeclarativeGeoMap._cuteAt(address)

  def map(self) -> Optional[QGeoMap]:
    """
    Calls Qt's 'QGeoMap *QDeclarativeGeoMapItemBase::map() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#map

    Returns
    -------

    Optional[QGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMap *QDeclarativeGeoMapItemBase::map() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase3mapEv',
    )
    return QGeoMap._cuteAt(address)

  def geoShape(self) -> QGeoShape:
    """
    Calls Qt's 'const QGeoShape &QDeclarativeGeoMapItemBase::geoShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#geoShape

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  const QGeoShape &QDeclarativeGeoMapItemBase::geoShape() const
    address = self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase8geoShapeEv',
    )
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def autoFadeIn(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMapItemBase::autoFadeIn() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#autoFadeIn
    """
    #  bool QDeclarativeGeoMapItemBase::autoFadeIn() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase10autoFadeInEv',
    )

  def referenceSurface(self) -> QLocation.ReferenceSurface:
    """
    Calls Qt's 'QLocation::ReferenceSurface
    QDeclarativeGeoMapItemBase::referenceSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#referenceSurface

    Returns
    -------

    QLocation.ReferenceSurface
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocation.ReferenceSurface(number)' gives.
    """
    #  QLocation::ReferenceSurface
    #      QDeclarativeGeoMapItemBase::referenceSurface() const
    return QLocation.ReferenceSurface(self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase16referenceSurfaceEv',
    ))

  def lodThreshold(self) -> int:
    """
    Calls Qt's 'int QDeclarativeGeoMapItemBase::lodThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#lodThreshold
    """
    #  int QDeclarativeGeoMapItemBase::lodThreshold() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase12lodThresholdEv',
    )

  @overload(int)
  def zoomForLOD(self, zoom: int) -> int:
    """
    Calls Qt's 'unsigned int QDeclarativeGeoMapItemBase::zoomForLOD(int zoom)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#zoomForLOD

    Parameters
    ----------

    zoom : int
      Passed on as it is.
    """
    #  unsigned int QDeclarativeGeoMapItemBase::zoomForLOD(int zoom) const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase10zoomForLODEi', zoom,
    )

  def itemType(self) -> QGeoMap.ItemType:
    """
    Calls Qt's 'QGeoMap::ItemType QDeclarativeGeoMapItemBase::itemType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#itemType

    Returns
    -------

    QGeoMap.ItemType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QGeoMap.ItemType(number)'
      gives.
    """
    #  QGeoMap::ItemType QDeclarativeGeoMapItemBase::itemType() const
    return QGeoMap.ItemType(self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase8itemTypeEv',
    ))

  def mapItemOpacity(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMapItemBase::mapItemOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#mapItemOpacity
    """
    #  qreal QDeclarativeGeoMapItemBase::mapItemOpacity() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase14mapItemOpacityEv',
    )

  def zoomLevelOpacity(self) -> float:
    """
    Calls Qt's 'float QDeclarativeGeoMapItemBase::zoomLevelOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#zoomLevelOpacity
    """
    #  float QDeclarativeGeoMapItemBase::zoomLevelOpacity() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase16zoomLevelOpacityEv',
    )

  def isPolishScheduled(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMapItemBase::isPolishScheduled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#isPolishScheduled
    """
    #  bool QDeclarativeGeoMapItemBase::isPolishScheduled() const
    return self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase17isPolishScheduledEv',
    )

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
    Calls Qt's 'void QDeclarativeGeoMapItemBase::setMap(QDeclarativeGeoMap
    *quickMap, QGeoMap *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#setMap

    Parameters
    ----------

    quickMap : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    map : Optional[QGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMapItemBase::setMap(QDeclarativeGeoMap *quickMap,
    #      QGeoMap *map)
    ritual = (
        'ritual_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarativeGeoMap'
        'P7QGeoMap')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativeGeoMapItemBase6setMapEP18QDeclarative'
          'GeoMapP7QGeoMap')
    self.uglySide.call(
        ritual, self._addressOf(quickMap), self._addressOf(map),
    )

  @overload(QGeoCoordinate, QPointF)
  def setPositionOnMap(
      self,
      coordinate: QGeoCoordinate,
      offset: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::setPositionOnMap(const
    QGeoCoordinate &coordinate, const QPointF &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#setPositionOnMap

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapItemBase::setPositionOnMap(const QGeoCoordinate
    #      &coordinate, const QPointF &offset)
    ritual = (
        'ritual_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14QGeoCo'
        'ordinateRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativeGeoMapItemBase16setPositionOnMapERK14'
          'QGeoCoordinateRK7QPointF')
    self.uglySide.call(
        ritual, self._valueOf(coordinate), self._valueOf(offset, 'QPointF'),
    )

  @overload(QGeoShape)
  def setGeoShape(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::setGeoShape(const QGeoShape
    &shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#setGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMapItemBase::setGeoShape(const QGeoShape &shape)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase11setGeoShapeERK9QGeoShape',
        self._valueOf(shape),
    )

  @overload(bool)
  def setAutoFadeIn(self, fadeIn: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::setAutoFadeIn(bool fadeIn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#setAutoFadeIn

    Parameters
    ----------

    fadeIn : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemBase::setAutoFadeIn(bool fadeIn)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase13setAutoFadeInEb', fadeIn,
    )

  @overload(QLocation.ReferenceSurface)
  def setReferenceSurface(
      self,
      referenceSurface: QLocation.ReferenceSurface,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemBase::setReferenceSurface(QLocation::
    ReferenceSurface referenceSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html

    Parameters
    ----------

    referenceSurface : QLocation.ReferenceSurface
      Passed on as its number.
    """
    #  void QDeclarativeGeoMapItemBase::setReferenceSurface(QLocation::
    #      ReferenceSurface referenceSurface)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase19setReferenceSurfaceEN9QLoca'
        'tion16ReferenceSurfaceE',
        referenceSurface.value,
    )

  @overload(int)
  def setLodThreshold(self, lt: int) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::setLodThreshold(int lt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#setLodThreshold

    Parameters
    ----------

    lt : int
      Passed on as it is.
    """
    #  void QDeclarativeGeoMapItemBase::setLodThreshold(int lt)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase15setLodThresholdEi', lt,
    )

  @overload(QQuickShape, float)
  @overload(NoneType, float)
  def setShapeTriangulationScale(
      self,
      shape: Optional[QQuickShape],
      maxCoord: float,
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMapItemBase::setShapeTriangulationScale(QQuickShape
    *shape, qreal maxCoord) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html

    Parameters
    ----------

    shape : Optional[QQuickShape]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    maxCoord : float
      Passed on as it is.
    """
    #  void
    #      QDeclarativeGeoMapItemBase::setShapeTriangulationScale(QQuickShape
    #      *shape, qreal maxCoord) const
    self.uglySide.call(
        'ritual_ZNK26QDeclarativeGeoMapItemBase26setShapeTriangulationScale'
        'EP11QQuickShaped',
        self._addressOf(shape), maxCoord,
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
    'QDeclarativeGeoMapItemBase::QDeclarativeGeoMapItemBase(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoMapItemBase::QDeclarativeGeoMapItemBase(QQuickItem
    #      *parent)
    self._noteCreation(QDeclarativeGeoMapItemBase, lambda: Rituals.call(
        'ritual_ZN26QDeclarativeGeoMapItemBaseC1EP10QQuickItem',
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
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode
    *a0, UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#updatePaintNode

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
    #  QSGNode *QDeclarativeGeoMapItemBase::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN26QDeclarativeGeoMapItemBase15updatePaintNodeEP7QSGNodePN'
        '10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativeGeoMapItemBase15updatePaintNodeEP7QSG'
          'NodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

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
    *QDeclarativeGeoMapItemBase::updateMapItemPaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html

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
    #  QSGNode *QDeclarativeGeoMapItemBase::updateMapItemPaintNode(QSGNode
    #      *a0, UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNodeEP7QS'
        'GNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativeGeoMapItemBase22updateMapItemPaintNod'
          'eEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def mapItemOpacityChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::mapItemOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html
    """
    #  void QDeclarativeGeoMapItemBase::mapItemOpacityChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase21mapItemOpacityChangedEv',
    )

  def addTransitionFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::addTransitionFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html
    """
    #  void QDeclarativeGeoMapItemBase::addTransitionFinished()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase21addTransitionFinishedEv',
    )

  def removeTransitionFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::removeTransitionFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html
    """
    #  void QDeclarativeGeoMapItemBase::removeTransitionFinished()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase24removeTransitionFinishedEv',
    )

  def referenceSurfaceChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::referenceSurfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html
    """
    #  void QDeclarativeGeoMapItemBase::referenceSurfaceChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase23referenceSurfaceChangedEv',
    )

  def lodThresholdChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::lodThresholdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html
    """
    #  void QDeclarativeGeoMapItemBase::lodThresholdChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase19lodThresholdChangedEv',
    )

  def afterChildrenChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::afterChildrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html
    """
    #  void QDeclarativeGeoMapItemBase::afterChildrenChanged()
    ritual = 'ritual_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QDeclarativeGeoMapItemBase20afterChildrenChangedE'
          'v')
    self.uglySide.call(ritual)

  @overload(QGeoMapViewportChangeEvent)
  def afterViewportChanged(self, event: QGeoMapViewportChangeEvent) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::afterViewportChanged(const
    QGeoMapViewportChangeEvent &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html

    Parameters
    ----------

    event : QGeoMapViewportChangeEvent
      Passed on as a value: Qt reads the C++ QGeoMapViewportChangeEvent,
      which stays Python's own.
    """
    #  void QDeclarativeGeoMapItemBase::afterViewportChanged(const
    #      QGeoMapViewportChangeEvent &event)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase20afterViewportChangedERK26QG'
        'eoMapViewportChangeEvent',
        self._valueOf(event),
    )

  def polishAndUpdate(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::polishAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#polishAndUpdate
    """
    #  void QDeclarativeGeoMapItemBase::polishAndUpdate()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase15polishAndUpdateEv',
    )

  @overload(QGeoCameraData)
  def baseCameraDataChanged(self, camera: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::baseCameraDataChanged(const
    QGeoCameraData &camera)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html

    Parameters
    ----------

    camera : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMapItemBase::baseCameraDataChanged(const
    #      QGeoCameraData &camera)
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase21baseCameraDataChangedERK14Q'
        'GeoCameraData',
        self._valueOf(camera),
    )

  def visibleAreaChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMapItemBase::visibleAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomapitembase.html#visibleAreaChanged
    """
    #  void QDeclarativeGeoMapItemBase::visibleAreaChanged()
    self.uglySide.call(
        'ritual_ZN26QDeclarativeGeoMapItemBase18visibleAreaChangedEv',
    )

  @staticmethod
  def quickChildren(*__, **_) -> Never:
    """
    Qt's 'QDeclarativeGeoMapItemBase::quickChildren': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoMapItemBase.quickChildren' has no cute function "
        "yet. Qt's 'QDeclarativeGeoMapItemBase::quickChildren': a template: "
        "a pattern and no single function.")

  @staticmethod
  def setParentGroup(*__, **_) -> Never:
    """
    Qt's 'void
    QDeclarativeGeoMapItemBase::setParentGroup(QDeclarativeGeoMapItemGroup
    &parentGroup)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoMapItemBase.setParentGroup' has no cute function "
        "yet. Qt's 'void "
        "QDeclarativeGeoMapItemBase::setParentGroup(QDeclarativeGeoMapItemGr"
        "oup &parentGroup)': takes a type Python has no way to hand over "
        "yet.")
