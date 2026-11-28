"""
QKeyEventTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qkeyeventtransition.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QObject
from . import QEventTransition

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


class QKeyEventTransition(QEventTransition):
  """
  The cute side of Qt's QKeyEventTransition: a plain Python object standing
  in front of one C++ QKeyEventTransition.

  It is built on the cute 'QEventTransition', as Qt's QKeyEventTransition is
  built on Qt's QEventTransition, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QKeyEventTransition that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'key',
  'setKey', 'modifierMask', 'setModifierMask', 'onTransition', 'eventTest'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QKeyEventTransition::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QKeyEventTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QKeyEventTransition::~QKeyEventTransition()': the destructor:
    Python never removes a C++ QKeyEventTransition.
  - Qt's 'QBindable<int> QKeyEventTransition::bindableKey()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<Qt::KeyboardModifiers>
    QKeyEventTransition::bindableModifierMask()': gives a type Python has no
    way to take yet.
  - Qt's 'QKeyEventTransitionPrivate *QKeyEventTransition::d_func()': gives
    'QKeyEventTransitionPrivate', which has no cute class yet.
  - Qt's 'const QKeyEventTransitionPrivate *QKeyEventTransition::d_func()
    const': gives 'QKeyEventTransitionPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QKeyEventTransition is created at the first use, not by
    'QKeyEventTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QKeyEventTransition.
  - Qt tells when it has removed the C++ QKeyEventTransition. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QKeyEventTransition that has no cute function yet,
    'bindableKey', 'bindableModifierMask', holds a function that raises
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
    Calls Qt's 'QString QKeyEventTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyeventtransition.html#tr

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
    #  QString QKeyEventTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QKeyEventTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeyEventTransition'

  #  A C++ QKeyEventTransition Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QKeyEventTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QKeyEventTransition::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeyeventtransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QKeyEventTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QKeyEventTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def key(self) -> int:
    """
    Calls Qt's 'int QKeyEventTransition::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyeventtransition.html#key
    """
    #  int QKeyEventTransition::key() const
    return self.uglySide.call('ritual_ZNK19QKeyEventTransition3keyEv')

  def modifierMask(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QKeyEventTransition::modifierMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeyeventtransition.html#modifierMask

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QKeyEventTransition::modifierMask() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK19QKeyEventTransition12modifierMaskEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setKey(self, key: int) -> None:
    """
    Calls Qt's 'void QKeyEventTransition::setKey(int key)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyeventtransition.html#setKey

    Parameters
    ----------

    key : int
      Passed on as it is.
    """
    #  void QKeyEventTransition::setKey(int key)
    self.uglySide.call('ritual_ZN19QKeyEventTransition6setKeyEi', key)

  @overload(Qt.KeyboardModifiers)
  def setModifierMask(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QKeyEventTransition::setModifierMask(Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeyeventtransition.html#setModifierMask

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QKeyEventTransition::setModifierMask(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN19QKeyEventTransition15setModifierMaskE6QFlagsIN2Qt16Keyb'
        'oardModifierEE',
        modifiers.value,
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
    'QKeyEventTransition::QKeyEventTransition(QState *sourceState)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeyeventtransition.html#QKeyEventTransition

    Parameters
    ----------

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QKeyEventTransition::QKeyEventTransition(QState *sourceState)
    self._noteCreation(QKeyEventTransition, lambda: Rituals.call(
        'ritual_ZN19QKeyEventTransitionC1EP6QState',
        self._addressOf(sourceState),
    ))

  @overload(QObject, QEvent.Type, int)
  @overload(NoneType, QEvent.Type, int)
  @overload(QObject, QEvent.Type, int, QState)
  @overload(QObject, QEvent.Type, int, NoneType)
  @overload(NoneType, QEvent.Type, int, QState)
  @overload(NoneType, QEvent.Type, int, NoneType)
  def __init__(
      self,
      object: Optional[QObject],
      type: QEvent.Type,
      key: int,
      sourceState: Optional[QState] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QKeyEventTransition::QKeyEventTransition(QObject *object, QEvent::Type
    type, int key, QState *sourceState)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeyeventtransition.html#QKeyEventTransition

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QEvent.Type
      Passed on as its number.

    key : int
      Passed on as it is.

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QKeyEventTransition::QKeyEventTransition(QObject *object, QEvent::Type
    #      type, int key, QState *sourceState)
    self._noteCreation(QKeyEventTransition, lambda: Rituals.call(
        'ritual_ZN19QKeyEventTransitionC1EP7QObjectN6QEvent4TypeEiP6QState',
        self._addressOf(object, 'QObject'), type.value, key,
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
  def onTransition(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QKeyEventTransition::onTransition(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeyeventtransition.html#onTransition

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QKeyEventTransition::onTransition(QEvent *event)
    ritual = 'ritual_ZN19QKeyEventTransition12onTransitionEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QKeyEventTransition12onTransitionEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def eventTest(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QKeyEventTransition::eventTest(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyeventtransition.html#eventTest

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QKeyEventTransition::eventTest(QEvent *event)
    ritual = 'ritual_ZN19QKeyEventTransition9eventTestEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QKeyEventTransition9eventTestEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def bindableKey(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> QKeyEventTransition::bindableKey()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QKeyEventTransition.bindableKey' has no cute function yet. Qt's "
        "'QBindable<int> QKeyEventTransition::bindableKey()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableModifierMask(*__, **_) -> Never:
    """
    Qt's 'QBindable<Qt::KeyboardModifiers>
    QKeyEventTransition::bindableModifierMask()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QKeyEventTransition.bindableModifierMask' has no cute function "
        "yet. Qt's 'QBindable<Qt::KeyboardModifiers> "
        "QKeyEventTransition::bindableModifierMask()': gives a type Python "
        "has no way to take yet.")
