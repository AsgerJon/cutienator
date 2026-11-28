"""
QGeoManeuver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qgeomaneuver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from ..QtPositioning import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QVariant = WAIT['QVariant']


class QGeoManeuver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoManeuver: a plain Python object standing in front
  of one C++ QGeoManeuver.

  C++ hands a QGeoManeuver around as a copy, so every C++ QGeoManeuver behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoManeuver that has a ritual and that Python can
  call so far, 18 names in all: '__eq__', '__ne__', 'isValid', 'setPosition',
  'position', 'setInstructionText', 'instructionText', 'setDirection',
  'direction', 'setTimeToNextInstruction', 'timeToNextInstruction',
  'setDistanceToNextInstruction', 'distanceToNextInstruction', 'setWaypoint',
  'waypoint', 'setExtendedAttributes', 'extendedAttributes', 'isEqual'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoManeuver::QGeoManeuver(QGeoManeuver &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QGeoManeuver::~QGeoManeuver()': the destructor: Python removes its
    C++ QGeoManeuver by it, and has no other use for it.
  - Qt's 'QGeoManeuver &QGeoManeuver::operator=(const QGeoManeuver &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoManeuver &QGeoManeuver::operator=(QGeoManeuver &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoManeuver::swap(QGeoManeuver &other)': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 28 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoManeuver is created at the first use, not by
    'QGeoManeuver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoManeuver back gives a copy the ritual made for
    Python, in a new cute QGeoManeuver.
  - Each name of Qt's QGeoManeuver that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QGeoManeuver, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class InstructionDirection(CuteNum):
    """
    The enum 'QGeoManeuver::InstructionDirection' of Qt, with the 12 names Qt
    gives in it.
    """

    NoDirection = Kee[int](0)
    DirectionForward = Kee[int](1)
    DirectionBearRight = Kee[int](2)
    DirectionLightRight = Kee[int](3)
    DirectionRight = Kee[int](4)
    DirectionHardRight = Kee[int](5)
    DirectionUTurnRight = Kee[int](6)
    DirectionUTurnLeft = Kee[int](7)
    DirectionHardLeft = Kee[int](8)
    DirectionLeft = Kee[int](9)
    DirectionLightLeft = Kee[int](10)
    DirectionBearLeft = Kee[int](11)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoManeuver'

  #  Qt's '~QGeoManeuver()'. Naming it makes this a value class: Python owns
  #  every C++ QGeoManeuver behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QGeoManeuverD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoManeuver::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#isValid
    """
    #  bool QGeoManeuver::isValid() const
    return self.uglySide.call('ritual_ZNK12QGeoManeuver7isValidEv')

  def position(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoManeuver::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#position

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoManeuver::position() const
    address = self.uglySide.call('ritual_ZNK12QGeoManeuver8positionEv')
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def instructionText(self) -> str:
    """
    Calls Qt's 'QString QGeoManeuver::instructionText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#instructionText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoManeuver::instructionText() const
    return self.uglySide.call('ritual_ZNK12QGeoManeuver15instructionTextEv')

  def direction(self) -> InstructionDirection:
    """
    Calls Qt's 'InstructionDirection QGeoManeuver::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#direction

    Returns
    -------

    InstructionDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'InstructionDirection(number)' gives.
    """
    #  InstructionDirection QGeoManeuver::direction() const
    return QGeoManeuver.InstructionDirection(self.uglySide.call(
        'ritual_ZNK12QGeoManeuver9directionEv',
    ))

  def timeToNextInstruction(self) -> int:
    """
    Calls Qt's 'int QGeoManeuver::timeToNextInstruction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#timeToNextInstruction
    """
    #  int QGeoManeuver::timeToNextInstruction() const
    return self.uglySide.call(
        'ritual_ZNK12QGeoManeuver21timeToNextInstructionEv',
    )

  def distanceToNextInstruction(self) -> float:
    """
    Calls Qt's 'qreal QGeoManeuver::distanceToNextInstruction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#distanceToNextInstruction
    """
    #  qreal QGeoManeuver::distanceToNextInstruction() const
    return self.uglySide.call(
        'ritual_ZNK12QGeoManeuver25distanceToNextInstructionEv',
    )

  def waypoint(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoManeuver::waypoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#waypoint

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoManeuver::waypoint() const
    address = self.uglySide.call('ritual_ZNK12QGeoManeuver8waypointEv')
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def extendedAttributes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoManeuver::extendedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#extendedAttributes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoManeuver::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK12QGeoManeuver18extendedAttributesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QGeoManeuver) -> bool:
    """
    Calls Qt's 'bool QGeoManeuver::isEqual(const QGeoManeuver &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#isEqual

    Parameters
    ----------

    other : QGeoManeuver
      Passed on as a value: Qt reads the C++ QGeoManeuver, which stays
      Python's own.
    """
    #  bool QGeoManeuver::isEqual(const QGeoManeuver &other) const
    return self.uglySide.call(
        'ritual_ZNK12QGeoManeuver7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setPosition(self, position: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setPosition(const QGeoCoordinate
    &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#setPosition

    Parameters
    ----------

    position : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoManeuver::setPosition(const QGeoCoordinate &position)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver11setPositionERK14QGeoCoordinate',
        self._valueOf(position),
    )

  @overload(str)
  def setInstructionText(self, instructionText: str) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setInstructionText(const QString
    &instructionText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#setInstructionText

    Parameters
    ----------

    instructionText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoManeuver::setInstructionText(const QString &instructionText)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver18setInstructionTextERK7QString',
        instructionText,
    )

  @overload(InstructionDirection)
  def setDirection(self, direction: InstructionDirection) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setDirection(InstructionDirection
    direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#setDirection

    Parameters
    ----------

    direction : InstructionDirection
      Passed on as its number.
    """
    #  void QGeoManeuver::setDirection(InstructionDirection direction)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver12setDirectionENS_20InstructionDirectionE',
        direction.value,
    )

  @overload(int)
  def setTimeToNextInstruction(self, secs: int) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setTimeToNextInstruction(int secs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#setTimeToNextInstruction

    Parameters
    ----------

    secs : int
      Passed on as it is.
    """
    #  void QGeoManeuver::setTimeToNextInstruction(int secs)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver24setTimeToNextInstructionEi', secs,
    )

  @overload(float)
  def setDistanceToNextInstruction(self, distance: float) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setDistanceToNextInstruction(qreal
    distance)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#setDistanceToNextInstruction

    Parameters
    ----------

    distance : float
      Passed on as it is.
    """
    #  void QGeoManeuver::setDistanceToNextInstruction(qreal distance)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver28setDistanceToNextInstructionEd', distance,
    )

  @overload(QGeoCoordinate)
  def setWaypoint(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setWaypoint(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#setWaypoint

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoManeuver::setWaypoint(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver11setWaypointERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(QMap[str, QVariant])
  def setExtendedAttributes(
      self,
      extendedAttributes: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QGeoManeuver::setExtendedAttributes(const QVariantMap
    &extendedAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuver.html#setExtendedAttributes

    Parameters
    ----------

    extendedAttributes : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoManeuver::setExtendedAttributes(const QVariantMap
    #      &extendedAttributes)
    self.uglySide.call(
        'ritual_ZN12QGeoManeuver21setExtendedAttributesERK4QMapI7QString8QV'
        'ariantE',
        self._valueOf(extendedAttributes),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoManeuver) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoManeuver &lhs, const QGeoManeuver
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#operator==

    Parameters
    ----------

    rhs : QGeoManeuver
      Passed on as a value: Qt reads the C++ QGeoManeuver, which stays
      Python's own.
    """
    #  bool operator==(const QGeoManeuver &lhs, const QGeoManeuver &rhs)
    return Rituals.call(
        'ritual_ZeqRK12QGeoManeuverS1_',
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
  def __ne__(self, rhs: QGeoManeuver) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoManeuver &lhs, const QGeoManeuver
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#operator!=

    Parameters
    ----------

    rhs : QGeoManeuver
      Passed on as a value: Qt reads the C++ QGeoManeuver, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoManeuver &lhs, const QGeoManeuver &rhs)
    return Rituals.call(
        'ritual_ZneRK12QGeoManeuverS1_',
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
    Notes what was given, for Qt's 'QGeoManeuver::QGeoManeuver()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#QGeoManeuver
    """
    #  QGeoManeuver::QGeoManeuver()
    self._noteCreation(QGeoManeuver, lambda: Rituals.call(
        'ritual_ZN12QGeoManeuverC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoManeuver) -> None:
    """
    Notes what was given, for Qt's 'QGeoManeuver::QGeoManeuver(const
    QGeoManeuver &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuver.html#QGeoManeuver

    Parameters
    ----------

    other : QGeoManeuver
      Passed on as a value: Qt reads the C++ QGeoManeuver, which stays
      Python's own.
    """
    #  QGeoManeuver::QGeoManeuver(const QGeoManeuver &other)
    self._noteCreation(QGeoManeuver, lambda: Rituals.call(
        'ritual_ZN12QGeoManeuverC1ERKS_', self._valueOf(other),
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
    Qt's 'void QGeoManeuver::swap(QGeoManeuver &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoManeuver.swap' has no cute function yet. Qt's 'void "
        "QGeoManeuver::swap(QGeoManeuver &other)': takes a type Python has "
        "no way to hand over yet.")
