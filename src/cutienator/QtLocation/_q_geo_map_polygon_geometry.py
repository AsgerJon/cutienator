"""
QGeoMapPolygonGeometry binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoMapPolygonGeometry to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QGeoMapItemGeometry

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QPainterPath


class QGeoMapPolygonGeometry(QGeoMapItemGeometry):
  """
  The cute side of Qt's QGeoMapPolygonGeometry: a plain Python object
  standing in front of one C++ QGeoMapPolygonGeometry.

  It is built on the cute 'QGeoMapItemGeometry', as Qt's
  QGeoMapPolygonGeometry is built on Qt's QGeoMapItemGeometry, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoMapPolygonGeometry that has a ritual and that
  Python can call so far, 3 names in all: 'setAssumeSimple', 'srcPath',
  'maxCoord'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QGeoMapPolygonGeometry::updateSourcePoints(const QGeoMap &map,
    const QList<QList<QDoubleVector2D>> &path, MapBorderBehaviour wrapping)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoMapPolygonGeometry is created at the first use, not by
    'QGeoMapPolygonGeometry(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoMapPolygonGeometry.
  - Each name of Qt's QGeoMapPolygonGeometry that has no cute function yet,
    'updateSourcePoints', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QGeoMapPolygonGeometry, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class MapBorderBehaviour(CuteNum):
    """
    The enum 'QGeoMapPolygonGeometry::MapBorderBehaviour' of Qt, with the 3
    names Qt gives in it.
    """

    DrawOnce = Kee[int](0)
    Duplicate = Kee[int](1)
    WrapAround = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoMapPolygonGeometry'

  #  A C++ QGeoMapPolygonGeometry Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoMapPolygonGeometry'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def srcPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QGeoMapPolygonGeometry::srcPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappolygongeometry.html#srcPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QGeoMapPolygonGeometry::srcPath() const
    address = self.uglySide.call(
        'ritual_ZNK22QGeoMapPolygonGeometry7srcPathEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  def maxCoord(self) -> float:
    """
    Calls Qt's 'qreal QGeoMapPolygonGeometry::maxCoord() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappolygongeometry.html#maxCoord
    """
    #  qreal QGeoMapPolygonGeometry::maxCoord() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoMapPolygonGeometry8maxCoordEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAssumeSimple(self, value: bool) -> None:
    """
    Calls Qt's 'void QGeoMapPolygonGeometry::setAssumeSimple(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappolygongeometry.html#setAssumeSimple

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QGeoMapPolygonGeometry::setAssumeSimple(bool value)
    self.uglySide.call(
        'ritual_ZN22QGeoMapPolygonGeometry15setAssumeSimpleEb', value,
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
    Notes what was given, for Qt's
    'QGeoMapPolygonGeometry::QGeoMapPolygonGeometry()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomappolygongeometry.html#QGeoMapPolygonGeometry
    """
    #  QGeoMapPolygonGeometry::QGeoMapPolygonGeometry()
    self._noteCreation(QGeoMapPolygonGeometry, lambda: Rituals.call(
        'ritual_ZN22QGeoMapPolygonGeometryC1Ev',
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

  @staticmethod
  def updateSourcePoints(*__, **_) -> Never:
    """
    Qt's 'void QGeoMapPolygonGeometry::updateSourcePoints(const QGeoMap &map,
    const QList<QList<QDoubleVector2D>> &path, MapBorderBehaviour wrapping)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoMapPolygonGeometry.updateSourcePoints' has no cute function "
        "yet. Qt's 'void QGeoMapPolygonGeometry::updateSourcePoints(const "
        "QGeoMap &map, const QList<QList<QDoubleVector2D>> &path, "
        "MapBorderBehaviour wrapping)': takes a type Python has no way to "
        "hand over yet.")
