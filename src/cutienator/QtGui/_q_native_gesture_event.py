"""
QNativeGestureEvent binding of the Qt C++
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
from ..QtCore import Qt
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


class QNativeGestureEvent(QSinglePointEvent):
  """
  The cute side of Qt's QNativeGestureEvent: a plain Python object standing
  in front of one C++ QNativeGestureEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QNativeGestureEvent is
  built on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNativeGestureEvent that has a ritual and that
  Python can call so far, 10 names in all: 'clone', 'gestureType',
  'fingerCount', 'value', 'delta', 'pos', 'globalPos', 'localPos',
  'windowPos', 'screenPos'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNativeGestureEvent::~QNativeGestureEvent()': the destructor:
    Python never removes a C++ QNativeGestureEvent.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QNativeGestureEvent is created at the first use, not by
    'QNativeGestureEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeGestureEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeGestureEvent'

  #  A C++ QNativeGestureEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeGestureEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QNativeGestureEvent]:
    """
    Calls Qt's 'QNativeGestureEvent *QNativeGestureEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#clone

    Returns
    -------

    Optional[QNativeGestureEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNativeGestureEvent *QNativeGestureEvent::clone() const
    ritual = 'ritual_ZNK19QNativeGestureEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QNativeGestureEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QNativeGestureEvent._cuteAt(address)

  def gestureType(self) -> Qt.NativeGestureType:
    """
    Calls Qt's 'Qt::NativeGestureType QNativeGestureEvent::gestureType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativegestureevent.html#gestureType

    Returns
    -------

    Qt.NativeGestureType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.NativeGestureType(number)' gives.
    """
    #  Qt::NativeGestureType QNativeGestureEvent::gestureType() const
    return Qt.NativeGestureType(self.uglySide.call(
        'ritual_ZNK19QNativeGestureEvent11gestureTypeEv',
    ))

  def fingerCount(self) -> int:
    """
    Calls Qt's 'int QNativeGestureEvent::fingerCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativegestureevent.html#fingerCount
    """
    #  int QNativeGestureEvent::fingerCount() const
    return self.uglySide.call(
        'ritual_ZNK19QNativeGestureEvent11fingerCountEv',
    )

  def value(self) -> float:
    """
    Calls Qt's 'qreal QNativeGestureEvent::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#value
    """
    #  qreal QNativeGestureEvent::value() const
    return self.uglySide.call('ritual_ZNK19QNativeGestureEvent5valueEv')

  def delta(self) -> QPointF:
    """
    Calls Qt's 'QPointF QNativeGestureEvent::delta() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#delta

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QNativeGestureEvent::delta() const
    address = self.uglySide.call('ritual_ZNK19QNativeGestureEvent5deltaEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint QNativeGestureEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint QNativeGestureEvent::pos() const
    address = self.uglySide.call('ritual_ZNK19QNativeGestureEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'const QPoint QNativeGestureEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  const QPoint QNativeGestureEvent::globalPos() const
    address = self.uglySide.call(
        'ritual_ZNK19QNativeGestureEvent9globalPosEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def localPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QNativeGestureEvent::localPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#localPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QNativeGestureEvent::localPos() const
    address = self.uglySide.call(
        'ritual_ZNK19QNativeGestureEvent8localPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def windowPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QNativeGestureEvent::windowPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#windowPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QNativeGestureEvent::windowPos() const
    address = self.uglySide.call(
        'ritual_ZNK19QNativeGestureEvent9windowPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QNativeGestureEvent::screenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnativegestureevent.html#screenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QNativeGestureEvent::screenPos() const
    address = self.uglySide.call(
        'ritual_ZNK19QNativeGestureEvent9screenPosEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

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
      Qt.NativeGestureType, QPointingDevice, QPointF, QPointF, QPointF,
      float, int, int,
  )
  @overload(
      Qt.NativeGestureType, NoneType, QPointF, QPointF, QPointF, float, int,
      int,
  )
  def __init__(
      self,
      type: Qt.NativeGestureType,
      dev: Optional[QPointingDevice],
      localPos: QPointF,
      scenePos: QPointF,
      globalPos: QPointF,
      value: float,
      sequenceId: int,
      intArgument: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
    const QPointingDevice *dev, const QPointF &localPos, const QPointF
    &scenePos, const QPointF &globalPos, qreal value, quint64 sequenceId,
    quint64 intArgument)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativegestureevent.html#QNativeGestureEvent

    Parameters
    ----------

    type : Qt.NativeGestureType
      Passed on as its number.

    dev : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : float
      Passed on as it is.

    sequenceId : int
      Passed on as it is.

    intArgument : int
      Passed on as it is.
    """
    #  QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
    #      const QPointingDevice *dev, const QPointF &localPos, const QPointF
    #      &scenePos, const QPointF &globalPos, qreal value, quint64
    #      sequenceId, quint64 intArgument)
    self._noteCreation(QNativeGestureEvent, lambda: Rituals.call(
        'ritual_ZN19QNativeGestureEventC1EN2Qt17NativeGestureTypeEPK15QPoin'
        'tingDeviceRK7QPointFS7_S7_dyy',
        type.value, self._addressOf(dev), self._valueOf(localPos),
        self._valueOf(scenePos), self._valueOf(globalPos), value, sequenceId,
        intArgument,
    ))

  @overload(
      Qt.NativeGestureType, QPointingDevice, int, QPointF, QPointF, QPointF,
      float, QPointF,
  )
  @overload(
      Qt.NativeGestureType, NoneType, int, QPointF, QPointF, QPointF, float,
      QPointF,
  )
  @overload(
      Qt.NativeGestureType, QPointingDevice, int, QPointF, QPointF, QPointF,
      float, QPointF, int,
  )
  @overload(
      Qt.NativeGestureType, NoneType, int, QPointF, QPointF, QPointF, float,
      QPointF, int,
  )
  def __init__(
      self,
      type: Qt.NativeGestureType,
      dev: Optional[QPointingDevice],
      fingerCount: int,
      localPos: QPointF,
      scenePos: QPointF,
      globalPos: QPointF,
      value: float,
      delta: QPointF,
      sequenceId: int = 18446744073709551615,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
    const QPointingDevice *dev, int fingerCount, const QPointF &localPos,
    const QPointF &scenePos, const QPointF &globalPos, qreal value, const
    QPointF &delta, quint64 sequenceId)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativegestureevent.html#QNativeGestureEvent

    Parameters
    ----------

    type : Qt.NativeGestureType
      Passed on as its number.

    dev : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fingerCount : int
      Passed on as it is.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    value : float
      Passed on as it is.

    delta : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    sequenceId : int
      Passed on as it is. May be left out, as in Qt: it is then
      18446744073709551615.
    """
    #  QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
    #      const QPointingDevice *dev, int fingerCount, const QPointF
    #      &localPos, const QPointF &scenePos, const QPointF &globalPos,
    #      qreal value, const QPointF &delta, quint64 sequenceId)
    self._noteCreation(QNativeGestureEvent, lambda: Rituals.call(
        'ritual_ZN19QNativeGestureEventC1EN2Qt17NativeGestureTypeEPK15QPoin'
        'tingDeviceiRK7QPointFS7_S7_dS7_y',
        type.value, self._addressOf(dev), fingerCount,
        self._valueOf(localPos), self._valueOf(scenePos),
        self._valueOf(globalPos), value, self._valueOf(delta), sequenceId,
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
