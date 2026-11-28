"""
QDesignerMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_menu_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMenu to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QMenu, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect
  from ..QtGui import QAction, QActionEvent, QContextMenuEvent
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QKeyEvent, QMouseEvent, QPaintEvent
  from ..QtGui import QPainter, QShowEvent
  from . import QDesignerActionProviderExtension
  from . import QDesignerFormWindowInterface, QDesignerMenuBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QActionEvent = WAIT['QActionEvent']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerMenu(QMenu):
  """
  The cute side of Qt's QDesignerMenu: a plain Python object standing in
  front of one C++ QDesignerMenu.

  It is built on the cute 'QMenu', as Qt's QDesignerMenu is built on Qt's
  QMenu, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerMenu that has a ritual and that Python can
  call so far, 63 names in all: 'metaObject', 'tr', 'handleEvent',
  'deactivateMenu', 'formWindow', 'actionProvider', 'parentMenu',
  'parentMenuBar', 'setVisible', 'adjustSpecialActions',
  'createRealMenuAction', 'removeRealMenu', 'drawSelection', 'dragging',
  'closeMenuChain', 'moveLeft', 'moveRight', 'moveUp', 'moveDown',
  'deleteAction', 'slotAddSeparator', 'slotRemoveSelectedAction',
  'slotShowSubMenuNow', 'slotDeactivateNow', 'slotAdjustSizeNow',
  'stopInlineEditing', 'actionEvent', 'dragEnterEvent', 'dragMoveEvent',
  'dragLeaveEvent', 'dropEvent', 'paintEvent', 'keyPressEvent',
  'keyReleaseEvent', 'showEvent', 'handleMouseDoubleClickEvent',
  'handleMousePressEvent', 'handleMouseReleaseEvent', 'handleMouseMoveEvent',
  'handleContextMenuEvent', 'handleKeyPressEvent', 'startDrag',
  'adjustIndicator', 'findAction', 'currentAction', 'realActionCount',
  'showSubMenu', 'enterEditMode', 'showLineEdit', 'createAction',
  'findOrCreateSubMenu', 'safeActionAt', 'safeMenuAction', 'swap',
  'hideSubMenu', 'canCreateSubMenu', 'findRootMenu', 'findActivatedMenu',
  'subMenuPixmapRect', 'hasSubMenuPixmap', 'selectCurrentAction',
  'hideSubMenuOnCursorKey', 'showSubMenuOnCursorKey'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerMenu::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QDesignerMenu::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerMenu::~QDesignerMenu()': the destructor: Python never
    removes a C++ QDesignerMenu.
  - Qt's 'ActionDragCheck QDesignerMenu::checkAction(QAction *action) const':
    gives the enum 'QDesignerMenu::ActionDragCheck', whose class cannot be
    named here.
  - Qt's 'void QDesignerMenu::leaveEditMode(LeaveEditMode mode)': names the
    enum 'QDesignerMenu::LeaveEditMode', whose class cannot be named here.

  What has no ritual
  ------------------

  2 of the 72 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerMenu is created at the first use, not by
    'QDesignerMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMenu.
  - Qt tells when it has removed the C++ QDesignerMenu. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerMenu that has no cute function yet,
    'checkAction', 'leaveEditMode', holds a function that raises
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
    Calls Qt's 'QString QDesignerMenu::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#tr

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
    #  QString QDesignerMenu::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QDesignerMenu2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QPainter, QRect)
  @overload(NoneType, QRect)
  def drawSelection(p: Optional[QPainter], r: QRect) -> None:
    """
    Calls Qt's 'void QDesignerMenu::drawSelection(QPainter *p, const QRect
    &r)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#drawSelection

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    r : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QDesignerMenu::drawSelection(QPainter *p, const QRect &r)
    Rituals.call(
        'ritual_ZN13QDesignerMenu13drawSelectionEP8QPainterRK5QRect',
        CuteMixin._addressOf(p), CuteMixin._valueOf(r),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMenu'

  #  A C++ QDesignerMenu Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMenu'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerMenu::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerMenu::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QDesignerMenu10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface *QDesignerMenu::formWindow()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface *QDesignerMenu::formWindow() const
    address = self.uglySide.call('ritual_ZNK13QDesignerMenu10formWindowEv')
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def parentMenu(self) -> Optional[QDesignerMenu]:
    """
    Calls Qt's 'QDesignerMenu *QDesignerMenu::parentMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#parentMenu

    Returns
    -------

    Optional[QDesignerMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMenu *QDesignerMenu::parentMenu() const
    address = self.uglySide.call('ritual_ZNK13QDesignerMenu10parentMenuEv')
    return QDesignerMenu._cuteAt(address)

  def parentMenuBar(self) -> Optional[QDesignerMenuBar]:
    """
    Calls Qt's 'QDesignerMenuBar *QDesignerMenu::parentMenuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#parentMenuBar

    Returns
    -------

    Optional[QDesignerMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMenuBar *QDesignerMenu::parentMenuBar() const
    address = self.uglySide.call(
        'ritual_ZNK13QDesignerMenu13parentMenuBarEv',
    )
    from . import QDesignerMenuBar
    return QDesignerMenuBar._cuteAt(address)

  def dragging(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::dragging() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#dragging
    """
    #  bool QDesignerMenu::dragging() const
    return self.uglySide.call('ritual_ZNK13QDesignerMenu8draggingEv')

  @overload(QPoint)
  def findAction(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QDesignerMenu::findAction(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#findAction

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QDesignerMenu::findAction(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK13QDesignerMenu10findActionERK6QPoint',
        self._valueOf(pos),
    )

  def currentAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerMenu::currentAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#currentAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerMenu::currentAction() const
    address = self.uglySide.call(
        'ritual_ZNK13QDesignerMenu13currentActionEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def realActionCount(self) -> int:
    """
    Calls Qt's 'int QDesignerMenu::realActionCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#realActionCount
    """
    #  int QDesignerMenu::realActionCount() const
    return self.uglySide.call('ritual_ZNK13QDesignerMenu15realActionCountEv')

  @overload(int)
  def safeActionAt(self, index: int) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerMenu::safeActionAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#safeActionAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerMenu::safeActionAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13QDesignerMenu12safeActionAtEi', index,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def safeMenuAction(
      self,
      menu: Optional[QDesignerMenu],
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerMenu::safeMenuAction(QDesignerMenu *menu)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#safeMenuAction

    Parameters
    ----------

    menu : Optional[QDesignerMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerMenu::safeMenuAction(QDesignerMenu *menu) const
    address = self.uglySide.call(
        'ritual_ZNK13QDesignerMenu14safeMenuActionEPS_',
        self._addressOf(menu),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def canCreateSubMenu(self, action: Optional[QAction]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::canCreateSubMenu(QAction *action) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#canCreateSubMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::canCreateSubMenu(QAction *action) const
    return self.uglySide.call(
        'ritual_ZNK13QDesignerMenu16canCreateSubMenuEP7QAction',
        self._addressOf(action),
    )

  def findRootMenu(self) -> Optional[QDesignerMenu]:
    """
    Calls Qt's 'QDesignerMenu *QDesignerMenu::findRootMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#findRootMenu

    Returns
    -------

    Optional[QDesignerMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMenu *QDesignerMenu::findRootMenu() const
    address = self.uglySide.call('ritual_ZNK13QDesignerMenu12findRootMenuEv')
    return QDesignerMenu._cuteAt(address)

  def findActivatedMenu(self) -> Optional[QDesignerMenu]:
    """
    Calls Qt's 'QDesignerMenu *QDesignerMenu::findActivatedMenu() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#findActivatedMenu

    Returns
    -------

    Optional[QDesignerMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMenu *QDesignerMenu::findActivatedMenu() const
    address = self.uglySide.call(
        'ritual_ZNK13QDesignerMenu17findActivatedMenuEv',
    )
    return QDesignerMenu._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def subMenuPixmapRect(self, action: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect QDesignerMenu::subMenuPixmapRect(QAction *action)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#subMenuPixmapRect

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDesignerMenu::subMenuPixmapRect(QAction *action) const
    address = self.uglySide.call(
        'ritual_ZNK13QDesignerMenu17subMenuPixmapRectEP7QAction',
        self._addressOf(action),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QAction)
  @overload(NoneType)
  def hasSubMenuPixmap(self, action: Optional[QAction]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::hasSubMenuPixmap(QAction *action) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#hasSubMenuPixmap

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::hasSubMenuPixmap(QAction *action) const
    return self.uglySide.call(
        'ritual_ZNK13QDesignerMenu16hasSubMenuPixmapEP7QAction',
        self._addressOf(action),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QDesignerMenu::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QDesignerMenu::setVisible(bool visible)
    ritual = 'ritual_ZN13QDesignerMenu10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu10setVisibleEb'
    self.uglySide.call(ritual, visible)

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
    Notes what was given, for Qt's 'QDesignerMenu::QDesignerMenu(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#QDesignerMenu

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerMenu::QDesignerMenu(QWidget *parent)
    self._noteCreation(QDesignerMenu, lambda: Rituals.call(
        'ritual_ZN13QDesignerMenuC1EP7QWidget', self._addressOf(parent),
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
  def handleEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#handleEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleEvent(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu11handleEventEP6QEvent',
        self._addressOf(event),
    )

  def deactivateMenu(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::deactivateMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#deactivateMenu
    """
    #  void QDesignerMenu::deactivateMenu()
    self.uglySide.call('ritual_ZN13QDesignerMenu14deactivateMenuEv')

  def actionProvider(self) -> Optional[QDesignerActionProviderExtension]:
    """
    Calls Qt's 'QDesignerActionProviderExtension
    *QDesignerMenu::actionProvider()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#actionProvider

    Returns
    -------

    Optional[QDesignerActionProviderExtension]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerActionProviderExtension *QDesignerMenu::actionProvider()
    address = self.uglySide.call(
        'ritual_ZN13QDesignerMenu14actionProviderEv',
    )
    from . import QDesignerActionProviderExtension
    return QDesignerActionProviderExtension._cuteAt(address)

  def adjustSpecialActions(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::adjustSpecialActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#adjustSpecialActions
    """
    #  void QDesignerMenu::adjustSpecialActions()
    self.uglySide.call('ritual_ZN13QDesignerMenu20adjustSpecialActionsEv')

  @overload(QAction)
  @overload(NoneType)
  def createRealMenuAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::createRealMenuAction(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#createRealMenuAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::createRealMenuAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu20createRealMenuActionEP7QAction',
        self._addressOf(action),
    )

  @overload(QAction)
  @overload(NoneType)
  def removeRealMenu(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::removeRealMenu(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#removeRealMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::removeRealMenu(QAction *action)
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu14removeRealMenuEP7QAction',
        self._addressOf(action),
    )

  def closeMenuChain(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::closeMenuChain()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#closeMenuChain
    """
    #  void QDesignerMenu::closeMenuChain()
    self.uglySide.call('ritual_ZN13QDesignerMenu14closeMenuChainEv')

  def moveLeft(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::moveLeft()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#moveLeft
    """
    #  void QDesignerMenu::moveLeft()
    self.uglySide.call('ritual_ZN13QDesignerMenu8moveLeftEv')

  def moveRight(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::moveRight()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#moveRight
    """
    #  void QDesignerMenu::moveRight()
    self.uglySide.call('ritual_ZN13QDesignerMenu9moveRightEv')

  @overload(bool)
  def moveUp(self, ctrl: bool) -> None:
    """
    Calls Qt's 'void QDesignerMenu::moveUp(bool ctrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#moveUp

    Parameters
    ----------

    ctrl : bool
      Passed on as it is.
    """
    #  void QDesignerMenu::moveUp(bool ctrl)
    self.uglySide.call('ritual_ZN13QDesignerMenu6moveUpEb', ctrl)

  @overload(bool)
  def moveDown(self, ctrl: bool) -> None:
    """
    Calls Qt's 'void QDesignerMenu::moveDown(bool ctrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#moveDown

    Parameters
    ----------

    ctrl : bool
      Passed on as it is.
    """
    #  void QDesignerMenu::moveDown(bool ctrl)
    self.uglySide.call('ritual_ZN13QDesignerMenu8moveDownEb', ctrl)

  @overload(QAction)
  @overload(NoneType)
  def deleteAction(self, a: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::deleteAction(QAction *a)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#deleteAction

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::deleteAction(QAction *a)
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu12deleteActionEP7QAction',
        self._addressOf(a),
    )

  @overload()
  def deleteAction(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::deleteAction()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#deleteAction
    """
    #  void QDesignerMenu::deleteAction()
    self.uglySide.call('ritual_ZN13QDesignerMenu12deleteActionEv')

  def slotAddSeparator(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::slotAddSeparator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#slotAddSeparator
    """
    #  void QDesignerMenu::slotAddSeparator()
    self.uglySide.call('ritual_ZN13QDesignerMenu16slotAddSeparatorEv')

  def slotRemoveSelectedAction(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::slotRemoveSelectedAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#slotRemoveSelectedAction
    """
    #  void QDesignerMenu::slotRemoveSelectedAction()
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu24slotRemoveSelectedActionEv',
    )

  def slotShowSubMenuNow(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::slotShowSubMenuNow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#slotShowSubMenuNow
    """
    #  void QDesignerMenu::slotShowSubMenuNow()
    self.uglySide.call('ritual_ZN13QDesignerMenu18slotShowSubMenuNowEv')

  def slotDeactivateNow(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::slotDeactivateNow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#slotDeactivateNow
    """
    #  void QDesignerMenu::slotDeactivateNow()
    self.uglySide.call('ritual_ZN13QDesignerMenu17slotDeactivateNowEv')

  def slotAdjustSizeNow(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::slotAdjustSizeNow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#slotAdjustSizeNow
    """
    #  void QDesignerMenu::slotAdjustSizeNow()
    self.uglySide.call('ritual_ZN13QDesignerMenu17slotAdjustSizeNowEv')

  def stopInlineEditing(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::stopInlineEditing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#stopInlineEditing
    """
    #  void QDesignerMenu::stopInlineEditing()
    self.uglySide.call('ritual_ZN13QDesignerMenu17stopInlineEditingEv')

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, event: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::actionEvent(QActionEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#actionEvent

    Parameters
    ----------

    event : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::actionEvent(QActionEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu11actionEventEP12QActionEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QDesignerMenu14dragEnterEventEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QDesignerMenu13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::dragLeaveEvent(QDragLeaveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QDesignerMenu14dragLeaveEventEP15QDragLeaveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::showEvent(QShowEvent *event)
    ritual = 'ritual_ZN13QDesignerMenu9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDesignerMenu9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseDoubleClickEvent(
      self,
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleMouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#handleMouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleMouseDoubleClickEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu27handleMouseDoubleClickEventEP11QMouseEve'
        'nt',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMousePressEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleMousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#handleMousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleMousePressEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu21handleMousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseReleaseEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleMouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#handleMouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleMouseReleaseEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu23handleMouseReleaseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseMoveEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleMouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#handleMouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleMouseMoveEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu20handleMouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def handleContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleContextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#handleContextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleContextMenuEvent(QContextMenuEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu22handleContextMenuEventEP17QContextMenuEv'
        'ent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def handleKeyPressEvent(self, event: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::handleKeyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#handleKeyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenu::handleKeyPressEvent(QKeyEvent *event)
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu19handleKeyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QPoint, Qt.KeyboardModifiers)
  def startDrag(self, pos: QPoint, modifiers: Qt.KeyboardModifiers) -> None:
    """
    Calls Qt's 'void QDesignerMenu::startDrag(const QPoint &pos,
    Qt::KeyboardModifiers modifiers)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#startDrag

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QDesignerMenu::startDrag(const QPoint &pos, Qt::KeyboardModifiers
    #      modifiers)
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu9startDragERK6QPoint6QFlagsIN2Qt16Keyboard'
        'ModifierEE',
        self._valueOf(pos), modifiers.value,
    )

  @overload(QPoint)
  def adjustIndicator(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QDesignerMenu::adjustIndicator(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#adjustIndicator

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDesignerMenu::adjustIndicator(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu15adjustIndicatorERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QAction)
  @overload(NoneType)
  def showSubMenu(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerMenu::showSubMenu(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#showSubMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenu::showSubMenu(QAction *action)
    self.uglySide.call(
        'ritual_ZN13QDesignerMenu11showSubMenuEP7QAction',
        self._addressOf(action),
    )

  def enterEditMode(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::enterEditMode()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#enterEditMode
    """
    #  void QDesignerMenu::enterEditMode()
    self.uglySide.call('ritual_ZN13QDesignerMenu13enterEditModeEv')

  def showLineEdit(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::showLineEdit()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#showLineEdit
    """
    #  void QDesignerMenu::showLineEdit()
    self.uglySide.call('ritual_ZN13QDesignerMenu12showLineEditEv')

  @overload(str)
  @overload(str, bool)
  def createAction(
      self,
      text: str,
      separator: bool = False,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerMenu::createAction(const QString &text,
    bool separator)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#createAction

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    separator : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerMenu::createAction(const QString &text, bool
    #      separator)
    address = self.uglySide.call(
        'ritual_ZN13QDesignerMenu12createActionERK7QStringb',
        text, separator,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def findOrCreateSubMenu(
      self,
      action: Optional[QAction],
  ) -> Optional[QDesignerMenu]:
    """
    Calls Qt's 'QDesignerMenu *QDesignerMenu::findOrCreateSubMenu(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#findOrCreateSubMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QDesignerMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerMenu *QDesignerMenu::findOrCreateSubMenu(QAction *action)
    address = self.uglySide.call(
        'ritual_ZN13QDesignerMenu19findOrCreateSubMenuEP7QAction',
        self._addressOf(action),
    )
    return QDesignerMenu._cuteAt(address)

  @overload(int, int)
  def swap(self, a: int, b: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::swap(int a, int b)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#swap

    Parameters
    ----------

    a : int
      Passed on as it is.

    b : int
      Passed on as it is.
    """
    #  bool QDesignerMenu::swap(int a, int b)
    return self.uglySide.call('ritual_ZN13QDesignerMenu4swapEii', a, b)

  def hideSubMenu(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::hideSubMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenu.html#hideSubMenu
    """
    #  void QDesignerMenu::hideSubMenu()
    self.uglySide.call('ritual_ZN13QDesignerMenu11hideSubMenuEv')

  def selectCurrentAction(self) -> None:
    """
    Calls Qt's 'void QDesignerMenu::selectCurrentAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#selectCurrentAction
    """
    #  void QDesignerMenu::selectCurrentAction()
    self.uglySide.call('ritual_ZN13QDesignerMenu19selectCurrentActionEv')

  def hideSubMenuOnCursorKey(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::hideSubMenuOnCursorKey()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#hideSubMenuOnCursorKey
    """
    #  bool QDesignerMenu::hideSubMenuOnCursorKey()
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu22hideSubMenuOnCursorKeyEv',
    )

  def showSubMenuOnCursorKey(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMenu::showSubMenuOnCursorKey()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenu.html#showSubMenuOnCursorKey
    """
    #  bool QDesignerMenu::showSubMenuOnCursorKey()
    return self.uglySide.call(
        'ritual_ZN13QDesignerMenu22showSubMenuOnCursorKeyEv',
    )

  @staticmethod
  def checkAction(*__, **_) -> Never:
    """
    Qt's 'ActionDragCheck QDesignerMenu::checkAction(QAction *action) const':
    gives the enum 'QDesignerMenu::ActionDragCheck', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QDesignerMenu.checkAction' has no cute function yet. Qt's "
        "'ActionDragCheck QDesignerMenu::checkAction(QAction *action) "
        "const': gives the enum 'QDesignerMenu::ActionDragCheck', whose "
        "class cannot be named here.")

  @staticmethod
  def leaveEditMode(*__, **_) -> Never:
    """
    Qt's 'void QDesignerMenu::leaveEditMode(LeaveEditMode mode)': names the
    enum 'QDesignerMenu::LeaveEditMode', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QDesignerMenu.leaveEditMode' has no cute function yet. Qt's 'void "
        "QDesignerMenu::leaveEditMode(LeaveEditMode mode)': names the enum "
        "'QDesignerMenu::LeaveEditMode', whose class cannot be named here.")
