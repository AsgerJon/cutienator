"""
QEventTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qeventtransition.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QEvent, QObject
from . import QAbstractTransition

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QEventTransition(QAbstractTransition):
  """
  The cute side of Qt's QEventTransition: a plain Python object standing in
  front of one C++ QEventTransition.

  It is built on the cute 'QAbstractTransition', as Qt's QEventTransition is
  built on Qt's QAbstractTransition, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QEventTransition that has a ritual and that Python
  can call so far, 9 names in all: 'metaObject', 'tr', 'eventSource',
  'setEventSource', 'eventType', 'setEventType', 'eventTest', 'onTransition',
  'event'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QEventTransition::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QEventTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QEventTransition::~QEventTransition()': the destructor: Python
    never removes a C++ QEventTransition.
  - Qt's 'QBindable<QObject *> QEventTransition::bindableEventSource()':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<QEvent::Type> QEventTransition::bindableEventType()':
    gives a type Python has no way to take yet.
  - Qt's 'QEventTransition::QEventTransition(QEventTransitionPrivate &dd,
    QState *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QEventTransition::QEventTransition(QEventTransitionPrivate &dd,
    QObject *object, QEvent::Type type, QState *parent)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QEventTransitionPrivate *QEventTransition::d_func()': gives
    'QEventTransitionPrivate', which has no cute class yet.
  - Qt's 'const QEventTransitionPrivate *QEventTransition::d_func() const':
    gives 'QEventTransitionPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QEventTransition is created at the first use, not by
    'QEventTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QEventTransition.
  - Qt tells when it has removed the C++ QEventTransition. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QEventTransition that has no cute function yet,
    'bindableEventSource', 'bindableEventType', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QEventTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#tr

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
    #  QString QEventTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QEventTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QEventTransition'

  #  A C++ QEventTransition Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QEventTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QEventTransition::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QEventTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QEventTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def eventSource(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QEventTransition::eventSource() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#eventSource

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QEventTransition::eventSource() const
    address = self.uglySide.call(
        'ritual_ZNK16QEventTransition11eventSourceEv',
    )
    return QObject._cuteAt(address)

  def eventType(self) -> QEvent.Type:
    """
    Calls Qt's 'QEvent::Type QEventTransition::eventType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#eventType

    Returns
    -------

    QEvent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QEvent.Type(number)'
      gives.
    """
    #  QEvent::Type QEventTransition::eventType() const
    return QEvent.Type(self.uglySide.call(
        'ritual_ZNK16QEventTransition9eventTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setEventSource(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QEventTransition::setEventSource(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventtransition.html#setEventSource

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventTransition::setEventSource(QObject *object)
    self.uglySide.call(
        'ritual_ZN16QEventTransition14setEventSourceEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QEvent.Type)
  def setEventType(self, type: QEvent.Type) -> None:
    """
    Calls Qt's 'void QEventTransition::setEventType(QEvent::Type type)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#setEventType

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.
    """
    #  void QEventTransition::setEventType(QEvent::Type type)
    self.uglySide.call(
        'ritual_ZN16QEventTransition12setEventTypeEN6QEvent4TypeE',
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
    Notes what was given, for Qt's 'QEventTransition::QEventTransition(QState
    *sourceState)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventtransition.html#QEventTransition

    Parameters
    ----------

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QEventTransition::QEventTransition(QState *sourceState)
    self._noteCreation(QEventTransition, lambda: Rituals.call(
        'ritual_ZN16QEventTransitionC1EP6QState',
        self._addressOf(sourceState),
    ))

  @overload(QObject, QEvent.Type)
  @overload(NoneType, QEvent.Type)
  @overload(QObject, QEvent.Type, QState)
  @overload(QObject, QEvent.Type, NoneType)
  @overload(NoneType, QEvent.Type, QState)
  @overload(NoneType, QEvent.Type, NoneType)
  def __init__(
      self,
      object: Optional[QObject],
      type: QEvent.Type,
      sourceState: Optional[QState] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QEventTransition::QEventTransition(QObject *object, QEvent::Type type,
    QState *sourceState)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qeventtransition.html#QEventTransition

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QEvent.Type
      Passed on as its number.

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QEventTransition::QEventTransition(QObject *object, QEvent::Type type,
    #      QState *sourceState)
    self._noteCreation(QEventTransition, lambda: Rituals.call(
        'ritual_ZN16QEventTransitionC1EP7QObjectN6QEvent4TypeEP6QState',
        self._addressOf(object, 'QObject'), type.value,
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

  @overload(QEvent)
  @overload(NoneType)
  def eventTest(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QEventTransition::eventTest(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#eventTest

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QEventTransition::eventTest(QEvent *event)
    ritual = 'ritual_ZN16QEventTransition9eventTestEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QEventTransition9eventTestEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onTransition(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QEventTransition::onTransition(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#onTransition

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QEventTransition::onTransition(QEvent *event)
    ritual = 'ritual_ZN16QEventTransition12onTransitionEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QEventTransition12onTransitionEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QEventTransition::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qeventtransition.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QEventTransition::event(QEvent *e)
    ritual = 'ritual_ZN16QEventTransition5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QEventTransition5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @staticmethod
  def bindableEventSource(*__, **_) -> Never:
    """
    Qt's 'QBindable<QObject *> QEventTransition::bindableEventSource()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QEventTransition.bindableEventSource' has no cute function yet. "
        "Qt's 'QBindable<QObject *> "
        "QEventTransition::bindableEventSource()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def bindableEventType(*__, **_) -> Never:
    """
    Qt's 'QBindable<QEvent::Type> QEventTransition::bindableEventType()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QEventTransition.bindableEventType' has no cute function yet. "
        "Qt's 'QBindable<QEvent::Type> "
        "QEventTransition::bindableEventType()': gives a type Python has no "
        "way to take yet.")
