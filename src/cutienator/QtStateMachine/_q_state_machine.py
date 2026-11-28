"""
QStateMachine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qstatemachine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QEvent, QList, QObject
from . import QAbstractState, QState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractAnimation, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimation = WAIT['QAbstractAnimation']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStateMachine(QState):
  """
  The cute side of Qt's QStateMachine: a plain Python object standing in
  front of one C++ QStateMachine.

  It is built on the cute 'QState', as Qt's QStateMachine is built on Qt's
  QState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStateMachine that has a ritual and that Python can
  call so far, 32 names in all: 'metaObject', 'tr', 'addState',
  'removeState', 'error', 'errorString', 'clearError', 'isRunning',
  'isAnimated', 'setAnimated', 'addDefaultAnimation', 'defaultAnimations',
  'removeDefaultAnimation', 'globalRestorePolicy', 'setGlobalRestorePolicy',
  'postEvent', 'postDelayedEvent', 'cancelDelayedEvent', 'eventFilter',
  'start', 'stop', 'setRunning', 'started', 'stopped', 'runningChanged',
  'onEntry', 'onExit', 'beginSelectTransitions', 'endSelectTransitions',
  'beginMicrostep', 'endMicrostep', 'event'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStateMachine::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QStateMachine::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QStateMachine::~QStateMachine()': the destructor: Python never
    removes a C++ QStateMachine.
  - Qt's 'QBindable<QString> QStateMachine::bindableErrorString() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QStateMachine::bindableAnimated()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<QState::RestorePolicy>
    QStateMachine::bindableGlobalRestorePolicy()': gives a type Python has no
    way to take yet.
  - Qt's 'QSet<QAbstractState *> QStateMachine::configuration() const': gives
    a type Python has no way to take yet.
  - Qt's 'int QStateMachine::postDelayedEvent(QEvent *event,
    std::chrono::milliseconds delay)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QStateMachine::QStateMachine(QStateMachinePrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QStateMachinePrivate *QStateMachine::d_func()': gives
    'QStateMachinePrivate', which has no cute class yet.
  - Qt's 'const QStateMachinePrivate *QStateMachine::d_func() const': gives
    'QStateMachinePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 49 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QStateMachine is created at the first use, not by
    'QStateMachine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStateMachine.
  - Qt tells when it has removed the C++ QStateMachine. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QStateMachine that has no cute function yet,
    'bindableAnimated', 'bindableErrorString', 'bindableGlobalRestorePolicy',
    'configuration', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QStateMachine, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QStateMachine::Error' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    NoInitialStateError = Kee[int](1)
    NoDefaultStateInHistoryStateError = Kee[int](2)
    NoCommonAncestorForTransitionError = Kee[int](3)
    StateMachineChildModeSetToParallelError = Kee[int](4)

  class EventPriority(CuteNum):
    """
    The enum 'QStateMachine::EventPriority' of Qt, with the 2 names Qt gives
    in it.
    """

    NormalPriority = Kee[int](0)
    HighPriority = Kee[int](1)

  #  The classes Qt writes inside QStateMachine, each a class in here as in
  #  C++.

  class SignalEvent(QEvent):
    """
    The cute side of Qt's QStateMachine::SignalEvent: a plain Python object
    standing in front of one C++ QStateMachine::SignalEvent.

    It is built on the cute 'QEvent', as Qt's QStateMachine::SignalEvent is
    built on Qt's QEvent, and has everything that class has.

    C++ hands a QStateMachine::SignalEvent around as a copy, so every C++
    QStateMachine::SignalEvent behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QStateMachine::SignalEvent that has a ritual and
    that Python can call so far, 3 names in all: 'sender', 'signalIndex',
    'arguments'. It can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QStateMachine::SignalEvent::~SignalEvent()': the destructor:
      Python removes its C++ QStateMachine::SignalEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QStateMachine::SignalEvent is created at the first use, not by
      'QStateMachine::SignalEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QStateMachine::SignalEvent back gives a copy the
      ritual made for Python, in a new cute QStateMachine::SignalEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QObject = WAIT['QObject']
      QVariant = WAIT['QVariant']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QStateMachine::SignalEvent'

    #  A C++ QStateMachine::SignalEvent Python makes is of a C++ class of
    #  ours, in which Python can take functions over. This ritual hands one
    #  over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QStateMachine_SignalEvent'

    #  Qt's '~QStateMachine::SignalEvent()'. Naming it makes this a value
    #  class: Python owns every C++ QStateMachine::SignalEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QStateMachine11SignalEventD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def sender(self) -> Optional[QObject]:
      """
      Calls Qt's 'QObject *QStateMachine::SignalEvent::sender() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-signalevent.html#sender

      Returns
      -------

      Optional[QObject]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QObject *QStateMachine::SignalEvent::sender() const
      address = self.uglySide.call(
          'ritual_ZNK13QStateMachine11SignalEvent6senderEv',
      )
      from ..QtCore import QObject
      return QObject._cuteAt(address)

    def signalIndex(self) -> int:
      """
      Calls Qt's 'int QStateMachine::SignalEvent::signalIndex() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-signalevent.html#signalIndex
      """
      #  int QStateMachine::SignalEvent::signalIndex() const
      return self.uglySide.call(
          'ritual_ZNK13QStateMachine11SignalEvent11signalIndexEv',
      )

    def arguments(self) -> QList[QVariant]:
      """
      Calls Qt's 'QList<QVariant> QStateMachine::SignalEvent::arguments()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-signalevent.html#arguments

      Returns
      -------

      QList[QVariant]
        A new cute list around the copy Qt gave back. Python owns it.
      """
      #  QList<QVariant> QStateMachine::SignalEvent::arguments() const
      address = self.uglySide.call(
          'ritual_ZNK13QStateMachine11SignalEvent9argumentsEv',
      )
      from ..QtCore import QVariant
      return QList[QVariant]._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QObject, int, QList[QVariant])
    @overload(NoneType, int, QList[QVariant])
    def __init__(
        self,
        sender: Optional[QObject],
        signalIndex: int,
        arguments: QList[QVariant],
    ) -> None:
      """
      Notes what was given, for Qt's
      'QStateMachine::SignalEvent::SignalEvent(QObject *sender, int
      signalIndex, const QList<QVariant> &arguments)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-signalevent.html#SignalEvent

      Parameters
      ----------

      sender : Optional[QObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      signalIndex : int
        Passed on as it is.

      arguments : QList[QVariant]
        Passed on as a list of Qt: Qt reads the C++ list, which stays
        Python's own. A list or tuple of Python is made into one first, and
        refused when an element does not fit.
      """
      #  QStateMachine::SignalEvent::SignalEvent(QObject *sender, int
      #      signalIndex, const QList<QVariant> &arguments)
      self._noteCreation(QStateMachine.SignalEvent, lambda: Rituals.call(
          'ritual_ZN13QStateMachine11SignalEventC1EP7QObjectiRK5QListI8QVar'
          'iantE',
          self._addressOf(sender, 'QObject'), signalIndex,
          self._valueOf(arguments),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class WrappedEvent(QEvent):
    """
    The cute side of Qt's QStateMachine::WrappedEvent: a plain Python object
    standing in front of one C++ QStateMachine::WrappedEvent.

    It is built on the cute 'QEvent', as Qt's QStateMachine::WrappedEvent is
    built on Qt's QEvent, and has everything that class has.

    C++ hands a QStateMachine::WrappedEvent around as a copy, so every C++
    QStateMachine::WrappedEvent behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QStateMachine::WrappedEvent that has a ritual and
    that Python can call so far, 2 names in all: 'object', 'event'. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QStateMachine::WrappedEvent::~WrappedEvent()': the destructor:
      Python removes its C++ QStateMachine::WrappedEvent by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QStateMachine::WrappedEvent is created at the first use, not by
      'QStateMachine::WrappedEvent(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QStateMachine::WrappedEvent back gives a copy the
      ritual made for Python, in a new cute QStateMachine::WrappedEvent.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QObject = WAIT['QObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QStateMachine::WrappedEvent'

    #  A C++ QStateMachine::WrappedEvent Python makes is of a C++ class of
    #  ours, in which Python can take functions over. This ritual hands one
    #  over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QStateMachine_WrappedEvent'

    #  Qt's '~QStateMachine::WrappedEvent()'. Naming it makes this a value
    #  class: Python owns every C++ QStateMachine::WrappedEvent behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QStateMachine12WrappedEventD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def object(self) -> Optional[QObject]:
      """
      Calls Qt's 'QObject *QStateMachine::WrappedEvent::object() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-wrappedevent.html#object

      Returns
      -------

      Optional[QObject]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QObject *QStateMachine::WrappedEvent::object() const
      address = self.uglySide.call(
          'ritual_ZNK13QStateMachine12WrappedEvent6objectEv',
      )
      from ..QtCore import QObject
      return QObject._cuteAt(address)

    def event(self) -> Optional[QEvent]:
      """
      Calls Qt's 'QEvent *QStateMachine::WrappedEvent::event() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-wrappedevent.html#event

      Returns
      -------

      Optional[QEvent]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QEvent *QStateMachine::WrappedEvent::event() const
      address = self.uglySide.call(
          'ritual_ZNK13QStateMachine12WrappedEvent5eventEv',
      )
      return QEvent._cuteAt(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QObject, QEvent)
    @overload(QObject, NoneType)
    @overload(NoneType, QEvent)
    @overload(NoneType, NoneType)
    def __init__(
        self,
        object: Optional[QObject],
        event: Optional[QEvent],
    ) -> None:
      """
      Notes what was given, for Qt's
      'QStateMachine::WrappedEvent::WrappedEvent(QObject *object, QEvent
      *event)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qstatemachine-wrappedevent.html#WrappedEvent

      Parameters
      ----------

      object : Optional[QObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      event : Optional[QEvent]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QStateMachine::WrappedEvent::WrappedEvent(QObject *object, QEvent
      #      *event)
      self._noteCreation(QStateMachine.WrappedEvent, lambda: Rituals.call(
          'ritual_ZN13QStateMachine12WrappedEventC1EP7QObjectP6QEvent',
          self._addressOf(object, 'QObject'), self._addressOf(event),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QStateMachine::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStateMachine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QStateMachine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStateMachine'

  #  A C++ QStateMachine Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QStateMachine'

  #  The functions Qt calls itself that QStateMachine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'beginSelectTransitions': (
          ('_ZN13QStateMachine22beginSelectTransitionsEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'endSelectTransitions': (
          ('_ZN13QStateMachine20endSelectTransitionsEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'beginMicrostep': (
          ('_ZN13QStateMachine14beginMicrostepEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'endMicrostep': (
          ('_ZN13QStateMachine12endMicrostepEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStateMachine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStateMachine::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QStateMachine10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def error(self) -> Error:
    """
    Calls Qt's 'Error QStateMachine::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QStateMachine::error() const
    return QStateMachine.Error(self.uglySide.call(
        'ritual_ZNK13QStateMachine5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QStateMachine::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QStateMachine::errorString() const
    return self.uglySide.call('ritual_ZNK13QStateMachine11errorStringEv')

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QStateMachine::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#isRunning
    """
    #  bool QStateMachine::isRunning() const
    return self.uglySide.call('ritual_ZNK13QStateMachine9isRunningEv')

  def isAnimated(self) -> bool:
    """
    Calls Qt's 'bool QStateMachine::isAnimated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#isAnimated
    """
    #  bool QStateMachine::isAnimated() const
    return self.uglySide.call('ritual_ZNK13QStateMachine10isAnimatedEv')

  def defaultAnimations(self) -> QList[QAbstractAnimation]:
    """
    Calls Qt's 'QList<QAbstractAnimation *>
    QStateMachine::defaultAnimations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#defaultAnimations

    Returns
    -------

    QList[QAbstractAnimation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractAnimation *> QStateMachine::defaultAnimations() const
    address = self.uglySide.call(
        'ritual_ZNK13QStateMachine17defaultAnimationsEv',
    )
    from ..QtCore import QAbstractAnimation
    return QList[QAbstractAnimation]._cuteOwning(address)

  def globalRestorePolicy(self) -> QState.RestorePolicy:
    """
    Calls Qt's 'QState::RestorePolicy QStateMachine::globalRestorePolicy()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#globalRestorePolicy

    Returns
    -------

    QState.RestorePolicy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QState.RestorePolicy(number)' gives.
    """
    #  QState::RestorePolicy QStateMachine::globalRestorePolicy() const
    return QState.RestorePolicy(self.uglySide.call(
        'ritual_ZNK13QStateMachine19globalRestorePolicyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAnimated(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QStateMachine::setAnimated(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#setAnimated

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QStateMachine::setAnimated(bool enabled)
    self.uglySide.call('ritual_ZN13QStateMachine11setAnimatedEb', enabled)

  @overload(QState.RestorePolicy)
  def setGlobalRestorePolicy(
      self,
      restorePolicy: QState.RestorePolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QStateMachine::setGlobalRestorePolicy(QState::RestorePolicy
    restorePolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#setGlobalRestorePolicy

    Parameters
    ----------

    restorePolicy : QState.RestorePolicy
      Passed on as its number.
    """
    #  void QStateMachine::setGlobalRestorePolicy(QState::RestorePolicy
    #      restorePolicy)
    self.uglySide.call(
        'ritual_ZN13QStateMachine22setGlobalRestorePolicyEN6QState13Restore'
        'PolicyE',
        restorePolicy.value,
    )

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QStateMachine::setRunning(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QStateMachine::setRunning(bool running)
    self.uglySide.call('ritual_ZN13QStateMachine10setRunningEb', running)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QStateMachine::QStateMachine(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#QStateMachine

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStateMachine::QStateMachine(QObject *parent)
    self._noteCreation(QStateMachine, lambda: Rituals.call(
        'ritual_ZN13QStateMachineC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QState.ChildMode)
  @overload(QState.ChildMode, QObject)
  @overload(QState.ChildMode, NoneType)
  def __init__(
      self,
      childMode: QState.ChildMode,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QStateMachine::QStateMachine(QState::ChildMode childMode, QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#QStateMachine

    Parameters
    ----------

    childMode : QState.ChildMode
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QStateMachine::QStateMachine(QState::ChildMode childMode, QObject
    #      *parent)
    self._noteCreation(QStateMachine, lambda: Rituals.call(
        'ritual_ZN13QStateMachineC1EN6QState9ChildModeEP7QObject',
        childMode.value, self._addressOf(parent, 'QObject'),
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

  @overload(QAbstractState)
  @overload(NoneType)
  def addState(self, state: Optional[QAbstractState]) -> None:
    """
    Calls Qt's 'void QStateMachine::addState(QAbstractState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#addState

    Parameters
    ----------

    state : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::addState(QAbstractState *state)
    self.uglySide.call(
        'ritual_ZN13QStateMachine8addStateEP14QAbstractState',
        self._addressOf(state),
    )

  @overload(QAbstractState)
  @overload(NoneType)
  def removeState(self, state: Optional[QAbstractState]) -> None:
    """
    Calls Qt's 'void QStateMachine::removeState(QAbstractState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#removeState

    Parameters
    ----------

    state : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::removeState(QAbstractState *state)
    self.uglySide.call(
        'ritual_ZN13QStateMachine11removeStateEP14QAbstractState',
        self._addressOf(state),
    )

  def clearError(self) -> None:
    """
    Calls Qt's 'void QStateMachine::clearError()'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#clearError
    """
    #  void QStateMachine::clearError()
    self.uglySide.call('ritual_ZN13QStateMachine10clearErrorEv')

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def addDefaultAnimation(
      self,
      animation: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void QStateMachine::addDefaultAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#addDefaultAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::addDefaultAnimation(QAbstractAnimation *animation)
    self.uglySide.call(
        'ritual_ZN13QStateMachine19addDefaultAnimationEP18QAbstractAnimatio'
        'n',
        self._addressOf(animation),
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def removeDefaultAnimation(
      self,
      animation: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void QStateMachine::removeDefaultAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#removeDefaultAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::removeDefaultAnimation(QAbstractAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN13QStateMachine22removeDefaultAnimationEP18QAbstractAnima'
        'tion',
        self._addressOf(animation),
    )

  @overload(QEvent)
  @overload(NoneType)
  @overload(QEvent, EventPriority)
  @overload(NoneType, EventPriority)
  def postEvent(
      self,
      event: Optional[QEvent],
      priority: EventPriority = EventPriority.NormalPriority,
  ) -> None:
    """
    Calls Qt's 'void QStateMachine::postEvent(QEvent *event, EventPriority
    priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#postEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    priority : EventPriority
      Passed on as its number. May be left out, as in Qt: it is then
      EventPriority.NormalPriority.
    """
    #  void QStateMachine::postEvent(QEvent *event, EventPriority priority)
    self.uglySide.call(
        'ritual_ZN13QStateMachine9postEventEP6QEventNS_13EventPriorityE',
        self._addressOf(event), priority.value,
    )

  @overload(QEvent, int)
  @overload(NoneType, int)
  def postDelayedEvent(self, event: Optional[QEvent], delay: int) -> int:
    """
    Calls Qt's 'int QStateMachine::postDelayedEvent(QEvent *event, int
    delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#postDelayedEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    delay : int
      Passed on as it is.
    """
    #  int QStateMachine::postDelayedEvent(QEvent *event, int delay)
    return self.uglySide.call(
        'ritual_ZN13QStateMachine16postDelayedEventEP6QEventi',
        self._addressOf(event), delay,
    )

  @overload(int)
  def cancelDelayedEvent(self, id: int) -> bool:
    """
    Calls Qt's 'bool QStateMachine::cancelDelayedEvent(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#cancelDelayedEvent

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  bool QStateMachine::cancelDelayedEvent(int id)
    return self.uglySide.call(
        'ritual_ZN13QStateMachine18cancelDelayedEventEi', id,
    )

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QStateMachine::eventFilter(QObject *watched, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStateMachine::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN13QStateMachine11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QStateMachine::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#start
    """
    #  void QStateMachine::start()
    self.uglySide.call('ritual_ZN13QStateMachine5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QStateMachine::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#stop
    """
    #  void QStateMachine::stop()
    self.uglySide.call('ritual_ZN13QStateMachine4stopEv')

  def started(self) -> None:
    """
    Calls Qt's 'void QStateMachine::started(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#started
    """
    #  void QStateMachine::started(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN13QStateMachine7startedENS_14QPrivateSignalE',
    )

  def stopped(self) -> None:
    """
    Calls Qt's 'void QStateMachine::stopped(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#stopped
    """
    #  void QStateMachine::stopped(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN13QStateMachine7stoppedENS_14QPrivateSignalE',
    )

  @overload(bool)
  def runningChanged(self, running: bool) -> None:
    """
    Calls Qt's 'void QStateMachine::runningChanged(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#runningChanged

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QStateMachine::runningChanged(bool running)
    self.uglySide.call('ritual_ZN13QStateMachine14runningChangedEb', running)

  @overload(QEvent)
  @overload(NoneType)
  def onEntry(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QStateMachine::onEntry(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#onEntry

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::onEntry(QEvent *event)
    ritual = 'ritual_ZN13QStateMachine7onEntryEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine7onEntryEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onExit(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QStateMachine::onExit(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#onExit

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::onExit(QEvent *event)
    ritual = 'ritual_ZN13QStateMachine6onExitEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine6onExitEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def beginSelectTransitions(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QStateMachine::beginSelectTransitions(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#beginSelectTransitions

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::beginSelectTransitions(QEvent *event)
    ritual = 'ritual_ZN13QStateMachine22beginSelectTransitionsEP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QStateMachine22beginSelectTransitionsEP6QEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def endSelectTransitions(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QStateMachine::endSelectTransitions(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstatemachine.html#endSelectTransitions

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::endSelectTransitions(QEvent *event)
    ritual = 'ritual_ZN13QStateMachine20endSelectTransitionsEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine20endSelectTransitionsEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def beginMicrostep(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QStateMachine::beginMicrostep(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#beginMicrostep

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::beginMicrostep(QEvent *event)
    ritual = 'ritual_ZN13QStateMachine14beginMicrostepEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine14beginMicrostepEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def endMicrostep(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QStateMachine::endMicrostep(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#endMicrostep

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStateMachine::endMicrostep(QEvent *event)
    ritual = 'ritual_ZN13QStateMachine12endMicrostepEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine12endMicrostepEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QStateMachine::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qstatemachine.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QStateMachine::event(QEvent *e)
    ritual = 'ritual_ZN13QStateMachine5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QStateMachine5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def bindableAnimated(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QStateMachine::bindableAnimated()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStateMachine.bindableAnimated' has no cute function yet. Qt's "
        "'QBindable<bool> QStateMachine::bindableAnimated()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableErrorString(*__, **_) -> Never:
    """
    Qt's 'QBindable<QString> QStateMachine::bindableErrorString() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStateMachine.bindableErrorString' has no cute function yet. Qt's "
        "'QBindable<QString> QStateMachine::bindableErrorString() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableGlobalRestorePolicy(*__, **_) -> Never:
    """
    Qt's 'QBindable<QState::RestorePolicy>
    QStateMachine::bindableGlobalRestorePolicy()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QStateMachine.bindableGlobalRestorePolicy' has no cute function "
        "yet. Qt's 'QBindable<QState::RestorePolicy> "
        "QStateMachine::bindableGlobalRestorePolicy()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def configuration(*__, **_) -> Never:
    """
    Qt's 'QSet<QAbstractState *> QStateMachine::configuration() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QStateMachine.configuration' has no cute function yet. Qt's "
        "'QSet<QAbstractState *> QStateMachine::configuration() const': "
        "gives a type Python has no way to take yet.")
