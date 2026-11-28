"""
QGeoMapPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomap_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoMapPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QGeoMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF, QSize
  from . import QDeclarativeGeoMapItemBase, QGeoCameraCapabilities
  from . import QGeoCameraData, QGeoMapType, QGeoMappingManagerEngine
  from . import QGeoProjection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMapItemBase = WAIT['QDeclarativeGeoMapItemBase']
  QGeoCameraCapabilities = WAIT['QGeoCameraCapabilities']
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoMapType = WAIT['QGeoMapType']
  QGeoMappingManagerEngine = WAIT['QGeoMappingManagerEngine']
  QGeoProjection = WAIT['QGeoProjection']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoMapPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGeoMapPrivate: a plain Python object standing in
  front of one C++ QGeoMapPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGeoMapPrivate is built
  on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoMapPrivate that has a ritual and that Python can
  call so far, 18 names in all: 'q_func', 'setCameraCapabilities',
  'cameraCapabilities', 'supportedMapItemTypes', 'addMapItem',
  'removeMapItem', 'changeViewportSize', 'changeCameraData',
  'changeActiveMapType', 'mapWidth', 'mapHeight', 'setCopyrightVisible',
  'copyrightVisible', 'maximumCenterLatitudeAtZoom',
  'minimumCenterLatitudeAtZoom', 'setVisibleArea', 'visibleArea',
  'clampVisibleArea'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGeoMap *QGeoMapPrivate::q_func() const': takes in Python
    what 'QGeoMap *QGeoMapPrivate::q_func()' takes.
  - Qt's 'QGeoMapPrivate::~QGeoMapPrivate()': the destructor: Python never
    removes a C++ QGeoMapPrivate.
  - Qt's 'const QGeoMapPrivate *QGeoMapPrivate::get(const QGeoMap &map)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 23 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QGeoMapPrivate is created at the first use, not by
    'QGeoMapPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoMapPrivate.
  - Each name of Qt's QGeoMapPrivate that has no cute function yet,
    'geoProjection', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMapPrivate'

  #  A C++ QGeoMapPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoMapPrivate'

  #  The functions Qt calls itself that QGeoMapPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'supportedMapItemTypes': (
          ('_ZNK14QGeoMapPrivate21supportedMapItemTypesEv',
           ('int', 'flags', 'QtLocation:QGeoMap.ItemType'),
           ()),
      ),
      'addMapItem': (
          ('_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapItemBase',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtLocation:QDeclarativeGeoMapItemBase'),
           )),
      ),
      'removeMapItem': (
          ('_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoMapItemBas'
           'e',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtLocation:QDeclarativeGeoMapItemBase'),
           )),
      ),
      'changeViewportSize': (
          ('_ZN14QGeoMapPrivate18changeViewportSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'changeCameraData': (
          ('_ZN14QGeoMapPrivate16changeCameraDataERK14QGeoCameraData',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoCameraData'),
           )),
      ),
      'changeActiveMapType': (
          ('_ZN14QGeoMapPrivate19changeActiveMapTypeERK11QGeoMapType',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoMapType'),
           )),
      ),
      'mapWidth': (
          ('_ZNK14QGeoMapPrivate8mapWidthEv',
           ('double', 'number', ''),
           ()),
      ),
      'mapHeight': (
          ('_ZNK14QGeoMapPrivate9mapHeightEv',
           ('double', 'number', ''),
           ()),
      ),
      'setCopyrightVisible': (
          ('_ZN14QGeoMapPrivate19setCopyrightVisibleEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'copyrightVisible': (
          ('_ZNK14QGeoMapPrivate16copyrightVisibleEv',
           ('bool', 'number', ''),
           ()),
      ),
      'maximumCenterLatitudeAtZoom': (
          ('_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14QGeoCamer'
           'aData',
           ('double', 'number', ''),
           (
               ('address', 'value', 'QtLocation:QGeoCameraData'),
           )),
      ),
      'minimumCenterLatitudeAtZoom': (
          ('_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14QGeoCamer'
           'aData',
           ('double', 'number', ''),
           (
               ('address', 'value', 'QtLocation:QGeoCameraData'),
           )),
      ),
      'setVisibleArea': (
          ('_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'visibleArea': (
          ('_ZNK14QGeoMapPrivate11visibleAreaEv',
           ('address', 'value', 'QtCore:QRectF'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cameraCapabilities(self) -> QGeoCameraCapabilities:
    """
    Calls Qt's 'const QGeoCameraCapabilities
    &QGeoMapPrivate::cameraCapabilities() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#cameraCapabilities

    Returns
    -------

    QGeoCameraCapabilities
      A new cute QGeoCameraCapabilities around the copy Qt gave back. Python
      owns it.
    """
    #  const QGeoCameraCapabilities &QGeoMapPrivate::cameraCapabilities()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoMapPrivate18cameraCapabilitiesEv',
    )
    from . import QGeoCameraCapabilities
    return QGeoCameraCapabilities._cuteOwning(address)

  def supportedMapItemTypes(self) -> QGeoMap.ItemTypes:
    """
    Calls Qt's 'QGeoMap::ItemTypes QGeoMapPrivate::supportedMapItemTypes()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#supportedMapItemTypes

    Returns
    -------

    QGeoMap.ItemTypes
      The value standing for the combination Qt gave back.
    """
    #  QGeoMap::ItemTypes QGeoMapPrivate::supportedMapItemTypes() const
    ritual = 'ritual_ZNK14QGeoMapPrivate21supportedMapItemTypesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoMapPrivate21supportedMapItemTypesEv'
    return QGeoMap.ItemTypes(self.uglySide.call(ritual))

  def mapWidth(self) -> float:
    """
    Calls Qt's 'double QGeoMapPrivate::mapWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#mapWidth
    """
    #  double QGeoMapPrivate::mapWidth() const
    ritual = 'ritual_ZNK14QGeoMapPrivate8mapWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoMapPrivate8mapWidthEv'
    return self.uglySide.call(ritual)

  def mapHeight(self) -> float:
    """
    Calls Qt's 'double QGeoMapPrivate::mapHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#mapHeight
    """
    #  double QGeoMapPrivate::mapHeight() const
    ritual = 'ritual_ZNK14QGeoMapPrivate9mapHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoMapPrivate9mapHeightEv'
    return self.uglySide.call(ritual)

  def copyrightVisible(self) -> bool:
    """
    Calls Qt's 'bool QGeoMapPrivate::copyrightVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#copyrightVisible
    """
    #  bool QGeoMapPrivate::copyrightVisible() const
    ritual = 'ritual_ZNK14QGeoMapPrivate16copyrightVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoMapPrivate16copyrightVisibleEv'
    return self.uglySide.call(ritual)

  @overload(QGeoCameraData)
  def maximumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double QGeoMapPrivate::maximumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#maximumCenterLatitudeAtZoom

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoMapPrivate::maximumCenterLatitudeAtZoom(const
    #      QGeoCameraData &cameraData) const
    ritual = (
        'ritual_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14QGeoCa'
        'meraData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QGeoMapPrivate27maximumCenterLatitudeAtZoomERK14'
          'QGeoCameraData')
    return self.uglySide.call(ritual, self._valueOf(cameraData))

  @overload(QGeoCameraData)
  def minimumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double QGeoMapPrivate::minimumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#minimumCenterLatitudeAtZoom

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoMapPrivate::minimumCenterLatitudeAtZoom(const
    #      QGeoCameraData &cameraData) const
    ritual = (
        'ritual_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14QGeoCa'
        'meraData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QGeoMapPrivate27minimumCenterLatitudeAtZoomERK14'
          'QGeoCameraData')
    return self.uglySide.call(ritual, self._valueOf(cameraData))

  def visibleArea(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGeoMapPrivate::visibleArea() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#visibleArea

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGeoMapPrivate::visibleArea() const
    ritual = 'ritual_ZNK14QGeoMapPrivate11visibleAreaEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoMapPrivate11visibleAreaEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def clampVisibleArea(self, visibleArea: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGeoMapPrivate::clampVisibleArea(const QRectF
    &visibleArea) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#clampVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGeoMapPrivate::clampVisibleArea(const QRectF &visibleArea)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoMapPrivate16clampVisibleAreaERK6QRectF',
        self._valueOf(visibleArea),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCameraCapabilities)
  def setCameraCapabilities(
      self,
      cameraCapabilities: QGeoCameraCapabilities,
  ) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::setCameraCapabilities(const
    QGeoCameraCapabilities &cameraCapabilities)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#setCameraCapabilities

    Parameters
    ----------

    cameraCapabilities : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  void QGeoMapPrivate::setCameraCapabilities(const
    #      QGeoCameraCapabilities &cameraCapabilities)
    self.uglySide.call(
        'ritual_ZN14QGeoMapPrivate21setCameraCapabilitiesERK22QGeoCameraCap'
        'abilities',
        self._valueOf(cameraCapabilities),
    )

  @overload(bool)
  def setCopyrightVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::setCopyrightVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#setCopyrightVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QGeoMapPrivate::setCopyrightVisible(bool visible)
    ritual = 'ritual_ZN14QGeoMapPrivate19setCopyrightVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QGeoMapPrivate19setCopyrightVisibleEb'
    self.uglySide.call(ritual, visible)

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoMapPrivate::setVisibleArea(const QRectF &visibleArea)
    ritual = 'ritual_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QGeoMapPrivate14setVisibleAreaERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(visibleArea))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoMappingManagerEngine, QGeoProjection)
  @overload(QGeoMappingManagerEngine, NoneType)
  @overload(NoneType, QGeoProjection)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QGeoMappingManagerEngine],
      geoProjection: Optional[QGeoProjection],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QGeoMapPrivate::QGeoMapPrivate(QGeoMappingManagerEngine *engine,
    QGeoProjection *geoProjection)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#QGeoMapPrivate

    Parameters
    ----------

    engine : Optional[QGeoMappingManagerEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    geoProjection : Optional[QGeoProjection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QGeoMapPrivate::QGeoMapPrivate(QGeoMappingManagerEngine *engine,
    #      QGeoProjection *geoProjection)
    self._noteCreation(QGeoMapPrivate, lambda: Rituals.call(
        'ritual_ZN14QGeoMapPrivateC1EP24QGeoMappingManagerEngineP14QGeoProj'
        'ection',
        self._addressOf(engine), self._addressOf(geoProjection),
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

  def q_func(self) -> Optional[QGeoMap]:
    """
    Calls Qt's 'QGeoMap *QGeoMapPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#q_func

    Returns
    -------

    Optional[QGeoMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGeoMap *QGeoMapPrivate::q_func()
    address = self.uglySide.call('ritual_ZN14QGeoMapPrivate6q_funcEv')
    return QGeoMap._cuteAt(address)

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def addMapItem(self, item: Optional[QDeclarativeGeoMapItemBase]) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::addMapItem(QDeclarativeGeoMapItemBase
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#addMapItem

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoMapPrivate::addMapItem(QDeclarativeGeoMapItemBase *item)
    ritual = (
        'ritual_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapItemBas'
        'e')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QGeoMapPrivate10addMapItemEP26QDeclarativeGeoMapI'
          'temBase')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QDeclarativeGeoMapItemBase)
  @overload(NoneType)
  def removeMapItem(
      self,
      item: Optional[QDeclarativeGeoMapItemBase],
  ) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::removeMapItem(QDeclarativeGeoMapItemBase
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomapprivate.html#removeMapItem

    Parameters
    ----------

    item : Optional[QDeclarativeGeoMapItemBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoMapPrivate::removeMapItem(QDeclarativeGeoMapItemBase *item)
    ritual = (
        'ritual_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoMapItem'
        'Base')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QGeoMapPrivate13removeMapItemEP26QDeclarativeGeoM'
          'apItemBase')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QSize)
  def changeViewportSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::changeViewportSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#changeViewportSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoMapPrivate::changeViewportSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN14QGeoMapPrivate18changeViewportSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QGeoCameraData)
  def changeCameraData(self, oldCameraData: QGeoCameraData) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::changeCameraData(const QGeoCameraData
    &oldCameraData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#changeCameraData

    Parameters
    ----------

    oldCameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  void QGeoMapPrivate::changeCameraData(const QGeoCameraData
    #      &oldCameraData)
    self.uglySide.call(
        'ritual_ZN14QGeoMapPrivate16changeCameraDataERK14QGeoCameraData',
        self._valueOf(oldCameraData),
    )

  @overload(QGeoMapType)
  def changeActiveMapType(self, mapType: QGeoMapType) -> None:
    """
    Calls Qt's 'void QGeoMapPrivate::changeActiveMapType(const QGeoMapType
    &mapType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomapprivate.html#changeActiveMapType

    Parameters
    ----------

    mapType : QGeoMapType
      Passed on as a value: Qt reads the C++ QGeoMapType, which stays
      Python's own.
    """
    #  void QGeoMapPrivate::changeActiveMapType(const QGeoMapType &mapType)
    self.uglySide.call(
        'ritual_ZN14QGeoMapPrivate19changeActiveMapTypeERK11QGeoMapType',
        self._valueOf(mapType),
    )

  @staticmethod
  def geoProjection(*__, **_) -> Never:
    """
    Qt's 'const QGeoProjection *QGeoMapPrivate::geoProjection() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QGeoMapPrivate.geoProjection' has no cute function yet. Qt's "
        "'const QGeoProjection *QGeoMapPrivate::geoProjection() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
