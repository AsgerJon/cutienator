"""
QTabletEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent
from . import QSinglePointEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QPointF
  from . import QPointingDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QPointingDevice = WAIT['QPointingDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTabletEvent(QSinglePointEvent):
  """
  The cute side of Qt's QTabletEvent: a plain Python object standing in front
  of one C++ QTabletEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QTabletEvent is built
  on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTabletEvent that has a ritual and that Python can
  call so far, 18 names in all: 'clone', 'pos', 'globalPos', 'posF',
  'globalPosF', 'x', 'y', 'globalX', 'globalY', 'hiResGlobalX',
  'hiResGlobalY', 'uniqueId', 'pressure', 'rotation', 'z',
  'tangentialPressure', 'xTilt', 'yTilt'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTabletEvent::QTabletEvent(const QTabletEvent &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QTabletEvent &QTabletEvent::operator=(const QTabletEvent &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QTabletEvent::~QTabletEvent()': the destructor: Python never
    removes a C++ QTabletEvent.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QTabletEvent is created at the first use, not by
    'QTabletEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTabletEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTabletEvent'

  #  A C++ QTabletEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTabletEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QTabletEvent]:
    """
    Calls Qt's 'QTabletEvent *QTabletEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#clone

    Returns
    -------

    Optional[QTabletEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTabletEvent *QTabletEvent::clone() const
    ritual = 'ritual_ZNK12QTabletEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QTabletEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QTabletEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QTabletEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QTabletEvent::pos() const
    address = self.uglySide.call('ritual_ZNK12QTabletEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QTabletEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QTabletEvent::globalPos() const
    address = self.uglySide.call('ritual_ZNK12QTabletEvent9globalPosEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def posF(self) -> QPointF:
    """
    Calls Qt's 'const QPointF QTabletEvent::posF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#posF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  const QPointF QTabletEvent::posF() const
    address = self.uglySide.call('ritual_ZNK12QTabletEvent4posFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def globalPosF(self) -> QPointF:
    """
    Calls Qt's 'const QPointF QTabletEvent::globalPosF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#globalPosF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  const QPointF QTabletEvent::globalPosF() const
    address = self.uglySide.call('ritual_ZNK12QTabletEvent10globalPosFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QTabletEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#x
    """
    #  int QTabletEvent::x() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QTabletEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#y
    """
    #  int QTabletEvent::y() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent1yEv')

  def globalX(self) -> int:
    """
    Calls Qt's 'int QTabletEvent::globalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#globalX
    """
    #  int QTabletEvent::globalX() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent7globalXEv')

  def globalY(self) -> int:
    """
    Calls Qt's 'int QTabletEvent::globalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#globalY
    """
    #  int QTabletEvent::globalY() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent7globalYEv')

  def hiResGlobalX(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::hiResGlobalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#hiResGlobalX
    """
    #  qreal QTabletEvent::hiResGlobalX() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent12hiResGlobalXEv')

  def hiResGlobalY(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::hiResGlobalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#hiResGlobalY
    """
    #  qreal QTabletEvent::hiResGlobalY() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent12hiResGlobalYEv')

  def uniqueId(self) -> int:
    """
    Calls Qt's 'qint64 QTabletEvent::uniqueId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#uniqueId
    """
    #  qint64 QTabletEvent::uniqueId() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent8uniqueIdEv')

  def pressure(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::pressure() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#pressure
    """
    #  qreal QTabletEvent::pressure() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent8pressureEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#rotation
    """
    #  qreal QTabletEvent::rotation() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent8rotationEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#z
    """
    #  qreal QTabletEvent::z() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent1zEv')

  def tangentialPressure(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::tangentialPressure() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabletevent.html#tangentialPressure
    """
    #  qreal QTabletEvent::tangentialPressure() const
    return self.uglySide.call(
        'ritual_ZNK12QTabletEvent18tangentialPressureEv',
    )

  def xTilt(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::xTilt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#xTilt
    """
    #  qreal QTabletEvent::xTilt() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent5xTiltEv')

  def yTilt(self) -> float:
    """
    Calls Qt's 'qreal QTabletEvent::yTilt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#yTilt
    """
    #  qreal QTabletEvent::yTilt() const
    return self.uglySide.call('ritual_ZNK12QTabletEvent5yTiltEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      QEvent.Type, QPointingDevice, QPointF, QPointF, float, float, float,
      float, float, float, Qt.KeyboardModifiers, Qt.MouseButton,
      Qt.MouseButtons,
  )
  @overload(
      QEvent.Type, NoneType, QPointF, QPointF, float, float, float, float,
      float, float, Qt.KeyboardModifiers, Qt.MouseButton, Qt.MouseButtons,
  )
  def __init__(
      self,
      t: QEvent.Type,
      device: Optional[QPointingDevice],
      pos: QPointF,
      globalPos: QPointF,
      pressure: float,
      xTilt: float,
      yTilt: float,
      tangentialPressure: float,
      rotation: float,
      z: float,
      keyState: Qt.KeyboardModifiers,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTabletEvent::QTabletEvent(Type t, const
    QPointingDevice *device, const QPointF &pos, const QPointF &globalPos,
    qreal pressure, float xTilt, float yTilt, float tangentialPressure, qreal
    rotation, float z, Qt::KeyboardModifiers keyState, Qt::MouseButton
    button, Qt::MouseButtons buttons)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtabletevent.html#QTabletEvent

    Parameters
    ----------

    t : QEvent.Type
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    pressure : float
      Passed on as it is.

    xTilt : float
      Passed on as it is.

    yTilt : float
      Passed on as it is.

    tangentialPressure : float
      Passed on as it is.

    rotation : float
      Passed on as it is.

    z : float
      Passed on as it is.

    keyState : Qt.KeyboardModifiers
      Passed on as its number.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.
    """
    #  QTabletEvent::QTabletEvent(Type t, const QPointingDevice *device,
    #      const QPointF &pos, const QPointF &globalPos, qreal pressure,
    #      float xTilt, float yTilt, float tangentialPressure, qreal
    #      rotation, float z, Qt::KeyboardModifiers keyState, Qt::MouseButton
    #      button, Qt::MouseButtons buttons)
    self._noteCreation(QTabletEvent, lambda: Rituals.call(
        'ritual_ZN12QTabletEventC1EN6QEvent4TypeEPK15QPointingDeviceRK7QPoi'
        'ntFS7_dfffdf6QFlagsIN2Qt16KeyboardModifierEENS9_11MouseButtonES8_I'
        'SC_E',
        t.value, self._addressOf(device), self._valueOf(pos, 'QPointF'),
        self._valueOf(globalPos, 'QPointF'), pressure, xTilt, yTilt,
        tangentialPressure, rotation, z, keyState.value, button.value,
        buttons.value,
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
