"""
QSignalTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qsignaltransition.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractTransition

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QEvent, QMetaObject
  from . import QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QEvent = WAIT['QEvent']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSignalTransition(QAbstractTransition):
  """
  The cute side of Qt's QSignalTransition: a plain Python object standing in
  front of one C++ QSignalTransition.

  It is built on the cute 'QAbstractTransition', as Qt's QSignalTransition is
  built on Qt's QAbstractTransition, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSignalTransition that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'senderObject',
  'setSenderObject', 'signal', 'setSignal', 'eventTest', 'onTransition',
  'event', 'senderObjectChanged', 'signalChanged'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSignalTransition::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSignalTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSignalTransition::~QSignalTransition()': the destructor: Python
    never removes a C++ QSignalTransition.
  - Qt's 'QBindable<const QObject *>
    QSignalTransition::bindableSenderObject()': gives a type Python has no
    way to take yet.
  - Qt's 'QBindable<QByteArray> QSignalTransition::bindableSignal()': gives a
    type Python has no way to take yet.
  - Qt's 'QSignalTransitionPrivate *QSignalTransition::d_func()': gives
    'QSignalTransitionPrivate', which has no cute class yet.
  - Qt's 'const QSignalTransitionPrivate *QSignalTransition::d_func() const':
    gives 'QSignalTransitionPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 25 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QSignalTransition is created at the first use, not by
    'QSignalTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSignalTransition.
  - Qt tells when it has removed the C++ QSignalTransition. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSignalTransition that has no cute function yet,
    'bindableSenderObject', 'bindableSignal', holds a function that raises
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
    Calls Qt's 'QString QSignalTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignaltransition.html#tr

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
    #  QString QSignalTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QSignalTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSignalTransition'

  #  A C++ QSignalTransition Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSignalTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSignalTransition::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsignaltransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSignalTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QSignalTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def senderObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'const QObject *QSignalTransition::senderObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#senderObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QObject *QSignalTransition::senderObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QSignalTransition12senderObjectEv',
    )
    return QObject._cuteAt(address)

  def signal(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSignalTransition::signal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsignaltransition.html#signal

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSignalTransition::signal() const
    address = self.uglySide.call('ritual_ZNK17QSignalTransition6signalEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setSenderObject(self, sender: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QSignalTransition::setSenderObject(const QObject
    *sender)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#setSenderObject

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSignalTransition::setSenderObject(const QObject *sender)
    self.uglySide.call(
        'ritual_ZN17QSignalTransition15setSenderObjectEPK7QObject',
        self._addressOf(sender, 'QObject'),
    )

  @overload(QByteArray)
  def setSignal(self, signal: QByteArray) -> None:
    """
    Calls Qt's 'void QSignalTransition::setSignal(const QByteArray &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignaltransition.html#setSignal

    Parameters
    ----------

    signal : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSignalTransition::setSignal(const QByteArray &signal)
    self.uglySide.call(
        'ritual_ZN17QSignalTransition9setSignalERK10QByteArray',
        self._valueOf(signal),
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
    'QSignalTransition::QSignalTransition(QState *sourceState)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#QSignalTransition

    Parameters
    ----------

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSignalTransition::QSignalTransition(QState *sourceState)
    self._noteCreation(QSignalTransition, lambda: Rituals.call(
        'ritual_ZN17QSignalTransitionC1EP6QState',
        self._addressOf(sourceState),
    ))

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(QObject, str, QState)
  @overload(QObject, str, NoneType)
  @overload(QObject, NoneType, QState)
  @overload(QObject, NoneType, NoneType)
  @overload(NoneType, str, QState)
  @overload(NoneType, str, NoneType)
  @overload(NoneType, NoneType, QState)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      sender: Optional[QObject],
      signal: Optional[str],
      sourceState: Optional[QState] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSignalTransition::QSignalTransition(const QObject *sender, const char
    *signal, QState *sourceState)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#QSignalTransition

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSignalTransition::QSignalTransition(const QObject *sender, const char
    #      *signal, QState *sourceState)
    self._noteCreation(QSignalTransition, lambda: Rituals.call(
        'ritual_ZN17QSignalTransitionC1EPK7QObjectPKcP6QState',
        self._addressOf(sender, 'QObject'), self._bytesOf(signal),
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
    Calls Qt's 'bool QSignalTransition::eventTest(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignaltransition.html#eventTest

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSignalTransition::eventTest(QEvent *event)
    ritual = 'ritual_ZN17QSignalTransition9eventTestEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSignalTransition9eventTestEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onTransition(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QSignalTransition::onTransition(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#onTransition

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSignalTransition::onTransition(QEvent *event)
    ritual = 'ritual_ZN17QSignalTransition12onTransitionEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSignalTransition12onTransitionEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSignalTransition::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qsignaltransition.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSignalTransition::event(QEvent *e)
    ritual = 'ritual_ZN17QSignalTransition5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QSignalTransition5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def senderObjectChanged(self) -> None:
    """
    Calls Qt's 'void QSignalTransition::senderObjectChanged(QPrivateSignal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#senderObjectChanged
    """
    #  void QSignalTransition::senderObjectChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN17QSignalTransition19senderObjectChangedENS_14QPrivateSig'
        'nalE',
    )

  def signalChanged(self) -> None:
    """
    Calls Qt's 'void QSignalTransition::signalChanged(QPrivateSignal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsignaltransition.html#signalChanged
    """
    #  void QSignalTransition::signalChanged(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN17QSignalTransition13signalChangedENS_14QPrivateSignalE',
    )

  @staticmethod
  def bindableSenderObject(*__, **_) -> Never:
    """
    Qt's 'QBindable<const QObject *>
    QSignalTransition::bindableSenderObject()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QSignalTransition.bindableSenderObject' has no cute function yet. "
        "Qt's 'QBindable<const QObject *> "
        "QSignalTransition::bindableSenderObject()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableSignal(*__, **_) -> Never:
    """
    Qt's 'QBindable<QByteArray> QSignalTransition::bindableSignal()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSignalTransition.bindableSignal' has no cute function yet. Qt's "
        "'QBindable<QByteArray> QSignalTransition::bindableSignal()': gives "
        "a type Python has no way to take yet.")
