"""
QQuickKeysAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickKeysAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickItemKeyFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from ..QtGui import QInputMethodEvent, QKeyEvent
  from . import QQuickKeyEvent, QQuickKeysAttachedPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QQuickKeyEvent = WAIT['QQuickKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickKeysAttached(QObject, QQuickItemKeyFilter):
  """
  The cute side of Qt's QQuickKeysAttached: a plain Python object standing in
  front of one C++ QQuickKeysAttached.

  It is built on the cute 'QObject', as Qt's QQuickKeysAttached is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQuickItemKeyFilter' as well, as Qt's QQuickKeysAttached is built on Qt's
  QQuickItemKeyFilter too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickKeysAttached that has a ritual and that Python
  can call so far, 59 names in all: 'metaObject', 'tr', 'd_func', 'enabled',
  'setEnabled', 'priority', 'setPriority', 'componentComplete',
  'qmlAttachedProperties', 'enabledChanged', 'priorityChanged', 'pressed',
  'released', 'shortcutOverride', 'digit0Pressed', 'digit1Pressed',
  'digit2Pressed', 'digit3Pressed', 'digit4Pressed', 'digit5Pressed',
  'digit6Pressed', 'digit7Pressed', 'digit8Pressed', 'digit9Pressed',
  'leftPressed', 'rightPressed', 'upPressed', 'downPressed', 'tabPressed',
  'backtabPressed', 'asteriskPressed', 'numberSignPressed', 'escapePressed',
  'returnPressed', 'enterPressed', 'deletePressed', 'spacePressed',
  'backPressed', 'cancelPressed', 'selectPressed', 'yesPressed', 'noPressed',
  'context1Pressed', 'context2Pressed', 'context3Pressed', 'context4Pressed',
  'callPressed', 'hangupPressed', 'flipPressed', 'menuPressed',
  'volumeUpPressed', 'volumeDownPressed', 'keyPressed', 'keyReleased',
  'inputMethodEvent', 'inputMethodQuery', 'shortcutOverrideEvent',
  'keyToSignal', 'isConnected'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickKeysAttached::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickKeysAttached::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickKeysAttachedPrivate *QQuickKeysAttached::d_func()
    const': takes in Python what 'QQuickKeysAttachedPrivate
    *QQuickKeysAttached::d_func()' takes.
  - Qt's 'void QQuickKeysAttached::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickKeysAttached::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickKeysAttached::~QQuickKeysAttached()': the destructor: Python
    never removes a C++ QQuickKeysAttached.
  - Qt's 'QQmlListProperty<QQuickItem> QQuickKeysAttached::forwardTo()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 69 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickKeysAttached is created at the first use, not by
    'QQuickKeysAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickKeysAttached.
  - Qt tells when it has removed the C++ QQuickKeysAttached. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickKeysAttached that has no cute function yet,
    'forwardTo', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuickKeysAttached, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Priority(CuteNum):
    """
    The enum 'QQuickKeysAttached::Priority' of Qt, with the 2 names Qt gives
    in it.
    """

    BeforeItem = Kee[int](0)
    AfterItem = Kee[int](1)

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
    Calls Qt's 'QString QQuickKeysAttached::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#tr

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
    #  QString QQuickKeysAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickKeysAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      a0: Optional[QObject],
  ) -> Optional[QQuickKeysAttached]:
    """
    Calls Qt's 'QQuickKeysAttached
    *QQuickKeysAttached::qmlAttachedProperties(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#qmlAttachedProperties

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickKeysAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickKeysAttached *QQuickKeysAttached::qmlAttachedProperties(QObject
    #      *a0)
    address = Rituals.call(
        'ritual_ZN18QQuickKeysAttached21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    return QQuickKeysAttached._cuteAt(address)

  @staticmethod
  @overload(int)
  def keyToSignal(key: int) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQuickKeysAttached::keyToSignal(int key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#keyToSignal

    Parameters
    ----------

    key : int
      Passed on as it is.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQuickKeysAttached::keyToSignal(int key)
    address = Rituals.call(
        'ritual_ZN18QQuickKeysAttached11keyToSignalEi', key,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickKeysAttached'

  #  Qt's QQuickKeysAttached is built on more than one class. The part of a
  #  C++ QQuickKeysAttached that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemKeyFilter':
          'ritual_cast_QQuickKeysAttached_QQuickItemKeyFilter',
  }

  #  A C++ QQuickKeysAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickKeysAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickKeysAttached::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickKeysAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickKeysAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickKeysAttached::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#enabled
    """
    #  bool QQuickKeysAttached::enabled() const
    return self.uglySide.call('ritual_ZNK18QQuickKeysAttached7enabledEv')

  def priority(self) -> Priority:
    """
    Calls Qt's 'Priority QQuickKeysAttached::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#priority

    Returns
    -------

    Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Priority(number)' gives.
    """
    #  Priority QQuickKeysAttached::priority() const
    return QQuickKeysAttached.Priority(self.uglySide.call(
        'ritual_ZNK18QQuickKeysAttached8priorityEv',
    ))

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QQuickKeysAttached::inputMethodQuery(Qt::InputMethodQuery query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickKeysAttached::inputMethodQuery(Qt::InputMethodQuery
    #      query) const
    ritual = (
        'ritual_ZNK18QQuickKeysAttached16inputMethodQueryEN2Qt16InputMethod'
        'QueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QQuickKeysAttached16inputMethodQueryEN2Qt16Input'
          'MethodQueryE')
    address = self.uglySide.call(ritual, query.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(str)
  @overload(NoneType)
  def isConnected(self, signalName: Optional[str]) -> bool:
    """
    Calls Qt's 'bool QQuickKeysAttached::isConnected(const char *signalName)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#isConnected

    Parameters
    ----------

    signalName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  bool QQuickKeysAttached::isConnected(const char *signalName) const
    return self.uglySide.call(
        'ritual_ZNK18QQuickKeysAttached11isConnectedEPKc',
        self._bytesOf(signalName),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickKeysAttached::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached10setEnabledEb', enabled,
    )

  @overload(Priority)
  def setPriority(self, a0: Priority) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::setPriority(Priority a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#setPriority

    Parameters
    ----------

    a0 : Priority
      Passed on as its number.
    """
    #  void QQuickKeysAttached::setPriority(Priority a0)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11setPriorityENS_8PriorityE', a0.value,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickKeysAttached::QQuickKeysAttached(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#QQuickKeysAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickKeysAttached::QQuickKeysAttached(QObject *parent)
    self._noteCreation(QQuickKeysAttached, lambda: Rituals.call(
        'ritual_ZN18QQuickKeysAttachedC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QQuickKeysAttachedPrivate]:
    """
    Calls Qt's 'QQuickKeysAttachedPrivate *QQuickKeysAttached::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#d_func

    Returns
    -------

    Optional[QQuickKeysAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickKeysAttachedPrivate *QQuickKeysAttached::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickKeysAttached6d_funcEv')
    from . import QQuickKeysAttachedPrivate
    return QQuickKeysAttachedPrivate._cuteAt(address)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#componentComplete
    """
    #  void QQuickKeysAttached::componentComplete()
    ritual = 'ritual_ZN18QQuickKeysAttached17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickKeysAttached17componentCompleteEv'
    self.uglySide.call(ritual)

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#enabledChanged
    """
    #  void QQuickKeysAttached::enabledChanged()
    self.uglySide.call('ritual_ZN18QQuickKeysAttached14enabledChangedEv')

  def priorityChanged(self) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::priorityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#priorityChanged
    """
    #  void QQuickKeysAttached::priorityChanged()
    self.uglySide.call('ritual_ZN18QQuickKeysAttached15priorityChangedEv')

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::pressed(QQuickKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached7pressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def released(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::released(QQuickKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#released

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::released(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached8releasedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def shortcutOverride(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::shortcutOverride(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#shortcutOverride

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::shortcutOverride(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached16shortcutOverrideEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit0Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit0Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit0Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit0Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit0PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit1Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit1Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit1Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit1Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit1PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit2Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit2Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit2Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit2Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit2PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit3Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit3Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit3Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit3Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit3PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit4Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit4Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit4Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit4Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit4PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit5Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit5Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit5Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit5Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit5PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit6Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit6Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit6Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit6Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit6PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit7Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit7Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit7Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit7Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit7PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit8Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit8Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit8Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit8Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit8PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def digit9Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::digit9Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#digit9Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::digit9Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13digit9PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def leftPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::leftPressed(QQuickKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#leftPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::leftPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11leftPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def rightPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::rightPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#rightPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::rightPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached12rightPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def upPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::upPressed(QQuickKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#upPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::upPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached9upPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def downPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::downPressed(QQuickKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#downPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::downPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11downPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def tabPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::tabPressed(QQuickKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#tabPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::tabPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached10tabPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def backtabPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::backtabPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#backtabPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::backtabPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached14backtabPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def asteriskPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::asteriskPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#asteriskPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::asteriskPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached15asteriskPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def numberSignPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::numberSignPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#numberSignPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::numberSignPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached17numberSignPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def escapePressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::escapePressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#escapePressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::escapePressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13escapePressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def returnPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::returnPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#returnPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::returnPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13returnPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def enterPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::enterPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#enterPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::enterPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached12enterPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def deletePressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::deletePressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#deletePressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::deletePressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13deletePressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def spacePressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::spacePressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#spacePressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::spacePressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached12spacePressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def backPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::backPressed(QQuickKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#backPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::backPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11backPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def cancelPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::cancelPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#cancelPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::cancelPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13cancelPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def selectPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::selectPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#selectPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::selectPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13selectPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def yesPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::yesPressed(QQuickKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#yesPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::yesPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached10yesPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def noPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::noPressed(QQuickKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#noPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::noPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached9noPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def context1Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::context1Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#context1Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::context1Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached15context1PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def context2Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::context2Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#context2Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::context2Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached15context2PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def context3Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::context3Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#context3Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::context3Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached15context3PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def context4Pressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::context4Pressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#context4Pressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::context4Pressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached15context4PressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def callPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::callPressed(QQuickKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#callPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::callPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11callPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def hangupPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::hangupPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#hangupPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::hangupPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached13hangupPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def flipPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::flipPressed(QQuickKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#flipPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::flipPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11flipPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def menuPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::menuPressed(QQuickKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#menuPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::menuPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached11menuPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def volumeUpPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::volumeUpPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#volumeUpPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::volumeUpPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached15volumeUpPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QQuickKeyEvent)
  @overload(NoneType)
  def volumeDownPressed(self, event: Optional[QQuickKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::volumeDownPressed(QQuickKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#volumeDownPressed

    Parameters
    ----------

    event : Optional[QQuickKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::volumeDownPressed(QQuickKeyEvent *event)
    self.uglySide.call(
        'ritual_ZN18QQuickKeysAttached17volumeDownPressedEP14QQuickKeyEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def keyPressed(self, event: Optional[QKeyEvent], post: bool) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::keyPressed(QKeyEvent *event, bool
    post)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeysattached.html#keyPressed

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickKeysAttached::keyPressed(QKeyEvent *event, bool post)
    ritual = 'ritual_ZN18QQuickKeysAttached10keyPressedEP9QKeyEventb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickKeysAttached10keyPressedEP9QKeyEventb'
    self.uglySide.call(ritual, self._addressOf(event), post)

  @overload(QKeyEvent, bool)
  @overload(NoneType, bool)
  def keyReleased(self, event: Optional[QKeyEvent], post: bool) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::keyReleased(QKeyEvent *event, bool
    post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#keyReleased

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickKeysAttached::keyReleased(QKeyEvent *event, bool post)
    ritual = 'ritual_ZN18QQuickKeysAttached11keyReleasedEP9QKeyEventb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickKeysAttached11keyReleasedEP9QKeyEventb'
    self.uglySide.call(ritual, self._addressOf(event), post)

  @overload(QInputMethodEvent, bool)
  @overload(NoneType, bool)
  def inputMethodEvent(
      self,
      a0: Optional[QInputMethodEvent],
      post: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::inputMethodEvent(QInputMethodEvent
    *a0, bool post)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#inputMethodEvent

    Parameters
    ----------

    a0 : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    post : bool
      Passed on as it is.
    """
    #  void QQuickKeysAttached::inputMethodEvent(QInputMethodEvent *a0, bool
    #      post)
    ritual = (
        'ritual_ZN18QQuickKeysAttached16inputMethodEventEP17QInputMethodEve'
        'ntb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickKeysAttached16inputMethodEventEP17QInputMet'
          'hodEventb')
    self.uglySide.call(ritual, self._addressOf(a0), post)

  @overload(QKeyEvent)
  @overload(NoneType)
  def shortcutOverrideEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickKeysAttached::shortcutOverrideEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickkeysattached.html#shortcutOverrideEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickKeysAttached::shortcutOverrideEvent(QKeyEvent *event)
    ritual = (
        'ritual_ZN18QQuickKeysAttached21shortcutOverrideEventEP9QKeyEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickKeysAttached21shortcutOverrideEventEP9QKeyE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def forwardTo(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickItem> QQuickKeysAttached::forwardTo()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickKeysAttached.forwardTo' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickItem> QQuickKeysAttached::forwardTo()': "
        "gives a type Python has no way to take yet.")
