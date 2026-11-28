"""
QHistoryState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qhistorystate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QAbstractState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QAbstractTransition, QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractTransition = WAIT['QAbstractTransition']
  QEvent = WAIT['QEvent']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHistoryState(QAbstractState):
  """
  The cute side of Qt's QHistoryState: a plain Python object standing in
  front of one C++ QHistoryState.

  It is built on the cute 'QAbstractState', as Qt's QHistoryState is built on
  Qt's QAbstractState, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHistoryState that has a ritual and that Python can
  call so far, 14 names in all: 'metaObject', 'tr', 'defaultTransition',
  'setDefaultTransition', 'defaultState', 'setDefaultState', 'historyType',
  'setHistoryType', 'defaultTransitionChanged', 'defaultStateChanged',
  'historyTypeChanged', 'onEntry', 'onExit', 'event'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QHistoryState::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QHistoryState::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QHistoryState::~QHistoryState()': the destructor: Python never
    removes a C++ QHistoryState.
  - Qt's 'QBindable<QAbstractTransition *>
    QHistoryState::bindableDefaultTransition()': gives a type Python has no
    way to take yet.
  - Qt's 'QBindable<QHistoryState::HistoryType>
    QHistoryState::bindableHistoryType()': gives a type Python has no way to
    take yet.
  - Qt's 'QHistoryStatePrivate *QHistoryState::d_func()': gives
    'QHistoryStatePrivate', which has no cute class yet.
  - Qt's 'const QHistoryStatePrivate *QHistoryState::d_func() const': gives
    'QHistoryStatePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QHistoryState is created at the first use, not by
    'QHistoryState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHistoryState.
  - Qt tells when it has removed the C++ QHistoryState. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QHistoryState that has no cute function yet,
    'bindableDefaultTransition', 'bindableHistoryType', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QHistoryState, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HistoryType(CuteNum):
    """
    The enum 'QHistoryState::HistoryType' of Qt, with the 2 names Qt gives in
    it.
    """

    ShallowHistory = Kee[int](0)
    DeepHistory = Kee[int](1)

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
    Calls Qt's 'QString QHistoryState::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#tr

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
    #  QString QHistoryState::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QHistoryState2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHistoryState'

  #  A C++ QHistoryState Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHistoryState'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QHistoryState::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QHistoryState::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QHistoryState10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultTransition(self) -> Optional[QAbstractTransition]:
    """
    Calls Qt's 'QAbstractTransition *QHistoryState::defaultTransition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhistorystate.html#defaultTransition

    Returns
    -------

    Optional[QAbstractTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractTransition *QHistoryState::defaultTransition() const
    address = self.uglySide.call(
        'ritual_ZNK13QHistoryState17defaultTransitionEv',
    )
    from . import QAbstractTransition
    return QAbstractTransition._cuteAt(address)

  def defaultState(self) -> Optional[QAbstractState]:
    """
    Calls Qt's 'QAbstractState *QHistoryState::defaultState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#defaultState

    Returns
    -------

    Optional[QAbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractState *QHistoryState::defaultState() const
    address = self.uglySide.call('ritual_ZNK13QHistoryState12defaultStateEv')
    return QAbstractState._cuteAt(address)

  def historyType(self) -> HistoryType:
    """
    Calls Qt's 'HistoryType QHistoryState::historyType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#historyType

    Returns
    -------

    HistoryType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HistoryType(number)'
      gives.
    """
    #  HistoryType QHistoryState::historyType() const
    return QHistoryState.HistoryType(self.uglySide.call(
        'ritual_ZNK13QHistoryState11historyTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractTransition)
  @overload(NoneType)
  def setDefaultTransition(
      self,
      transition: Optional[QAbstractTransition],
  ) -> None:
    """
    Calls Qt's 'void QHistoryState::setDefaultTransition(QAbstractTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhistorystate.html#setDefaultTransition

    Parameters
    ----------

    transition : Optional[QAbstractTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHistoryState::setDefaultTransition(QAbstractTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN13QHistoryState20setDefaultTransitionEP19QAbstractTransit'
        'ion',
        self._addressOf(transition),
    )

  @overload(QAbstractState)
  @overload(NoneType)
  def setDefaultState(self, state: Optional[QAbstractState]) -> None:
    """
    Calls Qt's 'void QHistoryState::setDefaultState(QAbstractState *state)'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#setDefaultState

    Parameters
    ----------

    state : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHistoryState::setDefaultState(QAbstractState *state)
    self.uglySide.call(
        'ritual_ZN13QHistoryState15setDefaultStateEP14QAbstractState',
        self._addressOf(state),
    )

  @overload(HistoryType)
  def setHistoryType(self, type: HistoryType) -> None:
    """
    Calls Qt's 'void QHistoryState::setHistoryType(HistoryType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#setHistoryType

    Parameters
    ----------

    type : HistoryType
      Passed on as its number.
    """
    #  void QHistoryState::setHistoryType(HistoryType type)
    self.uglySide.call(
        'ritual_ZN13QHistoryState14setHistoryTypeENS_11HistoryTypeE',
        type.value,
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
  @overload(QState)
  @overload(NoneType)
  def __init__(self, parent: Optional[QState] = None) -> None:
    """
    Notes what was given, for Qt's 'QHistoryState::QHistoryState(QState
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#QHistoryState

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHistoryState::QHistoryState(QState *parent)
    self._noteCreation(QHistoryState, lambda: Rituals.call(
        'ritual_ZN13QHistoryStateC1EP6QState', self._addressOf(parent),
    ))

  @overload(HistoryType)
  @overload(HistoryType, QState)
  @overload(HistoryType, NoneType)
  def __init__(
      self,
      type: HistoryType,
      parent: Optional[QState] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHistoryState::QHistoryState(HistoryType
    type, QState *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#QHistoryState

    Parameters
    ----------

    type : HistoryType
      Passed on as its number.

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHistoryState::QHistoryState(HistoryType type, QState *parent)
    self._noteCreation(QHistoryState, lambda: Rituals.call(
        'ritual_ZN13QHistoryStateC1ENS_11HistoryTypeEP6QState',
        type.value, self._addressOf(parent),
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

  def defaultTransitionChanged(self) -> None:
    """
    Calls Qt's 'void QHistoryState::defaultTransitionChanged(QPrivateSignal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhistorystate.html#defaultTransitionChanged
    """
    #  void QHistoryState::defaultTransitionChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN13QHistoryState24defaultTransitionChangedENS_14QPrivateSi'
        'gnalE',
    )

  def defaultStateChanged(self) -> None:
    """
    Calls Qt's 'void QHistoryState::defaultStateChanged(QPrivateSignal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhistorystate.html#defaultStateChanged
    """
    #  void QHistoryState::defaultStateChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN13QHistoryState19defaultStateChangedENS_14QPrivateSignalE',
    )

  def historyTypeChanged(self) -> None:
    """
    Calls Qt's 'void QHistoryState::historyTypeChanged(QPrivateSignal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhistorystate.html#historyTypeChanged
    """
    #  void QHistoryState::historyTypeChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN13QHistoryState18historyTypeChangedENS_14QPrivateSignalE',
    )

  @overload(QEvent)
  @overload(NoneType)
  def onEntry(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QHistoryState::onEntry(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#onEntry

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHistoryState::onEntry(QEvent *event)
    ritual = 'ritual_ZN13QHistoryState7onEntryEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QHistoryState7onEntryEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onExit(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QHistoryState::onExit(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#onExit

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QHistoryState::onExit(QEvent *event)
    ritual = 'ritual_ZN13QHistoryState6onExitEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QHistoryState6onExitEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QHistoryState::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qhistorystate.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QHistoryState::event(QEvent *e)
    ritual = 'ritual_ZN13QHistoryState5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QHistoryState5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def bindableDefaultTransition(*__, **_) -> Never:
    """
    Qt's 'QBindable<QAbstractTransition *>
    QHistoryState::bindableDefaultTransition()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QHistoryState.bindableDefaultTransition' has no cute function "
        "yet. Qt's 'QBindable<QAbstractTransition *> "
        "QHistoryState::bindableDefaultTransition()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableHistoryType(*__, **_) -> Never:
    """
    Qt's 'QBindable<QHistoryState::HistoryType>
    QHistoryState::bindableHistoryType()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QHistoryState.bindableHistoryType' has no cute function yet. Qt's "
        "'QBindable<QHistoryState::HistoryType> "
        "QHistoryState::bindableHistoryType()': gives a type Python has no "
        "way to take yet.")
