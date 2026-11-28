"""
SignalTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachineQml/6.12.0/QtStateMachineQml/private/signaltransition_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means SignalTransition to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQmlParserStatus
from ..QtStateMachine import QSignalTransition

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtQml import QJSValue, QQmlScriptString
  from ..QtStateMachine import QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QJSValue = WAIT['QJSValue']
  QQmlScriptString = WAIT['QQmlScriptString']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SignalTransition(QSignalTransition, QQmlParserStatus):
  """
  The cute side of Qt's SignalTransition: a plain Python object standing in
  front of one C++ SignalTransition.

  It is built on the cute 'QSignalTransition', as Qt's SignalTransition is
  built on Qt's QSignalTransition, and has everything that class has. It is
  built on the cute 'QQmlParserStatus' as well, as Qt's SignalTransition is
  built on Qt's QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's SignalTransition that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'guard', 'setGuard',
  'eventTest', 'onTransition', 'signal', 'setSignal', 'invoke',
  'guardChanged', 'invokeYourself', 'qmlSignalChanged', 'classBegin',
  'componentComplete', 'connectTriggered', '_qt_property_m_signal_offset',
  '_qt_property_m_guard_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *SignalTransition::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int SignalTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBindable<QQmlScriptString> SignalTransition::bindableGuard()':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<QJSValue> SignalTransition::bindableSignal()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ SignalTransition is created at the first use, not by
    'SignalTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ SignalTransition.
  - Qt tells when it has removed the C++ SignalTransition. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's SignalTransition that has no cute function yet,
    'bindableGuard', holds a function that raises 'NotImplementedError', and
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
    Calls Qt's 'QString SignalTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#tr

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
    #  QString SignalTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16SignalTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_signal_offset() -> int:
    """
    Calls Qt's 'size_t SignalTransition::_qt_property_m_signal_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#_qt_property_m_signal_offset
    """
    #  size_t SignalTransition::_qt_property_m_signal_offset()
    return Rituals.call(
        'ritual_ZN16SignalTransition28_qt_property_m_signal_offsetEv',
    )

  @staticmethod
  def _qt_property_m_guard_offset() -> int:
    """
    Calls Qt's 'size_t SignalTransition::_qt_property_m_guard_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#_qt_property_m_guard_offset
    """
    #  size_t SignalTransition::_qt_property_m_guard_offset()
    return Rituals.call(
        'ritual_ZN16SignalTransition27_qt_property_m_guard_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'SignalTransition'

  #  Qt's SignalTransition is built on more than one class. The part of a C++
  #  SignalTransition that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_SignalTransition_QQmlParserStatus',
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
    Calls Qt's 'const QMetaObject *SignalTransition::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *SignalTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16SignalTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def guard(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString SignalTransition::guard() const'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#guard

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString SignalTransition::guard() const
    address = self.uglySide.call('ritual_ZNK16SignalTransition5guardEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlScriptString)
  def setGuard(self, guard: QQmlScriptString) -> None:
    """
    Calls Qt's 'void SignalTransition::setGuard(const QQmlScriptString
    &guard)'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#setGuard

    Parameters
    ----------

    guard : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void SignalTransition::setGuard(const QQmlScriptString &guard)
    self.uglySide.call(
        'ritual_ZN16SignalTransition8setGuardERK16QQmlScriptString',
        self._valueOf(guard),
    )

  @overload(QJSValue)
  def setSignal(self, signal: QJSValue) -> None:
    """
    Calls Qt's 'void SignalTransition::setSignal(const QJSValue &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#setSignal

    Parameters
    ----------

    signal : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void SignalTransition::setSignal(const QJSValue &signal)
    self.uglySide.call(
        'ritual_ZN16SignalTransition9setSignalERK8QJSValue',
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
  def __init__(self, parent: Optional[QState] = None) -> None:
    """
    Notes what was given, for Qt's 'SignalTransition::SignalTransition(QState
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#SignalTransition

    Parameters
    ----------

    parent : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  SignalTransition::SignalTransition(QState *parent)
    self._noteCreation(SignalTransition, lambda: Rituals.call(
        'ritual_ZN16SignalTransitionC1EP6QState', self._addressOf(parent),
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
    Calls Qt's 'bool SignalTransition::eventTest(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#eventTest

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool SignalTransition::eventTest(QEvent *event)
    ritual = 'ritual_ZN16SignalTransition9eventTestEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16SignalTransition9eventTestEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def onTransition(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void SignalTransition::onTransition(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#onTransition

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void SignalTransition::onTransition(QEvent *event)
    ritual = 'ritual_ZN16SignalTransition12onTransitionEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16SignalTransition12onTransitionEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def signal(self) -> QJSValue:
    """
    Calls Qt's 'const QJSValue &SignalTransition::signal()'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#signal

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  const QJSValue &SignalTransition::signal()
    address = self.uglySide.call('ritual_ZN16SignalTransition6signalEv')
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def invoke(self) -> None:
    """
    Calls Qt's 'void SignalTransition::invoke()'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#invoke
    """
    #  void SignalTransition::invoke()
    self.uglySide.call('ritual_ZN16SignalTransition6invokeEv')

  def guardChanged(self) -> None:
    """
    Calls Qt's 'void SignalTransition::guardChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#guardChanged
    """
    #  void SignalTransition::guardChanged()
    self.uglySide.call('ritual_ZN16SignalTransition12guardChangedEv')

  def invokeYourself(self) -> None:
    """
    Calls Qt's 'void SignalTransition::invokeYourself()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#invokeYourself
    """
    #  void SignalTransition::invokeYourself()
    self.uglySide.call('ritual_ZN16SignalTransition14invokeYourselfEv')

  def qmlSignalChanged(self) -> None:
    """
    Calls Qt's 'void SignalTransition::qmlSignalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#qmlSignalChanged
    """
    #  void SignalTransition::qmlSignalChanged()
    self.uglySide.call('ritual_ZN16SignalTransition16qmlSignalChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void SignalTransition::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/signaltransition.html#classBegin
    """
    #  void SignalTransition::classBegin()
    ritual = 'ritual_ZN16SignalTransition10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16SignalTransition10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void SignalTransition::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#componentComplete
    """
    #  void SignalTransition::componentComplete()
    ritual = 'ritual_ZN16SignalTransition17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16SignalTransition17componentCompleteEv'
    self.uglySide.call(ritual)

  def connectTriggered(self) -> None:
    """
    Calls Qt's 'void SignalTransition::connectTriggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/signaltransition.html#connectTriggered
    """
    #  void SignalTransition::connectTriggered()
    self.uglySide.call('ritual_ZN16SignalTransition16connectTriggeredEv')

  @staticmethod
  def bindableGuard(*__, **_) -> Never:
    """
    Qt's 'QBindable<QQmlScriptString> SignalTransition::bindableGuard()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'SignalTransition.bindableGuard' has no cute function yet. Qt's "
        "'QBindable<QQmlScriptString> SignalTransition::bindableGuard()': "
        "gives a type Python has no way to take yet.")
