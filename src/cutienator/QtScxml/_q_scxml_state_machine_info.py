"""
QScxmlStateMachineInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachineinfo_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QScxmlStateMachineInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlStateMachineInfo(QObject):
  """
  The cute side of Qt's QScxmlStateMachineInfo: a plain Python object
  standing in front of one C++ QScxmlStateMachineInfo.

  It is built on the cute 'QObject', as Qt's QScxmlStateMachineInfo is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlStateMachineInfo that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr',
  'stateMachine', 'stateName', 'stateParent', 'stateType',
  'initialTransition', 'transitionType', 'transitionSource',
  'transitionEvents'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlStateMachineInfo::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QScxmlStateMachineInfo::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QList<StateId> QScxmlStateMachineInfo::allStates() const': gives a
    type Python has no way to take yet.
  - Qt's 'QList<TransitionId> QScxmlStateMachineInfo::allTransitions()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<StateId> QScxmlStateMachineInfo::stateChildren(StateId
    stateId) const': gives a type Python has no way to take yet.
  - Qt's 'QList<StateId>
    QScxmlStateMachineInfo::transitionTargets(TransitionId transitionId)
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<StateId> QScxmlStateMachineInfo::configuration() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QScxmlStateMachineInfo::statesEntered(const
    QList<QScxmlStateMachineInfo::StateId> &states)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QScxmlStateMachineInfo::statesExited(const
    QList<QScxmlStateMachineInfo::StateId> &states)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QScxmlStateMachineInfo::transitionsTriggered(const
    QList<QScxmlStateMachineInfo::TransitionId> &transitions)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QScxmlStateMachineInfoPrivate *QScxmlStateMachineInfo::d_func()':
    gives 'QScxmlStateMachineInfoPrivate', which has no cute class yet.
  - Qt's 'const QScxmlStateMachineInfoPrivate
    *QScxmlStateMachineInfo::d_func() const': gives
    'QScxmlStateMachineInfoPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 25 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlStateMachineInfo is created at the first use, not by
    'QScxmlStateMachineInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlStateMachineInfo.
  - Qt tells when it has removed the C++ QScxmlStateMachineInfo. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlStateMachineInfo that has no cute function yet,
    'allStates', 'allTransitions', 'configuration', 'stateChildren',
    'statesEntered', 'statesExited', 'transitionTargets',
    'transitionsTriggered', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QScxmlStateMachineInfo, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class StateType(CuteNum):
    """
    The enum 'QScxmlStateMachineInfo::StateType' of Qt, with the 6 names Qt
    gives in it.
    """

    InvalidState = Kee[int](-1)
    NormalState = Kee[int](0)
    ParallelState = Kee[int](1)
    FinalState = Kee[int](2)
    ShallowHistoryState = Kee[int](3)
    DeepHistoryState = Kee[int](4)

  class TransitionType(CuteNum):
    """
    The enum 'QScxmlStateMachineInfo::TransitionType' of Qt, with the 4 names
    Qt gives in it.
    """

    InvalidTransition = Kee[int](-1)
    InternalTransition = Kee[int](0)
    ExternalTransition = Kee[int](1)
    SyntheticTransition = Kee[int](2)

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
    Calls Qt's 'QString QScxmlStateMachineInfo::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#tr

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
    #  QString QScxmlStateMachineInfo::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QScxmlStateMachineInfo2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlStateMachineInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlStateMachineInfo::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlStateMachineInfo::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlStateMachineInfo::stateMachine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#stateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlStateMachineInfo::stateMachine() const
    address = self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo12stateMachineEv',
    )
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  @overload(int)
  def stateName(self, stateId: int) -> str:
    """
    Calls Qt's 'QString QScxmlStateMachineInfo::stateName(int stateId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#stateName

    Parameters
    ----------

    stateId : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlStateMachineInfo::stateName(int stateId) const
    return self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo9stateNameEi', stateId,
    )

  @overload(int)
  def stateParent(self, stateId: int) -> int:
    """
    Calls Qt's 'StateId QScxmlStateMachineInfo::stateParent(StateId stateId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#stateParent

    Parameters
    ----------

    stateId : int
      Passed on as it is.
    """
    #  StateId QScxmlStateMachineInfo::stateParent(StateId stateId) const
    return self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo11stateParentEi', stateId,
    )

  @overload(int)
  def stateType(self, stateId: int) -> StateType:
    """
    Calls Qt's 'StateType QScxmlStateMachineInfo::stateType(int stateId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#stateType

    Parameters
    ----------

    stateId : int
      Passed on as it is.

    Returns
    -------

    StateType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StateType(number)' gives.
    """
    #  StateType QScxmlStateMachineInfo::stateType(int stateId) const
    return QScxmlStateMachineInfo.StateType(self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo9stateTypeEi', stateId,
    ))

  @overload(int)
  def initialTransition(self, stateId: int) -> int:
    """
    Calls Qt's 'TransitionId
    QScxmlStateMachineInfo::initialTransition(StateId stateId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#initialTransition

    Parameters
    ----------

    stateId : int
      Passed on as it is.
    """
    #  TransitionId QScxmlStateMachineInfo::initialTransition(StateId
    #      stateId) const
    return self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo17initialTransitionEi', stateId,
    )

  @overload(int)
  def transitionType(self, transitionId: int) -> TransitionType:
    """
    Calls Qt's 'TransitionType
    QScxmlStateMachineInfo::transitionType(TransitionId transitionId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#transitionType

    Parameters
    ----------

    transitionId : int
      Passed on as it is.

    Returns
    -------

    TransitionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransitionType(number)'
      gives.
    """
    #  TransitionType QScxmlStateMachineInfo::transitionType(TransitionId
    #      transitionId) const
    return QScxmlStateMachineInfo.TransitionType(self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo14transitionTypeEi', transitionId,
    ))

  @overload(int)
  def transitionSource(self, transitionId: int) -> int:
    """
    Calls Qt's 'StateId QScxmlStateMachineInfo::transitionSource(TransitionId
    transitionId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#transitionSource

    Parameters
    ----------

    transitionId : int
      Passed on as it is.
    """
    #  StateId QScxmlStateMachineInfo::transitionSource(TransitionId
    #      transitionId) const
    return self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo16transitionSourceEi',
        transitionId,
    )

  @overload(int)
  def transitionEvents(self, transitionId: int) -> QStringList:
    """
    Calls Qt's 'QList<QString>
    QScxmlStateMachineInfo::transitionEvents(TransitionId transitionId)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#transitionEvents

    Parameters
    ----------

    transitionId : int
      Passed on as it is.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QScxmlStateMachineInfo::transitionEvents(TransitionId
    #      transitionId) const
    address = self.uglySide.call(
        'ritual_ZNK22QScxmlStateMachineInfo16transitionEventsEi',
        transitionId,
    )
    return QStringList._cuteOwning(address)

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

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def __init__(self, stateMachine: Optional[QScxmlStateMachine]) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlStateMachineInfo::QScxmlStateMachineInfo(QScxmlStateMachine
    *stateMachine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachineinfo.html#QScxmlStateMachineInfo

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlStateMachineInfo::QScxmlStateMachineInfo(QScxmlStateMachine
    #      *stateMachine)
    self._noteCreation(QScxmlStateMachineInfo, lambda: Rituals.call(
        'ritual_ZN22QScxmlStateMachineInfoC1EP18QScxmlStateMachine',
        self._addressOf(stateMachine),
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

  @staticmethod
  def allStates(*__, **_) -> Never:
    """
    Qt's 'QList<StateId> QScxmlStateMachineInfo::allStates() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.allStates' has no cute function yet. Qt's "
        "'QList<StateId> QScxmlStateMachineInfo::allStates() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def allTransitions(*__, **_) -> Never:
    """
    Qt's 'QList<TransitionId> QScxmlStateMachineInfo::allTransitions()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.allTransitions' has no cute function yet. "
        "Qt's 'QList<TransitionId> QScxmlStateMachineInfo::allTransitions() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def configuration(*__, **_) -> Never:
    """
    Qt's 'QList<StateId> QScxmlStateMachineInfo::configuration() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.configuration' has no cute function yet. "
        "Qt's 'QList<StateId> QScxmlStateMachineInfo::configuration() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def stateChildren(*__, **_) -> Never:
    """
    Qt's 'QList<StateId> QScxmlStateMachineInfo::stateChildren(StateId
    stateId) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.stateChildren' has no cute function yet. "
        "Qt's 'QList<StateId> QScxmlStateMachineInfo::stateChildren(StateId "
        "stateId) const': gives a type Python has no way to take yet.")

  @staticmethod
  def statesEntered(*__, **_) -> Never:
    """
    Qt's 'void QScxmlStateMachineInfo::statesEntered(const
    QList<QScxmlStateMachineInfo::StateId> &states)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.statesEntered' has no cute function yet. "
        "Qt's 'void QScxmlStateMachineInfo::statesEntered(const "
        "QList<QScxmlStateMachineInfo::StateId> &states)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def statesExited(*__, **_) -> Never:
    """
    Qt's 'void QScxmlStateMachineInfo::statesExited(const
    QList<QScxmlStateMachineInfo::StateId> &states)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.statesExited' has no cute function yet. "
        "Qt's 'void QScxmlStateMachineInfo::statesExited(const "
        "QList<QScxmlStateMachineInfo::StateId> &states)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def transitionTargets(*__, **_) -> Never:
    """
    Qt's 'QList<StateId>
    QScxmlStateMachineInfo::transitionTargets(TransitionId transitionId)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.transitionTargets' has no cute function "
        "yet. Qt's 'QList<StateId> "
        "QScxmlStateMachineInfo::transitionTargets(TransitionId "
        "transitionId) const': gives a type Python has no way to take yet.")

  @staticmethod
  def transitionsTriggered(*__, **_) -> Never:
    """
    Qt's 'void QScxmlStateMachineInfo::transitionsTriggered(const
    QList<QScxmlStateMachineInfo::TransitionId> &transitions)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachineInfo.transitionsTriggered' has no cute function "
        "yet. Qt's 'void QScxmlStateMachineInfo::transitionsTriggered(const "
        "QList<QScxmlStateMachineInfo::TransitionId> &transitions)': takes "
        "a type Python has no way to hand over yet.")
