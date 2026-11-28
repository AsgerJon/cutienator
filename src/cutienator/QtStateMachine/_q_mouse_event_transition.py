"""
QMouseEventTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtStateMachine/qmouseeventtransition.h, Qt 6.12.0. Changes made here are
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
  from ..QtGui import QPainterPath
  from . import QState
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QState = WAIT['QState']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMouseEventTransition(QEventTransition):
  """
  The cute side of Qt's QMouseEventTransition: a plain Python object standing
  in front of one C++ QMouseEventTransition.

  It is built on the cute 'QEventTransition', as Qt's QMouseEventTransition
  is built on Qt's QEventTransition, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMouseEventTransition that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'button',
  'setButton', 'modifierMask', 'setModifierMask', 'hitTestPath',
  'setHitTestPath', 'onTransition', 'eventTest'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMouseEventTransition::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QMouseEventTransition::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QMouseEventTransition::~QMouseEventTransition()': the destructor:
    Python never removes a C++ QMouseEventTransition.
  - Qt's 'QBindable<Qt::MouseButton>
    QMouseEventTransition::bindableButton()': gives a type Python has no way
    to take yet.
  - Qt's 'QBindable<Qt::KeyboardModifiers>
    QMouseEventTransition::bindableModifierMask()': gives a type Python has
    no way to take yet.
  - Qt's 'QMouseEventTransitionPrivate *QMouseEventTransition::d_func()':
    gives 'QMouseEventTransitionPrivate', which has no cute class yet.
  - Qt's 'const QMouseEventTransitionPrivate *QMouseEventTransition::d_func()
    const': gives 'QMouseEventTransitionPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 23 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMouseEventTransition is created at the first use, not by
    'QMouseEventTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMouseEventTransition.
  - Qt tells when it has removed the C++ QMouseEventTransition. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QMouseEventTransition that has no cute function yet,
    'bindableButton', 'bindableModifierMask', holds a function that raises
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
    Calls Qt's 'QString QMouseEventTransition::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseeventtransition.html#tr

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
    #  QString QMouseEventTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QMouseEventTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMouseEventTransition'

  #  A C++ QMouseEventTransition Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMouseEventTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMouseEventTransition::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMouseEventTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QMouseEventTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def button(self) -> Qt.MouseButton:
    """
    Calls Qt's 'Qt::MouseButton QMouseEventTransition::button() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmouseeventtransition.html#button

    Returns
    -------

    Qt.MouseButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.MouseButton(number)'
      gives.
    """
    #  Qt::MouseButton QMouseEventTransition::button() const
    return Qt.MouseButton(self.uglySide.call(
        'ritual_ZNK21QMouseEventTransition6buttonEv',
    ))

  def modifierMask(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QMouseEventTransition::modifierMask()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#modifierMask

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QMouseEventTransition::modifierMask() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK21QMouseEventTransition12modifierMaskEv',
    ))

  def hitTestPath(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QMouseEventTransition::hitTestPath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#hitTestPath

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QMouseEventTransition::hitTestPath() const
    address = self.uglySide.call(
        'ritual_ZNK21QMouseEventTransition11hitTestPathEv',
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.MouseButton)
  def setButton(self, button: Qt.MouseButton) -> None:
    """
    Calls Qt's 'void QMouseEventTransition::setButton(Qt::MouseButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#setButton

    Parameters
    ----------

    button : Qt.MouseButton
      Passed on as its number.
    """
    #  void QMouseEventTransition::setButton(Qt::MouseButton button)
    self.uglySide.call(
        'ritual_ZN21QMouseEventTransition9setButtonEN2Qt11MouseButtonE',
        button.value,
    )

  @overload(Qt.KeyboardModifiers)
  def setModifierMask(self, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void
    QMouseEventTransition::setModifierMask(Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#setModifierMask

    Parameters
    ----------

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QMouseEventTransition::setModifierMask(Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN21QMouseEventTransition15setModifierMaskE6QFlagsIN2Qt16Ke'
        'yboardModifierEE',
        modifiers.value,
    )

  @overload(QPainterPath)
  def setHitTestPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QMouseEventTransition::setHitTestPath(const QPainterPath
    &path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#setHitTestPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QMouseEventTransition::setHitTestPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN21QMouseEventTransition14setHitTestPathERK12QPainterPath',
        self._valueOf(path),
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
    'QMouseEventTransition::QMouseEventTransition(QState *sourceState)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#QMouseEventTransition

    Parameters
    ----------

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMouseEventTransition::QMouseEventTransition(QState *sourceState)
    self._noteCreation(QMouseEventTransition, lambda: Rituals.call(
        'ritual_ZN21QMouseEventTransitionC1EP6QState',
        self._addressOf(sourceState),
    ))

  @overload(QObject, QEvent.Type, Qt.MouseButton)
  @overload(NoneType, QEvent.Type, Qt.MouseButton)
  @overload(QObject, QEvent.Type, Qt.MouseButton, QState)
  @overload(QObject, QEvent.Type, Qt.MouseButton, NoneType)
  @overload(NoneType, QEvent.Type, Qt.MouseButton, QState)
  @overload(NoneType, QEvent.Type, Qt.MouseButton, NoneType)
  def __init__(
      self,
      object: Optional[QObject],
      type: QEvent.Type,
      button: Qt.MouseButton,
      sourceState: Optional[QState] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QMouseEventTransition::QMouseEventTransition(QObject *object,
    QEvent::Type type, Qt::MouseButton button, QState *sourceState)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#QMouseEventTransition

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QEvent.Type
      Passed on as its number.

    button : Qt.MouseButton
      Passed on as its number.

    sourceState : Optional[QState]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMouseEventTransition::QMouseEventTransition(QObject *object,
    #      QEvent::Type type, Qt::MouseButton button, QState *sourceState)
    self._noteCreation(QMouseEventTransition, lambda: Rituals.call(
        'ritual_ZN21QMouseEventTransitionC1EP7QObjectN6QEvent4TypeEN2Qt11Mo'
        'useButtonEP6QState',
        self._addressOf(object, 'QObject'), type.value, button.value,
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
    Calls Qt's 'void QMouseEventTransition::onTransition(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#onTransition

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMouseEventTransition::onTransition(QEvent *event)
    ritual = 'ritual_ZN21QMouseEventTransition12onTransitionEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QMouseEventTransition12onTransitionEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def eventTest(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QMouseEventTransition::eventTest(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmouseeventtransition.html#eventTest

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMouseEventTransition::eventTest(QEvent *event)
    ritual = 'ritual_ZN21QMouseEventTransition9eventTestEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QMouseEventTransition9eventTestEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def bindableButton(*__, **_) -> Never:
    """
    Qt's 'QBindable<Qt::MouseButton>
    QMouseEventTransition::bindableButton()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QMouseEventTransition.bindableButton' has no cute function yet. "
        "Qt's 'QBindable<Qt::MouseButton> "
        "QMouseEventTransition::bindableButton()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def bindableModifierMask(*__, **_) -> Never:
    """
    Qt's 'QBindable<Qt::KeyboardModifiers>
    QMouseEventTransition::bindableModifierMask()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QMouseEventTransition.bindableModifierMask' has no cute function "
        "yet. Qt's 'QBindable<Qt::KeyboardModifiers> "
        "QMouseEventTransition::bindableModifierMask()': gives a type "
        "Python has no way to take yet.")
