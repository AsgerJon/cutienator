"""
QQuickAbstractButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickabstractbutton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickAbstractButton to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QTimerEvent
  from ..QtGui import QFocusEvent, QKeyEvent, QKeySequence, QMouseEvent
  from . import QQuickAbstractButtonPrivate, QQuickAction, QQuickIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QKeySequence = WAIT['QKeySequence']
  QMouseEvent = WAIT['QMouseEvent']
  QQuickAction = WAIT['QQuickAction']
  QQuickIcon = WAIT['QQuickIcon']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractButton(QQuickControl):
  """
  The cute side of Qt's QQuickAbstractButton: a plain Python object standing
  in front of one C++ QQuickAbstractButton.

  It is built on the cute 'QQuickControl', as Qt's QQuickAbstractButton is
  built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAbstractButton that has a ritual and that
  Python can call so far, 78 names in all: 'metaObject', 'tr', 'text',
  'setText', 'resetText', 'isDown', 'setDown', 'resetDown', 'isPressed',
  'setPressed', 'isChecked', 'setChecked', 'isCheckable', 'setCheckable',
  'autoExclusive', 'setAutoExclusive', 'autoRepeat', 'setAutoRepeat',
  'indicator', 'setIndicator', 'icon', 'setIcon', 'display', 'setDisplay',
  'action', 'setAction', 'shortcut', 'setShortcut', 'autoRepeatDelay',
  'setAutoRepeatDelay', 'autoRepeatInterval', 'setAutoRepeatInterval',
  'pressX', 'pressY', 'implicitIndicatorWidth', 'implicitIndicatorHeight',
  'toggle', 'click', 'animateClick', 'pressed', 'released', 'canceled',
  'clicked', 'pressAndHold', 'doubleClicked', 'textChanged', 'downChanged',
  'pressedChanged', 'checkedChanged', 'checkableChanged',
  'autoExclusiveChanged', 'autoRepeatChanged', 'indicatorChanged', 'toggled',
  'iconChanged', 'displayChanged', 'actionChanged', 'autoRepeatDelayChanged',
  'autoRepeatIntervalChanged', 'pressXChanged', 'pressYChanged',
  'implicitIndicatorWidthChanged', 'implicitIndicatorHeightChanged',
  'componentComplete', 'event', 'focusOutEvent', 'keyPressEvent',
  'keyReleaseEvent', 'mousePressEvent', 'mouseDoubleClickEvent',
  'timerEvent', 'itemChange', 'nextCheckState', 'accessibilityActiveChanged',
  'accessibleRole', 'accessiblePressAction', 'accessibleToggleAction',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAbstractButton::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAbstractButton::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAbstractButton::~QQuickAbstractButton()': the destructor:
    Python never removes a C++ QQuickAbstractButton.
  - Qt's
    'QQuickAbstractButton::QQuickAbstractButton(QQuickAbstractButtonPrivate
    &dd, QQuickItem *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickAbstractButton::buttonChange(ButtonChange change)':
    names the enum 'QQuickAbstractButton::ButtonChange', whose class cannot
    be named here.
  - Qt's 'const QQuickAbstractButtonPrivate *QQuickAbstractButton::d_func()
    const': takes in Python what 'QQuickAbstractButtonPrivate
    *QQuickAbstractButton::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 89 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickAbstractButton is created at the first use, not by
    'QQuickAbstractButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractButton.
  - Qt tells when it has removed the C++ QQuickAbstractButton. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAbstractButton that has no cute function yet,
    'buttonChange', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QQuickAbstractButton, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Display(CuteNum):
    """
    The enum 'QQuickAbstractButton::Display' of Qt, with the 4 names Qt gives
    in it.
    """

    IconOnly = Kee[int](0)
    TextOnly = Kee[int](1)
    TextBesideIcon = Kee[int](2)
    TextUnderIcon = Kee[int](3)

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
    Calls Qt's 'QString QQuickAbstractButton::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#tr

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
    #  QString QQuickAbstractButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickAbstractButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractButton'

  #  A C++ QQuickAbstractButton Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractButton'

  #  The functions Qt calls itself that QQuickAbstractButton is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'buttonChange': (
          'void QQuickAbstractButton::buttonChange(ButtonChange)',
      ),
  }

  #  The functions Qt calls itself that QQuickAbstractButton is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'nextCheckState': (
          ('_ZN20QQuickAbstractButton14nextCheckStateEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QQuickAbstractButton::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAbstractButton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickAbstractButton::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAbstractButton::text() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractButton4textEv')

  def isDown(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::isDown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#isDown
    """
    #  bool QQuickAbstractButton::isDown() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractButton6isDownEv')

  def isPressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::isPressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#isPressed
    """
    #  bool QQuickAbstractButton::isPressed() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractButton9isPressedEv')

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::isChecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#isChecked
    """
    #  bool QQuickAbstractButton::isChecked() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractButton9isCheckedEv')

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::isCheckable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#isCheckable
    """
    #  bool QQuickAbstractButton::isCheckable() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton11isCheckableEv',
    )

  def autoExclusive(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::autoExclusive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoExclusive
    """
    #  bool QQuickAbstractButton::autoExclusive() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton13autoExclusiveEv',
    )

  def autoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::autoRepeat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoRepeat
    """
    #  bool QQuickAbstractButton::autoRepeat() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton10autoRepeatEv',
    )

  def indicator(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAbstractButton::indicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#indicator

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAbstractButton::indicator() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton9indicatorEv',
    )
    return QQuickItem._cuteAt(address)

  def icon(self) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickAbstractButton::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#icon

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickAbstractButton::icon() const
    address = self.uglySide.call('ritual_ZNK20QQuickAbstractButton4iconEv')
    from . import QQuickIcon
    return QQuickIcon._cuteOwning(address)

  def display(self) -> Display:
    """
    Calls Qt's 'Display QQuickAbstractButton::display() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#display

    Returns
    -------

    Display
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Display(number)' gives.
    """
    #  Display QQuickAbstractButton::display() const
    return QQuickAbstractButton.Display(self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton7displayEv',
    ))

  def action(self) -> Optional[QQuickAction]:
    """
    Calls Qt's 'QQuickAction *QQuickAbstractButton::action() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#action

    Returns
    -------

    Optional[QQuickAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAction *QQuickAbstractButton::action() const
    address = self.uglySide.call('ritual_ZNK20QQuickAbstractButton6actionEv')
    from . import QQuickAction
    return QQuickAction._cuteAt(address)

  def shortcut(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QQuickAbstractButton::shortcut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#shortcut

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QQuickAbstractButton::shortcut() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton8shortcutEv',
    )
    from ..QtGui import QKeySequence
    return QKeySequence._cuteOwning(address)

  def autoRepeatDelay(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractButton::autoRepeatDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoRepeatDelay
    """
    #  int QQuickAbstractButton::autoRepeatDelay() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton15autoRepeatDelayEv',
    )

  def autoRepeatInterval(self) -> int:
    """
    Calls Qt's 'int QQuickAbstractButton::autoRepeatInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoRepeatInterval
    """
    #  int QQuickAbstractButton::autoRepeatInterval() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton18autoRepeatIntervalEv',
    )

  def pressX(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractButton::pressX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#pressX
    """
    #  qreal QQuickAbstractButton::pressX() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractButton6pressXEv')

  def pressY(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractButton::pressY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#pressY
    """
    #  qreal QQuickAbstractButton::pressY() const
    return self.uglySide.call('ritual_ZNK20QQuickAbstractButton6pressYEv')

  def implicitIndicatorWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractButton::implicitIndicatorWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#implicitIndicatorWidth
    """
    #  qreal QQuickAbstractButton::implicitIndicatorWidth() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton22implicitIndicatorWidthEv',
    )

  def implicitIndicatorHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickAbstractButton::implicitIndicatorHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#implicitIndicatorHeight
    """
    #  qreal QQuickAbstractButton::implicitIndicatorHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAbstractButton23implicitIndicatorHeightEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickAbstractButton::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickAbstractButton::accessibleRole() const
    ritual = 'ritual_ZNK20QQuickAbstractButton14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickAbstractButton14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAbstractButton::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton7setTextERK7QString', text,
    )

  @overload(bool)
  def setDown(self, down: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setDown(bool down)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#setDown

    Parameters
    ----------

    down : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setDown(bool down)
    self.uglySide.call('ritual_ZN20QQuickAbstractButton7setDownEb', down)

  @overload(bool)
  def setPressed(self, pressed: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setPressed(bool pressed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setPressed

    Parameters
    ----------

    pressed : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setPressed(bool pressed)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton10setPressedEb', pressed,
    )

  @overload(bool)
  def setChecked(self, checked: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setChecked(bool checked)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setChecked

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setChecked(bool checked)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton10setCheckedEb', checked,
    )

  @overload(bool)
  def setCheckable(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setCheckable(bool checkable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setCheckable

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setCheckable(bool checkable)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton12setCheckableEb', checkable,
    )

  @overload(bool)
  def setAutoExclusive(self, exclusive: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setAutoExclusive(bool exclusive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setAutoExclusive

    Parameters
    ----------

    exclusive : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setAutoExclusive(bool exclusive)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton16setAutoExclusiveEb', exclusive,
    )

  @overload(bool)
  def setAutoRepeat(self, repeat: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setAutoRepeat(bool repeat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setAutoRepeat

    Parameters
    ----------

    repeat : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setAutoRepeat(bool repeat)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton13setAutoRepeatEb', repeat,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setIndicator(self, indicator: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setIndicator(QQuickItem
    *indicator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setIndicator

    Parameters
    ----------

    indicator : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::setIndicator(QQuickItem *indicator)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton12setIndicatorEP10QQuickItem',
        self._addressOf(indicator),
    )

  @overload(QQuickIcon)
  def setIcon(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setIcon(const QQuickIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#setIcon

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickAbstractButton::setIcon(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton7setIconERK10QQuickIcon',
        self._valueOf(icon),
    )

  @overload(Display)
  def setDisplay(self, display: Display) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setDisplay(Display display)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setDisplay

    Parameters
    ----------

    display : Display
      Passed on as its number.
    """
    #  void QQuickAbstractButton::setDisplay(Display display)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton10setDisplayENS_7DisplayE',
        display.value,
    )

  @overload(QQuickAction)
  @overload(NoneType)
  def setAction(self, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setAction(QQuickAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setAction

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::setAction(QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton9setActionEP12QQuickAction',
        self._addressOf(action),
    )

  @overload(QKeySequence)
  def setShortcut(self, shortcut: QKeySequence) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setShortcut(const QKeySequence
    &shortcut)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setShortcut

    Parameters
    ----------

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QQuickAbstractButton::setShortcut(const QKeySequence &shortcut)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton11setShortcutERK12QKeySequence',
        self._valueOf(shortcut),
    )

  @overload(int)
  def setAutoRepeatDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setAutoRepeatDelay(int delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setAutoRepeatDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setAutoRepeatDelay(int delay)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton18setAutoRepeatDelayEi', delay,
    )

  @overload(int)
  def setAutoRepeatInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::setAutoRepeatInterval(int
    interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#setAutoRepeatInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QQuickAbstractButton::setAutoRepeatInterval(int interval)
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton21setAutoRepeatIntervalEi', interval,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAbstractButton::QQuickAbstractButton(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#QQuickAbstractButton

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAbstractButton::QQuickAbstractButton(QQuickItem *parent)
    self._noteCreation(QQuickAbstractButton, lambda: Rituals.call(
        'ritual_ZN20QQuickAbstractButtonC1EP10QQuickItem',
        self._addressOf(parent),
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

  def resetText(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::resetText()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#resetText
    """
    #  void QQuickAbstractButton::resetText()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton9resetTextEv')

  def resetDown(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::resetDown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#resetDown
    """
    #  void QQuickAbstractButton::resetDown()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton9resetDownEv')

  def toggle(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::toggle()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#toggle
    """
    #  void QQuickAbstractButton::toggle()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton6toggleEv')

  def click(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::click()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#click
    """
    #  void QQuickAbstractButton::click()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton5clickEv')

  def animateClick(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::animateClick()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#animateClick
    """
    #  void QQuickAbstractButton::animateClick()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton12animateClickEv')

  def pressed(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#pressed
    """
    #  void QQuickAbstractButton::pressed()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::released()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#released
    """
    #  void QQuickAbstractButton::released()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton8releasedEv')

  def canceled(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::canceled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#canceled
    """
    #  void QQuickAbstractButton::canceled()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton8canceledEv')

  def clicked(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::clicked()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#clicked
    """
    #  void QQuickAbstractButton::clicked()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton7clickedEv')

  def pressAndHold(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::pressAndHold()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#pressAndHold
    """
    #  void QQuickAbstractButton::pressAndHold()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton12pressAndHoldEv')

  def doubleClicked(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::doubleClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#doubleClicked
    """
    #  void QQuickAbstractButton::doubleClicked()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton13doubleClickedEv')

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#textChanged
    """
    #  void QQuickAbstractButton::textChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton11textChangedEv')

  def downChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::downChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#downChanged
    """
    #  void QQuickAbstractButton::downChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton11downChangedEv')

  def pressedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::pressedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#pressedChanged
    """
    #  void QQuickAbstractButton::pressedChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton14pressedChangedEv')

  def checkedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::checkedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#checkedChanged
    """
    #  void QQuickAbstractButton::checkedChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton14checkedChangedEv')

  def checkableChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::checkableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#checkableChanged
    """
    #  void QQuickAbstractButton::checkableChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton16checkableChangedEv')

  def autoExclusiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::autoExclusiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoExclusiveChanged
    """
    #  void QQuickAbstractButton::autoExclusiveChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton20autoExclusiveChangedEv',
    )

  def autoRepeatChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::autoRepeatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoRepeatChanged
    """
    #  void QQuickAbstractButton::autoRepeatChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton17autoRepeatChangedEv',
    )

  def indicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::indicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#indicatorChanged
    """
    #  void QQuickAbstractButton::indicatorChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton16indicatorChangedEv')

  def toggled(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::toggled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#toggled
    """
    #  void QQuickAbstractButton::toggled()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton7toggledEv')

  def iconChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::iconChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#iconChanged
    """
    #  void QQuickAbstractButton::iconChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton11iconChangedEv')

  def displayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::displayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#displayChanged
    """
    #  void QQuickAbstractButton::displayChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton14displayChangedEv')

  def actionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::actionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#actionChanged
    """
    #  void QQuickAbstractButton::actionChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton13actionChangedEv')

  def autoRepeatDelayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::autoRepeatDelayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#autoRepeatDelayChanged
    """
    #  void QQuickAbstractButton::autoRepeatDelayChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton22autoRepeatDelayChangedEv',
    )

  def autoRepeatIntervalChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::autoRepeatIntervalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html
    """
    #  void QQuickAbstractButton::autoRepeatIntervalChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton25autoRepeatIntervalChangedEv',
    )

  def pressXChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::pressXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#pressXChanged
    """
    #  void QQuickAbstractButton::pressXChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton13pressXChangedEv')

  def pressYChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::pressYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#pressYChanged
    """
    #  void QQuickAbstractButton::pressYChanged()
    self.uglySide.call('ritual_ZN20QQuickAbstractButton13pressYChangedEv')

  def implicitIndicatorWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::implicitIndicatorWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html
    """
    #  void QQuickAbstractButton::implicitIndicatorWidthChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton29implicitIndicatorWidthChangedEv',
    )

  def implicitIndicatorHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::implicitIndicatorHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html
    """
    #  void QQuickAbstractButton::implicitIndicatorHeightChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton30implicitIndicatorHeightChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#componentComplete
    """
    #  void QQuickAbstractButton::componentComplete()
    ritual = 'ritual_ZN20QQuickAbstractButton17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractButton17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickAbstractButton::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickAbstractButton::event(QEvent *event)
    ritual = 'ritual_ZN20QQuickAbstractButton5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractButton5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::focusOutEvent(QFocusEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN20QQuickAbstractButton13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton13focusOutEventEP11QFocusEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN20QQuickAbstractButton13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton13keyPressEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::keyReleaseEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN20QQuickAbstractButton15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton15keyReleaseEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::mousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::mousePressEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN20QQuickAbstractButton15mousePressEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton15mousePressEventEP11QMouseEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN20QQuickAbstractButton21mouseDoubleClickEventEP11QMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton21mouseDoubleClickEventEP11QM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::timerEvent(QTimerEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractButton::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN20QQuickAbstractButton10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton10timerEventEP11QTimerEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::itemChange(ItemChange change,
    const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickAbstractButton::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN20QQuickAbstractButton10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::nextCheckState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#nextCheckState
    """
    #  void QQuickAbstractButton::nextCheckState()
    ritual = 'ritual_ZN20QQuickAbstractButton14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAbstractButton14nextCheckStateEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def accessibilityActiveChanged(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::accessibilityActiveChanged(bool
    active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickAbstractButton::accessibilityActiveChanged(bool active)
    ritual = 'ritual_ZN20QQuickAbstractButton26accessibilityActiveChangedEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAbstractButton26accessibilityActiveChangedE'
          'b')
    self.uglySide.call(ritual, active)

  def accessiblePressAction(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::accessiblePressAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#accessiblePressAction
    """
    #  void QQuickAbstractButton::accessiblePressAction()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton21accessiblePressActionEv',
    )

  def accessibleToggleAction(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractButton::accessibleToggleAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractbutton.html#accessibleToggleAction
    """
    #  void QQuickAbstractButton::accessibleToggleAction()
    self.uglySide.call(
        'ritual_ZN20QQuickAbstractButton22accessibleToggleActionEv',
    )

  def d_func(self) -> Optional[QQuickAbstractButtonPrivate]:
    """
    Calls Qt's 'QQuickAbstractButtonPrivate *QQuickAbstractButton::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickabstractbutton.html#d_func

    Returns
    -------

    Optional[QQuickAbstractButtonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButtonPrivate *QQuickAbstractButton::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickAbstractButton6d_funcEv')
    from . import QQuickAbstractButtonPrivate
    return QQuickAbstractButtonPrivate._cuteAt(address)

  @staticmethod
  def buttonChange(*__, **_) -> Never:
    """
    Qt's 'void QQuickAbstractButton::buttonChange(ButtonChange change)':
    names the enum 'QQuickAbstractButton::ButtonChange', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QQuickAbstractButton.buttonChange' has no cute function yet. Qt's "
        "'void QQuickAbstractButton::buttonChange(ButtonChange change)': "
        "names the enum 'QQuickAbstractButton::ButtonChange', whose class "
        "cannot be named here.")


#  Qt's 'QList<QQuickAbstractButton *>': the list of QQuickAbstractButton,
#  which 'QList[QQuickAbstractButton]' gives. It is made here, so that there
#  is one as soon as there can be a QQuickAbstractButton.
QList.createKind(
    QQuickAbstractButton, 'address',
    make='ritual_list_make_QQuickAbstractButton_ptr',
    add='ritual_list_add_QQuickAbstractButton_ptr',
    size='ritual_list_size_QQuickAbstractButton_ptr',
    at='ritual_list_at_QQuickAbstractButton_ptr',
    drop='ritual_list_drop_QQuickAbstractButton_ptr',
)
