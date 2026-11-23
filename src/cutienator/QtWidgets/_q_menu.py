"""
QMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qmenu.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize, QTimerEvent
  from ..QtGui import QAction, QActionEvent, QEnterEvent, QHideEvent, QIcon
  from ..QtGui import QKeyEvent, QKeySequence, QMouseEvent, QPaintEvent
  from ..QtGui import QWheelEvent
  from . import QStyleOptionMenuItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QActionEvent = WAIT['QActionEvent']
  QEnterEvent = WAIT['QEnterEvent']
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QIcon = WAIT['QIcon']
  QKeyEvent = WAIT['QKeyEvent']
  QKeySequence = WAIT['QKeySequence']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QStyleOptionMenuItem = WAIT['QStyleOptionMenuItem']
  QTimerEvent = WAIT['QTimerEvent']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMenu(QWidget):
  """
  The cute side of Qt's QMenu: a plain Python object standing in front of one
  C++ QMenu.

  It is built on the cute 'QWidget', as Qt's QMenu is built on Qt's QWidget,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMenu that has a ritual and that Python can call so
  far, 53 names in all: 'metaObject', 'tr', 'addAction', 'addMenu',
  'addSeparator', 'addSection', 'insertMenu', 'insertSeparator',
  'insertSection', 'isEmpty', 'clear', 'setTearOffEnabled',
  'isTearOffEnabled', 'isTearOffMenuVisible', 'showTearOffMenu',
  'hideTearOffMenu', 'setDefaultAction', 'defaultAction', 'setActiveAction',
  'activeAction', 'popup', 'exec', 'sizeHint', 'actionGeometry', 'actionAt',
  'menuAction', 'menuInAction', 'title', 'setTitle', 'icon', 'setIcon',
  'setNoReplayFor', 'separatorsCollapsible', 'setSeparatorsCollapsible',
  'toolTipsVisible', 'setToolTipsVisible', 'columnCount', 'changeEvent',
  'keyPressEvent', 'mouseReleaseEvent', 'mousePressEvent', 'mouseMoveEvent',
  'wheelEvent', 'enterEvent', 'leaveEvent', 'hideEvent', 'paintEvent',
  'actionEvent', 'timerEvent', 'event', 'focusNextPrevChild',
  'initStyleOption', 'internalDelayedPopup'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMenu::~QMenu()': the destructor: Python never removes a C++ QMenu.

  What has no ritual
  ------------------

  19 of the 83 functions Qt declares: 7 takes or gives a type that cannot be
  passed yet; 5 a template; 4 a signal; 2 forbidden; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QMenu is created at the first use, not by 'QMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMenu.
  - Qt tells when it has removed the C++ QMenu. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QMenu::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#tr

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
    #  QString QMenu::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN5QMenu2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QAction)
  @overload(NoneType)
  def menuInAction(action: Optional[QAction]) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenu::menuInAction(const QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#menuInAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenu::menuInAction(const QAction *action)
    address = Rituals.call(
        'ritual_ZN5QMenu12menuInActionEPK7QAction',
        CuteMixin._addressOf(action),
    )
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMenu'

  #  A C++ QMenu Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMenu'

  #  The functions Qt calls itself that QMenu is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK5QMenu15initStyleOptionEP20QStyleOptionMenuItemPK7QAction',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionMenuItem'),
               ('address', 'address', 'QtGui:QAction'),
           )),
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
    Calls Qt's 'const QMetaObject *QMenu::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMenu::metaObject() const
    address = self.uglySide.call('ritual_ZNK5QMenu10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QMenu::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#isEmpty
    """
    #  bool QMenu::isEmpty() const
    return self.uglySide.call('ritual_ZNK5QMenu7isEmptyEv')

  def isTearOffEnabled(self) -> bool:
    """
    Calls Qt's 'bool QMenu::isTearOffEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#isTearOffEnabled
    """
    #  bool QMenu::isTearOffEnabled() const
    return self.uglySide.call('ritual_ZNK5QMenu16isTearOffEnabledEv')

  def isTearOffMenuVisible(self) -> bool:
    """
    Calls Qt's 'bool QMenu::isTearOffMenuVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#isTearOffMenuVisible
    """
    #  bool QMenu::isTearOffMenuVisible() const
    return self.uglySide.call('ritual_ZNK5QMenu20isTearOffMenuVisibleEv')

  def defaultAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::defaultAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#defaultAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::defaultAction() const
    address = self.uglySide.call('ritual_ZNK5QMenu13defaultActionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def activeAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::activeAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#activeAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::activeAction() const
    address = self.uglySide.call('ritual_ZNK5QMenu12activeActionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMenu::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMenu::sizeHint() const
    ritual = 'ritual_ZNK5QMenu8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK5QMenu8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QAction)
  @overload(NoneType)
  def actionGeometry(self, a0: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect QMenu::actionGeometry(QAction *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#actionGeometry

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMenu::actionGeometry(QAction *a0) const
    address = self.uglySide.call(
        'ritual_ZNK5QMenu14actionGeometryEP7QAction', self._addressOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def actionAt(self, a0: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::actionAt(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#actionAt

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::actionAt(const QPoint &a0) const
    address = self.uglySide.call(
        'ritual_ZNK5QMenu8actionAtERK6QPoint', self._valueOf(a0),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def menuAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::menuAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#menuAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::menuAction() const
    address = self.uglySide.call('ritual_ZNK5QMenu10menuActionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QMenu::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMenu::title() const
    return self.uglySide.call('ritual_ZNK5QMenu5titleEv')

  def icon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QMenu::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#icon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QMenu::icon() const
    address = self.uglySide.call('ritual_ZNK5QMenu4iconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  def separatorsCollapsible(self) -> bool:
    """
    Calls Qt's 'bool QMenu::separatorsCollapsible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#separatorsCollapsible
    """
    #  bool QMenu::separatorsCollapsible() const
    return self.uglySide.call('ritual_ZNK5QMenu21separatorsCollapsibleEv')

  def toolTipsVisible(self) -> bool:
    """
    Calls Qt's 'bool QMenu::toolTipsVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#toolTipsVisible
    """
    #  bool QMenu::toolTipsVisible() const
    return self.uglySide.call('ritual_ZNK5QMenu15toolTipsVisibleEv')

  def columnCount(self) -> int:
    """
    Calls Qt's 'int QMenu::columnCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#columnCount
    """
    #  int QMenu::columnCount() const
    return self.uglySide.call('ritual_ZNK5QMenu11columnCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setTearOffEnabled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QMenu::setTearOffEnabled(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setTearOffEnabled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QMenu::setTearOffEnabled(bool a0)
    self.uglySide.call('ritual_ZN5QMenu17setTearOffEnabledEb', a0)

  @overload(QAction)
  @overload(NoneType)
  def setDefaultAction(self, a0: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QMenu::setDefaultAction(QAction *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setDefaultAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::setDefaultAction(QAction *a0)
    self.uglySide.call(
        'ritual_ZN5QMenu16setDefaultActionEP7QAction', self._addressOf(a0),
    )

  @overload(QAction)
  @overload(NoneType)
  def setActiveAction(self, act: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QMenu::setActiveAction(QAction *act)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setActiveAction

    Parameters
    ----------

    act : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::setActiveAction(QAction *act)
    self.uglySide.call(
        'ritual_ZN5QMenu15setActiveActionEP7QAction', self._addressOf(act),
    )

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QMenu::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMenu::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN5QMenu8setTitleERK7QString', title)

  @overload(QIcon)
  def setIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QMenu::setIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QMenu::setIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN5QMenu7setIconERK5QIcon', self._valueOf(icon),
    )

  @overload(QWidget)
  @overload(NoneType)
  def setNoReplayFor(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QMenu::setNoReplayFor(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setNoReplayFor

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::setNoReplayFor(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN5QMenu14setNoReplayForEP7QWidget', self._addressOf(widget),
    )

  @overload(bool)
  def setSeparatorsCollapsible(self, collapse: bool) -> None:
    """
    Calls Qt's 'void QMenu::setSeparatorsCollapsible(bool collapse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenu.html#setSeparatorsCollapsible

    Parameters
    ----------

    collapse : bool
      Passed on as it is.
    """
    #  void QMenu::setSeparatorsCollapsible(bool collapse)
    self.uglySide.call(
        'ritual_ZN5QMenu24setSeparatorsCollapsibleEb', collapse,
    )

  @overload(bool)
  def setToolTipsVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QMenu::setToolTipsVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#setToolTipsVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QMenu::setToolTipsVisible(bool visible)
    self.uglySide.call('ritual_ZN5QMenu18setToolTipsVisibleEb', visible)

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
    Notes what was given, for Qt's 'QMenu::QMenu(QWidget *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#QMenu

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMenu::QMenu(QWidget *parent)
    self._noteCreation(QMenu, lambda: Rituals.call(
        'ritual_ZN5QMenuC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, title: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QMenu::QMenu(const QString &title,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#QMenu

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMenu::QMenu(const QString &title, QWidget *parent)
    self._noteCreation(QMenu, lambda: Rituals.call(
        'ritual_ZN5QMenuC1ERK7QStringP7QWidget',
        title, self._addressOf(parent),
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

  @overload(str, QObject, str, QKeySequence)
  @overload(str, QObject, NoneType, QKeySequence)
  @overload(str, NoneType, str, QKeySequence)
  @overload(str, NoneType, NoneType, QKeySequence)
  def addAction(
      self,
      text: str,
      receiver: Optional[QObject],
      member: Optional[str],
      shortcut: QKeySequence,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::addAction(const QString &text, const QObject
    *receiver, const char *member, const QKeySequence &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::addAction(const QString &text, const QObject
    #      *receiver, const char *member, const QKeySequence &shortcut)
    address = self.uglySide.call(
        'ritual_ZN5QMenu9addActionERK7QStringPK7QObjectPKcRK12QKeySequence',
        text, self._addressOf(receiver, 'QObject'), self._bytesOf(member),
        self._valueOf(shortcut),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QIcon, str, QObject, str, QKeySequence)
  @overload(QIcon, str, QObject, NoneType, QKeySequence)
  @overload(QIcon, str, NoneType, str, QKeySequence)
  @overload(QIcon, str, NoneType, NoneType, QKeySequence)
  def addAction(
      self,
      icon: QIcon,
      text: str,
      receiver: Optional[QObject],
      member: Optional[str],
      shortcut: QKeySequence,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::addAction(const QIcon &icon, const QString
    &text, const QObject *receiver, const char *member, const QKeySequence
    &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addAction

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::addAction(const QIcon &icon, const QString &text,
    #      const QObject *receiver, const char *member, const QKeySequence
    #      &shortcut)
    address = self.uglySide.call(
        'ritual_ZN5QMenu9addActionERK5QIconRK7QStringPK7QObjectPKcRK12QKeyS'
        'equence',
        self._valueOf(icon), text, self._addressOf(receiver, 'QObject'),
        self._bytesOf(member), self._valueOf(shortcut),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def addMenu(self, menu: Optional[QMenu]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::addMenu(QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::addMenu(QMenu *menu)
    address = self.uglySide.call(
        'ritual_ZN5QMenu7addMenuEPS_', self._addressOf(menu),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(str)
  def addMenu(self, title: str) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenu::addMenu(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addMenu

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenu::addMenu(const QString &title)
    address = self.uglySide.call('ritual_ZN5QMenu7addMenuERK7QString', title)
    return QMenu._cuteAt(address)

  @overload(QIcon, str)
  def addMenu(self, icon: QIcon, title: str) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenu::addMenu(const QIcon &icon, const QString
    &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addMenu

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    title : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenu::addMenu(const QIcon &icon, const QString &title)
    address = self.uglySide.call(
        'ritual_ZN5QMenu7addMenuERK5QIconRK7QString',
        self._valueOf(icon), title,
    )
    return QMenu._cuteAt(address)

  def addSeparator(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::addSeparator()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addSeparator

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::addSeparator()
    address = self.uglySide.call('ritual_ZN5QMenu12addSeparatorEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(str)
  def addSection(self, text: str) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::addSection(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addSection

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::addSection(const QString &text)
    address = self.uglySide.call(
        'ritual_ZN5QMenu10addSectionERK7QString', text,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QIcon, str)
  def addSection(self, icon: QIcon, text: str) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::addSection(const QIcon &icon, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#addSection

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::addSection(const QIcon &icon, const QString &text)
    address = self.uglySide.call(
        'ritual_ZN5QMenu10addSectionERK5QIconRK7QString',
        self._valueOf(icon), text,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction, THIS)
  @overload(QAction, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def insertMenu(
      self,
      before: Optional[QAction],
      menu: Optional[QMenu],
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::insertMenu(QAction *before, QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#insertMenu

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::insertMenu(QAction *before, QMenu *menu)
    address = self.uglySide.call(
        'ritual_ZN5QMenu10insertMenuEP7QActionPS_',
        self._addressOf(before), self._addressOf(menu),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def insertSeparator(self, before: Optional[QAction]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::insertSeparator(QAction *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#insertSeparator

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::insertSeparator(QAction *before)
    address = self.uglySide.call(
        'ritual_ZN5QMenu15insertSeparatorEP7QAction',
        self._addressOf(before),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction, str)
  @overload(NoneType, str)
  def insertSection(
      self,
      before: Optional[QAction],
      text: str,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::insertSection(QAction *before, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#insertSection

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::insertSection(QAction *before, const QString &text)
    address = self.uglySide.call(
        'ritual_ZN5QMenu13insertSectionEP7QActionRK7QString',
        self._addressOf(before), text,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction, QIcon, str)
  @overload(NoneType, QIcon, str)
  def insertSection(
      self,
      before: Optional[QAction],
      icon: QIcon,
      text: str,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::insertSection(QAction *before, const QIcon
    &icon, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#insertSection

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::insertSection(QAction *before, const QIcon &icon,
    #      const QString &text)
    address = self.uglySide.call(
        'ritual_ZN5QMenu13insertSectionEP7QActionRK5QIconRK7QString',
        self._addressOf(before), self._valueOf(icon), text,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QMenu::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#clear
    """
    #  void QMenu::clear()
    self.uglySide.call('ritual_ZN5QMenu5clearEv')

  @overload()
  def showTearOffMenu(self) -> None:
    """
    Calls Qt's 'void QMenu::showTearOffMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#showTearOffMenu
    """
    #  void QMenu::showTearOffMenu()
    self.uglySide.call('ritual_ZN5QMenu15showTearOffMenuEv')

  @overload(QPoint)
  def showTearOffMenu(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QMenu::showTearOffMenu(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#showTearOffMenu

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QMenu::showTearOffMenu(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN5QMenu15showTearOffMenuERK6QPoint', self._valueOf(pos),
    )

  def hideTearOffMenu(self) -> None:
    """
    Calls Qt's 'void QMenu::hideTearOffMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#hideTearOffMenu
    """
    #  void QMenu::hideTearOffMenu()
    self.uglySide.call('ritual_ZN5QMenu15hideTearOffMenuEv')

  @overload(QPoint)
  @overload(QPoint, QAction)
  @overload(QPoint, NoneType)
  def popup(self, pos: QPoint, at: Optional[QAction] = None) -> None:
    """
    Calls Qt's 'void QMenu::popup(const QPoint &pos, QAction *at)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#popup

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    at : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QMenu::popup(const QPoint &pos, QAction *at)
    self.uglySide.call(
        'ritual_ZN5QMenu5popupERK6QPointP7QAction',
        self._valueOf(pos), self._addressOf(at),
    )

  @overload()
  def exec(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#exec

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::exec()
    address = self.uglySide.call('ritual_ZN5QMenu4execEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QPoint)
  @overload(QPoint, QAction)
  @overload(QPoint, NoneType)
  def exec(
      self,
      pos: QPoint,
      at: Optional[QAction] = None,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::exec(const QPoint &pos, QAction *at)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#exec

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    at : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::exec(const QPoint &pos, QAction *at)
    address = self.uglySide.call(
        'ritual_ZN5QMenu4execERK6QPointP7QAction',
        self._valueOf(pos), self._addressOf(at),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @staticmethod
  @overload(QList[QAction], QPoint)
  @overload(QList[QAction], QPoint, QAction)
  @overload(QList[QAction], QPoint, NoneType)
  @overload(QList[QAction], QPoint, QAction, QWidget)
  @overload(QList[QAction], QPoint, QAction, NoneType)
  @overload(QList[QAction], QPoint, NoneType, QWidget)
  @overload(QList[QAction], QPoint, NoneType, NoneType)
  def exec(
      actions: QList[QAction],
      pos: QPoint,
      at: Optional[QAction] = None,
      parent: Optional[QWidget] = None,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenu::exec(const QList<QAction *> &actions, const
    QPoint &pos, QAction *at, QWidget *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#exec

    Parameters
    ----------

    actions : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    at : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenu::exec(const QList<QAction *> &actions, const QPoint
    #      &pos, QAction *at, QWidget *parent)
    address = Rituals.call(
        'ritual_ZN5QMenu4execERK5QListIP7QActionERK6QPointS2_P7QWidget',
        CuteMixin._valueOf(actions), CuteMixin._valueOf(pos),
        CuteMixin._addressOf(at), CuteMixin._addressOf(parent),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QMenu::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::changeEvent(QEvent *a0)
    ritual = 'ritual_ZN5QMenu11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QMenu::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN5QMenu13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMenu::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN5QMenu17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMenu::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN5QMenu15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMenu::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN5QMenu14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, a0: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QMenu::wheelEvent(QWheelEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#wheelEvent

    Parameters
    ----------

    a0 : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::wheelEvent(QWheelEvent *a0)
    ritual = 'ritual_ZN5QMenu10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEnterEvent)
  @overload(NoneType)
  def enterEvent(self, a0: Optional[QEnterEvent]) -> None:
    """
    Calls Qt's 'void QMenu::enterEvent(QEnterEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#enterEvent

    Parameters
    ----------

    a0 : Optional[QEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::enterEvent(QEnterEvent *a0)
    ritual = 'ritual_ZN5QMenu10enterEventEP11QEnterEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu10enterEventEP11QEnterEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def leaveEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QMenu::leaveEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#leaveEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::leaveEvent(QEvent *a0)
    ritual = 'ritual_ZN5QMenu10leaveEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu10leaveEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QMenu::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::hideEvent(QHideEvent *a0)
    ritual = 'ritual_ZN5QMenu9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QMenu::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN5QMenu10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, a0: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QMenu::actionEvent(QActionEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#actionEvent

    Parameters
    ----------

    a0 : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::actionEvent(QActionEvent *a0)
    ritual = 'ritual_ZN5QMenu11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu11actionEventEP12QActionEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMenu::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN5QMenu10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QMenu::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMenu::event(QEvent *a0)
    ritual = 'ritual_ZN5QMenu5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QMenu::focusNextPrevChild(bool next)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QMenu::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN5QMenu18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN5QMenu18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  @overload(QStyleOptionMenuItem, QAction)
  @overload(QStyleOptionMenuItem, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def initStyleOption(
      self,
      option: Optional[QStyleOptionMenuItem],
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void QMenu::initStyleOption(QStyleOptionMenuItem *option,
    const QAction *action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenu::initStyleOption(QStyleOptionMenuItem *option, const
    #      QAction *action) const
    ritual = (
        'ritual_ZNK5QMenu15initStyleOptionEP20QStyleOptionMenuItemPK7QActio'
        'n')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK5QMenu15initStyleOptionEP20QStyleOptionMenuItemPK7'
          'QAction')
    self.uglySide.call(
        ritual, self._addressOf(option), self._addressOf(action),
    )

  def internalDelayedPopup(self) -> None:
    """
    Calls Qt's 'void QMenu::internalDelayedPopup()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenu.html#internalDelayedPopup
    """
    #  void QMenu::internalDelayedPopup()
    self.uglySide.call('ritual_ZN5QMenu20internalDelayedPopupEv')
