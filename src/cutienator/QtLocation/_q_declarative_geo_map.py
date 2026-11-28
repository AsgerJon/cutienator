"""
QDeclarativeGeoMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomap_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDeclarativeGeoMap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQuick import QQuickItem
from . import QGeoServiceProvider

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMargins, QMetaObject, QPointF, QRectF, QVariant
  from ..QtGui import QColor, QImage
  from ..QtPositioning import QGeoCoordinate, QGeoShape
  from ..QtQuick import QSGNode
  from . import QDeclarativeGeoMapItemBase, QDeclarativeGeoMapItemGroup
  from . import QDeclarativeGeoMapItemView, QDeclarativeGeoServiceProvider
  from . import QGeoCameraCapabilities, QGeoCameraData, QGeoMap, QGeoMapType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QDeclarativeGeoMapItemBase = WAIT['QDeclarativeGeoMapItemBase']
  QDeclarativeGeoMapItemGroup = WAIT['QDeclarativeGeoMapItemGroup']
  QDeclarativeGeoMapItemView = WAIT['QDeclarativeGeoMapItemView']
  QDeclarativeGeoServiceProvider = WAIT['QDeclarativeGeoServiceProvider']
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoMapType = WAIT['QGeoMapType']
  QGeoShape = WAIT['QGeoShape']
  QImage = WAIT['QImage']
  QMargins = WAIT['QMargins']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoMap(QQuickItem):
  """
  The cute side of Qt's QDeclarativeGeoMap: a plain Python object standing in
  front of one C++ QDeclarativeGeoMap.

  It is built on the cute 'QQuickItem', as Qt's QDeclarativeGeoMap is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoMap that has a ritual and that Python
  can call so far, 110 names in all: 'metaObject', 'tr', 'setPlugin',
  'plugin', 'setActiveMapType', 'activeMapType', 'setMinimumZoomLevel',
  'minimumZoomLevel', 'setMaximumZoomLevel', 'maximumZoomLevel',
  'setZoomLevel', 'zoomLevel', 'setBearing', 'bearing', 'setTilt', 'tilt',
  'setMinimumTilt', 'minimumTilt', 'setMaximumTilt', 'maximumTilt',
  'setFieldOfView', 'fieldOfView', 'setMinimumFieldOfView',
  'minimumFieldOfView', 'setMaximumFieldOfView', 'maximumFieldOfView',
  'setCenter', 'center', 'setVisibleRegion', 'visibleRegion',
  'setCopyrightsVisible', 'copyrightsVisible', 'setColor', 'color',
  'visibleArea', 'setVisibleArea', 'mapReady', 'supportedMapTypes',
  'alignCoordinateToPoint', 'removeMapItem', 'addMapItem', 'addMapItemGroup',
  'removeMapItemGroup', 'removeMapItemView', 'addMapItemView',
  'clearMapItems', 'mapItems', 'toCoordinate', 'fromCoordinate',
  'fitViewportToMapItems', 'fitViewportToVisibleMapItems', 'pan',
  'prefetchData', 'clearData', 'fitViewportToGeoShape', 'errorString',
  'error', 'map', 'itemChange', 'pluginChanged', 'zoomLevelChanged',
  'centerChanged', 'activeMapTypeChanged', 'supportedMapTypesChanged',
  'minimumZoomLevelChanged', 'maximumZoomLevelChanged', 'mapItemsChanged',
  'errorChanged', 'copyrightLinkActivated', 'copyrightsVisibleChanged',
  'colorChanged', 'bearingChanged', 'tiltChanged', 'fieldOfViewChanged',
  'minimumTiltChanged', 'maximumTiltChanged', 'minimumFieldOfViewChanged',
  'maximumFieldOfViewChanged', 'copyrightsImageChanged', 'copyrightsChanged',
  'mapReadyChanged', 'visibleAreaChanged', 'visibleRegionChanged',
  'componentComplete', 'updatePaintNode', 'geometryChange', 'setError',
  'initialize', 'addMapChild', 'removeMapChild', 'isGroupNested',
  'addMapItem_real', 'removeMapItem_real', 'addMapItemGroup_real',
  'removeMapItemGroup_real', 'addMapItemView_real', 'removeMapItemView_real',
  'updateItemToWindowTransform', 'onSGNodeChanged',
  'mappingManagerInitialized', 'pluginReady', 'onSupportedMapTypesChanged',
  'onCameraCapabilitiesChanged',
  'onAttachedCopyrightNoticeVisibilityChanged', 'onCameraDataChanged',
  'setupMapView', 'populateMap', 'attachCopyrightNotice',
  'detachCopyrightNotice', 'mapMargins'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoMap::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDeclarativeGeoMap::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoMap::~QDeclarativeGeoMap()': the destructor: Python
    never removes a C++ QDeclarativeGeoMap.
  - Qt's 'void QDeclarativeGeoMap::fitViewportToMapItemsRefine(const
    QList<QPointer<QDeclarativeGeoMapItemBase>> &mapItems, bool refine, bool
    onlyVisible)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 122 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDeclarativeGeoMap is created at the first use, not by
    'QDeclarativeGeoMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoMap.
  - Qt tells when it has removed the C++ QDeclarativeGeoMap. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativeGeoMap that has no cute function yet,
    'fitViewportToMapItemsRefine', holds a function that raises
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
    Calls Qt's 'QString QDeclarativeGeoMap::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#tr

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
    #  QString QDeclarativeGeoMap::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QDeclarativeGeoMap2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoMap'

  #  A C++ QDeclarativeGeoMap Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoMap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoMap::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoMap::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def plugin(self) -> Optional[QDeclarativeGeoServiceProvider]:
    """
    Calls Qt's 'QDeclarativeGeoServiceProvider *QDeclarativeGeoMap::plugin()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#plugin

    Returns
    -------

    Optional[QDeclarativeGeoServiceProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativeGeoServiceProvider *QDeclarativeGeoMap::plugin() const
    address = self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap6pluginEv')
    from . import QDeclarativeGeoServiceProvider
    return QDeclarativeGeoServiceProvider._cuteAt(address)

  def activeMapType(self) -> QGeoMapType:
    """
    Calls Qt's 'QGeoMapType QDeclarativeGeoMap::activeMapType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#activeMapType

    Returns
    -------

    QGeoMapType
      A new cute QGeoMapType around the copy Qt gave back. Python owns it.
    """
    #  QGeoMapType QDeclarativeGeoMap::activeMapType() const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap13activeMapTypeEv',
    )
    from . import QGeoMapType
    return QGeoMapType._cuteOwning(address)

  def minimumZoomLevel(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::minimumZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#minimumZoomLevel
    """
    #  qreal QDeclarativeGeoMap::minimumZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap16minimumZoomLevelEv',
    )

  def maximumZoomLevel(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::maximumZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#maximumZoomLevel
    """
    #  qreal QDeclarativeGeoMap::maximumZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap16maximumZoomLevelEv',
    )

  def zoomLevel(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::zoomLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#zoomLevel
    """
    #  qreal QDeclarativeGeoMap::zoomLevel() const
    return self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap9zoomLevelEv')

  def bearing(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::bearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#bearing
    """
    #  qreal QDeclarativeGeoMap::bearing() const
    return self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap7bearingEv')

  def tilt(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::tilt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#tilt
    """
    #  qreal QDeclarativeGeoMap::tilt() const
    return self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap4tiltEv')

  def minimumTilt(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::minimumTilt() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#minimumTilt
    """
    #  qreal QDeclarativeGeoMap::minimumTilt() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap11minimumTiltEv',
    )

  def maximumTilt(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::maximumTilt() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#maximumTilt
    """
    #  qreal QDeclarativeGeoMap::maximumTilt() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap11maximumTiltEv',
    )

  def fieldOfView(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::fieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#fieldOfView
    """
    #  qreal QDeclarativeGeoMap::fieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap11fieldOfViewEv',
    )

  def minimumFieldOfView(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::minimumFieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#minimumFieldOfView
    """
    #  qreal QDeclarativeGeoMap::minimumFieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap18minimumFieldOfViewEv',
    )

  def maximumFieldOfView(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativeGeoMap::maximumFieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#maximumFieldOfView
    """
    #  qreal QDeclarativeGeoMap::maximumFieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap18maximumFieldOfViewEv',
    )

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativeGeoMap::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativeGeoMap::center() const
    address = self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap6centerEv')
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def visibleRegion(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QDeclarativeGeoMap::visibleRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#visibleRegion

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QDeclarativeGeoMap::visibleRegion() const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap13visibleRegionEv',
    )
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def copyrightsVisible(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMap::copyrightsVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#copyrightsVisible
    """
    #  bool QDeclarativeGeoMap::copyrightsVisible() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap17copyrightsVisibleEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QDeclarativeGeoMap::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QDeclarativeGeoMap::color() const
    address = self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def visibleArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF QDeclarativeGeoMap::visibleArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#visibleArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QDeclarativeGeoMap::visibleArea() const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap11visibleAreaEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def mapReady(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMap::mapReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#mapReady
    """
    #  bool QDeclarativeGeoMap::mapReady() const
    return self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap8mapReadyEv')

  @overload(QPointF)
  @overload(QPointF, bool)
  def toCoordinate(
      self,
      position: QPointF,
      clipToViewPort: bool = True,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativeGeoMap::toCoordinate(const QPointF
    &position, bool clipToViewPort) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#toCoordinate

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    clipToViewPort : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativeGeoMap::toCoordinate(const QPointF
    #      &position, bool clipToViewPort) const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap12toCoordinateERK7QPointFb',
        self._valueOf(position, 'QPointF'), clipToViewPort,
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate)
  @overload(QGeoCoordinate, bool)
  def fromCoordinate(
      self,
      coordinate: QGeoCoordinate,
      clipToViewPort: bool = True,
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QDeclarativeGeoMap::fromCoordinate(const
    QGeoCoordinate &coordinate, bool clipToViewPort) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#fromCoordinate

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    clipToViewPort : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QDeclarativeGeoMap::fromCoordinate(const QGeoCoordinate
    #      &coordinate, bool clipToViewPort) const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap14fromCoordinateERK14QGeoCoordinateb',
        self._valueOf(coordinate), clipToViewPort,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoMap::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoMap::errorString() const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap11errorStringEv',
    )

  def error(self) -> QGeoServiceProvider.Error:
    """
    Calls Qt's 'QGeoServiceProvider::Error QDeclarativeGeoMap::error()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#error

    Returns
    -------

    QGeoServiceProvider.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoServiceProvider.Error(number)' gives.
    """
    #  QGeoServiceProvider::Error QDeclarativeGeoMap::error() const
    return QGeoServiceProvider.Error(self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap5errorEv',
    ))

  def map(self) -> Optional[QGeoMap]:
    """
    Calls Qt's 'QGeoMap *QDeclarativeGeoMap::map() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#map

    Returns
    -------

    Optional[QGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMap *QDeclarativeGeoMap::map() const
    address = self.uglySide.call('ritual_ZNK18QDeclarativeGeoMap3mapEv')
    from . import QGeoMap
    return QGeoMap._cuteAt(address)

  @overload(QDeclarativeGeoMapItemGroup)
  @overload(NoneType)
  def isGroupNested(
      self,
      group: Optional[QDeclarativeGeoMapItemGroup],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::isGroupNested(QDeclarativeGeoMapItemGroup *group)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#isGroupNested

    Parameters
    ----------

    group : Optional[QDeclarativeGeoMapItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::isGroupNested(QDeclarativeGeoMapItemGroup
    #      *group) const
    return self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap13isGroupNestedEP27QDeclarativeGeoMa'
        'pItemGroup',
        self._addressOf(group),
    )

  def mapMargins(self) -> QMargins:
    """
    Calls Qt's 'QMargins QDeclarativeGeoMap::mapMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#mapMargins

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QDeclarativeGeoMap::mapMargins() const
    address = self.uglySide.call(
        'ritual_ZNK18QDeclarativeGeoMap10mapMarginsEv',
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def setPlugin(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::setPlugin(QDeclarativeGeoServiceProvider *plugin)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setPlugin

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::setPlugin(QDeclarativeGeoServiceProvider
    #      *plugin)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap9setPluginEP30QDeclarativeGeoServiceP'
        'rovider',
        self._addressOf(plugin),
    )

  @overload(QGeoMapType)
  def setActiveMapType(self, mapType: QGeoMapType) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setActiveMapType(const QGeoMapType
    &mapType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setActiveMapType

    Parameters
    ----------

    mapType : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMap::setActiveMapType(const QGeoMapType &mapType)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap16setActiveMapTypeERK11QGeoMapType',
        self._valueOf(mapType),
    )

  @overload(float)
  @overload(float, bool)
  def setMinimumZoomLevel(
      self,
      minimumZoomLevel: float,
      userSet: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setMinimumZoomLevel(qreal
    minimumZoomLevel, bool userSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setMinimumZoomLevel

    Parameters
    ----------

    minimumZoomLevel : float
      Passed on as it is.

    userSet : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMap::setMinimumZoomLevel(qreal minimumZoomLevel,
    #      bool userSet)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap19setMinimumZoomLevelEdb',
        minimumZoomLevel, userSet,
    )

  @overload(float)
  @overload(float, bool)
  def setMaximumZoomLevel(
      self,
      maximumZoomLevel: float,
      userSet: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setMaximumZoomLevel(qreal
    maximumZoomLevel, bool userSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setMaximumZoomLevel

    Parameters
    ----------

    maximumZoomLevel : float
      Passed on as it is.

    userSet : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMap::setMaximumZoomLevel(qreal maximumZoomLevel,
    #      bool userSet)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap19setMaximumZoomLevelEdb',
        maximumZoomLevel, userSet,
    )

  @overload(float)
  def setZoomLevel(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setZoomLevel(qreal zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::setZoomLevel(qreal zoomLevel)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap12setZoomLevelEd', zoomLevel,
    )

  @overload(float, bool)
  def setZoomLevel(self, zoomLevel: float, overzoom: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setZoomLevel(qreal zoomLevel, bool
    overzoom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.

    overzoom : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::setZoomLevel(qreal zoomLevel, bool overzoom)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap12setZoomLevelEdb',
        zoomLevel, overzoom,
    )

  @overload(float)
  def setBearing(self, bearing: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setBearing(qreal bearing)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setBearing

    Parameters
    ----------

    bearing : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::setBearing(qreal bearing)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap10setBearingEd', bearing,
    )

  @overload(float, QGeoCoordinate)
  def setBearing(self, bearing: float, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setBearing(qreal bearing, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setBearing

    Parameters
    ----------

    bearing : float
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMap::setBearing(qreal bearing, const
    #      QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap10setBearingEdRK14QGeoCoordinate',
        bearing, self._valueOf(coordinate),
    )

  @overload(float)
  def setTilt(self, tilt: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setTilt(qreal tilt)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setTilt

    Parameters
    ----------

    tilt : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::setTilt(qreal tilt)
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap7setTiltEd', tilt)

  @overload(float)
  @overload(float, bool)
  def setMinimumTilt(self, minimumTilt: float, userSet: bool = True) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setMinimumTilt(qreal minimumTilt,
    bool userSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setMinimumTilt

    Parameters
    ----------

    minimumTilt : float
      Passed on as it is.

    userSet : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMap::setMinimumTilt(qreal minimumTilt, bool
    #      userSet)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14setMinimumTiltEdb',
        minimumTilt, userSet,
    )

  @overload(float)
  @overload(float, bool)
  def setMaximumTilt(self, maximumTilt: float, userSet: bool = True) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setMaximumTilt(qreal maximumTilt,
    bool userSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setMaximumTilt

    Parameters
    ----------

    maximumTilt : float
      Passed on as it is.

    userSet : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMap::setMaximumTilt(qreal maximumTilt, bool
    #      userSet)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14setMaximumTiltEdb',
        maximumTilt, userSet,
    )

  @overload(float)
  def setFieldOfView(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setFieldOfView(qreal fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setFieldOfView

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::setFieldOfView(qreal fieldOfView)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14setFieldOfViewEd', fieldOfView,
    )

  @overload(float)
  @overload(float, bool)
  def setMinimumFieldOfView(
      self,
      minimumFieldOfView: float,
      userSet: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setMinimumFieldOfView(qreal
    minimumFieldOfView, bool userSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setMinimumFieldOfView

    Parameters
    ----------

    minimumFieldOfView : float
      Passed on as it is.

    userSet : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMap::setMinimumFieldOfView(qreal
    #      minimumFieldOfView, bool userSet)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21setMinimumFieldOfViewEdb',
        minimumFieldOfView, userSet,
    )

  @overload(float)
  @overload(float, bool)
  def setMaximumFieldOfView(
      self,
      maximumFieldOfView: float,
      userSet: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setMaximumFieldOfView(qreal
    maximumFieldOfView, bool userSet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setMaximumFieldOfView

    Parameters
    ----------

    maximumFieldOfView : float
      Passed on as it is.

    userSet : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QDeclarativeGeoMap::setMaximumFieldOfView(qreal
    #      maximumFieldOfView, bool userSet)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21setMaximumFieldOfViewEdb',
        maximumFieldOfView, userSet,
    )

  @overload(QGeoCoordinate)
  def setCenter(self, center: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setCenter(const QGeoCoordinate
    &center)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setCenter

    Parameters
    ----------

    center : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMap::setCenter(const QGeoCoordinate &center)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap9setCenterERK14QGeoCoordinate',
        self._valueOf(center),
    )

  @overload(QGeoShape)
  def setVisibleRegion(self, shape: QGeoShape) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setVisibleRegion(const QGeoShape
    &shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setVisibleRegion

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::setVisibleRegion(const QGeoShape &shape)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap16setVisibleRegionERK9QGeoShape',
        self._valueOf(shape),
    )

  @overload(bool)
  def setCopyrightsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setCopyrightsVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setCopyrightsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::setCopyrightsVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap20setCopyrightsVisibleEb', visible,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::setVisibleArea(const QRectF &visibleArea)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14setVisibleAreaERK6QRectF',
        self._valueOf(visibleArea),
    )

  @overload(QGeoServiceProvider.Error, str)
  def setError(
      self,
      error: QGeoServiceProvider.Error,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::setError(QGeoServiceProvider::Error
    error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#setError

    Parameters
    ----------

    error : QGeoServiceProvider.Error
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMap::setError(QGeoServiceProvider::Error error,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap8setErrorEN19QGeoServiceProvider5Erro'
        'rERK7QString',
        error.value, errorString,
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
    'QDeclarativeGeoMap::QDeclarativeGeoMap(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#QDeclarativeGeoMap

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoMap::QDeclarativeGeoMap(QQuickItem *parent)
    self._noteCreation(QDeclarativeGeoMap, lambda: Rituals.call(
        'ritual_ZN18QDeclarativeGeoMapC1EP10QQuickItem',
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

  def supportedMapTypes(self) -> QList[QGeoMapType]:
    """
    Calls Qt's 'QList<QGeoMapType> QDeclarativeGeoMap::supportedMapTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#supportedMapTypes

    Returns
    -------

    QList[QGeoMapType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoMapType> QDeclarativeGeoMap::supportedMapTypes()
    address = self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap17supportedMapTypesEv',
    )
    from . import QGeoMapType
    return QList[QGeoMapType]._cuteOwning(address)

  @overload(QGeoCoordinate, QPointF)
  def alignCoordinateToPoint(
      self,
      coordinate: QGeoCoordinate,
      point: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::alignCoordinateToPoint(const
    QGeoCoordinate &coordinate, const QPointF &point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#alignCoordinateToPoint

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::alignCoordinateToPoint(const QGeoCoordinate
    #      &coordinate, const QPointF &point)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap22alignCoordinateToPointERK14QGeoCoor'
        'dinateRK7QPointF',
        self._valueOf(coordinate), self._valueOf(point, 'QPointF'),
    )

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def removeMapItem(
      self,
      item: Optional[QDeclarativeGeoMapItemBase],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::removeMapItem(QDeclarativeGeoMapItemBase *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapItem

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::removeMapItem(QDeclarativeGeoMapItemBase
    #      *item)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap13removeMapItemEP26QDeclarativeGeoMap'
        'ItemBase',
        self._addressOf(item),
    )

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def addMapItem(self, item: Optional[QDeclarativeGeoMapItemBase]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::addMapItem(QDeclarativeGeoMapItemBase *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapItem

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::addMapItem(QDeclarativeGeoMapItemBase *item)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap10addMapItemEP26QDeclarativeGeoMapIte'
        'mBase',
        self._addressOf(item),
    )

  @overload(QDeclarativeGeoMapItemGroup)
  @overload(NoneType)
  def addMapItemGroup(
      self,
      itemGroup: Optional[QDeclarativeGeoMapItemGroup],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::addMapItemGroup(QDeclarativeGeoMapItemGroup
    *itemGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapItemGroup

    Parameters
    ----------

    itemGroup : Optional[QDeclarativeGeoMapItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::addMapItemGroup(QDeclarativeGeoMapItemGroup
    #      *itemGroup)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap15addMapItemGroupEP27QDeclarativeGeoM'
        'apItemGroup',
        self._addressOf(itemGroup),
    )

  @overload(QDeclarativeGeoMapItemGroup)
  @overload(NoneType)
  def removeMapItemGroup(
      self,
      itemGroup: Optional[QDeclarativeGeoMapItemGroup],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::removeMapItemGroup(QDeclarativeGeoMapItemGroup
    *itemGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapItemGroup

    Parameters
    ----------

    itemGroup : Optional[QDeclarativeGeoMapItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QDeclarativeGeoMap::removeMapItemGroup(QDeclarativeGeoMapItemGroup
    #      *itemGroup)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap18removeMapItemGroupEP27QDeclarativeG'
        'eoMapItemGroup',
        self._addressOf(itemGroup),
    )

  @overload(QDeclarativeGeoMapItemView)
  @overload(NoneType)
  def removeMapItemView(
      self,
      itemView: Optional[QDeclarativeGeoMapItemView],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::removeMapItemView(QDeclarativeGeoMapItemView
    *itemView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapItemView

    Parameters
    ----------

    itemView : Optional[QDeclarativeGeoMapItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::removeMapItemView(QDeclarativeGeoMapItemView
    #      *itemView)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap17removeMapItemViewEP26QDeclarativeGe'
        'oMapItemView',
        self._addressOf(itemView),
    )

  @overload(QDeclarativeGeoMapItemView)
  @overload(NoneType)
  def addMapItemView(
      self,
      itemView: Optional[QDeclarativeGeoMapItemView],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::addMapItemView(QDeclarativeGeoMapItemView
    *itemView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapItemView

    Parameters
    ----------

    itemView : Optional[QDeclarativeGeoMapItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::addMapItemView(QDeclarativeGeoMapItemView
    #      *itemView)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14addMapItemViewEP26QDeclarativeGeoMa'
        'pItemView',
        self._addressOf(itemView),
    )

  def clearMapItems(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::clearMapItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#clearMapItems
    """
    #  void QDeclarativeGeoMap::clearMapItems()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap13clearMapItemsEv')

  def mapItems(self) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *> QDeclarativeGeoMap::mapItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#mapItems

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QDeclarativeGeoMap::mapItems()
    address = self.uglySide.call('ritual_ZN18QDeclarativeGeoMap8mapItemsEv')
    return QList[QObject]._cuteOwning(address)

  @overload(QList[QVariant])
  def fitViewportToMapItems(self, items: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::fitViewportToMapItems(const
    QVariantList &items)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#fitViewportToMapItems

    Parameters
    ----------

    items : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeGeoMap::fitViewportToMapItems(const QVariantList
    #      &items)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21fitViewportToMapItemsERK5QListI8QVa'
        'riantE',
        self._valueOf(items),
    )

  def fitViewportToVisibleMapItems(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::fitViewportToVisibleMapItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html
    """
    #  void QDeclarativeGeoMap::fitViewportToVisibleMapItems()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap28fitViewportToVisibleMapItemsEv',
    )

  @overload(int, int)
  def pan(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::pan(int dx, int dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#pan

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::pan(int dx, int dy)
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap3panEii', dx, dy)

  def prefetchData(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::prefetchData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#prefetchData
    """
    #  void QDeclarativeGeoMap::prefetchData()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap12prefetchDataEv')

  def clearData(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::clearData()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#clearData
    """
    #  void QDeclarativeGeoMap::clearData()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap9clearDataEv')

  @overload(QGeoShape, QVariant)
  def fitViewportToGeoShape(
      self,
      shape: QGeoShape,
      margins: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::fitViewportToGeoShape(const
    QGeoShape &shape, QVariant margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#fitViewportToGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    margins : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::fitViewportToGeoShape(const QGeoShape &shape,
    #      QVariant margins)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21fitViewportToGeoShapeERK9QGeoShape8'
        'QVariant',
        self._valueOf(shape), self._valueOf(margins),
    )

  @overload(QGeoShape)
  @overload(QGeoShape, QMargins)
  def fitViewportToGeoShape(
      self,
      shape: QGeoShape,
      borders: Optional[QMargins] = None,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::fitViewportToGeoShape(const
    QGeoShape &shape, const QMargins &borders)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#fitViewportToGeoShape

    Parameters
    ----------

    shape : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.

    borders : Optional[QMargins]
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own. May be left out, as in Qt: a new 'QMargins(10, 10, 10, 10)' is
      then passed on.
    """
    #  void QDeclarativeGeoMap::fitViewportToGeoShape(const QGeoShape &shape,
    #      const QMargins &borders)
    if borders is None:
      from ..QtCore import QMargins
      borders = QMargins(10, 10, 10, 10)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21fitViewportToGeoShapeERK9QGeoShapeR'
        'K8QMargins',
        self._valueOf(shape), self._valueOf(borders, 'QMargins'),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QDeclarativeGeoMap::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN18QDeclarativeGeoMap10itemChangeEN10QQuickItem10ItemChang'
        'eERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QDeclarativeGeoMap10itemChangeEN10QQuickItem10Ite'
          'mChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  @overload(QDeclarativeGeoServiceProvider)
  @overload(NoneType)
  def pluginChanged(
      self,
      plugin: Optional[QDeclarativeGeoServiceProvider],
  ) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::pluginChanged(QDeclarativeGeoServiceProvider
    *plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#pluginChanged

    Parameters
    ----------

    plugin : Optional[QDeclarativeGeoServiceProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::pluginChanged(QDeclarativeGeoServiceProvider
    #      *plugin)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap13pluginChangedEP30QDeclarativeGeoSer'
        'viceProvider',
        self._addressOf(plugin),
    )

  @overload(float)
  def zoomLevelChanged(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::zoomLevelChanged(qreal zoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#zoomLevelChanged

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::zoomLevelChanged(qreal zoomLevel)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap16zoomLevelChangedEd', zoomLevel,
    )

  @overload(QGeoCoordinate)
  def centerChanged(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::centerChanged(const QGeoCoordinate
    &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#centerChanged

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMap::centerChanged(const QGeoCoordinate
    #      &coordinate)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap13centerChangedERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  def activeMapTypeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::activeMapTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#activeMapTypeChanged
    """
    #  void QDeclarativeGeoMap::activeMapTypeChanged()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap20activeMapTypeChangedEv',
    )

  def supportedMapTypesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::supportedMapTypesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#supportedMapTypesChanged
    """
    #  void QDeclarativeGeoMap::supportedMapTypesChanged()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap24supportedMapTypesChangedEv',
    )

  @overload(float)
  def minimumZoomLevelChanged(self, minimumZoomLevel: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::minimumZoomLevelChanged(qreal
    minimumZoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#minimumZoomLevelChanged

    Parameters
    ----------

    minimumZoomLevel : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::minimumZoomLevelChanged(qreal
    #      minimumZoomLevel)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap23minimumZoomLevelChangedEd',
        minimumZoomLevel,
    )

  @overload(float)
  def maximumZoomLevelChanged(self, maximumZoomLevel: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::maximumZoomLevelChanged(qreal
    maximumZoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#maximumZoomLevelChanged

    Parameters
    ----------

    maximumZoomLevel : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::maximumZoomLevelChanged(qreal
    #      maximumZoomLevel)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap23maximumZoomLevelChangedEd',
        maximumZoomLevel,
    )

  def mapItemsChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::mapItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#mapItemsChanged
    """
    #  void QDeclarativeGeoMap::mapItemsChanged()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap15mapItemsChangedEv')

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::errorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#errorChanged
    """
    #  void QDeclarativeGeoMap::errorChanged()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap12errorChangedEv')

  @overload(str)
  def copyrightLinkActivated(self, link: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::copyrightLinkActivated(const QString
    &link)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#copyrightLinkActivated

    Parameters
    ----------

    link : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMap::copyrightLinkActivated(const QString &link)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap22copyrightLinkActivatedERK7QString',
        link,
    )

  @overload(bool)
  def copyrightsVisibleChanged(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::copyrightsVisibleChanged(bool
    visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#copyrightsVisibleChanged

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::copyrightsVisibleChanged(bool visible)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap24copyrightsVisibleChangedEb', visible,
    )

  @overload(QColor)
  def colorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::colorChanged(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#colorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::colorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap12colorChangedERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def bearingChanged(self, bearing: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::bearingChanged(qreal bearing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#bearingChanged

    Parameters
    ----------

    bearing : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::bearingChanged(qreal bearing)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14bearingChangedEd', bearing,
    )

  @overload(float)
  def tiltChanged(self, tilt: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::tiltChanged(qreal tilt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#tiltChanged

    Parameters
    ----------

    tilt : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::tiltChanged(qreal tilt)
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap11tiltChangedEd', tilt)

  @overload(float)
  def fieldOfViewChanged(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::fieldOfViewChanged(qreal
    fieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#fieldOfViewChanged

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::fieldOfViewChanged(qreal fieldOfView)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap18fieldOfViewChangedEd', fieldOfView,
    )

  @overload(float)
  def minimumTiltChanged(self, minimumTilt: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::minimumTiltChanged(qreal
    minimumTilt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#minimumTiltChanged

    Parameters
    ----------

    minimumTilt : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::minimumTiltChanged(qreal minimumTilt)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap18minimumTiltChangedEd', minimumTilt,
    )

  @overload(float)
  def maximumTiltChanged(self, maximumTilt: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::maximumTiltChanged(qreal
    maximumTilt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#maximumTiltChanged

    Parameters
    ----------

    maximumTilt : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::maximumTiltChanged(qreal maximumTilt)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap18maximumTiltChangedEd', maximumTilt,
    )

  @overload(float)
  def minimumFieldOfViewChanged(self, minimumFieldOfView: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::minimumFieldOfViewChanged(qreal
    minimumFieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#minimumFieldOfViewChanged

    Parameters
    ----------

    minimumFieldOfView : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::minimumFieldOfViewChanged(qreal
    #      minimumFieldOfView)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap25minimumFieldOfViewChangedEd',
        minimumFieldOfView,
    )

  @overload(float)
  def maximumFieldOfViewChanged(self, maximumFieldOfView: float) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::maximumFieldOfViewChanged(qreal
    maximumFieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#maximumFieldOfViewChanged

    Parameters
    ----------

    maximumFieldOfView : float
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::maximumFieldOfViewChanged(qreal
    #      maximumFieldOfView)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap25maximumFieldOfViewChangedEd',
        maximumFieldOfView,
    )

  @overload(QImage)
  def copyrightsImageChanged(self, copyrightsImage: QImage) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::copyrightsImageChanged(const QImage
    &copyrightsImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#copyrightsImageChanged

    Parameters
    ----------

    copyrightsImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::copyrightsImageChanged(const QImage
    #      &copyrightsImage)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap22copyrightsImageChangedERK6QImage',
        self._valueOf(copyrightsImage),
    )

  @overload(str)
  def copyrightsChanged(self, copyrightsHtml: str) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::copyrightsChanged(const QString
    &copyrightsHtml)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#copyrightsChanged

    Parameters
    ----------

    copyrightsHtml : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDeclarativeGeoMap::copyrightsChanged(const QString
    #      &copyrightsHtml)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap17copyrightsChangedERK7QString',
        copyrightsHtml,
    )

  @overload(bool)
  def mapReadyChanged(self, ready: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::mapReadyChanged(bool ready)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#mapReadyChanged

    Parameters
    ----------

    ready : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::mapReadyChanged(bool ready)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap15mapReadyChangedEb', ready,
    )

  def visibleAreaChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::visibleAreaChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#visibleAreaChanged
    """
    #  void QDeclarativeGeoMap::visibleAreaChanged()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap18visibleAreaChangedEv')

  def visibleRegionChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::visibleRegionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#visibleRegionChanged
    """
    #  void QDeclarativeGeoMap::visibleRegionChanged()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap20visibleRegionChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#componentComplete
    """
    #  void QDeclarativeGeoMap::componentComplete()
    ritual = 'ritual_ZN18QDeclarativeGeoMap17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QDeclarativeGeoMap17componentCompleteEv'
    self.uglySide.call(ritual)

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
    Calls Qt's 'QSGNode *QDeclarativeGeoMap::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#updatePaintNode

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
    #  QSGNode *QDeclarativeGeoMap::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN18QDeclarativeGeoMap15updatePaintNodeEP7QSGNodePN10QQuick'
        'Item19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QDeclarativeGeoMap15updatePaintNodeEP7QSGNodePN10'
          'QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QDeclarativeGeoMap::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN18QDeclarativeGeoMap14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QDeclarativeGeoMap14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeomap.html#initialize
    """
    #  void QDeclarativeGeoMap::initialize()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap10initializeEv')

  @overload(QObject)
  @overload(NoneType)
  def addMapChild(self, child: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMap::addMapChild(QObject *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapChild

    Parameters
    ----------

    child : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::addMapChild(QObject *child)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap11addMapChildEP7QObject',
        self._addressOf(child, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def removeMapChild(self, child: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoMap::removeMapChild(QObject *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapChild

    Parameters
    ----------

    child : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::removeMapChild(QObject *child)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap14removeMapChildEP7QObject',
        self._addressOf(child, 'QObject'),
    )

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def addMapItem_real(
      self,
      item: Optional[QDeclarativeGeoMapItemBase],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::addMapItem_real(QDeclarativeGeoMapItemBase *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapItem_real

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::addMapItem_real(QDeclarativeGeoMapItemBase
    #      *item)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap15addMapItem_realEP26QDeclarativeGeoM'
        'apItemBase',
        self._addressOf(item),
    )

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def removeMapItem_real(
      self,
      item: Optional[QDeclarativeGeoMapItemBase],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::removeMapItem_real(QDeclarativeGeoMapItemBase
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapItem_real

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::removeMapItem_real(QDeclarativeGeoMapItemBase
    #      *item)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap18removeMapItem_realEP26QDeclarativeG'
        'eoMapItemBase',
        self._addressOf(item),
    )

  @overload(QDeclarativeGeoMapItemGroup)
  @overload(NoneType)
  def addMapItemGroup_real(
      self,
      itemGroup: Optional[QDeclarativeGeoMapItemGroup],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::addMapItemGroup_real(QDeclarativeGeoMapItemGroup
    *itemGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapItemGroup_real

    Parameters
    ----------

    itemGroup : Optional[QDeclarativeGeoMapItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::addMapItemGroup_real(
    #      QDeclarativeGeoMapItemGroup *itemGroup)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap20addMapItemGroup_realEP27QDeclarativ'
        'eGeoMapItemGroup',
        self._addressOf(itemGroup),
    )

  @overload(QDeclarativeGeoMapItemGroup)
  @overload(NoneType)
  def removeMapItemGroup_real(
      self,
      itemGroup: Optional[QDeclarativeGeoMapItemGroup],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::removeMapItemGroup_real(QDeclarativeGeoMapItemGroup
    *itemGroup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapItemGroup_real

    Parameters
    ----------

    itemGroup : Optional[QDeclarativeGeoMapItemGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::removeMapItemGroup_real(
    #      QDeclarativeGeoMapItemGroup *itemGroup)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap23removeMapItemGroup_realEP27QDeclara'
        'tiveGeoMapItemGroup',
        self._addressOf(itemGroup),
    )

  @overload(QDeclarativeGeoMapItemView)
  @overload(NoneType)
  def addMapItemView_real(
      self,
      itemView: Optional[QDeclarativeGeoMapItemView],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::addMapItemView_real(QDeclarativeGeoMapItemView
    *itemView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#addMapItemView_real

    Parameters
    ----------

    itemView : Optional[QDeclarativeGeoMapItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      QDeclarativeGeoMap::addMapItemView_real(QDeclarativeGeoMapItemView
    #      *itemView)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap19addMapItemView_realEP26QDeclarative'
        'GeoMapItemView',
        self._addressOf(itemView),
    )

  @overload(QDeclarativeGeoMapItemView)
  @overload(NoneType)
  def removeMapItemView_real(
      self,
      itemView: Optional[QDeclarativeGeoMapItemView],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativeGeoMap::removeMapItemView_real(QDeclarativeGeoMapItemView
    *itemView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#removeMapItemView_real

    Parameters
    ----------

    itemView : Optional[QDeclarativeGeoMapItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDeclarativeGeoMap::removeMapItemView_real(
    #      QDeclarativeGeoMapItemView *itemView)
    return self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap22removeMapItemView_realEP26QDeclarat'
        'iveGeoMapItemView',
        self._addressOf(itemView),
    )

  def updateItemToWindowTransform(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::updateItemToWindowTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html
    """
    #  void QDeclarativeGeoMap::updateItemToWindowTransform()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap27updateItemToWindowTransformEv',
    )

  def onSGNodeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::onSGNodeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#onSGNodeChanged
    """
    #  void QDeclarativeGeoMap::onSGNodeChanged()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap15onSGNodeChangedEv')

  def mappingManagerInitialized(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::mappingManagerInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#mappingManagerInitialized
    """
    #  void QDeclarativeGeoMap::mappingManagerInitialized()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap25mappingManagerInitializedEv',
    )

  def pluginReady(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::pluginReady()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#pluginReady
    """
    #  void QDeclarativeGeoMap::pluginReady()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap11pluginReadyEv')

  def onSupportedMapTypesChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::onSupportedMapTypesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#onSupportedMapTypesChanged
    """
    #  void QDeclarativeGeoMap::onSupportedMapTypesChanged()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap26onSupportedMapTypesChangedEv',
    )

  @overload(QGeoCameraCapabilities)
  def onCameraCapabilitiesChanged(
      self,
      oldCameraCapabilities: QGeoCameraCapabilities,
  ) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::onCameraCapabilitiesChanged(const
    QGeoCameraCapabilities &oldCameraCapabilities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html

    Parameters
    ----------

    oldCameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  void QDeclarativeGeoMap::onCameraCapabilitiesChanged(const
    #      QGeoCameraCapabilities &oldCameraCapabilities)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap27onCameraCapabilitiesChangedERK22QGe'
        'oCameraCapabilities',
        self._valueOf(oldCameraCapabilities),
    )

  def onAttachedCopyrightNoticeVisibilityChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::onAttachedCopyrightNoticeVisibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html
    """
    #  void QDeclarativeGeoMap::onAttachedCopyrightNoticeVisibilityChanged()
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap42onAttachedCopyrightNoticeVisibility'
        'ChangedEv',
    )

  @overload(QGeoCameraData)
  def onCameraDataChanged(self, cameraData: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::onCameraDataChanged(const
    QGeoCameraData &cameraData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#onCameraDataChanged

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QDeclarativeGeoMap::onCameraDataChanged(const QGeoCameraData
    #      &cameraData)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap19onCameraDataChangedERK14QGeoCameraD'
        'ata',
        self._valueOf(cameraData),
    )

  @overload(QDeclarativeGeoMapItemView)
  @overload(NoneType)
  def setupMapView(self, view: Optional[QDeclarativeGeoMapItemView]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoMap::setupMapView(QDeclarativeGeoMapItemView *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#setupMapView

    Parameters
    ----------

    view : Optional[QDeclarativeGeoMapItemView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoMap::setupMapView(QDeclarativeGeoMapItemView
    #      *view)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap12setupMapViewEP26QDeclarativeGeoMapI'
        'temView',
        self._addressOf(view),
    )

  def populateMap(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::populateMap()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#populateMap
    """
    #  void QDeclarativeGeoMap::populateMap()
    self.uglySide.call('ritual_ZN18QDeclarativeGeoMap11populateMapEv')

  @overload(bool)
  def attachCopyrightNotice(self, initialVisibility: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::attachCopyrightNotice(bool
    initialVisibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#attachCopyrightNotice

    Parameters
    ----------

    initialVisibility : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::attachCopyrightNotice(bool initialVisibility)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21attachCopyrightNoticeEb',
        initialVisibility,
    )

  @overload(bool)
  def detachCopyrightNotice(self, currentVisibility: bool) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoMap::detachCopyrightNotice(bool
    currentVisibility)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeomap.html#detachCopyrightNotice

    Parameters
    ----------

    currentVisibility : bool
      Passed on as it is.
    """
    #  void QDeclarativeGeoMap::detachCopyrightNotice(bool currentVisibility)
    self.uglySide.call(
        'ritual_ZN18QDeclarativeGeoMap21detachCopyrightNoticeEb',
        currentVisibility,
    )

  @staticmethod
  def fitViewportToMapItemsRefine(*__, **_) -> Never:
    """
    Qt's 'void QDeclarativeGeoMap::fitViewportToMapItemsRefine(const
    QList<QPointer<QDeclarativeGeoMapItemBase>> &mapItems, bool refine, bool
    onlyVisible)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeGeoMap.fitViewportToMapItemsRefine' has no cute "
        "function yet. Qt's 'void "
        "QDeclarativeGeoMap::fitViewportToMapItemsRefine(const "
        "QList<QPointer<QDeclarativeGeoMapItemBase>> &mapItems, bool "
        "refine, bool onlyVisible)': takes a type Python has no way to hand "
        "over yet.")
