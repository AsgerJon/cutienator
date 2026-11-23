"""
QAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qaction.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from . import QKeySequence

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
  from . import QActionGroup, QFont, QIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QActionGroup = WAIT['QActionGroup']
  QEvent = WAIT['QEvent']
  QFont = WAIT['QFont']
  QIcon = WAIT['QIcon']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAction(QObject):
  """
  The cute side of Qt's QAction: a plain Python object standing in front of
  one C++ QAction.

  It is built on the cute 'QObject', as Qt's QAction is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAction that has a ritual and that Python can call
  so far, 57 names in all: 'metaObject', 'tr', 'associatedObjects',
  'setActionGroup', 'actionGroup', 'setIcon', 'icon', 'setText', 'text',
  'setIconText', 'iconText', 'setToolTip', 'toolTip', 'setStatusTip',
  'statusTip', 'setWhatsThis', 'whatsThis', 'setPriority', 'priority',
  'setSeparator', 'isSeparator', 'setShortcut', 'shortcut', 'setShortcuts',
  'shortcuts', 'setShortcutContext', 'shortcutContext', 'setAutoRepeat',
  'autoRepeat', 'setFont', 'font', 'setCheckable', 'isCheckable', 'data',
  'setData', 'isChecked', 'isEnabled', 'isVisible', 'activate',
  'setMenuRole', 'menuRole', 'setIconVisibleInMenu', 'isIconVisibleInMenu',
  'setShortcutVisibleInContextMenu', 'isShortcutVisibleInContextMenu',
  'showStatusText', 'event', 'trigger', 'hover', 'setChecked', 'toggle',
  'setEnabled', 'resetEnabled', 'setDisabled', 'setVisible', 'menuObject',
  'setMenuObject'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAction::~QAction()': the destructor: Python never removes a C++
    QAction.

  What has no ritual
  ------------------

  21 of the 83 functions Qt declares: 7 a signal; 6 a template; 5 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QAction is created at the first use, not by 'QAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAction.
  - Qt tells when it has removed the C++ QAction. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QAction, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class ActionEvent(CuteNum):
    """
    The enum 'QAction::ActionEvent' of Qt, with the 2 names Qt gives in it.
    """

    Trigger = Kee[int](0)
    Hover = Kee[int](1)

  class MenuRole(CuteNum):
    """
    The enum 'QAction::MenuRole' of Qt, with the 7 names Qt gives in it.
    """

    NoRole = Kee[int](0)
    TextHeuristicRole = Kee[int](1)
    ApplicationSpecificRole = Kee[int](2)
    AboutQtRole = Kee[int](3)
    AboutRole = Kee[int](4)
    PreferencesRole = Kee[int](5)
    QuitRole = Kee[int](6)

  class Priority(CuteNum):
    """
    The enum 'QAction::Priority' of Qt, with the 3 names Qt gives in it.
    """

    LowPriority = Kee[int](0)
    NormalPriority = Kee[int](128)
    HighPriority = Kee[int](256)

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
    Calls Qt's 'QString QAction::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#tr

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
    #  QString QAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAction'

  #  A C++ QAction Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAction::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAction::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QAction10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def associatedObjects(self) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *> QAction::associatedObjects() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#associatedObjects

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QAction::associatedObjects() const
    address = self.uglySide.call('ritual_ZNK7QAction17associatedObjectsEv')
    return QList[QObject]._cuteOwning(address)

  def actionGroup(self) -> Optional[QActionGroup]:
    """
    Calls Qt's 'QActionGroup *QAction::actionGroup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#actionGroup

    Returns
    -------

    Optional[QActionGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QActionGroup *QAction::actionGroup() const
    address = self.uglySide.call('ritual_ZNK7QAction11actionGroupEv')
    from . import QActionGroup
    return QActionGroup._cuteAt(address)

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QAction::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QAction::icon() const
    address = self.uglySide.call('ritual_ZNK7QAction4iconEv')
    from . import QIcon
    return QIcon._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QAction::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAction::text() const
    return self.uglySide.call('ritual_ZNK7QAction4textEv')

  def iconText(self) -> str:
    """
    Calls Qt's 'QString QAction::iconText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#iconText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAction::iconText() const
    return self.uglySide.call('ritual_ZNK7QAction8iconTextEv')

  def toolTip(self) -> str:
    """
    Calls Qt's 'QString QAction::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#toolTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAction::toolTip() const
    return self.uglySide.call('ritual_ZNK7QAction7toolTipEv')

  def statusTip(self) -> str:
    """
    Calls Qt's 'QString QAction::statusTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#statusTip

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAction::statusTip() const
    return self.uglySide.call('ritual_ZNK7QAction9statusTipEv')

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QAction::whatsThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAction::whatsThis() const
    return self.uglySide.call('ritual_ZNK7QAction9whatsThisEv')

  def priority(self) -> Priority:
    """
    Calls Qt's 'Priority QAction::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#priority

    Returns
    -------

    Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Priority(number)' gives.
    """
    #  Priority QAction::priority() const
    return QAction.Priority(self.uglySide.call(
        'ritual_ZNK7QAction8priorityEv',
    ))

  def isSeparator(self) -> bool:
    """
    Calls Qt's 'bool QAction::isSeparator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#isSeparator
    """
    #  bool QAction::isSeparator() const
    return self.uglySide.call('ritual_ZNK7QAction11isSeparatorEv')

  def shortcut(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QAction::shortcut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#shortcut

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QAction::shortcut() const
    address = self.uglySide.call('ritual_ZNK7QAction8shortcutEv')
    return QKeySequence._cuteOwning(address)

  def shortcuts(self) -> QList[QKeySequence]:
    """
    Calls Qt's 'QList<QKeySequence> QAction::shortcuts() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#shortcuts

    Returns
    -------

    QList[QKeySequence]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeySequence> QAction::shortcuts() const
    address = self.uglySide.call('ritual_ZNK7QAction9shortcutsEv')
    return QList[QKeySequence]._cuteOwning(address)

  def shortcutContext(self) -> Qt.ShortcutContext:
    """
    Calls Qt's 'Qt::ShortcutContext QAction::shortcutContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#shortcutContext

    Returns
    -------

    Qt.ShortcutContext
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ShortcutContext(number)' gives.
    """
    #  Qt::ShortcutContext QAction::shortcutContext() const
    return Qt.ShortcutContext(self.uglySide.call(
        'ritual_ZNK7QAction15shortcutContextEv',
    ))

  def autoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QAction::autoRepeat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#autoRepeat
    """
    #  bool QAction::autoRepeat() const
    return self.uglySide.call('ritual_ZNK7QAction10autoRepeatEv')

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QAction::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QAction::font() const
    address = self.uglySide.call('ritual_ZNK7QAction4fontEv')
    from . import QFont
    return QFont._cuteOwning(address)

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QAction::isCheckable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#isCheckable
    """
    #  bool QAction::isCheckable() const
    return self.uglySide.call('ritual_ZNK7QAction11isCheckableEv')

  def data(self) -> QVariant:
    """
    Calls Qt's 'QVariant QAction::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#data

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAction::data() const
    address = self.uglySide.call('ritual_ZNK7QAction4dataEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QAction::isChecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#isChecked
    """
    #  bool QAction::isChecked() const
    return self.uglySide.call('ritual_ZNK7QAction9isCheckedEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAction::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#isEnabled
    """
    #  bool QAction::isEnabled() const
    return self.uglySide.call('ritual_ZNK7QAction9isEnabledEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QAction::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#isVisible
    """
    #  bool QAction::isVisible() const
    return self.uglySide.call('ritual_ZNK7QAction9isVisibleEv')

  def menuRole(self) -> MenuRole:
    """
    Calls Qt's 'MenuRole QAction::menuRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#menuRole

    Returns
    -------

    MenuRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MenuRole(number)' gives.
    """
    #  MenuRole QAction::menuRole() const
    return QAction.MenuRole(self.uglySide.call(
        'ritual_ZNK7QAction8menuRoleEv',
    ))

  def isIconVisibleInMenu(self) -> bool:
    """
    Calls Qt's 'bool QAction::isIconVisibleInMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#isIconVisibleInMenu
    """
    #  bool QAction::isIconVisibleInMenu() const
    return self.uglySide.call('ritual_ZNK7QAction19isIconVisibleInMenuEv')

  def isShortcutVisibleInContextMenu(self) -> bool:
    """
    Calls Qt's 'bool QAction::isShortcutVisibleInContextMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaction.html#isShortcutVisibleInContextMenu
    """
    #  bool QAction::isShortcutVisibleInContextMenu() const
    return self.uglySide.call(
        'ritual_ZNK7QAction30isShortcutVisibleInContextMenuEv',
    )

  def menuObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QAction::menuObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#menuObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QAction::menuObject() const
    address = self.uglySide.call('ritual_ZNK7QAction10menuObjectEv')
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QActionGroup)
  @overload(NoneType)
  def setActionGroup(self, group: Optional[QActionGroup]) -> None:
    """
    Calls Qt's 'void QAction::setActionGroup(QActionGroup *group)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setActionGroup

    Parameters
    ----------

    group : Optional[QActionGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAction::setActionGroup(QActionGroup *group)
    self.uglySide.call(
        'ritual_ZN7QAction14setActionGroupEP12QActionGroup',
        self._addressOf(group),
    )

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QAction::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QAction::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN7QAction7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QAction::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAction::setText(const QString &text)
    self.uglySide.call('ritual_ZN7QAction7setTextERK7QString', text)

  @overload(str)
  def setIconText(self, text: str) -> None:
    """
    Calls Qt's 'void QAction::setIconText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setIconText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAction::setIconText(const QString &text)
    self.uglySide.call('ritual_ZN7QAction11setIconTextERK7QString', text)

  @overload(str)
  def setToolTip(self, tip: str) -> None:
    """
    Calls Qt's 'void QAction::setToolTip(const QString &tip)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setToolTip

    Parameters
    ----------

    tip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAction::setToolTip(const QString &tip)
    self.uglySide.call('ritual_ZN7QAction10setToolTipERK7QString', tip)

  @overload(str)
  def setStatusTip(self, statusTip: str) -> None:
    """
    Calls Qt's 'void QAction::setStatusTip(const QString &statusTip)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setStatusTip

    Parameters
    ----------

    statusTip : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAction::setStatusTip(const QString &statusTip)
    self.uglySide.call(
        'ritual_ZN7QAction12setStatusTipERK7QString', statusTip,
    )

  @overload(str)
  def setWhatsThis(self, what: str) -> None:
    """
    Calls Qt's 'void QAction::setWhatsThis(const QString &what)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setWhatsThis

    Parameters
    ----------

    what : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAction::setWhatsThis(const QString &what)
    self.uglySide.call('ritual_ZN7QAction12setWhatsThisERK7QString', what)

  @overload(Priority)
  def setPriority(self, priority: Priority) -> None:
    """
    Calls Qt's 'void QAction::setPriority(Priority priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setPriority

    Parameters
    ----------

    priority : Priority
      Passed on as its number.
    """
    #  void QAction::setPriority(Priority priority)
    self.uglySide.call(
        'ritual_ZN7QAction11setPriorityENS_8PriorityE', priority.value,
    )

  @overload(bool)
  def setSeparator(self, b: bool) -> None:
    """
    Calls Qt's 'void QAction::setSeparator(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setSeparator

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QAction::setSeparator(bool b)
    self.uglySide.call('ritual_ZN7QAction12setSeparatorEb', b)

  @overload(QKeySequence)
  def setShortcut(self, shortcut: QKeySequence) -> None:
    """
    Calls Qt's 'void QAction::setShortcut(const QKeySequence &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setShortcut

    Parameters
    ----------

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QAction::setShortcut(const QKeySequence &shortcut)
    self.uglySide.call(
        'ritual_ZN7QAction11setShortcutERK12QKeySequence',
        self._valueOf(shortcut),
    )

  @overload(QList[QKeySequence])
  def setShortcuts(self, shortcuts: QList[QKeySequence]) -> None:
    """
    Calls Qt's 'void QAction::setShortcuts(const QList<QKeySequence>
    &shortcuts)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setShortcuts

    Parameters
    ----------

    shortcuts : QList[QKeySequence]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAction::setShortcuts(const QList<QKeySequence> &shortcuts)
    self.uglySide.call(
        'ritual_ZN7QAction12setShortcutsERK5QListI12QKeySequenceE',
        self._valueOf(shortcuts),
    )

  @overload(QKeySequence.StandardKey)
  def setShortcuts(self, a0: QKeySequence.StandardKey) -> None:
    """
    Calls Qt's 'void QAction::setShortcuts(QKeySequence::StandardKey a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setShortcuts

    Parameters
    ----------

    a0 : QKeySequence.StandardKey
      Passed on as its number.
    """
    #  void QAction::setShortcuts(QKeySequence::StandardKey a0)
    self.uglySide.call(
        'ritual_ZN7QAction12setShortcutsEN12QKeySequence11StandardKeyE',
        a0.value,
    )

  @overload(Qt.ShortcutContext)
  def setShortcutContext(self, context: Qt.ShortcutContext) -> None:
    """
    Calls Qt's 'void QAction::setShortcutContext(Qt::ShortcutContext
    context)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setShortcutContext

    Parameters
    ----------

    context : Qt.ShortcutContext
      Passed on as its number.
    """
    #  void QAction::setShortcutContext(Qt::ShortcutContext context)
    self.uglySide.call(
        'ritual_ZN7QAction18setShortcutContextEN2Qt15ShortcutContextE',
        context.value,
    )

  @overload(bool)
  def setAutoRepeat(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAction::setAutoRepeat(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setAutoRepeat

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAction::setAutoRepeat(bool a0)
    self.uglySide.call('ritual_ZN7QAction13setAutoRepeatEb', a0)

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QAction::setFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QAction::setFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN7QAction7setFontERK5QFont', self._valueOf(font),
    )

  @overload(bool)
  def setCheckable(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAction::setCheckable(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setCheckable

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAction::setCheckable(bool a0)
    self.uglySide.call('ritual_ZN7QAction12setCheckableEb', a0)

  @overload(QVariant)
  def setData(self, var: QVariant) -> None:
    """
    Calls Qt's 'void QAction::setData(const QVariant &var)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setData

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QAction::setData(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN7QAction7setDataERK8QVariant', self._valueOf(var),
    )

  @overload(MenuRole)
  def setMenuRole(self, menuRole: MenuRole) -> None:
    """
    Calls Qt's 'void QAction::setMenuRole(MenuRole menuRole)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setMenuRole

    Parameters
    ----------

    menuRole : MenuRole
      Passed on as its number.
    """
    #  void QAction::setMenuRole(MenuRole menuRole)
    self.uglySide.call(
        'ritual_ZN7QAction11setMenuRoleENS_8MenuRoleE', menuRole.value,
    )

  @overload(bool)
  def setIconVisibleInMenu(self, visible: bool) -> None:
    """
    Calls Qt's 'void QAction::setIconVisibleInMenu(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setIconVisibleInMenu

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QAction::setIconVisibleInMenu(bool visible)
    self.uglySide.call('ritual_ZN7QAction20setIconVisibleInMenuEb', visible)

  @overload(bool)
  def setShortcutVisibleInContextMenu(self, show: bool) -> None:
    """
    Calls Qt's 'void QAction::setShortcutVisibleInContextMenu(bool show)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaction.html#setShortcutVisibleInContextMenu

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QAction::setShortcutVisibleInContextMenu(bool show)
    self.uglySide.call(
        'ritual_ZN7QAction31setShortcutVisibleInContextMenuEb', show,
    )

  @overload(bool)
  def setChecked(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAction::setChecked(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setChecked

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAction::setChecked(bool a0)
    self.uglySide.call('ritual_ZN7QAction10setCheckedEb', a0)

  @overload(bool)
  def setEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAction::setEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAction::setEnabled(bool a0)
    self.uglySide.call('ritual_ZN7QAction10setEnabledEb', a0)

  @overload(bool)
  def setDisabled(self, b: bool) -> None:
    """
    Calls Qt's 'void QAction::setDisabled(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setDisabled

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QAction::setDisabled(bool b)
    self.uglySide.call('ritual_ZN7QAction11setDisabledEb', b)

  @overload(bool)
  def setVisible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QAction::setVisible(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setVisible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QAction::setVisible(bool a0)
    self.uglySide.call('ritual_ZN7QAction10setVisibleEb', a0)

  @overload(QObject)
  @overload(NoneType)
  def setMenuObject(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAction::setMenuObject(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#setMenuObject

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAction::setMenuObject(QObject *object)
    self.uglySide.call(
        'ritual_ZN7QAction13setMenuObjectEP7QObject',
        self._addressOf(object, 'QObject'),
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
    Notes what was given, for Qt's 'QAction::QAction(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#QAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAction::QAction(QObject *parent)
    self._noteCreation(QAction, lambda: Rituals.call(
        'ritual_ZN7QActionC1EP7QObject', self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, text: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QAction::QAction(const QString &text,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#QAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAction::QAction(const QString &text, QObject *parent)
    self._noteCreation(QAction, lambda: Rituals.call(
        'ritual_ZN7QActionC1ERK7QStringP7QObject',
        text, self._addressOf(parent, 'QObject'),
    ))

  @overload(QIcon, str)
  @overload(QIcon, str, QObject)
  @overload(QIcon, str, NoneType)
  def __init__(
      self,
      icon: QIcon,
      text: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAction::QAction(const QIcon &icon, const
    QString &text, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#QAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAction::QAction(const QIcon &icon, const QString &text, QObject
    #      *parent)
    self._noteCreation(QAction, lambda: Rituals.call(
        'ritual_ZN7QActionC1ERK5QIconRK7QStringP7QObject',
        self._valueOf(icon), text, self._addressOf(parent, 'QObject'),
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

  @overload(ActionEvent)
  def activate(self, event: ActionEvent) -> None:
    """
    Calls Qt's 'void QAction::activate(ActionEvent event)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#activate

    Parameters
    ----------

    event : ActionEvent
      Passed on as its number.
    """
    #  void QAction::activate(ActionEvent event)
    self.uglySide.call(
        'ritual_ZN7QAction8activateENS_11ActionEventE', event.value,
    )

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def showStatusText(self, object: Optional[QObject] = None) -> bool:
    """
    Calls Qt's 'bool QAction::showStatusText(QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#showStatusText

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QAction::showStatusText(QObject *object)
    return self.uglySide.call(
        'ritual_ZN7QAction14showStatusTextEP7QObject',
        self._addressOf(object, 'QObject'),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAction::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAction::event(QEvent *a0)
    ritual = 'ritual_ZN7QAction5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QAction5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  def trigger(self) -> None:
    """
    Calls Qt's 'void QAction::trigger()'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#trigger
    """
    #  void QAction::trigger()
    self.uglySide.call('ritual_ZN7QAction7triggerEv')

  def hover(self) -> None:
    """
    Calls Qt's 'void QAction::hover()'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#hover
    """
    #  void QAction::hover()
    self.uglySide.call('ritual_ZN7QAction5hoverEv')

  def toggle(self) -> None:
    """
    Calls Qt's 'void QAction::toggle()'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#toggle
    """
    #  void QAction::toggle()
    self.uglySide.call('ritual_ZN7QAction6toggleEv')

  def resetEnabled(self) -> None:
    """
    Calls Qt's 'void QAction::resetEnabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qaction.html#resetEnabled
    """
    #  void QAction::resetEnabled()
    self.uglySide.call('ritual_ZN7QAction12resetEnabledEv')


#  Qt's 'QList<QAction *>': the list of QAction, which 'QList[QAction]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QAction.
QList.createKind(
    QAction, 'address',
    make='ritual_list_make_QAction_ptr',
    add='ritual_list_add_QAction_ptr',
    size='ritual_list_size_QAction_ptr',
    at='ritual_list_at_QAction_ptr',
    drop='ritual_list_drop_QAction_ptr',
)
