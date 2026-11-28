"""
QAbstractItemViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractItemViewPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QItemSelectionModel, QList
from . import QAbstractItemView, QAbstractScrollAreaPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QModelIndex, QPersistentModelIndex, QPoint
  from ..QtCore import QRect
  from ..QtGui import QDropEvent, QPainter, QPixmap, QRegion
  from . import QAbstractItemDelegate, QEditorInfo, QItemViewPaintPair
  from . import QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemDelegate = WAIT['QAbstractItemDelegate']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QPersistentModelIndex = WAIT['QPersistentModelIndex']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemViewPrivate(QAbstractScrollAreaPrivate):
  """
  The cute side of Qt's QAbstractItemViewPrivate: a plain Python object
  standing in front of one C++ QAbstractItemViewPrivate.

  It is built on the cute 'QAbstractScrollAreaPrivate', as Qt's
  QAbstractItemViewPrivate is built on Qt's QAbstractScrollAreaPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemViewPrivate that has a ritual and that
  Python can call so far, 71 names in all: 'q_func', 'init', 'rowsRemoved',
  'rowsInserted', 'columnsAboutToBeRemoved', 'columnsRemoved',
  'columnsInserted', 'modelDestroyed', 'layoutChanged', 'rowsMoved',
  'columnsMoved', 'intersectedRect', 'headerDataChanged',
  'scrollerStateChanged', 'fetchMore', 'shouldEdit', 'shouldForwardEvent',
  'shouldAutoScroll', 'doDelayedItemsLayout', 'interruptDelayedItemsLayout',
  'updateGeometry', 'startAutoScroll', 'stopAutoScroll', 'droppingOnItself',
  'editor', 'sendDelegateEvent', 'openEditor', 'updateEditorData',
  'selectAllInEditor', 'multiSelectionCommand', 'extendedSelectionCommand',
  'contiguousSelectionCommand', 'selectAll', 'setHoverIndex',
  'checkMouseMove', 'selectionBehaviorFlags', 'canDrop',
  'paintDropIndicator', 'draggablePaintPairs', 'adjustViewOptionsForIndex',
  'releaseEditor', 'executePostedLayout', 'setDirtyRegion',
  'scrollDirtyRegion', 'scrollContentsBy', 'updateDirtyRegion',
  'clearOrRemove', 'checkPersistentEditorFocus', 'renderToPixmap', 'offset',
  'editorForIndex', 'hasEditor', 'indexForEditor', 'addEditor',
  'removeEditor', 'isAnimating', 'isIndexValid', 'isIndexSelectable',
  'isIndexEnabled', 'isIndexDropEnabled', 'isIndexDragEnabled',
  'selectionAllowed', 'accessibleChildIndex', 'contentsOffset',
  'delegateRefCount', 'isPersistent', 'selectedDraggableIndexes',
  'maybeStartDrag', 'doDelayedReset', 'visualRect', 'delegateForIndex'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractItemView *QAbstractItemViewPrivate::q_func() const':
    takes in Python what 'QAbstractItemView
    *QAbstractItemViewPrivate::q_func()' takes.
  - Qt's 'QAbstractItemViewPrivate::~QAbstractItemViewPrivate()': the
    destructor: Python never removes a C++ QAbstractItemViewPrivate.
  - Qt's 'bool QAbstractItemViewPrivate::dropOn(QDropEvent *event, int *row,
    int *col, QModelIndex *index)': takes a number to change where it is.
  - Qt's 'QAbstractItemView::DropIndicatorPosition
    QAbstractItemViewPrivate::position(const QPoint &pos, const QRect &rect,
    const QModelIndex &idx) const': gives the enum
    'QAbstractItemView::DropIndicatorPosition', whose class cannot be named
    here.
  - Qt's 'void QAbstractItemViewPrivate::updateItemAccessibility(const
    QModelIndex &index, const QList<int> &roles)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  5 of the 82 functions Qt declares: 4 leans on 'QAbstractItemViewPrivate; 1
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file.

  What to expect
  --------------

  - The C++ QAbstractItemViewPrivate is created at the first use, not by
    'QAbstractItemViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemViewPrivate.
  - Each name of Qt's QAbstractItemViewPrivate that has no cute function yet,
    '__init__', 'connectDelegate', 'delegateSizeHintChanged',
    'disconnectAll', 'disconnectDelegate', 'dropOn', 'position',
    'updateItemAccessibility', holds a function that raises
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
  __qt_class__ = 'QAbstractItemViewPrivate'

  #  A C++ QAbstractItemViewPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemViewPrivate'

  #  The functions Qt calls itself that QAbstractItemViewPrivate is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dropOn': (
          'bool QAbstractItemViewPrivate::dropOn(QDropEvent *, int *, int '
          '*, QModelIndex *)',
      ),
      'position': (
          'QAbstractItemView::DropIndicatorPosition '
          'QAbstractItemViewPrivate::position(const QPoint &, const QRect '
          '&, const QModelIndex &) const',
      ),
      'draggablePaintPairs': (
          'QItemViewPaintPairs '
          'QAbstractItemViewPrivate::draggablePaintPairs(const '
          'QModelIndexList &, QRect *) const',
      ),
  }

  #  The functions Qt calls itself that QAbstractItemViewPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'rowsRemoved': (
          ('_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'rowsInserted': (
          ('_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'columnsAboutToBeRemoved': (
          ('_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QMod'
           'elIndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'columnsRemoved': (
          ('_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'columnsInserted': (
          ('_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexi'
           'i',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'modelDestroyed': (
          ('_ZN24QAbstractItemViewPrivate14modelDestroyedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'layoutChanged': (
          ('_ZN24QAbstractItemViewPrivate13layoutChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'rowsMoved': (
          ('_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'columnsMoved': (
          ('_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2'
           '_i',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
           )),
      ),
      'intersectedRect': (
          ('_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QMode'
           'lIndexS3_',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'selectAll': (
          ('_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelecti'
           'onModel13SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:QItemSelectionModel.SelectionFlag'),
           )),
      ),
      'adjustViewOptionsForIndex': (
          ('_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QS'
           'tyleOptionViewItemRK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionViewItem'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'selectionAllowed': (
          ('_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelInde'
           'x',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'accessibleChildIndex': (
          ('_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModel'
           'Index',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'visualRect': (
          ('_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelIndex',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
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

  @overload(QRect, QModelIndex, QModelIndex)
  def intersectedRect(
      self,
      rect: QRect,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> QRect:
    """
    Calls Qt's 'QRect QAbstractItemViewPrivate::intersectedRect(const QRect
    rect, const QModelIndex &topLeft, const QModelIndex &bottomRight) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#intersectedRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAbstractItemViewPrivate::intersectedRect(const QRect rect,
    #      const QModelIndex &topLeft, const QModelIndex &bottomRight) const
    ritual = (
        'ritual_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QM'
        'odelIndexS3_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRect'
          'RK11QModelIndexS3_')
    address = self.uglySide.call(
        ritual,
        self._valueOf(rect), self._valueOf(topLeft),
        self._valueOf(bottomRight),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QAbstractItemView.EditTrigger, QModelIndex)
  def shouldEdit(
      self,
      trigger: QAbstractItemView.EditTrigger,
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractItemViewPrivate::shouldEdit(QAbstractItemView::EditTrigger
    trigger, const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#shouldEdit

    Parameters
    ----------

    trigger : QAbstractItemView.EditTrigger
      Passed on as its number.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::shouldEdit(QAbstractItemView::
    #      EditTrigger trigger, const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate10shouldEditEN17QAbstractItemV'
        'iew11EditTriggerERK11QModelIndex',
        trigger.value, self._valueOf(index),
    )

  @overload(QAbstractItemView.EditTrigger, QEvent)
  @overload(QAbstractItemView.EditTrigger, NoneType)
  def shouldForwardEvent(
      self,
      trigger: QAbstractItemView.EditTrigger,
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QAbstractItemViewPrivate::shouldForwardEvent(QAbstractItemView::
    EditTrigger trigger, const QEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#shouldForwardEvent

    Parameters
    ----------

    trigger : QAbstractItemView.EditTrigger
      Passed on as its number.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemViewPrivate::shouldForwardEvent(QAbstractItemView::
    #      EditTrigger trigger, const QEvent *event) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate18shouldForwardEventEN17QAbstr'
        'actItemView11EditTriggerEPK6QEvent',
        trigger.value, self._addressOf(event),
    )

  @overload(QPoint)
  def shouldAutoScroll(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::shouldAutoScroll(const QPoint
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#shouldAutoScroll

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QAbstractItemViewPrivate::shouldAutoScroll(const QPoint &pos)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate16shouldAutoScrollERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QModelIndex, QEvent)
  @overload(QModelIndex, NoneType)
  def sendDelegateEvent(
      self,
      index: QModelIndex,
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::sendDelegateEvent(const
    QModelIndex &index, QEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#sendDelegateEvent

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemViewPrivate::sendDelegateEvent(const QModelIndex
    #      &index, QEvent *event) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate17sendDelegateEventERK11QModel'
        'IndexP6QEvent',
        self._valueOf(index), self._addressOf(event),
    )

  @overload(QModelIndex, QEvent)
  @overload(QModelIndex, NoneType)
  def multiSelectionCommand(
      self,
      index: QModelIndex,
      event: Optional[QEvent],
  ) -> QItemSelectionModel.SelectionFlags:
    """
    Calls Qt's 'QItemSelectionModel::SelectionFlags
    QAbstractItemViewPrivate::multiSelectionCommand(const QModelIndex &index,
    const QEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QItemSelectionModel.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QItemSelectionModel::SelectionFlags
    #      QAbstractItemViewPrivate::multiSelectionCommand(const QModelIndex
    #      &index, const QEvent *event) const
    return QItemSelectionModel.SelectionFlags(self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate21multiSelectionCommandERK11QM'
        'odelIndexPK6QEvent',
        self._valueOf(index), self._addressOf(event),
    ))

  @overload(QModelIndex, QEvent)
  @overload(QModelIndex, NoneType)
  def extendedSelectionCommand(
      self,
      index: QModelIndex,
      event: Optional[QEvent],
  ) -> QItemSelectionModel.SelectionFlags:
    """
    Calls Qt's 'QItemSelectionModel::SelectionFlags
    QAbstractItemViewPrivate::extendedSelectionCommand(const QModelIndex
    &index, const QEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QItemSelectionModel.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QItemSelectionModel::SelectionFlags
    #      QAbstractItemViewPrivate::extendedSelectionCommand(const
    #      QModelIndex &index, const QEvent *event) const
    return QItemSelectionModel.SelectionFlags(self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate24extendedSelectionCommandERK1'
        '1QModelIndexPK6QEvent',
        self._valueOf(index), self._addressOf(event),
    ))

  @overload(QModelIndex, QEvent)
  @overload(QModelIndex, NoneType)
  def contiguousSelectionCommand(
      self,
      index: QModelIndex,
      event: Optional[QEvent],
  ) -> QItemSelectionModel.SelectionFlags:
    """
    Calls Qt's 'QItemSelectionModel::SelectionFlags
    QAbstractItemViewPrivate::contiguousSelectionCommand(const QModelIndex
    &index, const QEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QItemSelectionModel.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QItemSelectionModel::SelectionFlags
    #      QAbstractItemViewPrivate::contiguousSelectionCommand(const
    #      QModelIndex &index, const QEvent *event) const
    return QItemSelectionModel.SelectionFlags(self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate26contiguousSelectionCommandER'
        'K11QModelIndexPK6QEvent',
        self._valueOf(index), self._addressOf(event),
    ))

  def selectionBehaviorFlags(self) -> QItemSelectionModel.SelectionFlags:
    """
    Calls Qt's 'QItemSelectionModel::SelectionFlags
    QAbstractItemViewPrivate::selectionBehaviorFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Returns
    -------

    QItemSelectionModel.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QItemSelectionModel::SelectionFlags
    #      QAbstractItemViewPrivate::selectionBehaviorFlags() const
    return QItemSelectionModel.SelectionFlags(self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate22selectionBehaviorFlagsEv',
    ))

  @overload(QList[QModelIndex], QRect)
  @overload(QList[QModelIndex], NoneType)
  def draggablePaintPairs(
      self,
      indexes: QList[QModelIndex],
      r: Optional[QRect],
  ) -> QList[QItemViewPaintPair]:
    """
    Calls Qt's 'QItemViewPaintPairs
    QAbstractItemViewPrivate::draggablePaintPairs(const QModelIndexList
    &indexes, QRect *r) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#draggablePaintPairs

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    r : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QItemViewPaintPair]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QItemViewPaintPairs
    #      QAbstractItemViewPrivate::draggablePaintPairs(const
    #      QModelIndexList &indexes, QRect *r) const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate19draggablePaintPairsERK5QList'
        'I11QModelIndexEP5QRect',
        self._valueOf(indexes), self._addressOf(r),
    )
    from . import QItemViewPaintPair
    return QList[QItemViewPaintPair]._cuteOwning(address)

  @overload(QList[QModelIndex], QRect)
  @overload(QList[QModelIndex], NoneType)
  def renderToPixmap(
      self,
      indexes: QList[QModelIndex],
      r: Optional[QRect],
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QAbstractItemViewPrivate::renderToPixmap(const
    QModelIndexList &indexes, QRect *r) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#renderToPixmap

    Parameters
    ----------

    indexes : QList[QModelIndex]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    r : Optional[QRect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QAbstractItemViewPrivate::renderToPixmap(const QModelIndexList
    #      &indexes, QRect *r) const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate14renderToPixmapERK5QListI11QM'
        'odelIndexEP5QRect',
        self._valueOf(indexes), self._addressOf(r),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def offset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAbstractItemViewPrivate::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#offset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAbstractItemViewPrivate::offset() const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate6offsetEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QModelIndex)
  def editorForIndex(self, index: QModelIndex) -> QEditorInfo:
    """
    Calls Qt's 'const QEditorInfo
    &QAbstractItemViewPrivate::editorForIndex(const QModelIndex &index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#editorForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QEditorInfo
      A new cute QEditorInfo around the copy Qt gave back. Python owns it.
    """
    #  const QEditorInfo &QAbstractItemViewPrivate::editorForIndex(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate14editorForIndexERK11QModelInd'
        'ex',
        self._valueOf(index),
    )
    from . import QEditorInfo
    return QEditorInfo._cuteOwning(address)

  @overload(QModelIndex)
  def hasEditor(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::hasEditor(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#hasEditor

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::hasEditor(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate9hasEditorERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QWidget)
  @overload(NoneType)
  def indexForEditor(self, editor: Optional[QWidget]) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemViewPrivate::indexForEditor(QWidget
    *editor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#indexForEditor

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemViewPrivate::indexForEditor(QWidget *editor)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate14indexForEditorEP7QWidget',
        self._addressOf(editor),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def isAnimating(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isAnimating() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isAnimating
    """
    #  bool QAbstractItemViewPrivate::isAnimating() const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate11isAnimatingEv',
    )

  @overload(QModelIndex)
  def isIndexValid(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isIndexValid(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isIndexValid

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::isIndexValid(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate12isIndexValidERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def isIndexSelectable(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isIndexSelectable(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isIndexSelectable

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::isIndexSelectable(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate17isIndexSelectableERK11QModel'
        'Index',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def isIndexEnabled(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isIndexEnabled(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isIndexEnabled

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::isIndexEnabled(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate14isIndexEnabledERK11QModelInd'
        'ex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def isIndexDropEnabled(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isIndexDropEnabled(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isIndexDropEnabled

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::isIndexDropEnabled(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate18isIndexDropEnabledERK11QMode'
        'lIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def isIndexDragEnabled(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isIndexDragEnabled(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isIndexDragEnabled

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::isIndexDragEnabled(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate18isIndexDragEnabledERK11QMode'
        'lIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def selectionAllowed(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::selectionAllowed(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#selectionAllowed

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::selectionAllowed(const QModelIndex
    #      &index) const
    ritual = (
        'ritual_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelI'
        'ndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11Q'
          'ModelIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

  @overload(QModelIndex)
  def accessibleChildIndex(self, index: QModelIndex) -> int:
    """
    Calls Qt's 'int QAbstractItemViewPrivate::accessibleChildIndex(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#accessibleChildIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QAbstractItemViewPrivate::accessibleChildIndex(const QModelIndex
    #      &index) const
    ritual = (
        'ritual_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QMo'
        'delIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractItemViewPrivate20accessibleChildIndexER'
          'K11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(index))

  def contentsOffset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAbstractItemViewPrivate::contentsOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#contentsOffset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAbstractItemViewPrivate::contentsOffset() const
    ritual = 'ritual_ZNK24QAbstractItemViewPrivate14contentsOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QAbstractItemViewPrivate14contentsOffsetEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  @overload(QAbstractItemDelegate)
  @overload(NoneType)
  def delegateRefCount(
      self,
      delegate: Optional[QAbstractItemDelegate],
  ) -> int:
    """
    Calls Qt's 'int QAbstractItemViewPrivate::delegateRefCount(const
    QAbstractItemDelegate *delegate) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#delegateRefCount

    Parameters
    ----------

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QAbstractItemViewPrivate::delegateRefCount(const
    #      QAbstractItemDelegate *delegate) const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate16delegateRefCountEPK21QAbstra'
        'ctItemDelegate',
        self._addressOf(delegate),
    )

  @overload(QModelIndex)
  def isPersistent(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::isPersistent(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#isPersistent

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::isPersistent(const QModelIndex &index)
    #      const
    return self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate12isPersistentERK11QModelIndex',
        self._valueOf(index),
    )

  def selectedDraggableIndexes(self) -> QList[QModelIndex]:
    """
    Calls Qt's 'QModelIndexList
    QAbstractItemViewPrivate::selectedDraggableIndexes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QModelIndexList QAbstractItemViewPrivate::selectedDraggableIndexes()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate24selectedDraggableIndexesEv',
    )
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QAbstractItemViewPrivate::visualRect(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#visualRect

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QAbstractItemViewPrivate::visualRect(const QModelIndex &index)
    #      const
    ritual = (
        'ritual_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelI'
          'ndex')
    address = self.uglySide.call(ritual, self._valueOf(index))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QModelIndex)
  def delegateForIndex(
      self,
      index: QModelIndex,
  ) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate
    *QAbstractItemViewPrivate::delegateForIndex(const QModelIndex &index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#delegateForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate
    #      *QAbstractItemViewPrivate::delegateForIndex(const QModelIndex
    #      &index) const
    address = self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate16delegateForIndexERK11QModelI'
        'ndex',
        self._valueOf(index),
    )
    from . import QAbstractItemDelegate
    return QAbstractItemDelegate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPersistentModelIndex)
  def setHoverIndex(self, index: QPersistentModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::setHoverIndex(const
    QPersistentModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#setHoverIndex

    Parameters
    ----------

    index : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.
    """
    #  void QAbstractItemViewPrivate::setHoverIndex(const
    #      QPersistentModelIndex &index)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate13setHoverIndexERK21QPersistent'
        'ModelIndex',
        self._valueOf(index),
    )

  @overload(QRegion)
  def setDirtyRegion(self, visualRegion: QRegion) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::setDirtyRegion(const QRegion
    &visualRegion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#setDirtyRegion

    Parameters
    ----------

    visualRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QAbstractItemViewPrivate::setDirtyRegion(const QRegion
    #      &visualRegion)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14setDirtyRegionERK7QRegion',
        self._valueOf(visualRegion),
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
    Qt's 'QAbstractItemViewPrivate::QAbstractItemViewPrivate()': leans on
    'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex const&,
    int, int)', which Qt's source does not mark for use from outside Qt and
    has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.__init__' has no cute function yet. Qt's "
        "'QAbstractItemViewPrivate::QAbstractItemViewPrivate()': leans on "
        "'QAbstractItemViewPrivate::columnsAboutToBeRemoved(QModelIndex "
        "const&, int, int)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QAbstractItemView]:
    """
    Calls Qt's 'QAbstractItemView *QAbstractItemViewPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#q_func

    Returns
    -------

    Optional[QAbstractItemView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemView *QAbstractItemViewPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate6q_funcEv',
    )
    return QAbstractItemView._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemviewprivate.html#init
    """
    #  void QAbstractItemViewPrivate::init()
    self.uglySide.call('ritual_ZN24QAbstractItemViewPrivate4initEv')

  @overload(QModelIndex, int, int)
  def rowsRemoved(self, parent: QModelIndex, start: int, end: int) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#rowsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent,
    #      int start, int end)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelI'
          'ndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int)
  def rowsInserted(self, parent: QModelIndex, start: int, end: int) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::rowsInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#rowsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::rowsInserted(const QModelIndex &parent,
    #      int start, int end)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexi'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModel'
          'Indexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int)
  def columnsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::columnsAboutToBeRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::columnsAboutToBeRemoved(const
    #      QModelIndex &parent, int start, int end)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11Q'
        'ModelIndexii',
        self._valueOf(parent), start, end,
    )

  @overload(QModelIndex, int, int)
  def columnsRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::columnsRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#columnsRemoved

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::columnsRemoved(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelInde'
        'xii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QMod'
          'elIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int)
  def columnsInserted(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::columnsInserted(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#columnsInserted

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    start : int
      Passed on as it is.

    end : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::columnsInserted(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelInd'
        'exii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QMo'
          'delIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  def modelDestroyed(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::modelDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#modelDestroyed
    """
    #  void QAbstractItemViewPrivate::modelDestroyed()
    ritual = 'ritual_ZN24QAbstractItemViewPrivate14modelDestroyedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QAbstractItemViewPrivate14modelDestroyedEv'
    self.uglySide.call(ritual)

  def layoutChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::layoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#layoutChanged
    """
    #  void QAbstractItemViewPrivate::layoutChanged()
    ritual = 'ritual_ZN24QAbstractItemViewPrivate13layoutChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QAbstractItemViewPrivate13layoutChangedEv'
    self.uglySide.call(ritual)

  @overload(QModelIndex, int, int, QModelIndex, int)
  def rowsMoved(
      self,
      source: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destination: QModelIndex,
      destinationStart: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::rowsMoved(const QModelIndex
    &source, int sourceStart, int sourceEnd, const QModelIndex &destination,
    int destinationStart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#rowsMoved

    Parameters
    ----------

    source : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destination : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationStart : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::rowsMoved(const QModelIndex &source,
    #      int sourceStart, int sourceEnd, const QModelIndex &destination,
    #      int destinationStart)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_'
        'i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelInde'
          'xiiS2_i')
    self.uglySide.call(
        ritual,
        self._valueOf(source), sourceStart, sourceEnd,
        self._valueOf(destination), destinationStart,
    )

  @overload(QModelIndex, int, int, QModelIndex, int)
  def columnsMoved(
      self,
      source: QModelIndex,
      sourceStart: int,
      sourceEnd: int,
      destination: QModelIndex,
      destinationStart: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::columnsMoved(const QModelIndex
    &source, int sourceStart, int sourceEnd, const QModelIndex &destination,
    int destinationStart)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#columnsMoved

    Parameters
    ----------

    source : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    sourceStart : int
      Passed on as it is.

    sourceEnd : int
      Passed on as it is.

    destination : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    destinationStart : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::columnsMoved(const QModelIndex &source,
    #      int sourceStart, int sourceEnd, const QModelIndex &destination,
    #      int destinationStart)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexi'
        'iS2_i')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModel'
          'IndexiiS2_i')
    self.uglySide.call(
        ritual,
        self._valueOf(source), sourceStart, sourceEnd,
        self._valueOf(destination), destinationStart,
    )

  def headerDataChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::headerDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#headerDataChanged
    """
    #  void QAbstractItemViewPrivate::headerDataChanged()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate17headerDataChangedEv',
    )

  def scrollerStateChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::scrollerStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#scrollerStateChanged
    """
    #  void QAbstractItemViewPrivate::scrollerStateChanged()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate20scrollerStateChangedEv',
    )

  def fetchMore(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::fetchMore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#fetchMore
    """
    #  void QAbstractItemViewPrivate::fetchMore()
    self.uglySide.call('ritual_ZN24QAbstractItemViewPrivate9fetchMoreEv')

  @overload()
  @overload(int)
  def doDelayedItemsLayout(self, delay: int = 0) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::doDelayedItemsLayout(int
    delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#doDelayedItemsLayout

    Parameters
    ----------

    delay : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QAbstractItemViewPrivate::doDelayedItemsLayout(int delay)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate20doDelayedItemsLayoutEi', delay,
    )

  def interruptDelayedItemsLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::interruptDelayedItemsLayout()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html
    """
    #  void QAbstractItemViewPrivate::interruptDelayedItemsLayout() const
    self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate27interruptDelayedItemsLayoutE'
        'v',
    )

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#updateGeometry
    """
    #  void QAbstractItemViewPrivate::updateGeometry()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14updateGeometryEv',
    )

  def startAutoScroll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::startAutoScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#startAutoScroll
    """
    #  void QAbstractItemViewPrivate::startAutoScroll()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate15startAutoScrollEv',
    )

  def stopAutoScroll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::stopAutoScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#stopAutoScroll
    """
    #  void QAbstractItemViewPrivate::stopAutoScroll()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14stopAutoScrollEv',
    )

  @overload(QDropEvent, QModelIndex)
  @overload(NoneType, QModelIndex)
  def droppingOnItself(
      self,
      event: Optional[QDropEvent],
      index: QModelIndex,
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::droppingOnItself(QDropEvent
    *event, const QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#droppingOnItself

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemViewPrivate::droppingOnItself(QDropEvent *event,
    #      const QModelIndex &index)
    return self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate16droppingOnItselfEP10QDropEven'
        'tRK11QModelIndex',
        self._addressOf(event), self._valueOf(index),
    )

  @overload(QModelIndex, QStyleOptionViewItem)
  def editor(
      self,
      index: QModelIndex,
      options: QStyleOptionViewItem,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractItemViewPrivate::editor(const QModelIndex
    &index, const QStyleOptionViewItem &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#editor

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    options : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractItemViewPrivate::editor(const QModelIndex &index,
    #      const QStyleOptionViewItem &options)
    address = self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate6editorERK11QModelIndexRK20QSty'
        'leOptionViewItem',
        self._valueOf(index), self._valueOf(options),
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  @overload(QModelIndex, QEvent)
  @overload(QModelIndex, NoneType)
  def openEditor(self, index: QModelIndex, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::openEditor(const QModelIndex
    &index, QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#openEditor

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemViewPrivate::openEditor(const QModelIndex &index,
    #      QEvent *event)
    return self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate10openEditorERK11QModelIndexP6Q'
        'Event',
        self._valueOf(index), self._addressOf(event),
    )

  @overload(QModelIndex, QModelIndex)
  def updateEditorData(
      self,
      topLeft: QModelIndex,
      bottomRight: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::updateEditorData(const
    QModelIndex &topLeft, const QModelIndex &bottomRight)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#updateEditorData

    Parameters
    ----------

    topLeft : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    bottomRight : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemViewPrivate::updateEditorData(const QModelIndex
    #      &topLeft, const QModelIndex &bottomRight)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate16updateEditorDataERK11QModelIn'
        'dexS2_',
        self._valueOf(topLeft), self._valueOf(bottomRight),
    )

  @overload(QWidget)
  @overload(NoneType)
  def selectAllInEditor(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::selectAllInEditor(QWidget
    *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#selectAllInEditor

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemViewPrivate::selectAllInEditor(QWidget *w)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate17selectAllInEditorEP7QWidget',
        self._addressOf(w),
    )

  @overload(QItemSelectionModel.SelectionFlags)
  def selectAll(self, command: QItemSelectionModel.SelectionFlags) -> None:
    """
    Calls Qt's 'void
    QAbstractItemViewPrivate::selectAll(QItemSelectionModel::SelectionFlags
    command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#selectAll

    Parameters
    ----------

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QAbstractItemViewPrivate::selectAll(QItemSelectionModel::
    #      SelectionFlags command)
    ritual = (
        'ritual_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSele'
        'ctionModel13SelectionFlagEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QIt'
          'emSelectionModel13SelectionFlagEE')
    self.uglySide.call(ritual, command.value)

  @overload(QPersistentModelIndex)
  def checkMouseMove(self, index: QPersistentModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::checkMouseMove(const
    QPersistentModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#checkMouseMove

    Parameters
    ----------

    index : QPersistentModelIndex
      Passed on as a value: Qt reads the C++ QPersistentModelIndex, which
      stays Python's own.
    """
    #  void QAbstractItemViewPrivate::checkMouseMove(const
    #      QPersistentModelIndex &index)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14checkMouseMoveERK21QPersisten'
        'tModelIndex',
        self._valueOf(index),
    )

  @overload(QPoint)
  def checkMouseMove(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::checkMouseMove(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#checkMouseMove

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstractItemViewPrivate::checkMouseMove(const QPoint &pos)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14checkMouseMoveERK6QPoint',
        self._valueOf(pos),
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def canDrop(self, event: Optional[QDropEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractItemViewPrivate::canDrop(QDropEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#canDrop

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemViewPrivate::canDrop(QDropEvent *event)
    return self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate7canDropEP10QDropEvent',
        self._addressOf(event),
    )

  @overload(QPainter)
  @overload(NoneType)
  def paintDropIndicator(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::paintDropIndicator(QPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#paintDropIndicator

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemViewPrivate::paintDropIndicator(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate18paintDropIndicatorEP8QPainter',
        self._addressOf(painter),
    )

  @overload(QStyleOptionViewItem, QModelIndex)
  @overload(NoneType, QModelIndex)
  def adjustViewOptionsForIndex(
      self,
      a0: Optional[QStyleOptionViewItem],
      a1: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewItem
    *a0, const QModelIndex &a1) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html

    Parameters
    ----------

    a0 : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemViewPrivate::adjustViewOptionsForIndex(
    #      QStyleOptionViewItem *a0, const QModelIndex &a1) const
    ritual = (
        'ritual_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP2'
        '0QStyleOptionViewItemRK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIn'
          'dexEP20QStyleOptionViewItemRK11QModelIndex')
    self.uglySide.call(ritual, self._addressOf(a0), self._valueOf(a1))

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, QModelIndex)
  @overload(NoneType, QModelIndex)
  def releaseEditor(
      self,
      editor: Optional[QWidget],
      index: Optional[QModelIndex] = None,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::releaseEditor(QWidget *editor,
    const QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#releaseEditor

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  void QAbstractItemViewPrivate::releaseEditor(QWidget *editor, const
    #      QModelIndex &index) const
    if index is None:
      from ..QtCore import QModelIndex
      index = QModelIndex()
    self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate13releaseEditorEP7QWidgetRK11Q'
        'ModelIndex',
        self._addressOf(editor), self._valueOf(index),
    )

  def executePostedLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::executePostedLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#executePostedLayout
    """
    #  void QAbstractItemViewPrivate::executePostedLayout() const
    self.uglySide.call(
        'ritual_ZNK24QAbstractItemViewPrivate19executePostedLayoutEv',
    )

  @overload(int, int)
  def scrollDirtyRegion(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::scrollDirtyRegion(int dx, int
    dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#scrollDirtyRegion

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::scrollDirtyRegion(int dx, int dy)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate17scrollDirtyRegionEii', dx, dy,
    )

  @overload(int, int)
  def scrollContentsBy(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::scrollContentsBy(int dx, int
    dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::scrollContentsBy(int dx, int dy)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate16scrollContentsByEii', dx, dy,
    )

  def updateDirtyRegion(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::updateDirtyRegion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#updateDirtyRegion
    """
    #  void QAbstractItemViewPrivate::updateDirtyRegion()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate17updateDirtyRegionEv',
    )

  def clearOrRemove(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::clearOrRemove()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#clearOrRemove
    """
    #  void QAbstractItemViewPrivate::clearOrRemove()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate13clearOrRemoveEv',
    )

  def checkPersistentEditorFocus(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::checkPersistentEditorFocus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html
    """
    #  void QAbstractItemViewPrivate::checkPersistentEditorFocus()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate26checkPersistentEditorFocusEv',
    )

  @overload(QModelIndex, QWidget, bool)
  @overload(QModelIndex, NoneType, bool)
  def addEditor(
      self,
      index: QModelIndex,
      editor: Optional[QWidget],
      isStatic: bool,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::addEditor(const QModelIndex
    &index, QWidget *editor, bool isStatic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#addEditor

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isStatic : bool
      Passed on as it is.
    """
    #  void QAbstractItemViewPrivate::addEditor(const QModelIndex &index,
    #      QWidget *editor, bool isStatic)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate9addEditorERK11QModelIndexP7QWi'
        'dgetb',
        self._valueOf(index), self._addressOf(editor), isStatic,
    )

  @overload(QWidget)
  @overload(NoneType)
  def removeEditor(self, editor: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::removeEditor(QWidget
    *editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#removeEditor

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemViewPrivate::removeEditor(QWidget *editor)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate12removeEditorEP7QWidget',
        self._addressOf(editor),
    )

  @overload(QPoint)
  def maybeStartDrag(self, eventPoint: QPoint) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::maybeStartDrag(QPoint
    eventPoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#maybeStartDrag

    Parameters
    ----------

    eventPoint : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QAbstractItemViewPrivate::maybeStartDrag(QPoint eventPoint)
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14maybeStartDragE6QPoint',
        self._valueOf(eventPoint),
    )

  def doDelayedReset(self) -> None:
    """
    Calls Qt's 'void QAbstractItemViewPrivate::doDelayedReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemviewprivate.html#doDelayedReset
    """
    #  void QAbstractItemViewPrivate::doDelayedReset()
    self.uglySide.call(
        'ritual_ZN24QAbstractItemViewPrivate14doDelayedResetEv',
    )

  @staticmethod
  def connectDelegate(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemViewPrivate::connectDelegate(QAbstractItemDelegate
    *delegate)': leans on
    'QAbstractItemViewPrivate::delegateSizeHintChanged(QModelIndex const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.connectDelegate' has no cute function "
        "yet. Qt's 'void "
        "QAbstractItemViewPrivate::connectDelegate(QAbstractItemDelegate "
        "*delegate)': leans on "
        "'QAbstractItemViewPrivate::delegateSizeHintChanged(QModelIndex "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def delegateSizeHintChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemViewPrivate::delegateSizeHintChanged(const
    QModelIndex &index)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'lcAIV'.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.delegateSizeHintChanged' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemViewPrivate::delegateSizeHintChanged(const "
        "QModelIndex &index)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'lcAIV'.")

  @staticmethod
  def disconnectAll(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemViewPrivate::disconnectAll()': leans on
    'QAbstractItemViewPrivate::delegateSizeHintChanged(QModelIndex const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.disconnectAll' has no cute function yet. "
        "Qt's 'void QAbstractItemViewPrivate::disconnectAll()': leans on "
        "'QAbstractItemViewPrivate::delegateSizeHintChanged(QModelIndex "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def disconnectDelegate(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractItemViewPrivate::disconnectDelegate(QAbstractItemDelegate
    *delegate)': leans on
    'QAbstractItemViewPrivate::delegateSizeHintChanged(QModelIndex const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.disconnectDelegate' has no cute function "
        "yet. Qt's 'void "
        "QAbstractItemViewPrivate::disconnectDelegate(QAbstractItemDelegate "
        "*delegate)': leans on "
        "'QAbstractItemViewPrivate::delegateSizeHintChanged(QModelIndex "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def dropOn(*__, **_) -> Never:
    """
    Qt's 'bool QAbstractItemViewPrivate::dropOn(QDropEvent *event, int *row,
    int *col, QModelIndex *index)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.dropOn' has no cute function yet. Qt's "
        "'bool QAbstractItemViewPrivate::dropOn(QDropEvent *event, int "
        "*row, int *col, QModelIndex *index)': takes a number to change "
        "where it is.")

  @staticmethod
  def position(*__, **_) -> Never:
    """
    Qt's 'QAbstractItemView::DropIndicatorPosition
    QAbstractItemViewPrivate::position(const QPoint &pos, const QRect &rect,
    const QModelIndex &idx) const': gives the enum
    'QAbstractItemView::DropIndicatorPosition', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.position' has no cute function yet. Qt's "
        "'QAbstractItemView::DropIndicatorPosition "
        "QAbstractItemViewPrivate::position(const QPoint &pos, const QRect "
        "&rect, const QModelIndex &idx) const': gives the enum "
        "'QAbstractItemView::DropIndicatorPosition', whose class cannot be "
        "named here.")

  @staticmethod
  def updateItemAccessibility(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemViewPrivate::updateItemAccessibility(const
    QModelIndex &index, const QList<int> &roles)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemViewPrivate.updateItemAccessibility' has no cute "
        "function yet. Qt's 'void "
        "QAbstractItemViewPrivate::updateItemAccessibility(const "
        "QModelIndex &index, const QList<int> &roles)': takes a type Python "
        "has no way to hand over yet.")
