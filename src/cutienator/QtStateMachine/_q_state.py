"""
QState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qstate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstractState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
  from . import QAbstractTransition, QSignalTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractTransition = WAIT['QAbstractTransition']
  QEvent = WAIT['QEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QState(QAbstractState):
  """
  The cute side of Qt's QState: a plain Python object standing in front of
  one C++ QState.

  It is built on the cute 'QAbstractState', as Qt's QState is built on Qt's
  QAbstractState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QState that has a ritual and that Python can call so
  far, 20 names in all: 'metaObject', 'tr', 'errorState', 'setErrorState',
  'addTransition', 'removeTransition', 'transitions', 'initialState',
  'setInitialState', 'childMode', 'setChildMode', 'assignProperty',
  'finished', 'propertiesAssigned', 'childModeChanged',
  'initialStateChanged', 'errorStateChanged', 'onEntry', 'onExit', 'event'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QState::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QState::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QState::~QState()': the destructor: Python never removes a C++
    QState.
  - Qt's 'QBindable<QAbstractState *> QState::bindableErrorState()': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<QAbstractState *> QState::bindableInitialState()': gives
    a type Python has no way to take yet.
  - Qt's 'QBindable<QState::ChildMode> QState::bindableChildMode()': gives a
    type Python has no way to take yet.
  - Qt's 'QState::QState(QStatePrivate &dd, QState *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QStatePrivate *QState::d_func()': gives 'QStatePrivate', which has
    no cute class yet.
  - Qt's 'const QStatePrivate *QState::d_func() const': gives
    'QStatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 38 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QState is created at the first use, not by 'QState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QState.
  - Qt tells when it has removed the C++ QState. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QState that has no cute function yet,
    'bindableChildMode', 'bindableErrorState', 'bindableInitialState', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QState, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ChildMode(CuteNum):
    """
    The enum 'QState::ChildMode' of Qt, with the 2 names Qt gives in it.
    """

    ExclusiveStates = Kee[int](0)
    ParallelStates = Kee[int](1)

  class RestorePolicy(CuteNum):
    """
    The enum 'QState::RestorePolicy' of Qt, with the 2 names Qt gives in it.
    """

    DontRestoreProperties = Kee[int](0)
    RestoreProperties = Kee[int](1)

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
    Calls Qt's 'QString QState::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#tr

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
    #  QString QState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QState'

  #  A C++ QState Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QState::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QState::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QState10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def errorState(self) -> Optional[QAbstractState]:
    """
    Calls Qt's 'QAbstractState *QState::errorState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#errorState

    Returns
    -------

    Optional[QAbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractState *QState::errorState() const
    address = self.uglySide.call('ritual_ZNK6QState10errorStateEv')
    return QAbstractState._cuteAt(address)

  def transitions(self) -> QList[QAbstractTransition]:
    """
    Calls Qt's 'QList<QAbstractTransition *> QState::transitions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#transitions

    Returns
    -------

    QList[QAbstractTransition]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractTransition *> QState::transitions() const
    address = self.uglySide.call('ritual_ZNK6QState11transitionsEv')
    from . import QAbstractTransition
    return QList[QAbstractTransition]._cuteOwning(address)

  def initialState(self) -> Optional[QAbstractState]:
    """
    Calls Qt's 'QAbstractState *QState::initialState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#initialState

    Returns
    -------

    Optional[QAbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractState *QState::initialState() const
    address = self.uglySide.call('ritual_ZNK6QState12initialStateEv')
    return QAbstractState._cuteAt(address)

  def childMode(self) -> ChildMode:
    """
    Calls Qt's 'ChildMode QState::childMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#childMode

    Returns
    -------

    ChildMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ChildMode(number)' gives.
    """
    #  ChildMode QState::childMode() const
    return QState.ChildMode(self.uglySide.call(
        'ritual_ZNK6QState9childModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractState)
  @overload(NoneType)
  def setErrorState(self, state: Optional[QAbstractState]) -> None:
    """
    Calls Qt's 'void QState::setErrorState(QAbstractState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#setErrorState

    Parameters
    ----------

    state : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QState::setErrorState(QAbstractState *state)
    self.uglySide.call(
        'ritual_ZN6QState13setErrorStateEP14QAbstractState',
        self._addressOf(state),
    )

  @overload(QAbstractState)
  @overload(NoneType)
  def setInitialState(self, state: Optional[QAbstractState]) -> None:
    """
    Calls Qt's 'void QState::setInitialState(QAbstractState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#setInitialState

    Parameters
    ----------

    state : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QState::setInitialState(QAbstractState *state)
    self.uglySide.call(
        'ritual_ZN6QState15setInitialStateEP14QAbstractState',
        self._addressOf(state),
    )

  @overload(ChildMode)
  def setChildMode(self, mode: ChildMode) -> None:
    """
    Calls Qt's 'void QState::setChildMode(ChildMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#setChildMode

    Parameters
    ----------

    mode : ChildMode
      Passed on as its number.
    """
    #  void QState::setChildMode(ChildMode mode)
    self.uglySide.call(
        'ritual_ZN6QState12setChildModeENS_9ChildModeE', mode.value,
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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QState] = None) -> None:
    """
    Notes what was given, for Qt's 'QState::QState(QState *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#QState

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QState::QState(QState *parent)
    self._noteCreation(QState, lambda: Rituals.call(
        'ritual_ZN6QStateC1EPS_', self._addressOf(parent),
    ))

  @overload(ChildMode)
  @overload(ChildMode, THIS)
  @overload(ChildMode, NoneType)
  def __init__(
      self,
      childMode: ChildMode,
      parent: Optional[QState] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QState::QState(ChildMode childMode,
    QState *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#QState

    Parameters
    ----------

    childMode : ChildMode
      Passed on as its number.

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QState::QState(ChildMode childMode, QState *parent)
    self._noteCreation(QState, lambda: Rituals.call(
        'ritual_ZN6QStateC1ENS_9ChildModeEPS_',
        childMode.value, self._addressOf(parent),
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

  @overload(QAbstractTransition)
  @overload(NoneType)
  def addTransition(self, transition: Optional[QAbstractTransition]) -> None:
    """
    Calls Qt's 'void QState::addTransition(QAbstractTransition *transition)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#addTransition

    Parameters
    ----------

    transition : Optional[QAbstractTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QState::addTransition(QAbstractTransition *transition)
    self.uglySide.call(
        'ritual_ZN6QState13addTransitionEP19QAbstractTransition',
        self._addressOf(transition),
    )

  @overload(QObject, str, QAbstractState)
  @overload(QObject, str, NoneType)
  @overload(QObject, NoneType, QAbstractState)
  @overload(QObject, NoneType, NoneType)
  @overload(NoneType, str, QAbstractState)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, QAbstractState)
  @overload(NoneType, NoneType, NoneType)
  def addTransition(
      self,
      sender: Optional[QObject],
      signal: Optional[str],
      target: Optional[QAbstractState],
  ) -> Optional[QSignalTransition]:
    """
    Calls Qt's 'QSignalTransition *QState::addTransition(const QObject
    *sender, const char *signal, QAbstractState *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#addTransition

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    target : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSignalTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSignalTransition *QState::addTransition(const QObject *sender, const
    #      char *signal, QAbstractState *target)
    address = self.uglySide.call(
        'ritual_ZN6QState13addTransitionEPK7QObjectPKcP14QAbstractState',
        self._addressOf(sender, 'QObject'), self._bytesOf(signal),
        self._addressOf(target),
    )
    from . import QSignalTransition
    return QSignalTransition._cuteAt(address)

  @overload(QAbstractState)
  def addTransition(
      self,
      target: Optional[QAbstractState],
  ) -> Optional[QAbstractTransition]:
    """
    Calls Qt's 'QAbstractTransition *QState::addTransition(QAbstractState
    *target)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#addTransition

    Parameters
    ----------

    target : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTransition *QState::addTransition(QAbstractState *target)
    address = self.uglySide.call(
        'ritual_ZN6QState13addTransitionEP14QAbstractState',
        self._addressOf(target),
    )
    from . import QAbstractTransition
    return QAbstractTransition._cuteAt(address)

  @overload(QAbstractTransition)
  @overload(NoneType)
  def removeTransition(
      self,
      transition: Optional[QAbstractTransition],
  ) -> None:
    """
    Calls Qt's 'void QState::removeTransition(QAbstractTransition
    *transition)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#removeTransition

    Parameters
    ----------

    transition : Optional[QAbstractTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QState::removeTransition(QAbstractTransition *transition)
    self.uglySide.call(
        'ritual_ZN6QState16removeTransitionEP19QAbstractTransition',
        self._addressOf(transition),
    )

  @overload(QObject, str, QVariant)
  @overload(QObject, NoneType, QVariant)
  @overload(NoneType, str, QVariant)
  @overload(NoneType, NoneType, QVariant)
  def assignProperty(
      self,
      object: Optional[QObject],
      name: Optional[str],
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QState::assignProperty(QObject *object, const char
    *name, const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#assignProperty

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QState::assignProperty(QObject *object, const char *name, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN6QState14assignPropertyEP7QObjectPKcRK8QVariant',
        self._addressOf(object, 'QObject'), self._bytesOf(name),
        self._valueOf(value),
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QState::finished(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#finished
    """
    #  void QState::finished(QPrivateSignal a0)
    self.uglySide.call('ritual_ZN6QState8finishedENS_14QPrivateSignalE')

  def propertiesAssigned(self) -> None:
    """
    Calls Qt's 'void QState::propertiesAssigned(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#propertiesAssigned
    """
    #  void QState::propertiesAssigned(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN6QState18propertiesAssignedENS_14QPrivateSignalE',
    )

  def childModeChanged(self) -> None:
    """
    Calls Qt's 'void QState::childModeChanged(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#childModeChanged
    """
    #  void QState::childModeChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN6QState16childModeChangedENS_14QPrivateSignalE',
    )

  def initialStateChanged(self) -> None:
    """
    Calls Qt's 'void QState::initialStateChanged(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#initialStateChanged
    """
    #  void QState::initialStateChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN6QState19initialStateChangedENS_14QPrivateSignalE',
    )

  def errorStateChanged(self) -> None:
    """
    Calls Qt's 'void QState::errorStateChanged(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#errorStateChanged
    """
    #  void QState::errorStateChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN6QState17errorStateChangedENS_14QPrivateSignalE',
    )

  @overload(QEvent)
  @overload(NoneType)
  def onEntry(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QState::onEntry(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#onEntry

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QState::onEntry(QEvent *event)
    ritual = 'ritual_ZN6QState7onEntryEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QState7onEntryEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onExit(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QState::onExit(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#onExit

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QState::onExit(QEvent *event)
    ritual = 'ritual_ZN6QState6onExitEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QState6onExitEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QState::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qstate.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QState::event(QEvent *e)
    ritual = 'ritual_ZN6QState5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QState5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def bindableChildMode(*__, **_) -> Never:
    """
    Qt's 'QBindable<QState::ChildMode> QState::bindableChildMode()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QState.bindableChildMode' has no cute function yet. Qt's "
        "'QBindable<QState::ChildMode> QState::bindableChildMode()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def bindableErrorState(*__, **_) -> Never:
    """
    Qt's 'QBindable<QAbstractState *> QState::bindableErrorState()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QState.bindableErrorState' has no cute function yet. Qt's "
        "'QBindable<QAbstractState *> QState::bindableErrorState()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def bindableInitialState(*__, **_) -> Never:
    """
    Qt's 'QBindable<QAbstractState *> QState::bindableInitialState()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QState.bindableInitialState' has no cute function yet. Qt's "
        "'QBindable<QAbstractState *> QState::bindableInitialState()': "
        "gives a type Python has no way to take yet.")
