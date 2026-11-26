"""
QAbstractButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractbutton.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QSize, QTimerEvent
  from ..QtGui import QFocusEvent, QIcon, QKeyEvent, QKeySequence
  from ..QtGui import QMouseEvent, QPaintEvent
  from . import QButtonGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QIcon = WAIT['QIcon']
  QKeyEvent = WAIT['QKeyEvent']
  QKeySequence = WAIT['QKeySequence']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractButton(QWidget):
  """
  The cute side of Qt's QAbstractButton: a plain Python object standing in
  front of one C++ QAbstractButton.

  It is built on the cute 'QWidget', as Qt's QAbstractButton is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractButton that has a ritual and that Python
  can call so far, 46 names in all: 'metaObject', 'tr', 'setText', 'text',
  'setIcon', 'icon', 'iconSize', 'setShortcut', 'shortcut', 'setCheckable',
  'isCheckable', 'isChecked', 'setDown', 'isDown', 'setAutoRepeat',
  'autoRepeat', 'setAutoRepeatDelay', 'autoRepeatDelay',
  'setAutoRepeatInterval', 'autoRepeatInterval', 'setAutoExclusive',
  'autoExclusive', 'group', 'setIconSize', 'animateClick', 'click', 'toggle',
  'setChecked', 'pressed', 'released', 'clicked', 'toggled', 'paintEvent',
  'hitButton', 'checkStateSet', 'nextCheckState', 'event', 'keyPressEvent',
  'keyReleaseEvent', 'mousePressEvent', 'mouseReleaseEvent',
  'mouseMoveEvent', 'focusInEvent', 'focusOutEvent', 'changeEvent',
  'timerEvent'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractButton::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractButton::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractButton::~QAbstractButton()': the destructor: Python never
    removes a C++ QAbstractButton.
  - Qt's 'QAbstractButton::QAbstractButton(QAbstractButtonPrivate &dd,
    QWidget *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractButtonPrivate *QAbstractButton::d_func()': gives
    'QAbstractButtonPrivate', which has no cute class yet.
  - Qt's 'const QAbstractButtonPrivate *QAbstractButton::d_func() const':
    gives 'QAbstractButtonPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 57 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractButton is created at the first use, not by
    'QAbstractButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractButton.
  - Qt tells when it has removed the C++ QAbstractButton. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QAbstractButton::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#tr

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
    #  QString QAbstractButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QAbstractButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractButton'

  #  A C++ QAbstractButton Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractButton'

  #  The functions Qt calls itself that QAbstractButton is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'hitButton': (
          ('_ZNK15QAbstractButton9hitButtonERK6QPoint',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'checkStateSet': (
          ('_ZN15QAbstractButton13checkStateSetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'nextCheckState': (
          ('_ZN15QAbstractButton14nextCheckStateEv',
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
    Calls Qt's 'const QMetaObject *QAbstractButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractButton::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAbstractButton10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QAbstractButton::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractButton::text() const
    return self.uglySide.call('ritual_ZNK15QAbstractButton4textEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QAbstractButton::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAbstractButton::icon() const
    address = self.uglySide.call('ritual_ZNK15QAbstractButton4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractButton::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractButton::iconSize() const
    address = self.uglySide.call('ritual_ZNK15QAbstractButton8iconSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def shortcut(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QAbstractButton::shortcut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#shortcut

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QAbstractButton::shortcut() const
    address = self.uglySide.call('ritual_ZNK15QAbstractButton8shortcutEv')
    from ..QtGui import QKeySequence
    return QKeySequence._cuteOwning(address)

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::isCheckable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#isCheckable
    """
    #  bool QAbstractButton::isCheckable() const
    return self.uglySide.call('ritual_ZNK15QAbstractButton11isCheckableEv')

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::isChecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#isChecked
    """
    #  bool QAbstractButton::isChecked() const
    return self.uglySide.call('ritual_ZNK15QAbstractButton9isCheckedEv')

  def isDown(self) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::isDown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#isDown
    """
    #  bool QAbstractButton::isDown() const
    return self.uglySide.call('ritual_ZNK15QAbstractButton6isDownEv')

  def autoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::autoRepeat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#autoRepeat
    """
    #  bool QAbstractButton::autoRepeat() const
    return self.uglySide.call('ritual_ZNK15QAbstractButton10autoRepeatEv')

  def autoRepeatDelay(self) -> int:
    """
    Calls Qt's 'int QAbstractButton::autoRepeatDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#autoRepeatDelay
    """
    #  int QAbstractButton::autoRepeatDelay() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractButton15autoRepeatDelayEv',
    )

  def autoRepeatInterval(self) -> int:
    """
    Calls Qt's 'int QAbstractButton::autoRepeatInterval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#autoRepeatInterval
    """
    #  int QAbstractButton::autoRepeatInterval() const
    return self.uglySide.call(
        'ritual_ZNK15QAbstractButton18autoRepeatIntervalEv',
    )

  def autoExclusive(self) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::autoExclusive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#autoExclusive
    """
    #  bool QAbstractButton::autoExclusive() const
    return self.uglySide.call('ritual_ZNK15QAbstractButton13autoExclusiveEv')

  def group(self) -> Optional[QButtonGroup]:
    """
    Calls Qt's 'QButtonGroup *QAbstractButton::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#group

    Returns
    -------

    Optional[QButtonGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QButtonGroup *QAbstractButton::group() const
    address = self.uglySide.call('ritual_ZNK15QAbstractButton5groupEv')
    from . import QButtonGroup
    return QButtonGroup._cuteAt(address)

  @overload(QPoint)
  def hitButton(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::hitButton(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#hitButton

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QAbstractButton::hitButton(const QPoint &pos) const
    ritual = 'ritual_ZNK15QAbstractButton9hitButtonERK6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAbstractButton9hitButtonERK6QPoint'
    return self.uglySide.call(ritual, self._valueOf(pos))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QAbstractButton::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractButton::setText(const QString &text)
    self.uglySide.call('ritual_ZN15QAbstractButton7setTextERK7QString', text)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QAbstractButton::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QAbstractButton::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN15QAbstractButton7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(QKeySequence)
  def setShortcut(self, key: QKeySequence) -> None:
    """
    Calls Qt's 'void QAbstractButton::setShortcut(const QKeySequence &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setShortcut

    Parameters
    ----------

    key : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QAbstractButton::setShortcut(const QKeySequence &key)
    self.uglySide.call(
        'ritual_ZN15QAbstractButton11setShortcutERK12QKeySequence',
        self._valueOf(key),
    )

  @overload(bool)
  def setCheckable(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractButton::setCheckable(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setCheckable

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractButton::setCheckable(bool a0)
    self.uglySide.call('ritual_ZN15QAbstractButton12setCheckableEb', a0)

  @overload(bool)
  def setDown(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractButton::setDown(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setDown

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractButton::setDown(bool a0)
    self.uglySide.call('ritual_ZN15QAbstractButton7setDownEb', a0)

  @overload(bool)
  def setAutoRepeat(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractButton::setAutoRepeat(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setAutoRepeat

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractButton::setAutoRepeat(bool a0)
    self.uglySide.call('ritual_ZN15QAbstractButton13setAutoRepeatEb', a0)

  @overload(int)
  def setAutoRepeatDelay(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractButton::setAutoRepeatDelay(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#setAutoRepeatDelay

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractButton::setAutoRepeatDelay(int a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractButton18setAutoRepeatDelayEi', a0,
    )

  @overload(int)
  def setAutoRepeatInterval(self, a0: int) -> None:
    """
    Calls Qt's 'void QAbstractButton::setAutoRepeatInterval(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#setAutoRepeatInterval

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QAbstractButton::setAutoRepeatInterval(int a0)
    self.uglySide.call(
        'ritual_ZN15QAbstractButton21setAutoRepeatIntervalEi', a0,
    )

  @overload(bool)
  def setAutoExclusive(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractButton::setAutoExclusive(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#setAutoExclusive

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractButton::setAutoExclusive(bool a0)
    self.uglySide.call('ritual_ZN15QAbstractButton16setAutoExclusiveEb', a0)

  @overload(QSize)
  def setIconSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QAbstractButton::setIconSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setIconSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QAbstractButton::setIconSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15QAbstractButton11setIconSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(bool)
  def setChecked(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAbstractButton::setChecked(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#setChecked

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAbstractButton::setChecked(bool a0)
    self.uglySide.call('ritual_ZN15QAbstractButton10setCheckedEb', a0)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QAbstractButton::QAbstractButton(QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#QAbstractButton

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractButton::QAbstractButton(QWidget *parent)
    self._noteCreation(QAbstractButton, lambda: Rituals.call(
        'ritual_ZN15QAbstractButtonC1EP7QWidget', self._addressOf(parent),
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

  def animateClick(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::animateClick()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#animateClick
    """
    #  void QAbstractButton::animateClick()
    self.uglySide.call('ritual_ZN15QAbstractButton12animateClickEv')

  def click(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::click()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#click
    """
    #  void QAbstractButton::click()
    self.uglySide.call('ritual_ZN15QAbstractButton5clickEv')

  def toggle(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::toggle()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#toggle
    """
    #  void QAbstractButton::toggle()
    self.uglySide.call('ritual_ZN15QAbstractButton6toggleEv')

  def pressed(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::pressed()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#pressed
    """
    #  void QAbstractButton::pressed()
    self.uglySide.call('ritual_ZN15QAbstractButton7pressedEv')

  def released(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::released()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#released
    """
    #  void QAbstractButton::released()
    self.uglySide.call('ritual_ZN15QAbstractButton8releasedEv')

  @overload()
  @overload(bool)
  def clicked(self, checked: bool = False) -> None:
    """
    Calls Qt's 'void QAbstractButton::clicked(bool checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#clicked

    Parameters
    ----------

    checked : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QAbstractButton::clicked(bool checked)
    self.uglySide.call('ritual_ZN15QAbstractButton7clickedEb', checked)

  @overload(bool)
  def toggled(self, checked: bool) -> None:
    """
    Calls Qt's 'void QAbstractButton::toggled(bool checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#toggled

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QAbstractButton::toggled(bool checked)
    self.uglySide.call('ritual_ZN15QAbstractButton7toggledEb', checked)

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::paintEvent(QPaintEvent *e)
    self.uglySide.call(
        'ritual_ZN15QAbstractButton10paintEventEP11QPaintEvent',
        self._addressOf(e),
    )

  def checkStateSet(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::checkStateSet()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#checkStateSet
    """
    #  void QAbstractButton::checkStateSet()
    ritual = 'ritual_ZN15QAbstractButton13checkStateSetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton13checkStateSetEv'
    self.uglySide.call(ritual)

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QAbstractButton::nextCheckState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#nextCheckState
    """
    #  void QAbstractButton::nextCheckState()
    ritual = 'ritual_ZN15QAbstractButton14nextCheckStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton14nextCheckStateEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractButton::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractButton::event(QEvent *e)
    ritual = 'ritual_ZN15QAbstractButton5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::keyPressEvent(QKeyEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#keyPressEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::keyPressEvent(QKeyEvent *e)
    ritual = 'ritual_ZN15QAbstractButton13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::keyReleaseEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#keyReleaseEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::keyReleaseEvent(QKeyEvent *e)
    ritual = 'ritual_ZN15QAbstractButton15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::mousePressEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::mousePressEvent(QMouseEvent *e)
    ritual = 'ritual_ZN15QAbstractButton15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractButton15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#mouseReleaseEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::mouseReleaseEvent(QMouseEvent *e)
    ritual = 'ritual_ZN15QAbstractButton17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractButton17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::mouseMoveEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractbutton.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::mouseMoveEvent(QMouseEvent *e)
    ritual = 'ritual_ZN15QAbstractButton14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QAbstractButton14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, e: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::focusInEvent(QFocusEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#focusInEvent

    Parameters
    ----------

    e : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::focusInEvent(QFocusEvent *e)
    ritual = 'ritual_ZN15QAbstractButton12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, e: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::focusOutEvent(QFocusEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#focusOutEvent

    Parameters
    ----------

    e : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::focusOutEvent(QFocusEvent *e)
    ritual = 'ritual_ZN15QAbstractButton13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::changeEvent(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::changeEvent(QEvent *e)
    ritual = 'ritual_ZN15QAbstractButton11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QAbstractButton::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractbutton.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractButton::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN15QAbstractButton10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAbstractButton10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))


#  Qt's 'QList<QAbstractButton *>': the list of QAbstractButton, which
#  'QList[QAbstractButton]' gives. It is made here, so that there is one as
#  soon as there can be a QAbstractButton.
QList.createKind(
    QAbstractButton, 'address',
    make='ritual_list_make_QAbstractButton_ptr',
    add='ritual_list_add_QAbstractButton_ptr',
    size='ritual_list_size_QAbstractButton_ptr',
    at='ritual_list_at_QAbstractButton_ptr',
    drop='ritual_list_drop_QAbstractButton_ptr',
)
