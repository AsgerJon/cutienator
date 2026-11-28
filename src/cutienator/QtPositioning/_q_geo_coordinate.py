"""
QGeoCoordinate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioning/qgeocoordinate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QGeoCoordinate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoCoordinate: a plain Python object standing in
  front of one C++ QGeoCoordinate.

  C++ hands a QGeoCoordinate around as a copy, so every C++ QGeoCoordinate
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCoordinate that has a ritual and that Python can
  call so far, 17 names in all: '__eq__', '__ne__', 'isValid', 'type',
  'setLatitude', 'latitude', 'setLongitude', 'longitude', 'setAltitude',
  'altitude', 'distanceTo', 'azimuthTo', 'atDistanceAndAzimuth', 'toString',
  'equals', '__rlshift__', 'debugStreaming'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoCoordinate::QGeoCoordinate(QGeoCoordinate &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QGeoCoordinate::~QGeoCoordinate()': the destructor: Python removes
    its C++ QGeoCoordinate by it, and has no other use for it.
  - Qt's 'QGeoCoordinate &QGeoCoordinate::operator=(const QGeoCoordinate
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoCoordinate &QGeoCoordinate::operator=(QGeoCoordinate &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoCoordinate::swap(QGeoCoordinate &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QGeoCoordinate::QGeoCoordinate(QGeoCoordinatePrivate &dd)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const QGeoCoordinate
    &coordinate)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &stream, QGeoCoordinate
    &coordinate)': an operator between other classes, written inside this
    one.
  - Qt's 'QDataStream &QGeoCoordinate::dataStreamOut(QDataStream &stream,
    const QGeoCoordinate &coordinate)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QDataStream &QGeoCoordinate::dataStreamIn(QDataStream &stream,
    QGeoCoordinate &coordinate)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  3 of the 34 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoCoordinate is created at the first use, not by
    'QGeoCoordinate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCoordinate back gives a copy the ritual made for
    Python, in a new cute QGeoCoordinate.
  - Each name of Qt's QGeoCoordinate that has no cute function yet,
    'dataStreamIn', 'dataStreamOut', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGeoCoordinate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CoordinateFormat(CuteNum):
    """
    The enum 'QGeoCoordinate::CoordinateFormat' of Qt, with the 6 names Qt
    gives in it.
    """

    Degrees = Kee[int](0)
    DegreesWithHemisphere = Kee[int](1)
    DegreesMinutes = Kee[int](2)
    DegreesMinutesWithHemisphere = Kee[int](3)
    DegreesMinutesSeconds = Kee[int](4)
    DegreesMinutesSecondsWithHemisphere = Kee[int](5)

  class CoordinateType(CuteNum):
    """
    The enum 'QGeoCoordinate::CoordinateType' of Qt, with the 3 names Qt
    gives in it.
    """

    InvalidCoordinate = Kee[int](0)
    Coordinate2D = Kee[int](1)
    Coordinate3D = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def equals(lhs: QGeoCoordinate, rhs: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool QGeoCoordinate::equals(const QGeoCoordinate &lhs, const
    QGeoCoordinate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#equals

    Parameters
    ----------

    lhs : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    rhs : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool QGeoCoordinate::equals(const QGeoCoordinate &lhs, const
    #      QGeoCoordinate &rhs)
    return Rituals.call(
        'ritual_ZN14QGeoCoordinate6equalsERKS_S1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  @staticmethod
  @overload(QDebug, THIS)
  def debugStreaming(dbg: QDebug, coord: QGeoCoordinate) -> QDebug:
    """
    Calls Qt's 'QDebug QGeoCoordinate::debugStreaming(QDebug dbg, const
    QGeoCoordinate &coord)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#debugStreaming

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    coord : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QGeoCoordinate::debugStreaming(QDebug dbg, const QGeoCoordinate
    #      &coord)
    address = Rituals.call(
        'ritual_ZN14QGeoCoordinate14debugStreamingE6QDebugRKS_',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(coord),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCoordinate'

  #  Qt's '~QGeoCoordinate()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoCoordinate behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QGeoCoordinateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoCoordinate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#isValid
    """
    #  bool QGeoCoordinate::isValid() const
    return self.uglySide.call('ritual_ZNK14QGeoCoordinate7isValidEv')

  def type(self) -> CoordinateType:
    """
    Calls Qt's 'CoordinateType QGeoCoordinate::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#type

    Returns
    -------

    CoordinateType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CoordinateType(number)'
      gives.
    """
    #  CoordinateType QGeoCoordinate::type() const
    return QGeoCoordinate.CoordinateType(self.uglySide.call(
        'ritual_ZNK14QGeoCoordinate4typeEv',
    ))

  def latitude(self) -> float:
    """
    Calls Qt's 'double QGeoCoordinate::latitude() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#latitude
    """
    #  double QGeoCoordinate::latitude() const
    return self.uglySide.call('ritual_ZNK14QGeoCoordinate8latitudeEv')

  def longitude(self) -> float:
    """
    Calls Qt's 'double QGeoCoordinate::longitude() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#longitude
    """
    #  double QGeoCoordinate::longitude() const
    return self.uglySide.call('ritual_ZNK14QGeoCoordinate9longitudeEv')

  def altitude(self) -> float:
    """
    Calls Qt's 'double QGeoCoordinate::altitude() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#altitude
    """
    #  double QGeoCoordinate::altitude() const
    return self.uglySide.call('ritual_ZNK14QGeoCoordinate8altitudeEv')

  @overload(THIS)
  def distanceTo(self, other: QGeoCoordinate) -> float:
    """
    Calls Qt's 'qreal QGeoCoordinate::distanceTo(const QGeoCoordinate &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#distanceTo

    Parameters
    ----------

    other : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  qreal QGeoCoordinate::distanceTo(const QGeoCoordinate &other) const
    return self.uglySide.call(
        'ritual_ZNK14QGeoCoordinate10distanceToERKS_', self._valueOf(other),
    )

  @overload(THIS)
  def azimuthTo(self, other: QGeoCoordinate) -> float:
    """
    Calls Qt's 'qreal QGeoCoordinate::azimuthTo(const QGeoCoordinate &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#azimuthTo

    Parameters
    ----------

    other : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  qreal QGeoCoordinate::azimuthTo(const QGeoCoordinate &other) const
    return self.uglySide.call(
        'ritual_ZNK14QGeoCoordinate9azimuthToERKS_', self._valueOf(other),
    )

  @overload(float, float)
  @overload(float, float, float)
  def atDistanceAndAzimuth(
      self,
      distance: float,
      azimuth: float,
      distanceUp: float = 0.0,
  ) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoCoordinate::atDistanceAndAzimuth(qreal
    distance, qreal azimuth, qreal distanceUp) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocoordinate.html#atDistanceAndAzimuth

    Parameters
    ----------

    distance : float
      Passed on as it is.

    azimuth : float
      Passed on as it is.

    distanceUp : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoCoordinate::atDistanceAndAzimuth(qreal distance,
    #      qreal azimuth, qreal distanceUp) const
    address = self.uglySide.call(
        'ritual_ZNK14QGeoCoordinate20atDistanceAndAzimuthEddd',
        distance, azimuth, distanceUp,
    )
    return QGeoCoordinate._cuteOwning(address)

  @overload()
  @overload(CoordinateFormat)
  def toString(
      self,
      format: CoordinateFormat = (
          CoordinateFormat.DegreesMinutesSecondsWithHemisphere),
  ) -> str:
    """
    Calls Qt's 'QString QGeoCoordinate::toString(CoordinateFormat format)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#toString

    Parameters
    ----------

    format : CoordinateFormat
      Passed on as its number. May be left out, as in Qt: it is then
      CoordinateFormat.DegreesMinutesSecondsWithHemisphere.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoCoordinate::toString(CoordinateFormat format) const
    return self.uglySide.call(
        'ritual_ZNK14QGeoCoordinate8toStringENS_16CoordinateFormatE',
        format.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLatitude(self, latitude: float) -> None:
    """
    Calls Qt's 'void QGeoCoordinate::setLatitude(double latitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#setLatitude

    Parameters
    ----------

    latitude : float
      Passed on as it is.
    """
    #  void QGeoCoordinate::setLatitude(double latitude)
    self.uglySide.call('ritual_ZN14QGeoCoordinate11setLatitudeEd', latitude)

  @overload(float)
  def setLongitude(self, longitude: float) -> None:
    """
    Calls Qt's 'void QGeoCoordinate::setLongitude(double longitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#setLongitude

    Parameters
    ----------

    longitude : float
      Passed on as it is.
    """
    #  void QGeoCoordinate::setLongitude(double longitude)
    self.uglySide.call(
        'ritual_ZN14QGeoCoordinate12setLongitudeEd', longitude,
    )

  @overload(float)
  def setAltitude(self, altitude: float) -> None:
    """
    Calls Qt's 'void QGeoCoordinate::setAltitude(double altitude)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#setAltitude

    Parameters
    ----------

    altitude : float
      Passed on as it is.
    """
    #  void QGeoCoordinate::setAltitude(double altitude)
    self.uglySide.call('ritual_ZN14QGeoCoordinate11setAltitudeEd', altitude)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoCoordinate &lhs, const
    QGeoCoordinate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#operator==

    Parameters
    ----------

    rhs : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool operator==(const QGeoCoordinate &lhs, const QGeoCoordinate &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QGeoCoordinateS1_',
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
  def __ne__(self, rhs: QGeoCoordinate) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoCoordinate &lhs, const
    QGeoCoordinate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#operator!=

    Parameters
    ----------

    rhs : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoCoordinate &lhs, const QGeoCoordinate &rhs)
    return Rituals.call(
        'ritual_ZneRK14QGeoCoordinateS1_',
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

  @overload(QDebug)
  def __rlshift__(self, dbg: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug dbg, const QGeoCoordinate &coord)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#operator<<

    Parameters
    ----------

    dbg : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug dbg, const QGeoCoordinate &coord)
    address = Rituals.call(
        'ritual_Zls6QDebugRK14QGeoCoordinate',
        CuteMixin._valueOf(dbg), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QGeoCoordinate::QGeoCoordinate()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate
    """
    #  QGeoCoordinate::QGeoCoordinate()
    self._noteCreation(QGeoCoordinate, lambda: Rituals.call(
        'ritual_ZN14QGeoCoordinateC1Ev',
    ))

  @overload(float, float)
  def __init__(self, latitude: float, longitude: float) -> None:
    """
    Notes what was given, for Qt's 'QGeoCoordinate::QGeoCoordinate(double
    latitude, double longitude)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate

    Parameters
    ----------

    latitude : float
      Passed on as it is.

    longitude : float
      Passed on as it is.
    """
    #  QGeoCoordinate::QGeoCoordinate(double latitude, double longitude)
    self._noteCreation(QGeoCoordinate, lambda: Rituals.call(
        'ritual_ZN14QGeoCoordinateC1Edd', latitude, longitude,
    ))

  @overload(float, float, float)
  def __init__(
      self,
      latitude: float,
      longitude: float,
      altitude: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QGeoCoordinate::QGeoCoordinate(double
    latitude, double longitude, double altitude)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate

    Parameters
    ----------

    latitude : float
      Passed on as it is.

    longitude : float
      Passed on as it is.

    altitude : float
      Passed on as it is.
    """
    #  QGeoCoordinate::QGeoCoordinate(double latitude, double longitude,
    #      double altitude)
    self._noteCreation(QGeoCoordinate, lambda: Rituals.call(
        'ritual_ZN14QGeoCoordinateC1Eddd', latitude, longitude, altitude,
    ))

  @overload(THIS)
  def __init__(self, other: QGeoCoordinate) -> None:
    """
    Notes what was given, for Qt's 'QGeoCoordinate::QGeoCoordinate(const
    QGeoCoordinate &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocoordinate.html#QGeoCoordinate

    Parameters
    ----------

    other : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  QGeoCoordinate::QGeoCoordinate(const QGeoCoordinate &other)
    self._noteCreation(QGeoCoordinate, lambda: Rituals.call(
        'ritual_ZN14QGeoCoordinateC1ERKS_', self._valueOf(other),
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
  def dataStreamIn(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoCoordinate::dataStreamIn(QDataStream &stream,
    QGeoCoordinate &coordinate)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGeoCoordinate.dataStreamIn' has no cute function yet. Qt's "
        "'QDataStream &QGeoCoordinate::dataStreamIn(QDataStream &stream, "
        "QGeoCoordinate &coordinate)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def dataStreamOut(*__, **_) -> Never:
    """
    Qt's 'QDataStream &QGeoCoordinate::dataStreamOut(QDataStream &stream,
    const QGeoCoordinate &coordinate)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QGeoCoordinate.dataStreamOut' has no cute function yet. Qt's "
        "'QDataStream &QGeoCoordinate::dataStreamOut(QDataStream &stream, "
        "const QGeoCoordinate &coordinate)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoCoordinate::swap(QGeoCoordinate &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoCoordinate.swap' has no cute function yet. Qt's 'void "
        "QGeoCoordinate::swap(QGeoCoordinate &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QGeoCoordinate>': the list of QGeoCoordinate, which
#  'QList[QGeoCoordinate]' gives. It is made here, so that there is one as
#  soon as there can be a QGeoCoordinate.
QList.createKind(
    QGeoCoordinate, 'value',
    make='ritual_list_make_QGeoCoordinate',
    add='ritual_list_add_QGeoCoordinate',
    size='ritual_list_size_QGeoCoordinate',
    at='ritual_list_at_QGeoCoordinate',
    drop='ritual_list_drop_QGeoCoordinate',
)
