"""
QGeoRouteSegment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeoroutesegment.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

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


class QGeoRouteSegment(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoRouteSegment: a plain Python object standing in
  front of one C++ QGeoRouteSegment.

  C++ hands a QGeoRouteSegment around as a copy, so every C++
  QGeoRouteSegment behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoRouteSegment that has a ritual and that Python
  can call so far, 15 names in all: '__eq__', '__ne__', 'isValid',
  'isLegLastSegment', 'setNextRouteSegment', 'nextRouteSegment',
  'setTravelTime', 'travelTime', 'setDistance', 'distance', 'setPath',
  'path', 'setManeuver', 'maneuver', 'isEqual'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoRouteSegment::QGeoRouteSegment(QGeoRouteSegment &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QGeoRouteSegment::~QGeoRouteSegment()': the destructor: Python
    removes its C++ QGeoRouteSegment by it, and has no other use for it.
  - Qt's 'QGeoRouteSegment &QGeoRouteSegment::operator=(const
    QGeoRouteSegment &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QGeoRouteSegment &QGeoRouteSegment::operator=(QGeoRouteSegment
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoRouteSegment::swap(QGeoRouteSegment &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QGeoRouteSegment::QGeoRouteSegment(
    QExplicitlySharedDataPointer<QGeoRouteSegmentPrivate> &&dd)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoRouteSegment is created at the first use, not by
    'QGeoRouteSegment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoRouteSegment back gives a copy the ritual made
    for Python, in a new cute QGeoRouteSegment.
  - Each name of Qt's QGeoRouteSegment that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoRouteSegment'

  #  Qt's '~QGeoRouteSegment()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoRouteSegment behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QGeoRouteSegmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoRouteSegment::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#isValid
    """
    #  bool QGeoRouteSegment::isValid() const
    return self.uglySide.call('ritual_ZNK16QGeoRouteSegment7isValidEv')

  def isLegLastSegment(self) -> bool:
    """
    Calls Qt's 'bool QGeoRouteSegment::isLegLastSegment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegment.html#isLegLastSegment
    """
    #  bool QGeoRouteSegment::isLegLastSegment() const
    return self.uglySide.call(
        'ritual_ZNK16QGeoRouteSegment16isLegLastSegmentEv',
    )

  def nextRouteSegment(self) -> QGeoRouteSegment:
    """
    Calls Qt's 'QGeoRouteSegment QGeoRouteSegment::nextRouteSegment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegment.html#nextRouteSegment

    Returns
    -------

    QGeoRouteSegment
      A new cute QGeoRouteSegment around the copy Qt gave back. Python owns
      it.
    """
    #  QGeoRouteSegment QGeoRouteSegment::nextRouteSegment() const
    address = self.uglySide.call(
        'ritual_ZNK16QGeoRouteSegment16nextRouteSegmentEv',
    )
    return QGeoRouteSegment._cuteOwning(address)

  def travelTime(self) -> int:
    """
    Calls Qt's 'int QGeoRouteSegment::travelTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#travelTime
    """
    #  int QGeoRouteSegment::travelTime() const
    return self.uglySide.call('ritual_ZNK16QGeoRouteSegment10travelTimeEv')

  def distance(self) -> float:
    """
    Calls Qt's 'qreal QGeoRouteSegment::distance() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#distance
    """
    #  qreal QGeoRouteSegment::distance() const
    return self.uglySide.call('ritual_ZNK16QGeoRouteSegment8distanceEv')

  def path(self) -> QList[QGeoCoordinate]:
    """
    Calls Qt's 'QList<QGeoCoordinate> QGeoRouteSegment::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#path

    Returns
    -------

    QList[QGeoCoordinate]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QGeoCoordinate> QGeoRouteSegment::path() const
    address = self.uglySide.call('ritual_ZNK16QGeoRouteSegment4pathEv')
    from ..QtPositioning import QGeoCoordinate
    return QList[QGeoCoordinate]._cuteOwning(address)

  def maneuver(self) -> QGeoManeuver:
    """
    Calls Qt's 'QGeoManeuver QGeoRouteSegment::maneuver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#maneuver

    Returns
    -------

    QGeoManeuver
      A new cute QGeoManeuver around the copy Qt gave back. Python owns it.
    """
    #  QGeoManeuver QGeoRouteSegment::maneuver() const
    address = self.uglySide.call('ritual_ZNK16QGeoRouteSegment8maneuverEv')
    from . import QGeoManeuver
    return QGeoManeuver._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QGeoRouteSegment) -> bool:
    """
    Calls Qt's 'bool QGeoRouteSegment::isEqual(const QGeoRouteSegment &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#isEqual

    Parameters
    ----------

    other : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  bool QGeoRouteSegment::isEqual(const QGeoRouteSegment &other) const
    return self.uglySide.call(
        'ritual_ZNK16QGeoRouteSegment7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def setNextRouteSegment(self, routeSegment: QGeoRouteSegment) -> None:
    """
    Calls Qt's 'void QGeoRouteSegment::setNextRouteSegment(const
    QGeoRouteSegment &routeSegment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegment.html#setNextRouteSegment

    Parameters
    ----------

    routeSegment : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  void QGeoRouteSegment::setNextRouteSegment(const QGeoRouteSegment
    #      &routeSegment)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteSegment19setNextRouteSegmentERKS_',
        self._valueOf(routeSegment),
    )

  @overload(int)
  def setTravelTime(self, secs: int) -> None:
    """
    Calls Qt's 'void QGeoRouteSegment::setTravelTime(int secs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegment.html#setTravelTime

    Parameters
    ----------

    secs : int
      Passed on as it is.
    """
    #  void QGeoRouteSegment::setTravelTime(int secs)
    self.uglySide.call('ritual_ZN16QGeoRouteSegment13setTravelTimeEi', secs)

  @overload(float)
  def setDistance(self, distance: float) -> None:
    """
    Calls Qt's 'void QGeoRouteSegment::setDistance(qreal distance)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#setDistance

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QGeoRouteSegment::setDistance(qreal distance)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteSegment11setDistanceEd', distance,
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, path: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QGeoRouteSegment::setPath(const QList<QGeoCoordinate>
    &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#setPath

    Parameters
    ----------

    path : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QGeoRouteSegment::setPath(const QList<QGeoCoordinate> &path)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteSegment7setPathERK5QListI14QGeoCoordinateE',
        self._valueOf(path),
    )

  @overload(QGeoManeuver)
  def setManeuver(self, maneuver: QGeoManeuver) -> None:
    """
    Calls Qt's 'void QGeoRouteSegment::setManeuver(const QGeoManeuver
    &maneuver)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#setManeuver

    Parameters
    ----------

    maneuver : QGeoManeuver
      Passed on as a value: Qt reads the C++ QGeoManeuver, which stays
      Python's own.
    """
    #  void QGeoRouteSegment::setManeuver(const QGeoManeuver &maneuver)
    self.uglySide.call(
        'ritual_ZN16QGeoRouteSegment11setManeuverERK12QGeoManeuver',
        self._valueOf(maneuver),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoRouteSegment) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoRouteSegment &lhs, const
    QGeoRouteSegment &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#operator==

    Parameters
    ----------

    rhs : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  bool operator==(const QGeoRouteSegment &lhs, const QGeoRouteSegment
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QGeoRouteSegmentS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGeoRouteSegment) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoRouteSegment &lhs, const
    QGeoRouteSegment &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeoroutesegment.html#operator!=

    Parameters
    ----------

    rhs : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoRouteSegment &lhs, const QGeoRouteSegment
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QGeoRouteSegmentS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteSegment::QGeoRouteSegment()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegment.html#QGeoRouteSegment
    """
    #  QGeoRouteSegment::QGeoRouteSegment()
    self._noteCreation(QGeoRouteSegment, lambda: Rituals.call(
        'ritual_ZN16QGeoRouteSegmentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoRouteSegment) -> None:
    """
    Notes what was given, for Qt's 'QGeoRouteSegment::QGeoRouteSegment(const
    QGeoRouteSegment &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeoroutesegment.html#QGeoRouteSegment

    Parameters
    ----------

    other : QGeoRouteSegment
      Passed on as a value: Qt reads the C++ QGeoRouteSegment, which stays
      Python's own.
    """
    #  QGeoRouteSegment::QGeoRouteSegment(const QGeoRouteSegment &other)
    self._noteCreation(QGeoRouteSegment, lambda: Rituals.call(
        'ritual_ZN16QGeoRouteSegmentC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoRouteSegment::swap(QGeoRouteSegment &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoRouteSegment.swap' has no cute function yet. Qt's 'void "
        "QGeoRouteSegment::swap(QGeoRouteSegment &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QGeoRouteSegment>': the list of QGeoRouteSegment, which
#  'QList[QGeoRouteSegment]' gives. It is made here, so that there is one as
#  soon as there can be a QGeoRouteSegment.
QList.createKind(
    QGeoRouteSegment, 'value',
    make='ritual_list_make_QGeoRouteSegment',
    add='ritual_list_add_QGeoRouteSegment',
    size='ritual_list_size_QGeoRouteSegment',
    at='ritual_list_at_QGeoRouteSegment',
    drop='ritual_list_drop_QGeoRouteSegment',
)
