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
from ..QtGui import QIcon
from ..QtGui import QKeySequence
from ..QtCore import QMetaObject
from ..QtCore import QSize
from ._q_widget import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

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
  can call so far, 28 names in all: 'metaObject', 'tr', 'setText', 'text',
  'setIcon', 'icon', 'iconSize', 'setShortcut', 'shortcut', 'setCheckable',
  'isCheckable', 'isChecked', 'setDown', 'isDown', 'setAutoRepeat',
  'autoRepeat', 'setAutoRepeatDelay', 'autoRepeatDelay',
  'setAutoRepeatInterval', 'autoRepeatInterval', 'setAutoExclusive',
  'autoExclusive', 'group', 'setIconSize', 'animateClick', 'click', 'toggle',
  'setChecked'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractButton::~QAbstractButton()': the destructor: Python never
    removes a C++ QAbstractButton.

  What has no ritual
  ------------------

  28 of the 57 functions Qt declares: 15 protected; 4 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template;
  1 the class is abstract, so C++ cannot make one.

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

  #  The cute classes made after this one that its functions take or give;
  #  see 'WAIT'.
  QButtonGroup = WAIT['QButtonGroup']

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
    return self.QButtonGroup._cuteAt(address)

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
