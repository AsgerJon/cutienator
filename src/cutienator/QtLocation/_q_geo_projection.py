"""
QGeoProjection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoProjection to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QPointF, QRectF, QSize
  from ..QtGui import QMatrix4x4, QTransform
  from ..QtPositioning import QDoubleVector2D, QDoubleVector3D
  from ..QtPositioning import QGeoCoordinate, QGeoShape
  from . import QGeoCameraData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDoubleVector2D = WAIT['QDoubleVector2D']
  QGeoCameraData = WAIT['QGeoCameraData']
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QTransform = WAIT['QTransform']


class QGeoProjection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoProjection: a plain Python object standing in
  front of one C++ QGeoProjection.

  What exists
  -----------

  Every function of Qt's QGeoProjection that has a ritual and that Python can
  call so far, 21 names in all: 'setVisibleArea', 'setViewportSize',
  'setCameraData', 'cameraData', 'minimumZoom',
  'maximumCenterLatitudeAtZoom', 'minimumCenterLatitudeAtZoom',
  'itemPositionToCoordinate', 'coordinateToItemPosition', 'projectionGroup',
  'datum', 'projectionType', 'anchorCoordinateToPoint', 'visibleRegion',
  'setBearing', 'projectionTransformation',
  'projectionTransformation_centered', 'qsgTransform', 'centerMercator',
  'setItemToWindowTransform', 'itemToWindowTransform'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoProjection::~QGeoProjection()': the destructor: Python never
    removes a C++ QGeoProjection.

  What to expect
  --------------

  - The C++ QGeoProjection is created at the first use, not by
    'QGeoProjection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoProjection.
  """

  #  The enums Qt writes inside QGeoProjection, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Datum(CuteNum):
    """
    The enum 'QGeoProjection::Datum' of Qt, with the 3 names Qt gives in it.
    """

    DatumUnknown = Kee[int](0)
    DatumWGS84 = Kee[int](1)
    DatumSphere = Kee[int](2)

  class ProjectionGroup(CuteNum):
    """
    The enum 'QGeoProjection::ProjectionGroup' of Qt, with the 7 names Qt
    gives in it.
    """

    ProjectionOther = Kee[int](0)
    ProjectionCylindrical = Kee[int](1)
    ProjectionPseudocylindrical = Kee[int](2)
    ProjectionAzimuthal = Kee[int](3)
    ProjectionPseudoazimuthal = Kee[int](4)
    ProjectionConic = Kee[int](5)
    ProjectionPseudoconic = Kee[int](6)

  class ProjectionType(CuteNum):
    """
    The enum 'QGeoProjection::ProjectionType' of Qt, with the 3 names Qt
    gives in it.
    """

    ProjectionUnknown = Kee[int](0)
    ProjectionGeneralPerspective = Kee[int](1)
    ProjectionWebMercator = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoProjection'

  #  A C++ QGeoProjection Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoProjection'

  #  The functions Qt calls itself that QGeoProjection is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setVisibleArea': (
          ('_ZN14QGeoProjection14setVisibleAreaERK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'setViewportSize': (
          ('_ZN14QGeoProjection15setViewportSizeERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'setCameraData': (
          ('_ZN14QGeoProjection13setCameraDataERK14QGeoCameraDatab',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtLocation:QGeoCameraData'),
               ('bool', 'number', ''),
           )),
      ),
      'cameraData': (
          ('_ZNK14QGeoProjection10cameraDataEv',
           ('address', 'value', 'QtLocation:QGeoCameraData'),
           ()),
      ),
      'minimumZoom': (
          ('_ZNK14QGeoProjection11minimumZoomEv',
           ('double', 'number', ''),
           ()),
      ),
      'maximumCenterLatitudeAtZoom': (
          ('_ZNK14QGeoProjection27maximumCenterLatitudeAtZoomERK14QGeoCamer'
           'aData',
           ('double', 'number', ''),
           (
               ('address', 'value', 'QtLocation:QGeoCameraData'),
           )),
      ),
      'minimumCenterLatitudeAtZoom': (
          ('_ZNK14QGeoProjection27minimumCenterLatitudeAtZoomERK14QGeoCamer'
           'aData',
           ('double', 'number', ''),
           (
               ('address', 'value', 'QtLocation:QGeoCameraData'),
           )),
      ),
      'itemPositionToCoordinate': (
          ('_ZNK14QGeoProjection24itemPositionToCoordinateERK15QDoubleVecto'
           'r2Db',
           ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           (
               ('address', 'value', 'QtPositioning:QDoubleVector2D'),
               ('bool', 'number', ''),
           )),
      ),
      'coordinateToItemPosition': (
          ('_ZNK14QGeoProjection24coordinateToItemPositionERK14QGeoCoordina'
           'teb',
           ('address', 'value', 'QtPositioning:QDoubleVector2D'),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
               ('bool', 'number', ''),
           )),
      ),
      'projectionGroup': (
          ('_ZNK14QGeoProjection15projectionGroupEv',
           ('int', 'enum', 'QtLocation:QGeoProjection.ProjectionGroup'),
           ()),
      ),
      'datum': (
          ('_ZNK14QGeoProjection5datumEv',
           ('int', 'enum', 'QtLocation:QGeoProjection.Datum'),
           ()),
      ),
      'projectionType': (
          ('_ZNK14QGeoProjection14projectionTypeEv',
           ('int', 'enum', 'QtLocation:QGeoProjection.ProjectionType'),
           ()),
      ),
      'anchorCoordinateToPoint': (
          ('_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeoCoordinat'
           'eRK7QPointF',
           ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           (
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'visibleRegion': (
          ('_ZNK14QGeoProjection13visibleRegionEv',
           ('address', 'value', 'QtPositioning:QGeoShape'),
           ()),
      ),
      'setBearing': (
          ('_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
               ('address', 'value', 'QtPositioning:QGeoCoordinate'),
           )),
      ),
      'projectionTransformation': (
          ('_ZNK14QGeoProjection24projectionTransformationEv',
           ('address', 'value', 'QtGui:QMatrix4x4'),
           ()),
      ),
      'projectionTransformation_centered': (
          ('_ZNK14QGeoProjection33projectionTransformation_centeredEv',
           ('address', 'value', 'QtGui:QMatrix4x4'),
           ()),
      ),
      'qsgTransform': (
          ('_ZNK14QGeoProjection12qsgTransformEv',
           ('address', 'value', 'QtGui:QMatrix4x4'),
           ()),
      ),
      'centerMercator': (
          ('_ZNK14QGeoProjection14centerMercatorEv',
           ('address', 'value', 'QtPositioning:QDoubleVector3D'),
           ()),
      ),
      'itemToWindowTransform': (
          ('_ZNK14QGeoProjection21itemToWindowTransformEv',
           ('address', 'value', 'QtGui:QTransform'),
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

  def cameraData(self) -> QGeoCameraData:
    """
    Calls Qt's 'QGeoCameraData QGeoProjection::cameraData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#cameraData

    Returns
    -------

    QGeoCameraData
      A new cute QGeoCameraData around the copy Qt gave back. Python owns it.
    """
    #  QGeoCameraData QGeoProjection::cameraData() const
    address = self.uglySide.call('ritual_ZNK14QGeoProjection10cameraDataEv')
    from . import QGeoCameraData
    return QGeoCameraData._cuteOwning(address)

  def minimumZoom(self) -> float:
    """
    Calls Qt's 'double QGeoProjection::minimumZoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#minimumZoom
    """
    #  double QGeoProjection::minimumZoom() const
    return self.uglySide.call('ritual_ZNK14QGeoProjection11minimumZoomEv')

  @overload(QGeoCameraData)
  def maximumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double QGeoProjection::maximumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#maximumCenterLatitudeAtZoom

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoProjection::maximumCenterLatitudeAtZoom(const
    #      QGeoCameraData &cameraData) const
    return self.uglySide.call(
        'ritual_ZNK14QGeoProjection27maximumCenterLatitudeAtZoomERK14QGeoCa'
        'meraData',
        self._valueOf(cameraData),
    )

  @overload(QGeoCameraData)
  def minimumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double QGeoProjection::minimumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#minimumCenterLatitudeAtZoom

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoProjection::minimumCenterLatitudeAtZoom(const
    #      QGeoCameraData &cameraData) const
    return self.uglySide.call(
        'ritual_ZNK14QGeoProjection27minimumCenterLatitudeAtZoomERK14QGeoCa'
        'meraData',
        self._valueOf(cameraData),
    )

  @overload(QDoubleVector2D)
  @overload(QDoubleVector2D, bool)
  def itemPositionToCoordinate(
      self,
      pos: QDoubleVector2D,
      clipToViewport: bool = True,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoProjection::itemPositionToCoordinate(const
    QDoubleVector2D &pos, bool clipToViewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#itemPositionToCoordinate

    Parameters
    ----------

    pos : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    clipToViewport : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoProjection::itemPositionToCoordinate(const
    #      QDoubleVector2D &pos, bool clipToViewport) const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoProjection24itemPositionToCoordinateERK15QDoubleVe'
        'ctor2Db',
        self._valueOf(pos), clipToViewport,
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate)
  @overload(QGeoCoordinate, bool)
  def coordinateToItemPosition(
      self,
      coordinate: QGeoCoordinate,
      clipToViewport: bool = True,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjection::coordinateToItemPosition(const QGeoCoordinate
    &coordinate, bool clipToViewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#coordinateToItemPosition

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    clipToViewport : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QGeoProjection::coordinateToItemPosition(const
    #      QGeoCoordinate &coordinate, bool clipToViewport) const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoProjection24coordinateToItemPositionERK14QGeoCoord'
        'inateb',
        self._valueOf(coordinate), clipToViewport,
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  def projectionGroup(self) -> ProjectionGroup:
    """
    Calls Qt's 'ProjectionGroup QGeoProjection::projectionGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#projectionGroup

    Returns
    -------

    ProjectionGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProjectionGroup(number)'
      gives.
    """
    #  ProjectionGroup QGeoProjection::projectionGroup() const
    return QGeoProjection.ProjectionGroup(self.uglySide.call(
        'ritual_ZNK14QGeoProjection15projectionGroupEv',
    ))

  def datum(self) -> Datum:
    """
    Calls Qt's 'Datum QGeoProjection::datum() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#datum

    Returns
    -------

    Datum
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Datum(number)' gives.
    """
    #  Datum QGeoProjection::datum() const
    return QGeoProjection.Datum(self.uglySide.call(
        'ritual_ZNK14QGeoProjection5datumEv',
    ))

  def projectionType(self) -> ProjectionType:
    """
    Calls Qt's 'ProjectionType QGeoProjection::projectionType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#projectionType

    Returns
    -------

    ProjectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ProjectionType(number)'
      gives.
    """
    #  ProjectionType QGeoProjection::projectionType() const
    return QGeoProjection.ProjectionType(self.uglySide.call(
        'ritual_ZNK14QGeoProjection14projectionTypeEv',
    ))

  @overload(QGeoCoordinate, QPointF)
  def anchorCoordinateToPoint(
      self,
      coordinate: QGeoCoordinate,
      anchorPoint: QPointF,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoProjection::anchorCoordinateToPoint(const
    QGeoCoordinate &coordinate, const QPointF &anchorPoint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#anchorCoordinateToPoint

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    anchorPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoProjection::anchorCoordinateToPoint(const
    #      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
    ritual = (
        'ritual_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeoCoordi'
        'nateRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QGeoProjection23anchorCoordinateToPointERK14QGeo'
          'CoordinateRK7QPointF')
    address = self.uglySide.call(
        ritual,
        self._valueOf(coordinate), self._valueOf(anchorPoint, 'QPointF'),
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def visibleRegion(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QGeoProjection::visibleRegion() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#visibleRegion

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QGeoProjection::visibleRegion() const
    ritual = 'ritual_ZNK14QGeoProjection13visibleRegionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoProjection13visibleRegionEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def projectionTransformation(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QGeoProjection::projectionTransformation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#projectionTransformation

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QGeoProjection::projectionTransformation() const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoProjection24projectionTransformationEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def projectionTransformation_centered(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    QGeoProjection::projectionTransformation_centered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QGeoProjection::projectionTransformation_centered() const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoProjection33projectionTransformation_centeredEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def qsgTransform(self) -> QMatrix4x4:
    """
    Calls Qt's 'const QMatrix4x4 &QGeoProjection::qsgTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#qsgTransform

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  const QMatrix4x4 &QGeoProjection::qsgTransform() const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoProjection12qsgTransformEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def centerMercator(self) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QGeoProjection::centerMercator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#centerMercator

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QGeoProjection::centerMercator() const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoProjection14centerMercatorEv',
    )
    from ..QtPositioning import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  def itemToWindowTransform(self) -> QTransform:
    """
    Calls Qt's 'QTransform QGeoProjection::itemToWindowTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#itemToWindowTransform

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGeoProjection::itemToWindowTransform() const
    ritual = 'ritual_ZNK14QGeoProjection21itemToWindowTransformEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QGeoProjection21itemToWindowTransformEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoProjection::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoProjection::setVisibleArea(const QRectF &visibleArea)
    self.uglySide.call(
        'ritual_ZN14QGeoProjection14setVisibleAreaERK6QRectF',
        self._valueOf(visibleArea),
    )

  @overload(QSize)
  def setViewportSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGeoProjection::setViewportSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#setViewportSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoProjection::setViewportSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN14QGeoProjection15setViewportSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QGeoCameraData)
  @overload(QGeoCameraData, bool)
  def setCameraData(
      self,
      cameraData: QGeoCameraData,
      force: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QGeoProjection::setCameraData(const QGeoCameraData
    &cameraData, bool force)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#setCameraData

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.

    force : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGeoProjection::setCameraData(const QGeoCameraData &cameraData,
    #      bool force)
    self.uglySide.call(
        'ritual_ZN14QGeoProjection13setCameraDataERK14QGeoCameraDatab',
        self._valueOf(cameraData), force,
    )

  @overload(float, QGeoCoordinate)
  def setBearing(self, bearing: float, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoProjection::setBearing(qreal bearing, const
    QGeoCoordinate &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#setBearing

    Parameters
    ----------

    bearing : float
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoProjection::setBearing(qreal bearing, const QGeoCoordinate
    #      &coordinate)
    ritual = 'ritual_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QGeoProjection10setBearingEdRK14QGeoCoordinate')
    return self.uglySide.call(ritual, bearing, self._valueOf(coordinate))

  @overload(QTransform)
  def setItemToWindowTransform(
      self,
      itemToWindowTransform: QTransform,
  ) -> None:
    """
    Calls Qt's 'void QGeoProjection::setItemToWindowTransform(const
    QTransform &itemToWindowTransform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojection.html#setItemToWindowTransform

    Parameters
    ----------

    itemToWindowTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QGeoProjection::setItemToWindowTransform(const QTransform
    #      &itemToWindowTransform)
    self.uglySide.call(
        'ritual_ZN14QGeoProjection24setItemToWindowTransformERK10QTransform',
        self._valueOf(itemToWindowTransform),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoProjection::QGeoProjection()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeoprojection.html#QGeoProjection
    """
    #  QGeoProjection::QGeoProjection()
    self._noteCreation(QGeoProjection, lambda: Rituals.call(
        'ritual_ZN14QGeoProjectionC1Ev',
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
