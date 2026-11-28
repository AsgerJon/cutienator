"""
qdesigner_internal::ActionTreeView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ActionTreeView to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from ..QtWidgets import QTreeView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QModelIndex
  from ..QtGui import QAction, QContextMenuEvent, QDragEnterEvent
  from ..QtGui import QDragMoveEvent, QDropEvent, QFocusEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ActionTreeView(QTreeView):
  """
  The cute side of Qt's qdesigner_internal::ActionTreeView: a plain Python
  object standing in front of one C++ qdesigner_internal::ActionTreeView.

  It is built on the cute 'QTreeView', as Qt's
  qdesigner_internal::ActionTreeView is built on Qt's QTreeView, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionTreeView that has a ritual
  and that Python can call so far, 14 names in all: 'metaObject',
  'currentAction', 'filter', 'actionContextMenuRequested',
  'currentActionChanged', 'actionActivated', 'currentChanged',
  'dragEnterEvent', 'dragMoveEvent', 'dropEvent', 'focusInEvent',
  'contextMenuEvent', 'startDrag', 'slotActivated'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ActionTreeView::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::ActionTreeView::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 leans on
  'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionTreeView is created at the first use,
    not by 'qdesigner_internal::ActionTreeView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ActionTreeView.
  - Qt tells when it has removed the C++ qdesigner_internal::ActionTreeView.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ActionTreeView that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ActionTreeView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::ActionTreeView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ActionTreeView::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ActionTreeView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *qdesigner_internal::ActionTreeView::currentAction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ActionTreeView::currentAction() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal14ActionTreeView13currentActionEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::ActionTreeView::ActionTreeView(ActionModel
    *model, QWidget *parent)': leans on
    'qdesigner_internal::ActionTreeView::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ActionTreeView.__init__' has no cute function "
        "yet. Qt's "
        "'qdesigner_internal::ActionTreeView::ActionTreeView(ActionModel "
        "*model, QWidget *parent)': leans on "
        "'qdesigner_internal::ActionTreeView::staticMetaObject', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  @overload(str)
  def filter(self, text: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionTreeView::filter(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html#filter

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::ActionTreeView::filter(const QString &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView6filterERK7QString',
        text,
    )

  @overload(QContextMenuEvent, QAction)
  @overload(QContextMenuEvent, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def actionContextMenuRequested(
      self,
      event: Optional[QContextMenuEvent],
      a1: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::actionContextMenuRequested(
    QContextMenuEvent *event, QAction *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionTreeView::actionContextMenuRequested(
    #      QContextMenuEvent *event, QAction *a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView26actionContextMenuRe'
        'questedEP17QContextMenuEventP7QAction',
        self._addressOf(event), self._addressOf(a1),
    )

  @overload(QAction)
  @overload(NoneType)
  def currentActionChanged(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::currentActionChanged(QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionTreeView::currentActionChanged(QAction
    #      *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView20currentActionChange'
        'dEP7QAction',
        self._addressOf(action),
    )

  @overload(QAction, int)
  @overload(NoneType, int)
  def actionActivated(self, action: Optional[QAction], column: int) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::actionActivated(QAction *action, int
    column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ActionTreeView::actionActivated(QAction
    #      *action, int column)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView15actionActivatedEP7Q'
        'Actioni',
        self._addressOf(action), column,
    )

  @overload(QModelIndex, QModelIndex)
  def currentChanged(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionTreeView::currentChanged(const
    QModelIndex &current, const QModelIndex &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void qdesigner_internal::ActionTreeView::currentChanged(const
    #      QModelIndex &current, const QModelIndex &previous)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView14currentChangedERK11'
        'QModelIndexS3_',
        self._valueOf(current), self._valueOf(previous),
    )

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::dragEnterEvent(QDragEnterEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      qdesigner_internal::ActionTreeView::dragEnterEvent(QDragEnterEvent
    #      *event)
    ritual = (
        'ritual_ZN18qdesigner_internal14ActionTreeView14dragEnterEventEP15Q'
        'DragEnterEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ActionTreeView14dragEnterEven'
          'tEP15QDragEnterEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::dragMoveEvent(QDragMoveEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionTreeView::dragMoveEvent(QDragMoveEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView13dragMoveEventEP14QD'
        'ragMoveEvent',
        self._addressOf(event),
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionTreeView::dropEvent(QDropEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionTreeView::dropEvent(QDropEvent *event)
    ritual = (
        'ritual_ZN18qdesigner_internal14ActionTreeView9dropEventEP10QDropEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ActionTreeView9dropEventEP10Q'
          'DropEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionTreeView::focusInEvent(QFocusEvent
    #      *event)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView12focusInEventEP11QFo'
        'cusEvent',
        self._addressOf(event),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::contextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionTreeView::contextMenuEvent(
    #      QContextMenuEvent *event)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView16contextMenuEventEP1'
        '7QContextMenuEvent',
        self._addressOf(event),
    )

  @overload(Qt.DropActions)
  def startDrag(self, supportedActions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionTreeView::startDrag(Qt::DropActions
    supportedActions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html#startDrag

    Parameters
    ----------

    supportedActions : Qt.DropActions
      Passed on as its number.
    """
    #  void qdesigner_internal::ActionTreeView::startDrag(Qt::DropActions
    #      supportedActions)
    ritual = (
        'ritual_ZN18qdesigner_internal14ActionTreeView9startDragE6QFlagsIN2'
        'Qt10DropActionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal14ActionTreeView9startDragE6QFl'
          'agsIN2Qt10DropActionEE')
    self.uglySide.call(ritual, supportedActions.value)

  @overload(QModelIndex)
  def slotActivated(self, a0: QModelIndex) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionTreeView::slotActivated(const
    QModelIndex &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actiontreeview.html

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void qdesigner_internal::ActionTreeView::slotActivated(const
    #      QModelIndex &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal14ActionTreeView13slotActivatedERK11Q'
        'ModelIndex',
        self._valueOf(a0),
    )
