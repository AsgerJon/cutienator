"""
QGeoManeuverPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeomaneuver_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGeoManeuverPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QMap, QSharedData
from . import QGeoManeuver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
  from ..QtPositioning import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QVariant = WAIT['QVariant']


class QGeoManeuverPrivate(QSharedData):
  """
  The cute side of Qt's QGeoManeuverPrivate: a plain Python object standing
  in front of one C++ QGeoManeuverPrivate.

  It is built on the cute 'QSharedData', as Qt's QGeoManeuverPrivate is built
  on Qt's QSharedData, and has everything that class has.

  C++ hands a QGeoManeuverPrivate around as a copy, so every C++
  QGeoManeuverPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoManeuverPrivate that has a ritual and that
  Python can call so far, 19 names in all: 'equals', 'valid', 'setValid',
  'id', 'setId', 'position', 'setPosition', 'text', 'setText', 'direction',
  'setDirection', 'timeToNextInstruction', 'setTimeToNextInstruction',
  'distanceToNextInstruction', 'setDistanceToNextInstruction', 'waypoint',
  'setWaypoint', 'extendedAttributes', 'setExtendedAttributes'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoManeuverPrivate::~QGeoManeuverPrivate()': the destructor:
    Python removes its C++ QGeoManeuverPrivate by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QGeoManeuverPrivate is created at the first use, not by
    'QGeoManeuverPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoManeuverPrivate back gives a copy the ritual made
    for Python, in a new cute QGeoManeuverPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoManeuverPrivate'

  #  Qt's '~QGeoManeuverPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoManeuverPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QGeoManeuverPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def equals(self, other: QGeoManeuverPrivate) -> bool:
    """
    Calls Qt's 'bool QGeoManeuverPrivate::equals(const QGeoManeuverPrivate
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#equals

    Parameters
    ----------

    other : QGeoManeuverPrivate
      Passed on as a value: Qt reads the C++ QGeoManeuverPrivate, which stays
      Python's own.
    """
    #  bool QGeoManeuverPrivate::equals(const QGeoManeuverPrivate &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate6equalsERKS_', self._valueOf(other),
    )

  def valid(self) -> bool:
    """
    Calls Qt's 'bool QGeoManeuverPrivate::valid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#valid
    """
    #  bool QGeoManeuverPrivate::valid() const
    return self.uglySide.call('ritual_ZNK19QGeoManeuverPrivate5validEv')

  def id(self) -> str:
    """
    Calls Qt's 'QString QGeoManeuverPrivate::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoManeuverPrivate::id() const
    return self.uglySide.call('ritual_ZNK19QGeoManeuverPrivate2idEv')

  def position(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoManeuverPrivate::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#position

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoManeuverPrivate::position() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate8positionEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QGeoManeuverPrivate::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGeoManeuverPrivate::text() const
    return self.uglySide.call('ritual_ZNK19QGeoManeuverPrivate4textEv')

  def direction(self) -> QGeoManeuver.InstructionDirection:
    """
    Calls Qt's 'QGeoManeuver::InstructionDirection
    QGeoManeuverPrivate::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#direction

    Returns
    -------

    QGeoManeuver.InstructionDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGeoManeuver.InstructionDirection(number)' gives.
    """
    #  QGeoManeuver::InstructionDirection QGeoManeuverPrivate::direction()
    #      const
    return QGeoManeuver.InstructionDirection(self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate9directionEv',
    ))

  def timeToNextInstruction(self) -> int:
    """
    Calls Qt's 'int QGeoManeuverPrivate::timeToNextInstruction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#timeToNextInstruction
    """
    #  int QGeoManeuverPrivate::timeToNextInstruction() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate21timeToNextInstructionEv',
    )

  def distanceToNextInstruction(self) -> float:
    """
    Calls Qt's 'qreal QGeoManeuverPrivate::distanceToNextInstruction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#distanceToNextInstruction
    """
    #  qreal QGeoManeuverPrivate::distanceToNextInstruction() const
    return self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate25distanceToNextInstructionEv',
    )

  def waypoint(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoManeuverPrivate::waypoint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#waypoint

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoManeuverPrivate::waypoint() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate8waypointEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def extendedAttributes(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QGeoManeuverPrivate::extendedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#extendedAttributes

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QGeoManeuverPrivate::extendedAttributes() const
    address = self.uglySide.call(
        'ritual_ZNK19QGeoManeuverPrivate18extendedAttributesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setValid(self, valid: bool) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setValid(bool valid)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setValid

    Parameters
    ----------

    valid : bool
      Passed on as it is.
    """
    #  void QGeoManeuverPrivate::setValid(bool valid)
    self.uglySide.call('ritual_ZN19QGeoManeuverPrivate8setValidEb', valid)

  @overload(str)
  def setId(self, id: str) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setId(const QString &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoManeuverPrivate::setId(const QString &id)
    self.uglySide.call('ritual_ZN19QGeoManeuverPrivate5setIdERK7QString', id)

  @overload(QGeoCoordinate)
  def setPosition(self, position: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setPosition(const QGeoCoordinate
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setPosition

    Parameters
    ----------

    position : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoManeuverPrivate::setPosition(const QGeoCoordinate &position)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate11setPositionERK14QGeoCoordinate',
        self._valueOf(position),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGeoManeuverPrivate::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate7setTextERK7QString', text,
    )

  @overload(QGeoManeuver.InstructionDirection)
  def setDirection(
      self,
      direction: QGeoManeuver.InstructionDirection,
  ) -> None:
    """
    Calls Qt's 'void
    QGeoManeuverPrivate::setDirection(QGeoManeuver::InstructionDirection
    direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setDirection

    Parameters
    ----------

    direction : QGeoManeuver.InstructionDirection
      Passed on as its number.
    """
    #  void QGeoManeuverPrivate::setDirection(QGeoManeuver::
    #      InstructionDirection direction)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate12setDirectionEN12QGeoManeuver20Inst'
        'ructionDirectionE',
        direction.value,
    )

  @overload(int)
  def setTimeToNextInstruction(self, timeToNextInstruction: int) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setTimeToNextInstruction(int
    timeToNextInstruction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setTimeToNextInstruction

    Parameters
    ----------

    timeToNextInstruction : int
      Passed on as it is.
    """
    #  void QGeoManeuverPrivate::setTimeToNextInstruction(int
    #      timeToNextInstruction)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate24setTimeToNextInstructionEi',
        timeToNextInstruction,
    )

  @overload(float)
  def setDistanceToNextInstruction(
      self,
      distanceToNextInstruction: float,
  ) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setDistanceToNextInstruction(qreal
    distanceToNextInstruction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html

    Parameters
    ----------

    distanceToNextInstruction : float
      Passed on as it is.
    """
    #  void QGeoManeuverPrivate::setDistanceToNextInstruction(qreal
    #      distanceToNextInstruction)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate28setDistanceToNextInstructionEd',
        distanceToNextInstruction,
    )

  @overload(QGeoCoordinate)
  def setWaypoint(self, waypoint: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setWaypoint(const QGeoCoordinate
    &waypoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setWaypoint

    Parameters
    ----------

    waypoint : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoManeuverPrivate::setWaypoint(const QGeoCoordinate &waypoint)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate11setWaypointERK14QGeoCoordinate',
        self._valueOf(waypoint),
    )

  @overload(QMap[str, QVariant])
  def setExtendedAttributes(
      self,
      extendedAttributes: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QGeoManeuverPrivate::setExtendedAttributes(const
    QVariantMap &extendedAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeomaneuverprivate.html#setExtendedAttributes

    Parameters
    ----------

    extendedAttributes : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QGeoManeuverPrivate::setExtendedAttributes(const QVariantMap
    #      &extendedAttributes)
    self.uglySide.call(
        'ritual_ZN19QGeoManeuverPrivate21setExtendedAttributesERK4QMapI7QSt'
        'ring8QVariantE',
        self._valueOf(extendedAttributes),
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
