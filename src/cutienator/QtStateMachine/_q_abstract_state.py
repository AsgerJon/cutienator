"""
QAbstractState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qabstractstate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QState, QStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractState(QObject):
  """
  The cute side of Qt's QAbstractState: a plain Python object standing in
  front of one C++ QAbstractState.

  It is built on the cute 'QObject', as Qt's QAbstractState is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractState that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'parentState', 'machine',
  'active', 'entered', 'exited', 'activeChanged', 'onEntry', 'onExit',
  'event'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractState::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAbstractState::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractState::~QAbstractState()': the destructor: Python never
    removes a C++ QAbstractState.
  - Qt's 'QBindable<bool> QAbstractState::bindableActive()': gives a type
    Python has no way to take yet.
  - Qt's 'QAbstractState::QAbstractState(QAbstractStatePrivate &dd, QState
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractStatePrivate *QAbstractState::d_func()': gives
    'QAbstractStatePrivate', which has no cute class yet.
  - Qt's 'const QAbstractStatePrivate *QAbstractState::d_func() const': gives
    'QAbstractStatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractState is created at the first use, not by
    'QAbstractState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractState.
  - Qt tells when it has removed the C++ QAbstractState. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractState that has no cute function yet,
    'bindableActive', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

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
    Calls Qt's 'QString QAbstractState::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#tr

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
    #  QString QAbstractState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QAbstractState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractState'

  #  A C++ QAbstractState Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractState'

  #  The functions Qt calls itself that QAbstractState is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'onEntry': (
          ('_ZN14QAbstractState7onEntryEP6QEvent',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'onExit': (
          ('_ZN14QAbstractState6onExitEP6QEvent',
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
    Calls Qt's 'const QMetaObject *QAbstractState::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractState::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QAbstractState10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parentState(self) -> Optional[QState]:
    """
    Calls Qt's 'QState *QAbstractState::parentState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#parentState

    Returns
    -------

    Optional[QState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QState *QAbstractState::parentState() const
    address = self.uglySide.call('ritual_ZNK14QAbstractState11parentStateEv')
    from . import QState
    return QState._cuteAt(address)

  def machine(self) -> Optional[QStateMachine]:
    """
    Calls Qt's 'QStateMachine *QAbstractState::machine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#machine

    Returns
    -------

    Optional[QStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStateMachine *QAbstractState::machine() const
    address = self.uglySide.call('ritual_ZNK14QAbstractState7machineEv')
    from . import QStateMachine
    return QStateMachine._cuteAt(address)

  def active(self) -> bool:
    """
    Calls Qt's 'bool QAbstractState::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#active
    """
    #  bool QAbstractState::active() const
    return self.uglySide.call('ritual_ZNK14QAbstractState6activeEv')

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

  @overload()
  @overload(QState)
  @overload(NoneType)
  def __init__(self, parent: Optional[QState] = None) -> None:
    """
    Notes what was given, for Qt's 'QAbstractState::QAbstractState(QState
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#QAbstractState

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractState::QAbstractState(QState *parent)
    self._noteCreation(QAbstractState, lambda: Rituals.call(
        'ritual_ZN14QAbstractStateC1EP6QState', self._addressOf(parent),
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

  def entered(self) -> None:
    """
    Calls Qt's 'void QAbstractState::entered(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#entered
    """
    #  void QAbstractState::entered(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN14QAbstractState7enteredENS_14QPrivateSignalE',
    )

  def exited(self) -> None:
    """
    Calls Qt's 'void QAbstractState::exited(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#exited
    """
    #  void QAbstractState::exited(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN14QAbstractState6exitedENS_14QPrivateSignalE',
    )

  @overload(bool)
  def activeChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QAbstractState::activeChanged(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#activeChanged

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QAbstractState::activeChanged(bool active)
    self.uglySide.call('ritual_ZN14QAbstractState13activeChangedEb', active)

  @overload(QEvent)
  @overload(NoneType)
  def onEntry(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QAbstractState::onEntry(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#onEntry

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractState::onEntry(QEvent *event)
    self.uglySide.call(
        'ritual_ZN14QAbstractState7onEntryEP6QEvent', self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def onExit(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QAbstractState::onExit(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#onExit

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractState::onExit(QEvent *event)
    self.uglySide.call(
        'ritual_ZN14QAbstractState6onExitEP6QEvent', self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractState::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractstate.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractState::event(QEvent *e)
    ritual = 'ritual_ZN14QAbstractState5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QAbstractState5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def bindableActive(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QAbstractState::bindableActive()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractState.bindableActive' has no cute function yet. Qt's "
        "'QBindable<bool> QAbstractState::bindableActive()': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QAbstractState *>': the list of QAbstractState, which
#  'QList[QAbstractState]' gives. It is made here, so that there is one as
#  soon as there can be a QAbstractState.
QList.createKind(
    QAbstractState, 'address',
    make='ritual_list_make_QAbstractState_ptr',
    add='ritual_list_add_QAbstractState_ptr',
    size='ritual_list_size_QAbstractState_ptr',
    at='ritual_list_at_QAbstractState_ptr',
    drop='ritual_list_drop_QAbstractState_ptr',
)
