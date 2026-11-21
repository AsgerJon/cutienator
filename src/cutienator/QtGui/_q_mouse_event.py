"""
QMouseEvent binding of the Qt C++
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


class QMouseEvent(QSinglePointEvent):
  """
  The cute side of Qt's QMouseEvent: a plain Python object standing in front
  of one C++ QMouseEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QMouseEvent is built
  on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMouseEvent that has a ritual and that Python can
  call so far, 12 names in all: 'clone', 'pos', 'globalPos', 'x', 'y',
  'globalX', 'globalY', 'localPos', 'windowPos', 'screenPos', 'source',
  'flags'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMouseEvent::~QMouseEvent()': the destructor: Python never removes
    a C++ QMouseEvent.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QMouseEvent is created at the first use, not by
    'QMouseEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMouseEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMouseEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QMouseEvent]:
    """
    Calls Qt's 'QMouseEvent *QMouseEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#clone

    Returns
    -------

    Optional[QMouseEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMouseEvent *QMouseEvent::clone() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent5cloneEv')
    return QMouseEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QMouseEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QMouseEvent::pos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def globalPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QMouseEvent::globalPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#globalPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QMouseEvent::globalPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent9globalPosEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def x(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#x
    """
    #  int QMouseEvent::x() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent1xEv')

  def y(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#y
    """
    #  int QMouseEvent::y() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent1yEv')

  def globalX(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::globalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#globalX
    """
    #  int QMouseEvent::globalX() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent7globalXEv')

  def globalY(self) -> int:
    """
    Calls Qt's 'int QMouseEvent::globalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#globalY
    """
    #  int QMouseEvent::globalY() const
    return self.uglySide.call('ritual_ZNK11QMouseEvent7globalYEv')

  def localPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QMouseEvent::localPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#localPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMouseEvent::localPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent8localPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def windowPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QMouseEvent::windowPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#windowPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMouseEvent::windowPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent9windowPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def screenPos(self) -> QPointF:
    """
    Calls Qt's 'QPointF QMouseEvent::screenPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#screenPos

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QMouseEvent::screenPos() const
    address = self.uglySide.call('ritual_ZNK11QMouseEvent9screenPosEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def source(self) -> Qt.MouseEventSource:
    """
    Calls Qt's 'Qt::MouseEventSource QMouseEvent::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#source

    Returns
    -------

    Qt.MouseEventSource
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.MouseEventSource(number)' gives.
    """
    #  Qt::MouseEventSource QMouseEvent::source() const
    return Qt.MouseEventSource(self.uglySide.call(
        'ritual_ZNK11QMouseEvent6sourceEv',
    ))

  def flags(self) -> Qt.MouseEventFlags:
    """
    Calls Qt's 'Qt::MouseEventFlags QMouseEvent::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#flags

    Returns
    -------

    Qt.MouseEventFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::MouseEventFlags QMouseEvent::flags() const
    return Qt.MouseEventFlags(self.uglySide.call(
        'ritual_ZNK11QMouseEvent5flagsEv',
    ))

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
      QEvent.Type, QPointF, Qt.MouseButton, Qt.MouseButtons,
      Qt.KeyboardModifiers, QPointingDevice,
  )
  @overload(
      QEvent.Type, QPointF, Qt.MouseButton, Qt.MouseButtons,
      Qt.KeyboardModifiers, NoneType,
  )
  def __init__(
      self,
      type: QEvent.Type,
      localPos: QPointF,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      device: Optional[QPointingDevice],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMouseEvent::QMouseEvent(Type type, const
    QPointF &localPos, Qt::MouseButton button, Qt::MouseButtons buttons,
    Qt::KeyboardModifiers modifiers, const QPointingDevice *device)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos,
    #      Qt::MouseButton button, Qt::MouseButtons buttons,
    #      Qt::KeyboardModifiers modifiers, const QPointingDevice *device)
    self._noteCreation(QMouseEvent, lambda: Rituals.call(
        'ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFN2Qt11MouseButton'
        'E6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice',
        type.value, self._valueOf(localPos), button.value, buttons.value,
        modifiers.value, self._addressOf(device),
    ))

  @overload(
      QEvent.Type, QPointF, QPointF, Qt.MouseButton, Qt.MouseButtons,
      Qt.KeyboardModifiers, QPointingDevice,
  )
  @overload(
      QEvent.Type, QPointF, QPointF, Qt.MouseButton, Qt.MouseButtons,
      Qt.KeyboardModifiers, NoneType,
  )
  def __init__(
      self,
      type: QEvent.Type,
      localPos: QPointF,
      globalPos: QPointF,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      device: Optional[QPointingDevice],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMouseEvent::QMouseEvent(Type type, const
    QPointF &localPos, const QPointF &globalPos, Qt::MouseButton button,
    Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers, const
    QPointingDevice *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
    #      QPointF &globalPos, Qt::MouseButton button, Qt::MouseButtons
    #      buttons, Qt::KeyboardModifiers modifiers, const QPointingDevice
    #      *device)
    self._noteCreation(QMouseEvent, lambda: Rituals.call(
        'ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_N2Qt11MouseBut'
        'tonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice',
        type.value, self._valueOf(localPos), self._valueOf(globalPos),
        button.value, buttons.value, modifiers.value,
        self._addressOf(device),
    ))

  @overload(
      QEvent.Type, QPointF, QPointF, QPointF, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers, QPointingDevice,
  )
  @overload(
      QEvent.Type, QPointF, QPointF, QPointF, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers, NoneType,
  )
  def __init__(
      self,
      type: QEvent.Type,
      localPos: QPointF,
      scenePos: QPointF,
      globalPos: QPointF,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      device: Optional[QPointingDevice],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMouseEvent::QMouseEvent(Type type, const
    QPointF &localPos, const QPointF &scenePos, const QPointF &globalPos,
    Qt::MouseButton button, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    modifiers, const QPointingDevice *device)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
    #      QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton
    #      button, Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    #      const QPointingDevice *device)
    self._noteCreation(QMouseEvent, lambda: Rituals.call(
        'ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_S4_N2Qt11Mouse'
        'ButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEEPK15QPointingDevice',
        type.value, self._valueOf(localPos), self._valueOf(scenePos),
        self._valueOf(globalPos), button.value, buttons.value,
        modifiers.value, self._addressOf(device),
    ))

  @overload(
      QEvent.Type, QPointF, QPointF, QPointF, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers, Qt.MouseEventSource,
      QPointingDevice,
  )
  @overload(
      QEvent.Type, QPointF, QPointF, QPointF, Qt.MouseButton,
      Qt.MouseButtons, Qt.KeyboardModifiers, Qt.MouseEventSource, NoneType,
  )
  def __init__(
      self,
      type: QEvent.Type,
      localPos: QPointF,
      scenePos: QPointF,
      globalPos: QPointF,
      button: Qt.MouseButton,
      buttons: Qt.MouseButtons,
      modifiers: Qt.KeyboardModifiers,
      source: Qt.MouseEventSource,
      device: Optional[QPointingDevice],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMouseEvent::QMouseEvent(Type type, const
    QPointF &localPos, const QPointF &scenePos, const QPointF &globalPos,
    Qt::MouseButton button, Qt::MouseButtons buttons, Qt::KeyboardModifiers
    modifiers, Qt::MouseEventSource source, const QPointingDevice *device)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmouseevent.html#QMouseEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    button : Qt.MouseButton
      Passed on as its number.

    buttons : Qt.MouseButtons
      Passed on as its number.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    source : Qt.MouseEventSource
      Passed on as its number.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QMouseEvent::QMouseEvent(Type type, const QPointF &localPos, const
    #      QPointF &scenePos, const QPointF &globalPos, Qt::MouseButton
    #      button, Qt::MouseButtons buttons, Qt::KeyboardModifiers modifiers,
    #      Qt::MouseEventSource source, const QPointingDevice *device)
    self._noteCreation(QMouseEvent, lambda: Rituals.call(
        'ritual_ZN11QMouseEventC1EN6QEvent4TypeERK7QPointFS4_S4_N2Qt11Mouse'
        'ButtonE6QFlagsIS6_ES7_INS5_16KeyboardModifierEENS5_16MouseEventSou'
        'rceEPK15QPointingDevice',
        type.value, self._valueOf(localPos), self._valueOf(scenePos),
        self._valueOf(globalPos), button.value, buttons.value,
        modifiers.value, source.value, self._addressOf(device),
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
