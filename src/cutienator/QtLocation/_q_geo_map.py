"""
QGeoMap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomap_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGeoMap to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMargins, QMetaObject, QPointF, QRectF, QSize
  from ..QtGui import QImage, QTransform
  from ..QtPositioning import QGeoCoordinate, QGeoRectangle, QGeoShape
  from ..QtQuick import QQuickWindow, QSGNode
  from . import QDeclarativeGeoMapItemBase, QGeoCameraCapabilities
  from . import QGeoCameraData, QGeoMapPrivate, QGeoMapType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMapItemBase = WAIT['QDeclarativeGeoMapItemBase']
  QEvent = WAIT['QEvent']
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoMapType = WAIT['QGeoMapType']
  QGeoRectangle = WAIT['QGeoRectangle']
  QImage = WAIT['QImage']
  QMargins = WAIT['QMargins']
  QPointF = WAIT['QPointF']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSGNode = WAIT['QSGNode']
  QSize = WAIT['QSize']
  QTransform = WAIT['QTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoMap(QObject):
  """
  The cute side of Qt's QGeoMap: a plain Python object standing in front of
  one C++ QGeoMap.

  It is built on the cute 'QObject', as Qt's QGeoMap is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoMap that has a ritual and that Python can call
  so far, 45 names in all: 'metaObject', 'tr', 'd_func', 'setViewportSize',
  'viewportSize', 'viewportWidth', 'viewportHeight', 'cameraData',
  'cameraCapabilities', 'capabilities', 'setActiveMapType', 'activeMapType',
  'minimumZoom', 'maximumCenterLatitudeAtZoom',
  'minimumCenterLatitudeAtZoom', 'mapWidth', 'mapHeight', 'prefetchData',
  'clearData', 'supportedMapItemTypes', 'addMapItem', 'removeMapItem',
  'clearMapItems', 'copyrightsStyleSheet', 'setAcceptedGestures',
  'handleEvent', 'setBearing', 'visibleRegion', 'anchorCoordinateToPoint',
  'fitViewportToGeoRectangle', 'setCopyrightVisible',
  'setItemToWindowTransform', 'setVisibleArea', 'visibleArea',
  'setCameraData', 'setCameraCapabilities', 'updateSceneGraph',
  'cameraDataChanged', 'sgNodeChanged', 'activeMapTypeChanged',
  'cameraCapabilitiesChanged', 'copyrightsImageChanged', 'copyrightsChanged',
  'copyrightsStyleSheetChanged', 'visibleAreaChanged'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGeoMap::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QGeoMap::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'const QGeoMapPrivate *QGeoMap::d_func() const': takes in Python
    what 'QGeoMapPrivate *QGeoMap::d_func()' takes.
  - Qt's 'QGeoMap::~QGeoMap()': the destructor: Python never removes a C++
    QGeoMap.
  - Qt's 'const QGeoProjection &QGeoMap::geoProjection() const': gives a type
    Python has no way to take yet.
  - Qt's 'QGeoMap::QGeoMap(QGeoMapPrivate &dd, QObject *parent)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 55 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QGeoMap is created at the first use, not by 'QGeoMap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoMap.
  - Qt tells when it has removed the C++ QGeoMap. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QGeoMap that has no cute function yet, '__init__',
    'geoProjection', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QGeoMap, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Capability(CuteFlags):
    """
    The flags enum 'QGeoMap::Capability' of Qt, with the 6 names Qt gives in
    it. Qt names the type of its combinations 'QGeoMap::Capabilities'.
    """

    SupportsNothing = 0x0
    SupportsVisibleRegion = 0x1
    SupportsSetBearing = 0x2
    SupportsAnchoringCoordinate = 0x4
    SupportsFittingViewportToGeoRectangle = 0x8
    SupportsVisibleArea = 0x10

  Capabilities = Capability

  class ItemType(CuteFlags):
    """
    The flags enum 'QGeoMap::ItemType' of Qt, with the 7 names Qt gives in
    it. Qt names the type of its combinations 'QGeoMap::ItemTypes'.
    """

    NoItem = 0x0
    MapRectangle = 0x1
    MapCircle = 0x2
    MapPolyline = 0x4
    MapPolygon = 0x8
    MapQuickItem = 0x10
    CustomMapItem = 0x8000

  ItemTypes = ItemType

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
    Calls Qt's 'QString QGeoMap::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#tr

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
    #  QString QGeoMap::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QGeoMap2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMap'

  #  A C++ QGeoMap Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoMap'

  #  The functions Qt calls itself that QGeoMap is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'capabilities': (
          ('_ZNK7QGeoMap12capabilitiesEv',
           ('int', 'flags', 'QtLocation:QGeoMap.Capability'),
           ()),
      ),
      'prefetchData': (
          ('_ZN7QGeoMap12prefetchDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'clearData': (
          ('_ZN7QGeoMap9clearDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'copyrightsStyleSheet': (
          ('_ZNK7QGeoMap20copyrightsStyleSheetEv',
           ('address', 'text', ''),
           ()),
      ),
      'setAcceptedGestures': (
          ('_ZN7QGeoMap19setAcceptedGesturesEbbbbb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
               ('bool', 'number', ''),
               ('bool', 'number', ''),
               ('bool', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'handleEvent': (
          ('_ZN7QGeoMap11handleEventEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'setBearing': (
          ('_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'visibleRegion': (
          ('_ZNK7QGeoMap13visibleRegionEv',
           ('address', 'value', 'QtPositioning:QGeoShape'),
           ()),
      ),
      'anchorCoordinateToPoint': (
          ('_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinateRK7QPoin'
           'tF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'fitViewportToGeoRectangle': (
          ('_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectangleRK8QMar'
           'gins',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtPositioning:QGeoRectangle'),
               ('address', 'value', 'QtCore:QMargins'),
           )),
      ),
      'setCopyrightVisible': (
          ('_ZN7QGeoMap19setCopyrightVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setItemToWindowTransform': (
          ('_ZN7QGeoMap24setItemToWindowTransformERK10QTransform',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtGui:QTransform'),
           )),
      ),
      'updateSceneGraph': (
          ('_ZN7QGeoMap16updateSceneGraphEP7QSGNodeP12QQuickWindow',
           ('address', 'address', 'QtQuick:QSGNode'),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address', 'QtQuick:QQuickWindow'),
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
    Calls Qt's 'const QMetaObject *QGeoMap::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGeoMap::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QGeoMap10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def viewportSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGeoMap::viewportSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#viewportSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGeoMap::viewportSize() const
    address = self.uglySide.call('ritual_ZNK7QGeoMap12viewportSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def viewportWidth(self) -> int:
    """
    Calls Qt's 'int QGeoMap::viewportWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#viewportWidth
    """
    #  int QGeoMap::viewportWidth() const
    return self.uglySide.call('ritual_ZNK7QGeoMap13viewportWidthEv')

  def viewportHeight(self) -> int:
    """
    Calls Qt's 'int QGeoMap::viewportHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#viewportHeight
    """
    #  int QGeoMap::viewportHeight() const
    return self.uglySide.call('ritual_ZNK7QGeoMap14viewportHeightEv')

  def cameraData(self) -> QGeoCameraData:
    """
    Calls Qt's 'const QGeoCameraData &QGeoMap::cameraData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#cameraData

    Returns
    -------

    QGeoCameraData
      A new cute QGeoCameraData around the copy Qt gave back. Python owns it.
    """
    #  const QGeoCameraData &QGeoMap::cameraData() const
    address = self.uglySide.call('ritual_ZNK7QGeoMap10cameraDataEv')
    from . import QGeoCameraData
    return QGeoCameraData._cuteOwning(address)

  def cameraCapabilities(self) -> QGeoCameraCapabilities:
    """
    Calls Qt's 'QGeoCameraCapabilities QGeoMap::cameraCapabilities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#cameraCapabilities

    Returns
    -------

    QGeoCameraCapabilities
      A new cute QGeoCameraCapabilities around the copy Qt gave back. Python
      owns it.
    """
    #  QGeoCameraCapabilities QGeoMap::cameraCapabilities() const
    address = self.uglySide.call('ritual_ZNK7QGeoMap18cameraCapabilitiesEv')
    from . import QGeoCameraCapabilities
    return QGeoCameraCapabilities._cuteOwning(address)

  def capabilities(self) -> Capabilities:
    """
    Calls Qt's 'Capabilities QGeoMap::capabilities() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#capabilities

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  Capabilities QGeoMap::capabilities() const
    ritual = 'ritual_ZNK7QGeoMap12capabilitiesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QGeoMap12capabilitiesEv'
    return QGeoMap.Capabilities(self.uglySide.call(ritual))

  def activeMapType(self) -> QGeoMapType:
    """
    Calls Qt's 'QGeoMapType QGeoMap::activeMapType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#activeMapType

    Returns
    -------

    QGeoMapType
      A new cute QGeoMapType around the copy Qt gave back. Python owns it.
    """
    #  QGeoMapType QGeoMap::activeMapType() const
    address = self.uglySide.call('ritual_ZNK7QGeoMap13activeMapTypeEv')
    from . import QGeoMapType
    return QGeoMapType._cuteOwning(address)

  def minimumZoom(self) -> float:
    """
    Calls Qt's 'double QGeoMap::minimumZoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#minimumZoom
    """
    #  double QGeoMap::minimumZoom() const
    return self.uglySide.call('ritual_ZNK7QGeoMap11minimumZoomEv')

  @overload(QGeoCameraData)
  def maximumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double QGeoMap::maximumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#maximumCenterLatitudeAtZoom

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoMap::maximumCenterLatitudeAtZoom(const QGeoCameraData
    #      &cameraData) const
    return self.uglySide.call(
        'ritual_ZNK7QGeoMap27maximumCenterLatitudeAtZoomERK14QGeoCameraData',
        self._valueOf(cameraData),
    )

  @overload(QGeoCameraData)
  def minimumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double QGeoMap::minimumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#minimumCenterLatitudeAtZoom

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoMap::minimumCenterLatitudeAtZoom(const QGeoCameraData
    #      &cameraData) const
    return self.uglySide.call(
        'ritual_ZNK7QGeoMap27minimumCenterLatitudeAtZoomERK14QGeoCameraData',
        self._valueOf(cameraData),
    )

  def mapWidth(self) -> float:
    """
    Calls Qt's 'double QGeoMap::mapWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#mapWidth
    """
    #  double QGeoMap::mapWidth() const
    return self.uglySide.call('ritual_ZNK7QGeoMap8mapWidthEv')

  def mapHeight(self) -> float:
    """
    Calls Qt's 'double QGeoMap::mapHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#mapHeight
    """
    #  double QGeoMap::mapHeight() const
    return self.uglySide.call('ritual_ZNK7QGeoMap9mapHeightEv')

  def supportedMapItemTypes(self) -> ItemTypes:
    """
    Calls Qt's 'ItemTypes QGeoMap::supportedMapItemTypes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#supportedMapItemTypes

    Returns
    -------

    ItemTypes
      The value standing for the combination Qt gave back.
    """
    #  ItemTypes QGeoMap::supportedMapItemTypes() const
    return QGeoMap.ItemTypes(self.uglySide.call(
        'ritual_ZNK7QGeoMap21supportedMapItemTypesEv',
    ))

  def copyrightsStyleSheet(self) -> str:
    """
    Calls Qt's 'QString QGeoMap::copyrightsStyleSheet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#copyrightsStyleSheet

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoMap::copyrightsStyleSheet() const
    ritual = 'ritual_ZNK7QGeoMap20copyrightsStyleSheetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QGeoMap20copyrightsStyleSheetEv'
    return self.uglySide.call(ritual)

  def visibleRegion(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QGeoMap::visibleRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#visibleRegion

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QGeoMap::visibleRegion() const
    ritual = 'ritual_ZNK7QGeoMap13visibleRegionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK7QGeoMap13visibleRegionEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def visibleArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGeoMap::visibleArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#visibleArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGeoMap::visibleArea() const
    address = self.uglySide.call('ritual_ZNK7QGeoMap11visibleAreaEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setViewportSize(self, viewportSize: QSize) -> None:
    """
    Calls Qt's 'void QGeoMap::setViewportSize(const QSize &viewportSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setViewportSize

    Parameters
    ----------

    viewportSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoMap::setViewportSize(const QSize &viewportSize)
    self.uglySide.call(
        'ritual_ZN7QGeoMap15setViewportSizeERK5QSize',
        self._valueOf(viewportSize),
    )

  @overload(QGeoMapType)
  def setActiveMapType(self, mapType: QGeoMapType) -> None:
    """
    Calls Qt's 'void QGeoMap::setActiveMapType(const QGeoMapType &mapType)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setActiveMapType

    Parameters
    ----------

    mapType : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  void QGeoMap::setActiveMapType(const QGeoMapType &mapType)
    self.uglySide.call(
        'ritual_ZN7QGeoMap16setActiveMapTypeERK11QGeoMapType',
        self._valueOf(mapType),
    )

  @overload(bool, bool, bool, bool, bool)
  def setAcceptedGestures(
      self,
      pan: bool,
      flick: bool,
      pinch: bool,
      rotate: bool,
      tilt: bool,
  ) -> None:
    """
    Calls Qt's 'void QGeoMap::setAcceptedGestures(bool pan, bool flick, bool
    pinch, bool rotate, bool tilt)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setAcceptedGestures

    Parameters
    ----------

    pan : bool
      Passed on as it is.

    flick : bool
      Passed on as it is.

    pinch : bool
      Passed on as it is.

    rotate : bool
      Passed on as it is.

    tilt : bool
      Passed on as it is.
    """
    #  void QGeoMap::setAcceptedGestures(bool pan, bool flick, bool pinch,
    #      bool rotate, bool tilt)
    ritual = 'ritual_ZN7QGeoMap19setAcceptedGesturesEbbbbb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QGeoMap19setAcceptedGesturesEbbbbb'
    self.uglySide.call(ritual, pan, flick, pinch, rotate, tilt)

  @overload(float, QGeoCoordinate)
  def setBearing(self, bearing: float, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoMap::setBearing(qreal bearing, const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setBearing

    Parameters
    ----------

    bearing : float
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoMap::setBearing(qreal bearing, const QGeoCoordinate
    #      &coordinate)
    ritual = 'ritual_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QGeoMap10setBearingEdRK14QGeoCoordinate'
    return self.uglySide.call(ritual, bearing, self._valueOf(coordinate))

  @overload(bool)
  def setCopyrightVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QGeoMap::setCopyrightVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setCopyrightVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QGeoMap::setCopyrightVisible(bool visible)
    ritual = 'ritual_ZN7QGeoMap19setCopyrightVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QGeoMap19setCopyrightVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(QTransform)
  def setItemToWindowTransform(
      self,
      itemToWindowTransform: QTransform,
  ) -> None:
    """
    Calls Qt's 'void QGeoMap::setItemToWindowTransform(const QTransform
    &itemToWindowTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#setItemToWindowTransform

    Parameters
    ----------

    itemToWindowTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QGeoMap::setItemToWindowTransform(const QTransform
    #      &itemToWindowTransform)
    ritual = 'ritual_ZN7QGeoMap24setItemToWindowTransformERK10QTransform'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QGeoMap24setItemToWindowTransformERK10QTransform')
    self.uglySide.call(ritual, self._valueOf(itemToWindowTransform))

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoMap::setVisibleArea(const QRectF &visibleArea)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoMap::setVisibleArea(const QRectF &visibleArea)
    self.uglySide.call(
        'ritual_ZN7QGeoMap14setVisibleAreaERK6QRectF',
        self._valueOf(visibleArea),
    )

  @overload(QGeoCameraData)
  def setCameraData(self, cameraData: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QGeoMap::setCameraData(const QGeoCameraData
    &cameraData)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setCameraData

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QGeoMap::setCameraData(const QGeoCameraData &cameraData)
    self.uglySide.call(
        'ritual_ZN7QGeoMap13setCameraDataERK14QGeoCameraData',
        self._valueOf(cameraData),
    )

  @overload(QGeoCameraCapabilities)
  def setCameraCapabilities(
      self,
      cameraCapabilities: QGeoCameraCapabilities,
  ) -> None:
    """
    Calls Qt's 'void QGeoMap::setCameraCapabilities(const
    QGeoCameraCapabilities &cameraCapabilities)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#setCameraCapabilities

    Parameters
    ----------

    cameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  void QGeoMap::setCameraCapabilities(const QGeoCameraCapabilities
    #      &cameraCapabilities)
    self.uglySide.call(
        'ritual_ZN7QGeoMap21setCameraCapabilitiesERK22QGeoCameraCapabilitie'
        's',
        self._valueOf(cameraCapabilities),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGeoMap::QGeoMap(QGeoMapPrivate &dd, QObject *parent)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoMap.__init__' has no cute function yet. Qt's "
        "'QGeoMap::QGeoMap(QGeoMapPrivate &dd, QObject *parent)': takes a "
        "type Python has no way to hand over yet.")

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

  def d_func(self) -> Optional[QGeoMapPrivate]:
    """
    Calls Qt's 'QGeoMapPrivate *QGeoMap::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#d_func

    Returns
    -------

    Optional[QGeoMapPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMapPrivate *QGeoMap::d_func()
    address = self.uglySide.call('ritual_ZN7QGeoMap6d_funcEv')
    from . import QGeoMapPrivate
    return QGeoMapPrivate._cuteAt(address)

  def prefetchData(self) -> None:
    """
    Calls Qt's 'void QGeoMap::prefetchData()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#prefetchData
    """
    #  void QGeoMap::prefetchData()
    ritual = 'ritual_ZN7QGeoMap12prefetchDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QGeoMap12prefetchDataEv'
    self.uglySide.call(ritual)

  def clearData(self) -> None:
    """
    Calls Qt's 'void QGeoMap::clearData()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#clearData
    """
    #  void QGeoMap::clearData()
    ritual = 'ritual_ZN7QGeoMap9clearDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QGeoMap9clearDataEv'
    self.uglySide.call(ritual)

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def addMapItem(self, item: Optional[QDeclarativeGeoMapItemBase]) -> None:
    """
    Calls Qt's 'void QGeoMap::addMapItem(QDeclarativeGeoMapItemBase *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#addMapItem

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoMap::addMapItem(QDeclarativeGeoMapItemBase *item)
    self.uglySide.call(
        'ritual_ZN7QGeoMap10addMapItemEP26QDeclarativeGeoMapItemBase',
        self._addressOf(item),
    )

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def removeMapItem(
      self,
      item: Optional[QDeclarativeGeoMapItemBase],
  ) -> None:
    """
    Calls Qt's 'void QGeoMap::removeMapItem(QDeclarativeGeoMapItemBase
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#removeMapItem

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoMap::removeMapItem(QDeclarativeGeoMapItemBase *item)
    self.uglySide.call(
        'ritual_ZN7QGeoMap13removeMapItemEP26QDeclarativeGeoMapItemBase',
        self._addressOf(item),
    )

  def clearMapItems(self) -> None:
    """
    Calls Qt's 'void QGeoMap::clearMapItems()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#clearMapItems
    """
    #  void QGeoMap::clearMapItems()
    self.uglySide.call('ritual_ZN7QGeoMap13clearMapItemsEv')

  @overload(QEvent)
  @overload(NoneType)
  def handleEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QGeoMap::handleEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#handleEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGeoMap::handleEvent(QEvent *event)
    ritual = 'ritual_ZN7QGeoMap11handleEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QGeoMap11handleEventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGeoCoordinate, QPointF)
  def anchorCoordinateToPoint(
      self,
      coordinate: QGeoCoordinate,
      anchorPoint: QPointF,
  ) -> bool:
    """
    Calls Qt's 'bool QGeoMap::anchorCoordinateToPoint(const QGeoCoordinate
    &coordinate, const QPointF &anchorPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#anchorCoordinateToPoint

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    anchorPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QGeoMap::anchorCoordinateToPoint(const QGeoCoordinate
    #      &coordinate, const QPointF &anchorPoint)
    ritual = (
        'ritual_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinateRK7QP'
        'ointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QGeoMap23anchorCoordinateToPointERK14QGeoCoordinat'
          'eRK7QPointF')
    return self.uglySide.call(
        ritual,
        self._valueOf(coordinate), self._valueOf(anchorPoint, 'QPointF'),
    )

  @overload(QGeoRectangle, QMargins)
  def fitViewportToGeoRectangle(
      self,
      rectangle: QGeoRectangle,
      borders: QMargins,
  ) -> bool:
    """
    Calls Qt's 'bool QGeoMap::fitViewportToGeoRectangle(const QGeoRectangle
    &rectangle, const QMargins &borders)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#fitViewportToGeoRectangle

    Parameters
    ----------

    rectangle : QGeoRectangle
      Passed on as a value: Qt reads the C++ QGeoRectangle, which stays
      Python's own.

    borders : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  bool QGeoMap::fitViewportToGeoRectangle(const QGeoRectangle
    #      &rectangle, const QMargins &borders)
    ritual = (
        'ritual_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectangleRK8Q'
        'Margins')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN7QGeoMap25fitViewportToGeoRectangleERK13QGeoRectang'
          'leRK8QMargins')
    return self.uglySide.call(
        ritual, self._valueOf(rectangle), self._valueOf(borders, 'QMargins'),
    )

  @overload(QSGNode, QQuickWindow)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickWindow)
  @overload(NoneType, NoneType)
  def updateSceneGraph(
      self,
      node: Optional[QSGNode],
      window: Optional[QQuickWindow],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QGeoMap::updateSceneGraph(QSGNode *node,
    QQuickWindow *window)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#updateSceneGraph

    Parameters
    ----------

    node : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QGeoMap::updateSceneGraph(QSGNode *node, QQuickWindow
    #      *window)
    address = self.uglySide.call(
        'ritual_ZN7QGeoMap16updateSceneGraphEP7QSGNodeP12QQuickWindow',
        self._addressOf(node, 'QSGNode'), self._addressOf(window),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QGeoCameraData)
  def cameraDataChanged(self, cameraData: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QGeoMap::cameraDataChanged(const QGeoCameraData
    &cameraData)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#cameraDataChanged

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QGeoMap::cameraDataChanged(const QGeoCameraData &cameraData)
    self.uglySide.call(
        'ritual_ZN7QGeoMap17cameraDataChangedERK14QGeoCameraData',
        self._valueOf(cameraData),
    )

  def sgNodeChanged(self) -> None:
    """
    Calls Qt's 'void QGeoMap::sgNodeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#sgNodeChanged
    """
    #  void QGeoMap::sgNodeChanged()
    self.uglySide.call('ritual_ZN7QGeoMap13sgNodeChangedEv')

  def activeMapTypeChanged(self) -> None:
    """
    Calls Qt's 'void QGeoMap::activeMapTypeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#activeMapTypeChanged
    """
    #  void QGeoMap::activeMapTypeChanged()
    self.uglySide.call('ritual_ZN7QGeoMap20activeMapTypeChangedEv')

  @overload(QGeoCameraCapabilities)
  def cameraCapabilitiesChanged(
      self,
      oldCameraCapabilities: QGeoCameraCapabilities,
  ) -> None:
    """
    Calls Qt's 'void QGeoMap::cameraCapabilitiesChanged(const
    QGeoCameraCapabilities &oldCameraCapabilities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#cameraCapabilitiesChanged

    Parameters
    ----------

    oldCameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  void QGeoMap::cameraCapabilitiesChanged(const QGeoCameraCapabilities
    #      &oldCameraCapabilities)
    self.uglySide.call(
        'ritual_ZN7QGeoMap25cameraCapabilitiesChangedERK22QGeoCameraCapabil'
        'ities',
        self._valueOf(oldCameraCapabilities),
    )

  @overload(QImage)
  def copyrightsImageChanged(self, copyrightsImage: QImage) -> None:
    """
    Calls Qt's 'void QGeoMap::copyrightsImageChanged(const QImage
    &copyrightsImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#copyrightsImageChanged

    Parameters
    ----------

    copyrightsImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QGeoMap::copyrightsImageChanged(const QImage &copyrightsImage)
    self.uglySide.call(
        'ritual_ZN7QGeoMap22copyrightsImageChangedERK6QImage',
        self._valueOf(copyrightsImage),
    )

  @overload(str)
  def copyrightsChanged(self, copyrightsHtml: str) -> None:
    """
    Calls Qt's 'void QGeoMap::copyrightsChanged(const QString
    &copyrightsHtml)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#copyrightsChanged

    Parameters
    ----------

    copyrightsHtml : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoMap::copyrightsChanged(const QString &copyrightsHtml)
    self.uglySide.call(
        'ritual_ZN7QGeoMap17copyrightsChangedERK7QString', copyrightsHtml,
    )

  @overload(str)
  def copyrightsStyleSheetChanged(self, styleSheet: str) -> None:
    """
    Calls Qt's 'void QGeoMap::copyrightsStyleSheetChanged(const QString
    &styleSheet)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomap.html#copyrightsStyleSheetChanged

    Parameters
    ----------

    styleSheet : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoMap::copyrightsStyleSheetChanged(const QString &styleSheet)
    self.uglySide.call(
        'ritual_ZN7QGeoMap27copyrightsStyleSheetChangedERK7QString',
        styleSheet,
    )

  def visibleAreaChanged(self) -> None:
    """
    Calls Qt's 'void QGeoMap::visibleAreaChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomap.html#visibleAreaChanged
    """
    #  void QGeoMap::visibleAreaChanged()
    self.uglySide.call('ritual_ZN7QGeoMap18visibleAreaChangedEv')

  @staticmethod
  def geoProjection(*__, **_) -> Never:
    """
    Qt's 'const QGeoProjection &QGeoMap::geoProjection() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoMap.geoProjection' has no cute function yet. Qt's 'const "
        "QGeoProjection &QGeoMap::geoProjection() const': gives a type "
        "Python has no way to take yet.")
