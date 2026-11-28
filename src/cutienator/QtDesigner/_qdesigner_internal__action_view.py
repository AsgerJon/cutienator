"""
qdesigner_internal::ActionView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ActionView to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from ..QtWidgets import QAbstractItemView, QStackedWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QItemSelection, QMetaObject, QModelIndex
  from ..QtGui import QAction, QContextMenuEvent
  from . import QDesignerFormEditorInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDesignerFormEditorInterface = WAIT['QDesignerFormEditorInterface']
  QItemSelection = WAIT['QItemSelection']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ActionView(QStackedWidget):
  """
  The cute side of Qt's qdesigner_internal::ActionView: a plain Python object
  standing in front of one C++ qdesigner_internal::ActionView.

  It is built on the cute 'QStackedWidget', as Qt's
  qdesigner_internal::ActionView is built on Qt's QStackedWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionView that has a ritual and
  that Python can call so far, 21 names in all: 'metaObject', 'initialize',
  'viewMode', 'setViewMode', 'setSelectionMode', 'selectionMode', 'model',
  'currentAction', 'setCurrentIndex', 'selectedActions', 'selection',
  'filter', 'selectAll', 'clearSelection', 'selectAction',
  'contextMenuRequested', 'currentActionChanged', 'activated',
  'selectionChanged', 'resourceImageDropped', 'slotCurrentChanged'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ActionView::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::ActionView::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 leans on
  'qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionView is created at the first use, not
    by 'qdesigner_internal::ActionView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ActionView.
  - Qt tells when it has removed the C++ qdesigner_internal::ActionView.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::ActionView that has no cute
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
  __qt_class__ = 'qdesigner_internal::ActionView'

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
    *qdesigner_internal::ActionView::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ActionView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def viewMode(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::ActionView::viewMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#viewMode
    """
    #  int qdesigner_internal::ActionView::viewMode() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView8viewModeEv',
    )

  def selectionMode(self) -> QAbstractItemView.SelectionMode:
    """
    Calls Qt's 'QAbstractItemView::SelectionMode
    qdesigner_internal::ActionView::selectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#selectionMode

    Returns
    -------

    QAbstractItemView.SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAbstractItemView.SelectionMode(number)' gives.
    """
    #  QAbstractItemView::SelectionMode
    #      qdesigner_internal::ActionView::selectionMode() const
    return QAbstractItemView.SelectionMode(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView13selectionModeEv',
    ))

  def model(self) -> Optional[qdesigner_internal.ActionModel]:
    """
    Calls Qt's 'ActionModel *qdesigner_internal::ActionView::model() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#model

    Returns
    -------

    Optional[qdesigner_internal.ActionModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ActionModel *qdesigner_internal::ActionView::model() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView5modelEv',
    )
    return qdesigner_internal.ActionModel._cuteAt(address)

  def currentAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *qdesigner_internal::ActionView::currentAction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#currentAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ActionView::currentAction() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView13currentActionEv',
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def selectedActions(self) -> QList[QAction]:
    """
    Calls Qt's 'ActionList qdesigner_internal::ActionView::selectedActions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#selectedActions

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  ActionList qdesigner_internal::ActionView::selectedActions() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView15selectedActionsEv',
    )
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  def selection(self) -> QItemSelection:
    """
    Calls Qt's 'QItemSelection qdesigner_internal::ActionView::selection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#selection

    Returns
    -------

    QItemSelection
      A new cute QItemSelection around the copy Qt gave back. Python owns it.
    """
    #  QItemSelection qdesigner_internal::ActionView::selection() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal10ActionView9selectionEv',
    )
    from ..QtCore import QItemSelection
    return QItemSelection._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setViewMode(self, lm: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::setViewMode(int lm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#setViewMode

    Parameters
    ----------

    lm : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ActionView::setViewMode(int lm)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView11setViewModeEi', lm,
    )

  @overload(QAbstractItemView.SelectionMode)
  def setSelectionMode(self, sm: QAbstractItemView.SelectionMode) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionView::setSelectionMode(QAbstractItemView::
    SelectionMode sm)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html

    Parameters
    ----------

    sm : QAbstractItemView.SelectionMode
      Passed on as its number.
    """
    #  void qdesigner_internal::ActionView::setSelectionMode(
    #      QAbstractItemView::SelectionMode sm)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView16setSelectionModeEN17QAb'
        'stractItemView13SelectionModeE',
        sm.value,
    )

  @overload(QModelIndex)
  def setCurrentIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::setCurrentIndex(const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#setCurrentIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void qdesigner_internal::ActionView::setCurrentIndex(const QModelIndex
    #      &index)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView15setCurrentIndexERK11QMo'
        'delIndex',
        self._valueOf(index),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::ActionView::ActionView(QWidget *parent)': leans
    on 'qdesigner_internal::ActionView::selectionChanged(QItemSelection
    const&, QItemSelection const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.ActionView.__init__' has no cute function yet. "
        "Qt's 'qdesigner_internal::ActionView::ActionView(QWidget "
        "*parent)': leans on "
        "'qdesigner_internal::ActionView::selectionChanged(QItemSelection "
        "const&, QItemSelection const&)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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

  @overload(QDesignerFormEditorInterface)
  @overload(NoneType)
  def initialize(self, core: Optional[QDesignerFormEditorInterface]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionView::initialize(QDesignerFormEditorInterface
    *core)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#initialize

    Parameters
    ----------

    core : Optional[QDesignerFormEditorInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionView::initialize(
    #      QDesignerFormEditorInterface *core)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView10initializeEP28QDesigner'
        'FormEditorInterface',
        self._addressOf(core),
    )

  @overload(str)
  def filter(self, text: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::filter(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#filter

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::ActionView::filter(const QString &text)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView6filterERK7QString', text,
    )

  def selectAll(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::selectAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#selectAll
    """
    #  void qdesigner_internal::ActionView::selectAll()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView9selectAllEv',
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#clearSelection
    """
    #  void qdesigner_internal::ActionView::clearSelection()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView14clearSelectionEv',
    )

  @overload(QAction)
  @overload(NoneType)
  def selectAction(self, a: Optional[QAction]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::selectAction(QAction
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#selectAction

    Parameters
    ----------

    a : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionView::selectAction(QAction *a)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView12selectActionEP7QAction',
        self._addressOf(a),
    )

  @overload(QContextMenuEvent, QAction)
  @overload(QContextMenuEvent, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def contextMenuRequested(
      self,
      event: Optional[QContextMenuEvent],
      a1: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionView::contextMenuRequested(QContextMenuEvent
    *event, QAction *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionView::contextMenuRequested(
    #      QContextMenuEvent *event, QAction *a1)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView20contextMenuRequestedEP1'
        '7QContextMenuEventP7QAction',
        self._addressOf(event), self._addressOf(a1),
    )

  @overload(QAction)
  @overload(NoneType)
  def currentActionChanged(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionView::currentActionChanged(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionView::currentActionChanged(QAction
    #      *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView20currentActionChangedEP7'
        'QAction',
        self._addressOf(action),
    )

  @overload(QAction, int)
  @overload(NoneType, int)
  def activated(self, action: Optional[QAction], column: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::activated(QAction
    *action, int column)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html#activated

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    column : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ActionView::activated(QAction *action, int
    #      column)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView9activatedEP7QActioni',
        self._addressOf(action), column,
    )

  @overload(QItemSelection, QItemSelection)
  def selectionChanged(
      self,
      selected: QItemSelection,
      deselected: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ActionView::selectionChanged(const
    QItemSelection &selected, const QItemSelection &deselected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html

    Parameters
    ----------

    selected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    deselected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void qdesigner_internal::ActionView::selectionChanged(const
    #      QItemSelection &selected, const QItemSelection &deselected)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView16selectionChangedERK14QI'
        'temSelectionS3_',
        self._valueOf(selected), self._valueOf(deselected),
    )

  @overload(str, QAction)
  @overload(str, NoneType)
  def resourceImageDropped(
      self,
      data: str,
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionView::resourceImageDropped(const QString &data,
    QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionView::resourceImageDropped(const
    #      QString &data, QAction *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView20resourceImageDroppedERK'
        '7QStringP7QAction',
        data, self._addressOf(action),
    )

  @overload(QAction)
  @overload(NoneType)
  def slotCurrentChanged(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionView::slotCurrentChanged(QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionview.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionView::slotCurrentChanged(QAction
    #      *action)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal10ActionView18slotCurrentChangedEP7QA'
        'ction',
        self._addressOf(action),
    )
