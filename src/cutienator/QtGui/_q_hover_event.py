"""
QHoverEvent binding of the Qt C++
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


class QHoverEvent(QSinglePointEvent):
  """
  The cute side of Qt's QHoverEvent: a plain Python object standing in front
  of one C++ QHoverEvent.

  It is built on the cute 'QSinglePointEvent', as Qt's QHoverEvent is built
  on Qt's QSinglePointEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHoverEvent that has a ritual and that Python can
  call so far, 6 names in all: 'clone', 'pos', 'posF', 'isUpdateEvent',
  'oldPos', 'oldPosF'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHoverEvent::QHoverEvent(const QHoverEvent &a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QHoverEvent &QHoverEvent::operator=(const QHoverEvent &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHoverEvent::~QHoverEvent()': the destructor: Python never removes
    a C++ QHoverEvent.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QHoverEvent is created at the first use, not by
    'QHoverEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHoverEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHoverEvent'

  #  A C++ QHoverEvent Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHoverEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QHoverEvent]:
    """
    Calls Qt's 'QHoverEvent *QHoverEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#clone

    Returns
    -------

    Optional[QHoverEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHoverEvent *QHoverEvent::clone() const
    ritual = 'ritual_ZNK11QHoverEvent5cloneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QHoverEvent5cloneEv'
    address = self.uglySide.call(ritual)
    return QHoverEvent._cuteAt(address)

  def pos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QHoverEvent::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#pos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QHoverEvent::pos() const
    address = self.uglySide.call('ritual_ZNK11QHoverEvent3posEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def posF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QHoverEvent::posF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#posF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QHoverEvent::posF() const
    address = self.uglySide.call('ritual_ZNK11QHoverEvent4posFEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def isUpdateEvent(self) -> bool:
    """
    Calls Qt's 'bool QHoverEvent::isUpdateEvent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#isUpdateEvent
    """
    #  bool QHoverEvent::isUpdateEvent() const
    ritual = 'ritual_ZNK11QHoverEvent13isUpdateEventEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QHoverEvent13isUpdateEventEv'
    return self.uglySide.call(ritual)

  def oldPos(self) -> QPoint:
    """
    Calls Qt's 'QPoint QHoverEvent::oldPos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#oldPos

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QHoverEvent::oldPos() const
    address = self.uglySide.call('ritual_ZNK11QHoverEvent6oldPosEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def oldPosF(self) -> QPointF:
    """
    Calls Qt's 'QPointF QHoverEvent::oldPosF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#oldPosF

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QHoverEvent::oldPosF() const
    address = self.uglySide.call('ritual_ZNK11QHoverEvent7oldPosFEv')
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

  @overload(QEvent.Type, QPointF, QPointF, QPointF)
  @overload(QEvent.Type, QPointF, QPointF, QPointF, Qt.KeyboardModifiers)
  @overload(
      QEvent.Type, QPointF, QPointF, QPointF, Qt.KeyboardModifiers,
      QPointingDevice,
  )
  @overload(
      QEvent.Type, QPointF, QPointF, QPointF, Qt.KeyboardModifiers, NoneType,
  )
  def __init__(
      self,
      type: QEvent.Type,
      scenePos: QPointF,
      globalPos: QPointF,
      oldPos: QPointF,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
      device: Optional[QPointingDevice] = ...,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHoverEvent::QHoverEvent(Type type, const
    QPointF &scenePos, const QPointF &globalPos, const QPointF &oldPos,
    Qt::KeyboardModifiers modifiers, const QPointingDevice *device)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#QHoverEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    scenePos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    globalPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    oldPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: what
      'QPointingDevice.primaryPointingDevice()' gives is then passed on.
    """
    #  QHoverEvent::QHoverEvent(Type type, const QPointF &scenePos, const
    #      QPointF &globalPos, const QPointF &oldPos, Qt::KeyboardModifiers
    #      modifiers, const QPointingDevice *device)
    if device is ...:
      from . import QPointingDevice
      device = QPointingDevice.primaryPointingDevice()
    self._noteCreation(QHoverEvent, lambda: Rituals.call(
        'ritual_ZN11QHoverEventC1EN6QEvent4TypeERK7QPointFS4_S4_6QFlagsIN2Q'
        't16KeyboardModifierEEPK15QPointingDevice',
        type.value, self._valueOf(scenePos, 'QPointF'),
        self._valueOf(globalPos, 'QPointF'), self._valueOf(oldPos,
        'QPointF'), modifiers.value, self._addressOf(device),
    ))

  @overload(QEvent.Type, QPointF, QPointF)
  @overload(QEvent.Type, QPointF, QPointF, Qt.KeyboardModifiers)
  @overload(
      QEvent.Type, QPointF, QPointF, Qt.KeyboardModifiers, QPointingDevice,
  )
  @overload(QEvent.Type, QPointF, QPointF, Qt.KeyboardModifiers, NoneType)
  def __init__(
      self,
      type: QEvent.Type,
      pos: QPointF,
      oldPos: QPointF,
      modifiers: Qt.KeyboardModifiers = Qt.KeyboardModifiers.NoModifier,
      device: Optional[QPointingDevice] = ...,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHoverEvent::QHoverEvent(Type type, const
    QPointF &pos, const QPointF &oldPos, Qt::KeyboardModifiers modifiers,
    const QPointingDevice *device)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhoverevent.html#QHoverEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    oldPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.KeyboardModifiers.NoModifier.

    device : Optional[QPointingDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: what
      'QPointingDevice.primaryPointingDevice()' gives is then passed on.
    """
    #  QHoverEvent::QHoverEvent(Type type, const QPointF &pos, const QPointF
    #      &oldPos, Qt::KeyboardModifiers modifiers, const QPointingDevice
    #      *device)
    if device is ...:
      from . import QPointingDevice
      device = QPointingDevice.primaryPointingDevice()
    self._noteCreation(QHoverEvent, lambda: Rituals.call(
        'ritual_ZN11QHoverEventC1EN6QEvent4TypeERK7QPointFS4_6QFlagsIN2Qt16'
        'KeyboardModifierEEPK15QPointingDevice',
        type.value, self._valueOf(pos, 'QPointF'), self._valueOf(oldPos,
        'QPointF'), modifiers.value, self._addressOf(device),
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
