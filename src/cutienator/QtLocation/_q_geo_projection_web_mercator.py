"""
QGeoProjectionWebMercator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoProjectionWebMercator to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QGeoProjection

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QPointF, QRectF, QSize
  from ..QtGui import QMatrix4x4
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


class QGeoProjectionWebMercator(QGeoProjection):
  """
  The cute side of Qt's QGeoProjectionWebMercator: a plain Python object
  standing in front of one C++ QGeoProjectionWebMercator.

  It is built on the cute 'QGeoProjection', as Qt's QGeoProjectionWebMercator
  is built on Qt's QGeoProjection, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoProjectionWebMercator that has a ritual and that
  Python can call so far, 37 names in all: 'minimumZoom',
  'projectionTransformation', 'projectionTransformation_centered',
  'qsgTransform', 'centerMercator', 'maximumCenterLatitudeAtZoom',
  'minimumCenterLatitudeAtZoom', 'setVisibleArea', 'setViewportSize',
  'setCameraData', 'cameraData', 'itemPositionToCoordinate',
  'coordinateToItemPosition', 'projectionGroup', 'datum', 'projectionType',
  'anchorCoordinateToPoint', 'setBearing', 'visibleRegion', 'mapWidth',
  'mapHeight', 'geoToMapProjection', 'mapProjectionToGeo',
  'projectionWrapFactor', 'wrapMapProjection', 'unwrapMapProjection',
  'wrappedMapProjectionToItemPosition', 'itemPositionToWrappedMapProjection',
  'geoToWrappedMapProjection', 'wrappedMapProjectionToGeo',
  'quickItemTransformation', 'isProjectable', 'visibleGeometry',
  'visibleGeometryExpanded', 'projectableGeometry', 'setupCamera',
  'updateVisibleRegion'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoProjectionWebMercator::~QGeoProjectionWebMercator()': the
    destructor: Python never removes a C++ QGeoProjectionWebMercator.
  - Qt's 'QPair<QGeoCoordinate, qreal>
    QGeoProjectionWebMercator::fitViewportToGeoRectangle(const QGeoRectangle
    &rectangle, const QMargins &margins) const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  4 of the 44 functions Qt declares: 2 forbidden; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file; 1
  leans on 'QGeoProjectionWebMercator.

  What to expect
  --------------

  - The C++ QGeoProjectionWebMercator is created at the first use, not by
    'QGeoProjectionWebMercator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoProjectionWebMercator.
  - Each name of Qt's QGeoProjectionWebMercator that has no cute function
    yet, 'fitViewportToGeoRectangle', 'viewportToWrappedMapProjection', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QGeoProjectionWebMercator, each a class in
  #  here as in C++.

  class Line2D(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGeoProjectionWebMercator::Line2D: a plain Python
    object standing in front of one C++ QGeoProjectionWebMercator::Line2D.

    C++ hands a QGeoProjectionWebMercator::Line2D around as a copy, so every
    C++ QGeoProjectionWebMercator::Line2D behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QGeoProjectionWebMercator::Line2D that has a
    ritual and that Python can call so far, 1 name in all: 'isValid'. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGeoProjectionWebMercator::Line2D::~Line2D()': the destructor:
      Python removes its C++ QGeoProjectionWebMercator::Line2D by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QGeoProjectionWebMercator::Line2D is created at the first use,
      not by 'QGeoProjectionWebMercator::Line2D(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGeoProjectionWebMercator::Line2D back gives a copy
      the ritual made for Python, in a new cute
      QGeoProjectionWebMercator::Line2D.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDoubleVector2D = WAIT['QDoubleVector2D']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGeoProjectionWebMercator::Line2D'

    #  Qt's '~QGeoProjectionWebMercator::Line2D()'. Naming it makes this a
    #  value class: Python owns every C++ QGeoProjectionWebMercator::Line2D
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QGeoProjectionWebMercator6Line2DD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QGeoProjectionWebMercator::Line2D::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-line2d.html#isValid
      """
      #  bool QGeoProjectionWebMercator::Line2D::isValid() const
      return self.uglySide.call(
          'ritual_ZNK25QGeoProjectionWebMercator6Line2D7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGeoProjectionWebMercator::Line2D::Line2D()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-line2d.html#Line2D
      """
      #  QGeoProjectionWebMercator::Line2D::Line2D()
      self._noteCreation(
          QGeoProjectionWebMercator.Line2D, lambda: Rituals.call(
              'ritual_ZN25QGeoProjectionWebMercator6Line2DC1Ev',
          ))

    @overload(QDoubleVector2D, QDoubleVector2D)
    def __init__(
        self,
        linePoint: QDoubleVector2D,
        lineDirection: QDoubleVector2D,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QGeoProjectionWebMercator::Line2D::Line2D(const QDoubleVector2D
      &linePoint, const QDoubleVector2D &lineDirection)', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-line2d.html#Line2D

      Parameters
      ----------

      linePoint : QDoubleVector2D
        Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
        Python's own.

      lineDirection : QDoubleVector2D
        Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
        Python's own.
      """
      #  QGeoProjectionWebMercator::Line2D::Line2D(const QDoubleVector2D
      #      &linePoint, const QDoubleVector2D &lineDirection)
      self._noteCreation(
          QGeoProjectionWebMercator.Line2D, lambda: Rituals.call(
              'ritual_ZN25QGeoProjectionWebMercator6Line2DC1ERK15QDoubleVec'
              'tor2DS3_',
              self._valueOf(linePoint), self._valueOf(lineDirection),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class Plane(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGeoProjectionWebMercator::Plane: a plain Python
    object standing in front of one C++ QGeoProjectionWebMercator::Plane.

    C++ hands a QGeoProjectionWebMercator::Plane around as a copy, so every
    C++ QGeoProjectionWebMercator::Plane behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QGeoProjectionWebMercator::Plane that has a ritual
    and that Python can call so far, 2 names in all: 'lineIntersection',
    'isValid'. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QDoubleVector3D
      QGeoProjectionWebMercator::Plane::lineIntersection(const
      QDoubleVector3D &linePoint, const QDoubleVector3D &lineDirection,
      double &s) const': takes a number to change where it is.
    - Qt's 'QGeoProjectionWebMercator::Plane::~Plane()': the destructor:
      Python removes its C++ QGeoProjectionWebMercator::Plane by it, and has
      no other use for it.

    What has no ritual
    ------------------

    1 of the 7 functions Qt declares: 1 Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file.

    What to expect
    --------------

    - The C++ QGeoProjectionWebMercator::Plane is created at the first use,
      not by 'QGeoProjectionWebMercator::Plane(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGeoProjectionWebMercator::Plane back gives a copy
      the ritual made for Python, in a new cute
      QGeoProjectionWebMercator::Plane.
    - Each name of Qt's QGeoProjectionWebMercator::Plane that has no cute
      function yet, 'planeXYIntersection', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QDoubleVector3D = WAIT['QDoubleVector3D']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGeoProjectionWebMercator::Plane'

    #  Qt's '~QGeoProjectionWebMercator::Plane()'. Naming it makes this a
    #  value class: Python owns every C++ QGeoProjectionWebMercator::Plane
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN25QGeoProjectionWebMercator5PlaneD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QDoubleVector3D, QDoubleVector3D)
    def lineIntersection(
        self,
        linePoint: QDoubleVector3D,
        lineDirection: QDoubleVector3D,
    ) -> QDoubleVector3D:
      """
      Calls Qt's 'QDoubleVector3D
      QGeoProjectionWebMercator::Plane::lineIntersection(const
      QDoubleVector3D &linePoint, const QDoubleVector3D &lineDirection)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-plane.html

      Parameters
      ----------

      linePoint : QDoubleVector3D
        Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
        Python's own.

      lineDirection : QDoubleVector3D
        Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
        Python's own.

      Returns
      -------

      QDoubleVector3D
        A new cute QDoubleVector3D around the copy Qt gave back. Python owns
        it.
      """
      #  QDoubleVector3D
      #      QGeoProjectionWebMercator::Plane::lineIntersection(const
      #      QDoubleVector3D &linePoint, const QDoubleVector3D
      #      &lineDirection) const
      address = self.uglySide.call(
          'ritual_ZNK25QGeoProjectionWebMercator5Plane16lineIntersectionERK'
          '15QDoubleVector3DS3_',
          self._valueOf(linePoint), self._valueOf(lineDirection),
      )
      from ..QtPositioning import QDoubleVector3D
      return QDoubleVector3D._cuteOwning(address)

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QGeoProjectionWebMercator::Plane::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-plane.html#isValid
      """
      #  bool QGeoProjectionWebMercator::Plane::isValid() const
      return self.uglySide.call(
          'ritual_ZNK25QGeoProjectionWebMercator5Plane7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGeoProjectionWebMercator::Plane::Plane()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-plane.html#Plane
      """
      #  QGeoProjectionWebMercator::Plane::Plane()
      self._noteCreation(
          QGeoProjectionWebMercator.Plane, lambda: Rituals.call(
              'ritual_ZN25QGeoProjectionWebMercator5PlaneC1Ev',
          ))

    @overload(QDoubleVector3D, QDoubleVector3D)
    def __init__(
        self,
        planePoint: QDoubleVector3D,
        planeNormal: QDoubleVector3D,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QGeoProjectionWebMercator::Plane::Plane(const QDoubleVector3D
      &planePoint, const QDoubleVector3D &planeNormal)', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgeoprojectionwebmercator-plane.html#Plane

      Parameters
      ----------

      planePoint : QDoubleVector3D
        Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
        Python's own.

      planeNormal : QDoubleVector3D
        Passed on as a value: Qt reads the C++ QDoubleVector3D, which stays
        Python's own.
      """
      #  QGeoProjectionWebMercator::Plane::Plane(const QDoubleVector3D
      #      &planePoint, const QDoubleVector3D &planeNormal)
      self._noteCreation(
          QGeoProjectionWebMercator.Plane, lambda: Rituals.call(
              'ritual_ZN25QGeoProjectionWebMercator5PlaneC1ERK15QDoubleVect'
              'or3DS3_',
              self._valueOf(planePoint), self._valueOf(planeNormal),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def planeXYIntersection(*__, **_) -> Never:
      """
      Qt's 'Line2D QGeoProjectionWebMercator::Plane::planeXYIntersection()
      const': Qt's library has no name for it, and its code in Qt's source
      does not compile apart from its file: use of undeclared identifier
      'xyNormal'.
      """
      raise NotImplementedError(
          "'QGeoProjectionWebMercator.Plane.planeXYIntersection' has no "
          "cute function yet. Qt's 'Line2D "
          "QGeoProjectionWebMercator::Plane::planeXYIntersection() const': "
          "Qt's library has no name for it, and its code in Qt's source "
          "does not compile apart from its file: use of undeclared "
          "identifier 'xyNormal'.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoProjectionWebMercator'

  #  A C++ QGeoProjectionWebMercator Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoProjectionWebMercator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def minimumZoom(self) -> float:
    """
    Calls Qt's 'double QGeoProjectionWebMercator::minimumZoom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#minimumZoom
    """
    #  double QGeoProjectionWebMercator::minimumZoom() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator11minimumZoomEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator11minimumZoomEv'
    return self.uglySide.call(ritual)

  def projectionTransformation(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    QGeoProjectionWebMercator::projectionTransformation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QGeoProjectionWebMercator::projectionTransformation() const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator24projectionTransformationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator24projectionTransformat'
          'ionEv')
    address = self.uglySide.call(ritual)
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def projectionTransformation_centered(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    QGeoProjectionWebMercator::projectionTransformation_centered() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4
    #      QGeoProjectionWebMercator::projectionTransformation_centered()
    #      const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator33projectionTransformation_ce'
        'nteredEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator33projectionTransformat'
          'ion_centeredEv')
    address = self.uglySide.call(ritual)
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def qsgTransform(self) -> QMatrix4x4:
    """
    Calls Qt's 'const QMatrix4x4 &QGeoProjectionWebMercator::qsgTransform()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#qsgTransform

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  const QMatrix4x4 &QGeoProjectionWebMercator::qsgTransform() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator12qsgTransformEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator12qsgTransformEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def centerMercator(self) -> QDoubleVector3D:
    """
    Calls Qt's 'QDoubleVector3D QGeoProjectionWebMercator::centerMercator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#centerMercator

    Returns
    -------

    QDoubleVector3D
      A new cute QDoubleVector3D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector3D QGeoProjectionWebMercator::centerMercator() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator14centerMercatorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator14centerMercatorEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QDoubleVector3D
    return QDoubleVector3D._cuteOwning(address)

  @overload(QGeoCameraData)
  def maximumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double
    QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoProjectionWebMercator::maximumCenterLatitudeAtZoom(const
    #      QGeoCameraData &cameraData) const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator27maximumCenterLatitudeAtZoom'
        'ERK14QGeoCameraData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator27maximumCenterLatitude'
          'AtZoomERK14QGeoCameraData')
    return self.uglySide.call(ritual, self._valueOf(cameraData))

  @overload(QGeoCameraData)
  def minimumCenterLatitudeAtZoom(self, cameraData: QGeoCameraData) -> float:
    """
    Calls Qt's 'double
    QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(const
    QGeoCameraData &cameraData) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  double QGeoProjectionWebMercator::minimumCenterLatitudeAtZoom(const
    #      QGeoCameraData &cameraData) const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator27minimumCenterLatitudeAtZoom'
        'ERK14QGeoCameraData')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator27minimumCenterLatitude'
          'AtZoomERK14QGeoCameraData')
    return self.uglySide.call(ritual, self._valueOf(cameraData))

  def cameraData(self) -> QGeoCameraData:
    """
    Calls Qt's 'QGeoCameraData QGeoProjectionWebMercator::cameraData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#cameraData

    Returns
    -------

    QGeoCameraData
      A new cute QGeoCameraData around the copy Qt gave back. Python owns it.
    """
    #  QGeoCameraData QGeoProjectionWebMercator::cameraData() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator10cameraDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator10cameraDataEv'
    address = self.uglySide.call(ritual)
    from . import QGeoCameraData
    return QGeoCameraData._cuteOwning(address)

  @overload(QDoubleVector2D)
  @overload(QDoubleVector2D, bool)
  def itemPositionToCoordinate(
      self,
      pos: QDoubleVector2D,
      clipToViewport: bool = True,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate
    QGeoProjectionWebMercator::itemPositionToCoordinate(const QDoubleVector2D
    &pos, bool clipToViewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

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
    #  QGeoCoordinate
    #      QGeoProjectionWebMercator::itemPositionToCoordinate(const
    #      QDoubleVector2D &pos, bool clipToViewport) const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator24itemPositionToCoordinateERK'
        '15QDoubleVector2Db')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator24itemPositionToCoordin'
          'ateERK15QDoubleVector2Db')
    address = self.uglySide.call(ritual, self._valueOf(pos), clipToViewport)
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
    QGeoProjectionWebMercator::coordinateToItemPosition(const QGeoCoordinate
    &coordinate, bool clipToViewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

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
    #  QDoubleVector2D
    #      QGeoProjectionWebMercator::coordinateToItemPosition(const
    #      QGeoCoordinate &coordinate, bool clipToViewport) const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator24coordinateToItemPositionERK'
        '14QGeoCoordinateb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator24coordinateToItemPosit'
          'ionERK14QGeoCoordinateb')
    address = self.uglySide.call(
        ritual, self._valueOf(coordinate), clipToViewport,
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  def projectionGroup(self) -> QGeoProjection.ProjectionGroup:
    """
    Calls Qt's 'QGeoProjection::ProjectionGroup
    QGeoProjectionWebMercator::projectionGroup() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#projectionGroup

    Returns
    -------

    QGeoProjection.ProjectionGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoProjection.ProjectionGroup(number)' gives.
    """
    #  QGeoProjection::ProjectionGroup
    #      QGeoProjectionWebMercator::projectionGroup() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator15projectionGroupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator15projectionGroupEv'
    return QGeoProjection.ProjectionGroup(self.uglySide.call(ritual))

  def datum(self) -> QGeoProjection.Datum:
    """
    Calls Qt's 'QGeoProjection::Datum QGeoProjectionWebMercator::datum()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#datum

    Returns
    -------

    QGeoProjection.Datum
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoProjection.Datum(number)' gives.
    """
    #  QGeoProjection::Datum QGeoProjectionWebMercator::datum() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator5datumEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator5datumEv'
    return QGeoProjection.Datum(self.uglySide.call(ritual))

  def projectionType(self) -> QGeoProjection.ProjectionType:
    """
    Calls Qt's 'QGeoProjection::ProjectionType
    QGeoProjectionWebMercator::projectionType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#projectionType

    Returns
    -------

    QGeoProjection.ProjectionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoProjection.ProjectionType(number)' gives.
    """
    #  QGeoProjection::ProjectionType
    #      QGeoProjectionWebMercator::projectionType() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator14projectionTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator14projectionTypeEv'
    return QGeoProjection.ProjectionType(self.uglySide.call(ritual))

  @overload(QGeoCoordinate, QPointF)
  def anchorCoordinateToPoint(
      self,
      coordinate: QGeoCoordinate,
      anchorPoint: QPointF,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate
    QGeoProjectionWebMercator::anchorCoordinateToPoint(const QGeoCoordinate
    &coordinate, const QPointF &anchorPoint) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

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
    #  QGeoCoordinate
    #      QGeoProjectionWebMercator::anchorCoordinateToPoint(const
    #      QGeoCoordinate &coordinate, const QPointF &anchorPoint) const
    ritual = (
        'ritual_ZNK25QGeoProjectionWebMercator23anchorCoordinateToPointERK1'
        '4QGeoCoordinateRK7QPointF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGeoProjectionWebMercator23anchorCoordinateToPoi'
          'ntERK14QGeoCoordinateRK7QPointF')
    address = self.uglySide.call(
        ritual,
        self._valueOf(coordinate), self._valueOf(anchorPoint, 'QPointF'),
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def visibleRegion(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QGeoProjectionWebMercator::visibleRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#visibleRegion

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QGeoProjectionWebMercator::visibleRegion() const
    ritual = 'ritual_ZNK25QGeoProjectionWebMercator13visibleRegionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGeoProjectionWebMercator13visibleRegionEv'
    address = self.uglySide.call(ritual)
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def mapWidth(self) -> float:
    """
    Calls Qt's 'double QGeoProjectionWebMercator::mapWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#mapWidth
    """
    #  double QGeoProjectionWebMercator::mapWidth() const
    return self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator8mapWidthEv',
    )

  def mapHeight(self) -> float:
    """
    Calls Qt's 'double QGeoProjectionWebMercator::mapHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#mapHeight
    """
    #  double QGeoProjectionWebMercator::mapHeight() const
    return self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator9mapHeightEv',
    )

  @overload(QGeoCoordinate)
  def geoToMapProjection(
      self,
      coordinate: QGeoCoordinate,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjectionWebMercator::geoToMapProjection(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#geoToMapProjection

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QGeoProjectionWebMercator::geoToMapProjection(const
    #      QGeoCoordinate &coordinate) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator18geoToMapProjectionERK14QGeo'
        'Coordinate',
        self._valueOf(coordinate),
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @overload(QDoubleVector2D)
  def mapProjectionToGeo(
      self,
      projection: QDoubleVector2D,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate
    QGeoProjectionWebMercator::mapProjectionToGeo(const QDoubleVector2D
    &projection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#mapProjectionToGeo

    Parameters
    ----------

    projection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoProjectionWebMercator::mapProjectionToGeo(const
    #      QDoubleVector2D &projection) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator18mapProjectionToGeoERK15QDou'
        'bleVector2D',
        self._valueOf(projection),
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QDoubleVector2D)
  def projectionWrapFactor(self, projection: QDoubleVector2D) -> int:
    """
    Calls Qt's 'int QGeoProjectionWebMercator::projectionWrapFactor(const
    QDoubleVector2D &projection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    projection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  int QGeoProjectionWebMercator::projectionWrapFactor(const
    #      QDoubleVector2D &projection) const
    return self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator20projectionWrapFactorERK15QD'
        'oubleVector2D',
        self._valueOf(projection),
    )

  @overload(QDoubleVector2D)
  def wrapMapProjection(
      self,
      projection: QDoubleVector2D,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjectionWebMercator::wrapMapProjection(const QDoubleVector2D
    &projection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#wrapMapProjection

    Parameters
    ----------

    projection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QGeoProjectionWebMercator::wrapMapProjection(const
    #      QDoubleVector2D &projection) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator17wrapMapProjectionERK15QDoub'
        'leVector2D',
        self._valueOf(projection),
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @overload(QDoubleVector2D)
  def unwrapMapProjection(
      self,
      wrappedProjection: QDoubleVector2D,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjectionWebMercator::unwrapMapProjection(const QDoubleVector2D
    &wrappedProjection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#unwrapMapProjection

    Parameters
    ----------

    wrappedProjection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D QGeoProjectionWebMercator::unwrapMapProjection(const
    #      QDoubleVector2D &wrappedProjection) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator19unwrapMapProjectionERK15QDo'
        'ubleVector2D',
        self._valueOf(wrappedProjection),
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @overload(QDoubleVector2D)
  def wrappedMapProjectionToItemPosition(
      self,
      wrappedProjection: QDoubleVector2D,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjectionWebMercator::wrappedMapProjectionToItemPosition(const
    QDoubleVector2D &wrappedProjection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    wrappedProjection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D
    #      QGeoProjectionWebMercator::wrappedMapProjectionToItemPosition(
    #      const QDoubleVector2D &wrappedProjection) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator34wrappedMapProjectionToItemP'
        'ositionERK15QDoubleVector2D',
        self._valueOf(wrappedProjection),
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @overload(QDoubleVector2D)
  def itemPositionToWrappedMapProjection(
      self,
      itemPosition: QDoubleVector2D,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjectionWebMercator::itemPositionToWrappedMapProjection(const
    QDoubleVector2D &itemPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    itemPosition : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D
    #      QGeoProjectionWebMercator::itemPositionToWrappedMapProjection(
    #      const QDoubleVector2D &itemPosition) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator34itemPositionToWrappedMapPro'
        'jectionERK15QDoubleVector2D',
        self._valueOf(itemPosition),
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @overload(QGeoCoordinate)
  def geoToWrappedMapProjection(
      self,
      coordinate: QGeoCoordinate,
  ) -> QDoubleVector2D:
    """
    Calls Qt's 'QDoubleVector2D
    QGeoProjectionWebMercator::geoToWrappedMapProjection(const QGeoCoordinate
    &coordinate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QDoubleVector2D
      A new cute QDoubleVector2D around the copy Qt gave back. Python owns
      it.
    """
    #  QDoubleVector2D
    #      QGeoProjectionWebMercator::geoToWrappedMapProjection(const
    #      QGeoCoordinate &coordinate) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator25geoToWrappedMapProjectionER'
        'K14QGeoCoordinate',
        self._valueOf(coordinate),
    )
    from ..QtPositioning import QDoubleVector2D
    return QDoubleVector2D._cuteOwning(address)

  @overload(QDoubleVector2D)
  def wrappedMapProjectionToGeo(
      self,
      wrappedProjection: QDoubleVector2D,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate
    QGeoProjectionWebMercator::wrappedMapProjectionToGeo(const
    QDoubleVector2D &wrappedProjection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    wrappedProjection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate
    #      QGeoProjectionWebMercator::wrappedMapProjectionToGeo(const
    #      QDoubleVector2D &wrappedProjection) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator25wrappedMapProjectionToGeoER'
        'K15QDoubleVector2D',
        self._valueOf(wrappedProjection),
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  @overload(QGeoCoordinate, QPointF, float)
  def quickItemTransformation(
      self,
      coordinate: QGeoCoordinate,
      anchorPoint: QPointF,
      zoomLevel: float,
  ) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4
    QGeoProjectionWebMercator::quickItemTransformation(const QGeoCoordinate
    &coordinate, const QPointF &anchorPoint, qreal zoomLevel) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    anchorPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    zoomLevel : float
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QGeoProjectionWebMercator::quickItemTransformation(const
    #      QGeoCoordinate &coordinate, const QPointF &anchorPoint, qreal
    #      zoomLevel) const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator23quickItemTransformationERK1'
        '4QGeoCoordinateRK7QPointFd',
        self._valueOf(coordinate), self._valueOf(anchorPoint, 'QPointF'),
        zoomLevel,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QDoubleVector2D)
  def isProjectable(self, wrappedProjection: QDoubleVector2D) -> bool:
    """
    Calls Qt's 'bool QGeoProjectionWebMercator::isProjectable(const
    QDoubleVector2D &wrappedProjection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#isProjectable

    Parameters
    ----------

    wrappedProjection : QDoubleVector2D
      Passed on as a value: Qt reads the C++ QDoubleVector2D, which stays
      Python's own.
    """
    #  bool QGeoProjectionWebMercator::isProjectable(const QDoubleVector2D
    #      &wrappedProjection) const
    return self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator13isProjectableERK15QDoubleVe'
        'ctor2D',
        self._valueOf(wrappedProjection),
    )

  def visibleGeometry(self) -> QList[QDoubleVector2D]:
    """
    Calls Qt's 'QList<QDoubleVector2D>
    QGeoProjectionWebMercator::visibleGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#visibleGeometry

    Returns
    -------

    QList[QDoubleVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDoubleVector2D> QGeoProjectionWebMercator::visibleGeometry()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator15visibleGeometryEv',
    )
    from ..QtPositioning import QDoubleVector2D
    return QList[QDoubleVector2D]._cuteOwning(address)

  def visibleGeometryExpanded(self) -> QList[QDoubleVector2D]:
    """
    Calls Qt's 'QList<QDoubleVector2D>
    QGeoProjectionWebMercator::visibleGeometryExpanded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html

    Returns
    -------

    QList[QDoubleVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDoubleVector2D>
    #      QGeoProjectionWebMercator::visibleGeometryExpanded() const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator23visibleGeometryExpandedEv',
    )
    from ..QtPositioning import QDoubleVector2D
    return QList[QDoubleVector2D]._cuteOwning(address)

  def projectableGeometry(self) -> QList[QDoubleVector2D]:
    """
    Calls Qt's 'QList<QDoubleVector2D>
    QGeoProjectionWebMercator::projectableGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#projectableGeometry

    Returns
    -------

    QList[QDoubleVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QDoubleVector2D>
    #      QGeoProjectionWebMercator::projectableGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK25QGeoProjectionWebMercator19projectableGeometryEv',
    )
    from ..QtPositioning import QDoubleVector2D
    return QList[QDoubleVector2D]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setVisibleArea(self, visibleArea: QRectF) -> None:
    """
    Calls Qt's 'void QGeoProjectionWebMercator::setVisibleArea(const QRectF
    &visibleArea)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#setVisibleArea

    Parameters
    ----------

    visibleArea : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGeoProjectionWebMercator::setVisibleArea(const QRectF
    #      &visibleArea)
    ritual = 'ritual_ZN25QGeoProjectionWebMercator14setVisibleAreaERK6QRectF'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGeoProjectionWebMercator14setVisibleAreaERK6QRec'
          'tF')
    self.uglySide.call(ritual, self._valueOf(visibleArea))

  @overload(QSize)
  def setViewportSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QGeoProjectionWebMercator::setViewportSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#setViewportSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QGeoProjectionWebMercator::setViewportSize(const QSize &size)
    ritual = 'ritual_ZN25QGeoProjectionWebMercator15setViewportSizeERK5QSize'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGeoProjectionWebMercator15setViewportSizeERK5QSi'
          'ze')
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QGeoCameraData)
  @overload(QGeoCameraData, bool)
  def setCameraData(
      self,
      cameraData: QGeoCameraData,
      force: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QGeoProjectionWebMercator::setCameraData(const
    QGeoCameraData &cameraData, bool force)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#setCameraData

    Parameters
    ----------

    cameraData : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.

    force : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGeoProjectionWebMercator::setCameraData(const QGeoCameraData
    #      &cameraData, bool force)
    ritual = (
        'ritual_ZN25QGeoProjectionWebMercator13setCameraDataERK14QGeoCamera'
        'Datab')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGeoProjectionWebMercator13setCameraDataERK14QGeo'
          'CameraDatab')
    self.uglySide.call(ritual, self._valueOf(cameraData), force)

  @overload(float, QGeoCoordinate)
  def setBearing(self, bearing: float, coordinate: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoProjectionWebMercator::setBearing(qreal bearing,
    const QGeoCoordinate &coordinate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#setBearing

    Parameters
    ----------

    bearing : float
      Passed on as it is.

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoProjectionWebMercator::setBearing(qreal bearing, const
    #      QGeoCoordinate &coordinate)
    ritual = (
        'ritual_ZN25QGeoProjectionWebMercator10setBearingEdRK14QGeoCoordina'
        'te')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGeoProjectionWebMercator10setBearingEdRK14QGeoCo'
          'ordinate')
    return self.uglySide.call(ritual, bearing, self._valueOf(coordinate))

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
    Notes what was given, for Qt's
    'QGeoProjectionWebMercator::QGeoProjectionWebMercator()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html
    """
    #  QGeoProjectionWebMercator::QGeoProjectionWebMercator()
    self._noteCreation(QGeoProjectionWebMercator, lambda: Rituals.call(
        'ritual_ZN25QGeoProjectionWebMercatorC1Ev',
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

  def setupCamera(self) -> None:
    """
    Calls Qt's 'void QGeoProjectionWebMercator::setupCamera()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#setupCamera
    """
    #  void QGeoProjectionWebMercator::setupCamera()
    self.uglySide.call('ritual_ZN25QGeoProjectionWebMercator11setupCameraEv')

  def updateVisibleRegion(self) -> None:
    """
    Calls Qt's 'void QGeoProjectionWebMercator::updateVisibleRegion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoprojectionwebmercator.html#updateVisibleRegion
    """
    #  void QGeoProjectionWebMercator::updateVisibleRegion()
    self.uglySide.call(
        'ritual_ZN25QGeoProjectionWebMercator19updateVisibleRegionEv',
    )

  @staticmethod
  def fitViewportToGeoRectangle(*__, **_) -> Never:
    """
    Qt's 'QPair<QGeoCoordinate, qreal>
    QGeoProjectionWebMercator::fitViewportToGeoRectangle(const QGeoRectangle
    &rectangle, const QMargins &margins) const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QGeoProjectionWebMercator.fitViewportToGeoRectangle' has no cute "
        "function yet. Qt's 'QPair<QGeoCoordinate, qreal> "
        "QGeoProjectionWebMercator::fitViewportToGeoRectangle(const "
        "QGeoRectangle &rectangle, const QMargins &margins) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def viewportToWrappedMapProjection(*__, **_) -> Never:
    """
    - Qt's 'QDoubleVector2D
      QGeoProjectionWebMercator::viewportToWrappedMapProjection(const
      QDoubleVector2D &itemPosition, double &s) const': Qt's library has no
      name for it, and its code in Qt's source does not compile apart from
      its file: use of undeclared identifier 'xyPlane'.
    - Qt's 'QDoubleVector2D
      QGeoProjectionWebMercator::viewportToWrappedMapProjection(const
      QDoubleVector2D &itemPosition) const': leans on
      'QGeoProjectionWebMercator::viewportToWrappedMapProjection(
      QDoubleVector2D const&, double&) const', which Qt's source does not
      mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGeoProjectionWebMercator.viewportToWrappedMapProjection' has no "
        "cute function yet. Qt's 'QDoubleVector2D "
        "QGeoProjectionWebMercator::viewportToWrappedMapProjection(const "
        "QDoubleVector2D &itemPosition, double &s) const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'xyPlane'. Qt's "
        "'QDoubleVector2D "
        "QGeoProjectionWebMercator::viewportToWrappedMapProjection(const "
        "QDoubleVector2D &itemPosition) const': leans on "
        "'QGeoProjectionWebMercator::viewportToWrappedMapProjection(QDoubleV"
        "ector2D const&, double&) const', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")
