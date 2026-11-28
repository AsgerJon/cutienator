"""
QFinalState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qfinalstate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QAbstractState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFinalState(QAbstractState):
  """
  The cute side of Qt's QFinalState: a plain Python object standing in front
  of one C++ QFinalState.

  It is built on the cute 'QAbstractState', as Qt's QFinalState is built on
  Qt's QAbstractState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFinalState that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'tr', 'onEntry', 'onExit',
  'event'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFinalState::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QFinalState::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QFinalState::~QFinalState()': the destructor: Python never removes
    a C++ QFinalState.
  - Qt's 'QFinalState::QFinalState(QFinalStatePrivate &dd, QState *parent)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QFinalStatePrivate *QFinalState::d_func()': gives
    'QFinalStatePrivate', which has no cute class yet.
  - Qt's 'const QFinalStatePrivate *QFinalState::d_func() const': gives
    'QFinalStatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QFinalState is created at the first use, not by
    'QFinalState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFinalState.
  - Qt tells when it has removed the C++ QFinalState. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QFinalState::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfinalstate.html#tr

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
    #  QString QFinalState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QFinalState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFinalState'

  #  A C++ QFinalState Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFinalState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFinalState::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfinalstate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFinalState::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QFinalState10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QFinalState::QFinalState(QState
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfinalstate.html#QFinalState

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFinalState::QFinalState(QState *parent)
    self._noteCreation(QFinalState, lambda: Rituals.call(
        'ritual_ZN11QFinalStateC1EP6QState', self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def onEntry(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QFinalState::onEntry(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfinalstate.html#onEntry

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFinalState::onEntry(QEvent *event)
    ritual = 'ritual_ZN11QFinalState7onEntryEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFinalState7onEntryEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onExit(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QFinalState::onExit(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfinalstate.html#onExit

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFinalState::onExit(QEvent *event)
    ritual = 'ritual_ZN11QFinalState6onExitEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFinalState6onExitEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QFinalState::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qfinalstate.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFinalState::event(QEvent *e)
    ritual = 'ritual_ZN11QFinalState5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFinalState5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))
