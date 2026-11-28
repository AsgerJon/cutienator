"""
QAbstractTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qabstracttransition.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractAnimation, QEvent, QMetaObject
  from . import QAbstractState, QState, QStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimation = WAIT['QAbstractAnimation']
  QAbstractState = WAIT['QAbstractState']
  QEvent = WAIT['QEvent']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractTransition(QObject):
  """
  The cute side of Qt's QAbstractTransition: a plain Python object standing
  in front of one C++ QAbstractTransition.

  It is built on the cute 'QObject', as Qt's QAbstractTransition is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractTransition that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr', 'sourceState',
  'targetState', 'setTargetState', 'targetStates', 'setTargetStates',
  'transitionType', 'setTransitionType', 'machine', 'addAnimation',
  'removeAnimation', 'animations', 'triggered', 'targetStateChanged',
  'targetStatesChanged', 'eventTest', 'onTransition', 'event'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractTransition::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QAbstractTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractTransition::~QAbstractTransition()': the destructor:
    Python never removes a C++ QAbstractTransition.
  - Qt's 'QBindable<QAbstractTransition::TransitionType>
    QAbstractTransition::bindableTransitionType()': gives a type Python has
    no way to take yet.
  - Qt's 'QAbstractTransition::QAbstractTransition(QAbstractTransitionPrivate
    &dd, QState *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractTransitionPrivate *QAbstractTransition::d_func()': gives
    'QAbstractTransitionPrivate', which has no cute class yet.
  - Qt's 'const QAbstractTransitionPrivate *QAbstractTransition::d_func()
    const': gives 'QAbstractTransitionPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 31 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractTransition is created at the first use, not by
    'QAbstractTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractTransition.
  - Qt tells when it has removed the C++ QAbstractTransition. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractTransition that has no cute function yet,
    'bindableTransitionType', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractTransition, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class TransitionType(CuteNum):
    """
    The enum 'QAbstractTransition::TransitionType' of Qt, with the 2 names Qt
    gives in it.
    """

    ExternalTransition = Kee[int](0)
    InternalTransition = Kee[int](1)

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
    Calls Qt's 'QString QAbstractTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracttransition.html#tr

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
    #  QString QAbstractTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QAbstractTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractTransition'

  #  A C++ QAbstractTransition Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractTransition'

  #  The functions Qt calls itself that QAbstractTransition is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'eventTest': (
          ('_ZN19QAbstractTransition9eventTestEP6QEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'onTransition': (
          ('_ZN19QAbstractTransition12onTransitionEP6QEvent',
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
    Calls Qt's 'const QMetaObject *QAbstractTransition::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sourceState(self) -> Optional[QState]:
    """
    Calls Qt's 'QState *QAbstractTransition::sourceState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#sourceState

    Returns
    -------

    Optional[QState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QState *QAbstractTransition::sourceState() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractTransition11sourceStateEv',
    )
    from . import QState
    return QState._cuteAt(address)

  def targetState(self) -> Optional[QAbstractState]:
    """
    Calls Qt's 'QAbstractState *QAbstractTransition::targetState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#targetState

    Returns
    -------

    Optional[QAbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractState *QAbstractTransition::targetState() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractTransition11targetStateEv',
    )
    from . import QAbstractState
    return QAbstractState._cuteAt(address)

  def targetStates(self) -> QList[QAbstractState]:
    """
    Calls Qt's 'QList<QAbstractState *> QAbstractTransition::targetStates()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#targetStates

    Returns
    -------

    QList[QAbstractState]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractState *> QAbstractTransition::targetStates() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractTransition12targetStatesEv',
    )
    from . import QAbstractState
    return QList[QAbstractState]._cuteOwning(address)

  def transitionType(self) -> TransitionType:
    """
    Calls Qt's 'TransitionType QAbstractTransition::transitionType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#transitionType

    Returns
    -------

    TransitionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'TransitionType(number)'
      gives.
    """
    #  TransitionType QAbstractTransition::transitionType() const
    return QAbstractTransition.TransitionType(self.uglySide.call(
        'ritual_ZNK19QAbstractTransition14transitionTypeEv',
    ))

  def machine(self) -> Optional[QStateMachine]:
    """
    Calls Qt's 'QStateMachine *QAbstractTransition::machine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracttransition.html#machine

    Returns
    -------

    Optional[QStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStateMachine *QAbstractTransition::machine() const
    address = self.uglySide.call('ritual_ZNK19QAbstractTransition7machineEv')
    from . import QStateMachine
    return QStateMachine._cuteAt(address)

  def animations(self) -> QList[QAbstractAnimation]:
    """
    Calls Qt's 'QList<QAbstractAnimation *> QAbstractTransition::animations()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#animations

    Returns
    -------

    QList[QAbstractAnimation]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractAnimation *> QAbstractTransition::animations() const
    address = self.uglySide.call(
        'ritual_ZNK19QAbstractTransition10animationsEv',
    )
    from ..QtCore import QAbstractAnimation
    return QList[QAbstractAnimation]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractState)
  @overload(NoneType)
  def setTargetState(self, target: Optional[QAbstractState]) -> None:
    """
    Calls Qt's 'void QAbstractTransition::setTargetState(QAbstractState
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#setTargetState

    Parameters
    ----------

    target : Optional[QAbstractState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTransition::setTargetState(QAbstractState *target)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition14setTargetStateEP14QAbstractState',
        self._addressOf(target),
    )

  @overload(QList[QAbstractState])
  def setTargetStates(self, targets: QList[QAbstractState]) -> None:
    """
    Calls Qt's 'void QAbstractTransition::setTargetStates(const
    QList<QAbstractState *> &targets)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#setTargetStates

    Parameters
    ----------

    targets : QList[QAbstractState]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAbstractTransition::setTargetStates(const QList<QAbstractState
    #      *> &targets)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition15setTargetStatesERK5QListIP14QAbstr'
        'actStateE',
        self._valueOf(targets),
    )

  @overload(TransitionType)
  def setTransitionType(self, type: TransitionType) -> None:
    """
    Calls Qt's 'void QAbstractTransition::setTransitionType(TransitionType
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#setTransitionType

    Parameters
    ----------

    type : TransitionType
      Passed on as its number.
    """
    #  void QAbstractTransition::setTransitionType(TransitionType type)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition17setTransitionTypeENS_14TransitionT'
        'ypeE',
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
  def __init__(self, sourceState: Optional[QState] = None) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractTransition::QAbstractTransition(QState *sourceState)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#QAbstractTransition

    Parameters
    ----------

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractTransition::QAbstractTransition(QState *sourceState)
    self._noteCreation(QAbstractTransition, lambda: Rituals.call(
        'ritual_ZN19QAbstractTransitionC1EP6QState',
        self._addressOf(sourceState),
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

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def addAnimation(self, animation: Optional[QAbstractAnimation]) -> None:
    """
    Calls Qt's 'void QAbstractTransition::addAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#addAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTransition::addAnimation(QAbstractAnimation *animation)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition12addAnimationEP18QAbstractAnimation',
        self._addressOf(animation),
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def removeAnimation(self, animation: Optional[QAbstractAnimation]) -> None:
    """
    Calls Qt's 'void QAbstractTransition::removeAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#removeAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTransition::removeAnimation(QAbstractAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition15removeAnimationEP18QAbstractAnimat'
        'ion',
        self._addressOf(animation),
    )

  def triggered(self) -> None:
    """
    Calls Qt's 'void QAbstractTransition::triggered(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracttransition.html#triggered
    """
    #  void QAbstractTransition::triggered(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition9triggeredENS_14QPrivateSignalE',
    )

  def targetStateChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractTransition::targetStateChanged(QPrivateSignal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#targetStateChanged
    """
    #  void QAbstractTransition::targetStateChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition18targetStateChangedENS_14QPrivateSi'
        'gnalE',
    )

  def targetStatesChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractTransition::targetStatesChanged(QPrivateSignal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#targetStatesChanged
    """
    #  void QAbstractTransition::targetStatesChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition19targetStatesChangedENS_14QPrivateS'
        'ignalE',
    )

  @overload(QEvent)
  @overload(NoneType)
  def eventTest(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractTransition::eventTest(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracttransition.html#eventTest

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractTransition::eventTest(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN19QAbstractTransition9eventTestEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def onTransition(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QAbstractTransition::onTransition(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstracttransition.html#onTransition

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractTransition::onTransition(QEvent *event)
    self.uglySide.call(
        'ritual_ZN19QAbstractTransition12onTransitionEP6QEvent',
        self._addressOf(event),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractTransition::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstracttransition.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractTransition::event(QEvent *e)
    ritual = 'ritual_ZN19QAbstractTransition5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QAbstractTransition5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def bindableTransitionType(*__, **_) -> Never:
    """
    Qt's 'QBindable<QAbstractTransition::TransitionType>
    QAbstractTransition::bindableTransitionType()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractTransition.bindableTransitionType' has no cute function "
        "yet. Qt's 'QBindable<QAbstractTransition::TransitionType> "
        "QAbstractTransition::bindableTransitionType()': gives a type "
        "Python has no way to take yet.")


#  Qt's 'QList<QAbstractTransition *>': the list of QAbstractTransition,
#  which 'QList[QAbstractTransition]' gives. It is made here, so that there
#  is one as soon as there can be a QAbstractTransition.
QList.createKind(
    QAbstractTransition, 'address',
    make='ritual_list_make_QAbstractTransition_ptr',
    add='ritual_list_add_QAbstractTransition_ptr',
    size='ritual_list_size_QAbstractTransition_ptr',
    at='ritual_list_at_QAbstractTransition_ptr',
    drop='ritual_list_drop_QAbstractTransition_ptr',
)
