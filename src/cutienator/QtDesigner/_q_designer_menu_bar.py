"""
QDesignerMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_menubar_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerMenuBar to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QMenuBar, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint
  from ..QtGui import QAction, QActionEvent, QContextMenuEvent
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QFocusEvent, QKeyEvent, QMouseEvent
  from ..QtGui import QPaintEvent
  from . import QDesignerActionProviderExtension
  from . import QDesignerFormWindowInterface
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
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerMenuBar(QMenuBar):
  """
  The cute side of Qt's QDesignerMenuBar: a plain Python object standing in
  front of one C++ QDesignerMenuBar.

  It is built on the cute 'QMenuBar', as Qt's QDesignerMenuBar is built on
  Qt's QMenuBar, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerMenuBar that has a ritual and that Python
  can call so far, 45 names in all: 'metaObject', 'tr', 'handleEvent',
  'formWindow', 'actionProvider', 'adjustSpecialActions', 'dragging',
  'moveLeft', 'moveRight', 'moveUp', 'moveDown', 'contextMenuActions',
  'deleteMenuAction', 'deleteMenu', 'slotRemoveMenuBar', 'stopInlineEditing',
  'actionEvent', 'dragEnterEvent', 'dragMoveEvent', 'dragLeaveEvent',
  'dropEvent', 'paintEvent', 'focusOutEvent', 'keyPressEvent',
  'keyReleaseEvent', 'handleMouseDoubleClickEvent', 'handleMousePressEvent',
  'handleMouseReleaseEvent', 'handleMouseMoveEvent',
  'handleContextMenuEvent', 'handleKeyPressEvent', 'startDrag',
  'adjustIndicator', 'findAction', 'currentAction', 'realActionCount',
  'enterEditMode', 'showLineEdit', 'showMenu', 'hideMenu', 'safeActionAt',
  'swapActions', 'updateCurrentAction', 'movePrevious', 'moveNext'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerMenuBar::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDesignerMenuBar::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDesignerMenuBar::~QDesignerMenuBar()': the destructor: Python
    never removes a C++ QDesignerMenuBar.
  - Qt's 'ActionDragCheck QDesignerMenuBar::checkAction(QAction *action)
    const': gives the enum 'QDesignerMenuBar::ActionDragCheck', whose class
    cannot be named here.
  - Qt's 'void QDesignerMenuBar::leaveEditMode(LeaveEditMode mode)': names
    the enum 'QDesignerMenuBar::LeaveEditMode', whose class cannot be named
    here.

  What has no ritual
  ------------------

  2 of the 53 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerMenuBar is created at the first use, not by
    'QDesignerMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerMenuBar.
  - Qt tells when it has removed the C++ QDesignerMenuBar. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDesignerMenuBar that has no cute function yet,
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
    Calls Qt's 'QString QDesignerMenuBar::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#tr

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
    #  QString QDesignerMenuBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QDesignerMenuBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerMenuBar'

  #  A C++ QDesignerMenuBar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerMenuBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDesignerMenuBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerMenuBar::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QDesignerMenuBar10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface *QDesignerMenuBar::formWindow()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface *QDesignerMenuBar::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK16QDesignerMenuBar10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def dragging(self) -> bool:
    """
    Calls Qt's 'bool QDesignerMenuBar::dragging() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#dragging
    """
    #  bool QDesignerMenuBar::dragging() const
    return self.uglySide.call('ritual_ZNK16QDesignerMenuBar8draggingEv')

  @overload(QPoint)
  def findAction(self, pos: QPoint) -> int:
    """
    Calls Qt's 'int QDesignerMenuBar::findAction(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#findAction

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  int QDesignerMenuBar::findAction(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK16QDesignerMenuBar10findActionERK6QPoint',
        self._valueOf(pos),
    )

  def currentAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerMenuBar::currentAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#currentAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerMenuBar::currentAction() const
    address = self.uglySide.call(
        'ritual_ZNK16QDesignerMenuBar13currentActionEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def realActionCount(self) -> int:
    """
    Calls Qt's 'int QDesignerMenuBar::realActionCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#realActionCount
    """
    #  int QDesignerMenuBar::realActionCount() const
    return self.uglySide.call(
        'ritual_ZNK16QDesignerMenuBar15realActionCountEv',
    )

  @overload(int)
  def safeActionAt(self, index: int) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerMenuBar::safeActionAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#safeActionAt

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
    #  QAction *QDesignerMenuBar::safeActionAt(int index) const
    address = self.uglySide.call(
        'ritual_ZNK16QDesignerMenuBar12safeActionAtEi', index,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'QDesignerMenuBar::QDesignerMenuBar(QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#QDesignerMenuBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerMenuBar::QDesignerMenuBar(QWidget *parent)
    self._noteCreation(QDesignerMenuBar, lambda: Rituals.call(
        'ritual_ZN16QDesignerMenuBarC1EP7QWidget', self._addressOf(parent),
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
    Calls Qt's 'bool QDesignerMenuBar::handleEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#handleEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleEvent(QEvent *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar11handleEventEP6QEvent',
        self._addressOf(event),
    )

  def actionProvider(self) -> Optional[QDesignerActionProviderExtension]:
    """
    Calls Qt's 'QDesignerActionProviderExtension
    *QDesignerMenuBar::actionProvider()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#actionProvider

    Returns
    -------

    Optional[QDesignerActionProviderExtension]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerActionProviderExtension *QDesignerMenuBar::actionProvider()
    address = self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar14actionProviderEv',
    )
    from . import QDesignerActionProviderExtension
    return QDesignerActionProviderExtension._cuteAt(address)

  def adjustSpecialActions(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::adjustSpecialActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#adjustSpecialActions
    """
    #  void QDesignerMenuBar::adjustSpecialActions()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar20adjustSpecialActionsEv')

  @overload()
  @overload(bool)
  def moveLeft(self, ctrl: bool = False) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::moveLeft(bool ctrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#moveLeft

    Parameters
    ----------

    ctrl : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDesignerMenuBar::moveLeft(bool ctrl)
    self.uglySide.call('ritual_ZN16QDesignerMenuBar8moveLeftEb', ctrl)

  @overload()
  @overload(bool)
  def moveRight(self, ctrl: bool = False) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::moveRight(bool ctrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#moveRight

    Parameters
    ----------

    ctrl : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDesignerMenuBar::moveRight(bool ctrl)
    self.uglySide.call('ritual_ZN16QDesignerMenuBar9moveRightEb', ctrl)

  def moveUp(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::moveUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#moveUp
    """
    #  void QDesignerMenuBar::moveUp()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar6moveUpEv')

  def moveDown(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::moveDown()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#moveDown
    """
    #  void QDesignerMenuBar::moveDown()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar8moveDownEv')

  def contextMenuActions(self) -> QList[QAction]:
    """
    Calls Qt's 'QList<QAction *> QDesignerMenuBar::contextMenuActions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#contextMenuActions

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAction *> QDesignerMenuBar::contextMenuActions()
    address = self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar18contextMenuActionsEv',
    )
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  @overload(QAction)
  @overload(NoneType)
  def deleteMenuAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::deleteMenuAction(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#deleteMenuAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::deleteMenuAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar16deleteMenuActionEP7QAction',
        self._addressOf(action),
    )

  def deleteMenu(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::deleteMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#deleteMenu
    """
    #  void QDesignerMenuBar::deleteMenu()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar10deleteMenuEv')

  def slotRemoveMenuBar(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::slotRemoveMenuBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#slotRemoveMenuBar
    """
    #  void QDesignerMenuBar::slotRemoveMenuBar()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar17slotRemoveMenuBarEv')

  def stopInlineEditing(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::stopInlineEditing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#stopInlineEditing
    """
    #  void QDesignerMenuBar::stopInlineEditing()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar17stopInlineEditingEv')

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, event: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::actionEvent(QActionEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#actionEvent

    Parameters
    ----------

    event : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::actionEvent(QActionEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDesignerMenuBar11actionEventEP12QActionEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::dragEnterEvent(QDragEnterEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::dragEnterEvent(QDragEnterEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar14dragEnterEventEP15QDragEnterEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QDesignerMenuBar14dragEnterEventEP15QDragEnterEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::dragMoveEvent(QDragMoveEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QDesignerMenuBar13dragMoveEventEP14QDragMoveEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::dragLeaveEvent(QDragLeaveEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar14dragLeaveEventEP15QDragLeaveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QDesignerMenuBar14dragLeaveEventEP15QDragLeaveEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDesignerMenuBar9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDesignerMenuBar10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::focusOutEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QDesignerMenuBar13focusOutEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDesignerMenuBar13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::keyReleaseEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDesignerMenuBar::keyReleaseEvent(QKeyEvent *event)
    ritual = 'ritual_ZN16QDesignerMenuBar15keyReleaseEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDesignerMenuBar15keyReleaseEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseDoubleClickEvent(
      self,
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDesignerMenuBar::handleMouseDoubleClickEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#handleMouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleMouseDoubleClickEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar27handleMouseDoubleClickEventEP11QMouse'
        'Event',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMousePressEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenuBar::handleMousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#handleMousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleMousePressEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar21handleMousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseReleaseEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenuBar::handleMouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#handleMouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleMouseReleaseEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar23handleMouseReleaseEventEP11QMouseEven'
        't',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseMoveEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenuBar::handleMouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#handleMouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleMouseMoveEvent(QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar20handleMouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def handleContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDesignerMenuBar::handleContextMenuEvent(QContextMenuEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#handleContextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleContextMenuEvent(QContextMenuEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar22handleContextMenuEventEP17QContextMen'
        'uEvent',
        self._addressOf(event),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def handleKeyPressEvent(self, event: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QDesignerMenuBar::handleKeyPressEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#handleKeyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDesignerMenuBar::handleKeyPressEvent(QKeyEvent *event)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar19handleKeyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QPoint)
  def startDrag(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::startDrag(const QPoint &pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#startDrag

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDesignerMenuBar::startDrag(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar9startDragERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QPoint)
  def adjustIndicator(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::adjustIndicator(const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#adjustIndicator

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDesignerMenuBar::adjustIndicator(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar15adjustIndicatorERK6QPoint',
        self._valueOf(pos),
    )

  def enterEditMode(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::enterEditMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#enterEditMode
    """
    #  void QDesignerMenuBar::enterEditMode()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar13enterEditModeEv')

  def showLineEdit(self) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::showLineEdit()'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#showLineEdit
    """
    #  void QDesignerMenuBar::showLineEdit()
    self.uglySide.call('ritual_ZN16QDesignerMenuBar12showLineEditEv')

  @overload()
  @overload(int)
  def showMenu(self, index: int = -1) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::showMenu(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#showMenu

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QDesignerMenuBar::showMenu(int index)
    self.uglySide.call('ritual_ZN16QDesignerMenuBar8showMenuEi', index)

  @overload()
  @overload(int)
  def hideMenu(self, index: int = -1) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::hideMenu(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#hideMenu

    Parameters
    ----------

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QDesignerMenuBar::hideMenu(int index)
    self.uglySide.call('ritual_ZN16QDesignerMenuBar8hideMenuEi', index)

  @overload(int, int)
  def swapActions(self, a: int, b: int) -> bool:
    """
    Calls Qt's 'bool QDesignerMenuBar::swapActions(int a, int b)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#swapActions

    Parameters
    ----------

    a : int
      Passed on as it is.

    b : int
      Passed on as it is.
    """
    #  bool QDesignerMenuBar::swapActions(int a, int b)
    return self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar11swapActionsEii', a, b,
    )

  @overload(bool)
  def updateCurrentAction(self, selectAction: bool) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::updateCurrentAction(bool
    selectAction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignermenubar.html#updateCurrentAction

    Parameters
    ----------

    selectAction : bool
      Passed on as it is.
    """
    #  void QDesignerMenuBar::updateCurrentAction(bool selectAction)
    self.uglySide.call(
        'ritual_ZN16QDesignerMenuBar19updateCurrentActionEb', selectAction,
    )

  @overload(bool)
  def movePrevious(self, ctrl: bool) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::movePrevious(bool ctrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#movePrevious

    Parameters
    ----------

    ctrl : bool
      Passed on as it is.
    """
    #  void QDesignerMenuBar::movePrevious(bool ctrl)
    self.uglySide.call('ritual_ZN16QDesignerMenuBar12movePreviousEb', ctrl)

  @overload(bool)
  def moveNext(self, ctrl: bool) -> None:
    """
    Calls Qt's 'void QDesignerMenuBar::moveNext(bool ctrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qdesignermenubar.html#moveNext

    Parameters
    ----------

    ctrl : bool
      Passed on as it is.
    """
    #  void QDesignerMenuBar::moveNext(bool ctrl)
    self.uglySide.call('ritual_ZN16QDesignerMenuBar8moveNextEb', ctrl)

  @staticmethod
  def checkAction(*__, **_) -> Never:
    """
    Qt's 'ActionDragCheck QDesignerMenuBar::checkAction(QAction *action)
    const': gives the enum 'QDesignerMenuBar::ActionDragCheck', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QDesignerMenuBar.checkAction' has no cute function yet. Qt's "
        "'ActionDragCheck QDesignerMenuBar::checkAction(QAction *action) "
        "const': gives the enum 'QDesignerMenuBar::ActionDragCheck', whose "
        "class cannot be named here.")

  @staticmethod
  def leaveEditMode(*__, **_) -> Never:
    """
    Qt's 'void QDesignerMenuBar::leaveEditMode(LeaveEditMode mode)': names
    the enum 'QDesignerMenuBar::LeaveEditMode', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QDesignerMenuBar.leaveEditMode' has no cute function yet. Qt's "
        "'void QDesignerMenuBar::leaveEditMode(LeaveEditMode mode)': names "
        "the enum 'QDesignerMenuBar::LeaveEditMode', whose class cannot be "
        "named here.")
