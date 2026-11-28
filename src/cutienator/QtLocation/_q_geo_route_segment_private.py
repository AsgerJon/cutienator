"""
QGeoRouteSegmentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeoroutesegment_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoRouteSegmentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtPositioning import QGeoCoordinate
  from . import QGeoManeuver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoManeuver = WAIT['QGeoManeuver']


class QGeoRouteSegmentPrivate(QSharedData):
  """
  The cute side of Qt's QGeoRouteSegmentPrivate: a plain Python object
  standing in front of one C++ QGeoRouteSegmentPrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoRouteSegmentPrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoRouteSegmentPrivate around as a copy, so every C++
  QGeoRouteSegmentPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoRouteSegmentPrivate that has a ritual and that
  Python can call so far, 12 names in all: 'valid', 'setValid',
  'isLegLastSegment', 'setLegLastSegment', 'travelTime', 'setTravelTime',
  'distance', 'setDistance', 'path', 'setPath', 'maneuver', 'setManeuver'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRouteSegmentPrivate
    *QGeoRouteSegmentPrivate::get(QGeoRouteSegment &segment)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate>
    QGeoRouteSegmentPrivate::nextRouteSegment() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QGeoRouteSegmentPrivate::setNextRouteSegment(const
    QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate> &next)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QGeoRouteSegmentPrivate::~QGeoRouteSegmentPrivate()': the
    destructor: Python removes its C++ QGeoRouteSegmentPrivate by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 18 functions Qt declares: 1 leans on
  'operator==(QGeoRouteSegmentPrivate const&, QGeoRouteSegmentPrivate
  const&)', which Qt's source does not mark for use from outside Qt and has
  no code for that could be taken.

  What to expect
  --------------

  - The C++ QGeoRouteSegmentPrivate is created at the first use, not by
    'QGeoRouteSegmentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoRouteSegmentPrivate back gives a copy the ritual
    made for Python, in a new cute QGeoRouteSegmentPrivate.
  - Each name of Qt's QGeoRouteSegmentPrivate that has no cute function yet,
    'get', 'nextRouteSegment', 'setNextRouteSegment', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteSegmentPrivate'

  #  Qt's '~QGeoRouteSegmentPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoRouteSegmentPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QGeoRouteSegmentPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def valid(self) -> bool:
    """
    Calls Qt's 'bool QGeoRouteSegmentPrivate::valid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#valid
    """
    #  bool QGeoRouteSegmentPrivate::valid() const
    return self.uglySide.call('ritual_ZNK23QGeoRouteSegmentPrivate5validEv')

  def isLegLastSegment(self) -> bool:
    """
    Calls Qt's 'bool QGeoRouteSegmentPrivate::isLegLastSegment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#isLegLastSegment
    """
    #  bool QGeoRouteSegmentPrivate::isLegLastSegment() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoRouteSegmentPrivate16isLegLastSegmentEv',
    )

  def travelTime(self) -> int:
    """
    Calls Qt's 'int QGeoRouteSegmentPrivate::travelTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#travelTime
    """
    #  int QGeoRouteSegmentPrivate::travelTime() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoRouteSegmentPrivate10travelTimeEv',
    )

  def distance(self) -> float:
    """
    Calls Qt's 'qreal QGeoRouteSegmentPrivate::distance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#distance
    """
    #  qreal QGeoRouteSegmentPrivate::distance() const
    return self.uglySide.call(
        'ritual_ZNK23QGeoRouteSegmentPrivate8distanceEv',
    )

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoRouteSegmentPrivate::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoRouteSegmentPrivate::path() const
    address = self.uglySide.call(
        'ritual_ZNK23QGeoRouteSegmentPrivate4pathEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def maneuver(self) -> QGeoManeuver:
    """
    Calls Qt's 'QGeoManeuver QGeoRouteSegmentPrivate::maneuver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#maneuver

    Returns
    -------

    QGeoManeuver
      A new cute QGeoManeuver around the copy Qt gave back. Python owns it.
    """
    #  QGeoManeuver QGeoRouteSegmentPrivate::maneuver() const
    address = self.uglySide.call(
        'ritual_ZNK23QGeoRouteSegmentPrivate8maneuverEv',
    )
    from . import QGeoManeuver
    return QGeoManeuver._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setValid(self, valid: bool) -> None:
    """
    Calls Qt's 'void QGeoRouteSegmentPrivate::setValid(bool valid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#setValid

    Parameters
    ----------

    valid : bool
      Passed on as it is.
    """
    #  void QGeoRouteSegmentPrivate::setValid(bool valid)
    self.uglySide.call(
        'ritual_ZN23QGeoRouteSegmentPrivate8setValidEb', valid,
    )

  @overload(bool)
  def setLegLastSegment(self, lastSegment: bool) -> None:
    """
    Calls Qt's 'void QGeoRouteSegmentPrivate::setLegLastSegment(bool
    lastSegment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#setLegLastSegment

    Parameters
    ----------

    lastSegment : bool
      Passed on as it is.
    """
    #  void QGeoRouteSegmentPrivate::setLegLastSegment(bool lastSegment)
    self.uglySide.call(
        'ritual_ZN23QGeoRouteSegmentPrivate17setLegLastSegmentEb',
        lastSegment,
    )

  @overload(int)
  def setTravelTime(self, travelTime: int) -> None:
    """
    Calls Qt's 'void QGeoRouteSegmentPrivate::setTravelTime(int travelTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#setTravelTime

    Parameters
    ----------

    travelTime : int
      Passed on as it is.
    """
    #  void QGeoRouteSegmentPrivate::setTravelTime(int travelTime)
    self.uglySide.call(
        'ritual_ZN23QGeoRouteSegmentPrivate13setTravelTimeEi', travelTime,
    )

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QGeoRouteSegmentPrivate::setDistance(qreal distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QGeoRouteSegmentPrivate::setDistance(qreal distance)
    self.uglySide.call(
        'ritual_ZN23QGeoRouteSegmentPrivate11setDistanceEd', distance,
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoRouteSegmentPrivate::setPath(const
    QList<QGeoCoordinate> &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#setPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRouteSegmentPrivate::setPath(const QList<QGeoCoordinate>
    #      &path)
    self.uglySide.call(
        'ritual_ZN23QGeoRouteSegmentPrivate7setPathERK5QListI14QGeoCoordina'
        'teE',
        self._valueOf(path),
    )

  @overload(QGeoManeuver)
  def setManeuver(self, maneuver: QGeoManeuver) -> None:
    """
    Calls Qt's 'void QGeoRouteSegmentPrivate::setManeuver(const QGeoManeuver
    &maneuver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html#setManeuver

    Parameters
    ----------

    maneuver : QGeoManeuver
      Passed on as a value: Qt reads the C++ QGeoManeuver, which stays
      Python's own.
    """
    #  void QGeoRouteSegmentPrivate::setManeuver(const QGeoManeuver
    #      &maneuver)
    self.uglySide.call(
        'ritual_ZN23QGeoRouteSegmentPrivate11setManeuverERK12QGeoManeuver',
        self._valueOf(maneuver),
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
    'QGeoRouteSegmentPrivate::QGeoRouteSegmentPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegmentprivate.html
    """
    #  QGeoRouteSegmentPrivate::QGeoRouteSegmentPrivate()
    self._noteCreation(QGeoRouteSegmentPrivate, lambda: Rituals.call(
        'ritual_ZN23QGeoRouteSegmentPrivateC1Ev',
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
  def get(*__, **_) -> Never:
    """
    Qt's 'QGeoRouteSegmentPrivate
    *QGeoRouteSegmentPrivate::get(QGeoRouteSegment &segment)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteSegmentPrivate.get' has no cute function yet. Qt's "
        "'QGeoRouteSegmentPrivate "
        "*QGeoRouteSegmentPrivate::get(QGeoRouteSegment &segment)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def nextRouteSegment(*__, **_) -> Never:
    """
    Qt's 'QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate>
    QGeoRouteSegmentPrivate::nextRouteSegment() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QGeoRouteSegmentPrivate.nextRouteSegment' has no cute function "
        "yet. Qt's 'QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate> "
        "QGeoRouteSegmentPrivate::nextRouteSegment() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setNextRouteSegment(*__, **_) -> Never:
    """
    Qt's 'void QGeoRouteSegmentPrivate::setNextRouteSegment(const
    QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate> &next)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteSegmentPrivate.setNextRouteSegment' has no cute function "
        "yet. Qt's 'void QGeoRouteSegmentPrivate::setNextRouteSegment(const "
        "QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate> &next)': "
        "takes a type Python has no way to hand over yet.")
