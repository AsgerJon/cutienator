"""
QAbstractItemView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qabstractitemview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QItemSelectionModel, QList, QObject
from . import QAbstractItemDelegate, QAbstractScrollArea, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QAbstractItemModel, QEvent, QItemSelection
  from ..QtCore import QMetaObject, QModelIndex, QPoint, QRect, QSize
  from ..QtCore import QTimerEvent, QVariant
  from ..QtGui import QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent
  from ..QtGui import QDropEvent, QFocusEvent, QInputMethodEvent, QKeyEvent
  from ..QtGui import QMouseEvent, QRegion, QResizeEvent
  from . import QAbstractItemViewPrivate, QStyleOptionViewItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QInputMethodEvent = WAIT['QInputMethodEvent']
  QItemSelection = WAIT['QItemSelection']
  QKeyEvent = WAIT['QKeyEvent']
  QModelIndex = WAIT['QModelIndex']
  QMouseEvent = WAIT['QMouseEvent']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QResizeEvent = WAIT['QResizeEvent']
  QSize = WAIT['QSize']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractItemView(QAbstractScrollArea):
  """
  The cute side of Qt's QAbstractItemView: a plain Python object standing in
  front of one C++ QAbstractItemView.

  It is built on the cute 'QAbstractScrollArea', as Qt's QAbstractItemView is
  built on Qt's QAbstractScrollArea, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractItemView that has a ritual and that Python
  can call so far, 134 names in all: 'metaObject', 'tr', 'setModel', 'model',
  'setSelectionModel', 'selectionModel', 'setItemDelegate', 'itemDelegate',
  'setSelectionMode', 'selectionMode', 'setSelectionBehavior',
  'selectionBehavior', 'currentIndex', 'rootIndex', 'setEditTriggers',
  'editTriggers', 'setVerticalScrollMode', 'verticalScrollMode',
  'resetVerticalScrollMode', 'setHorizontalScrollMode',
  'horizontalScrollMode', 'resetHorizontalScrollMode', 'setAutoScroll',
  'hasAutoScroll', 'setAutoScrollMargin', 'autoScrollMargin',
  'setTabKeyNavigation', 'tabKeyNavigation', 'setDropIndicatorShown',
  'showDropIndicator', 'setDragEnabled', 'dragEnabled',
  'setDragDropOverwriteMode', 'dragDropOverwriteMode', 'setDragDropMode',
  'dragDropMode', 'setDefaultDropAction', 'defaultDropAction',
  'setAlternatingRowColors', 'alternatingRowColors', 'setIconSize',
  'iconSize', 'setTextElideMode', 'textElideMode', 'keyboardSearch',
  'visualRect', 'scrollTo', 'indexAt', 'sizeHintForIndex', 'sizeHintForRow',
  'sizeHintForColumn', 'updateThreshold', 'setUpdateThreshold',
  'keyboardSearchFlags', 'setKeyboardSearchFlags', 'openPersistentEditor',
  'closePersistentEditor', 'isPersistentEditorOpen', 'setIndexWidget',
  'indexWidget', 'setItemDelegateForRow', 'itemDelegateForRow',
  'setItemDelegateForColumn', 'itemDelegateForColumn',
  'itemDelegateForIndex', 'inputMethodQuery', 'reset', 'setRootIndex',
  'doItemsLayout', 'selectAll', 'edit', 'clearSelection', 'setCurrentIndex',
  'scrollToTop', 'scrollToBottom', 'update', 'rowsInserted',
  'rowsAboutToBeRemoved', 'selectionChanged', 'currentChanged',
  'updateEditorData', 'updateEditorGeometries', 'updateGeometries',
  'verticalScrollbarAction', 'horizontalScrollbarAction',
  'verticalScrollbarValueChanged', 'horizontalScrollbarValueChanged',
  'closeEditor', 'commitData', 'editorDestroyed', 'pressed', 'clicked',
  'doubleClicked', 'activated', 'entered', 'viewportEntered',
  'iconSizeChanged', 'horizontalOffset', 'verticalOffset', 'isIndexHidden',
  'setSelection', 'visualRegionForSelection', 'selectedIndexes',
  'selectionCommand', 'startDrag', 'initViewItemOption',
  'scheduleDelayedItemsLayout', 'executeDelayedItemsLayout',
  'setDirtyRegion', 'scrollDirtyRegion', 'dirtyRegionOffset',
  'startAutoScroll', 'stopAutoScroll', 'doAutoScroll', 'focusNextPrevChild',
  'event', 'viewportEvent', 'mousePressEvent', 'mouseMoveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'dragEnterEvent',
  'dragMoveEvent', 'dragLeaveEvent', 'dropEvent', 'focusInEvent',
  'focusOutEvent', 'keyPressEvent', 'resizeEvent', 'timerEvent',
  'inputMethodEvent', 'eventFilter', 'viewportSizeHint', 'd_func'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractItemView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractItemView::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractItemView::~QAbstractItemView()': the destructor: Python
    never removes a C++ QAbstractItemView.
  - Qt's 'void QAbstractItemView::dataChanged(const QModelIndex &topLeft,
    const QModelIndex &bottomRight, const QList<int> &roles)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QModelIndex QAbstractItemView::moveCursor(CursorAction
    cursorAction, Qt::KeyboardModifiers modifiers)': names the enum
    'QAbstractItemView::CursorAction', whose class cannot be named here.
  - Qt's 'State QAbstractItemView::state() const': gives the enum
    'QAbstractItemView::State', whose class cannot be named here.
  - Qt's 'void QAbstractItemView::setState(State state)': names the enum
    'QAbstractItemView::State', whose class cannot be named here.
  - Qt's 'DropIndicatorPosition QAbstractItemView::dropIndicatorPosition()
    const': gives the enum 'QAbstractItemView::DropIndicatorPosition', whose
    class cannot be named here.
  - Qt's 'const QAbstractItemViewPrivate *QAbstractItemView::d_func() const':
    takes in Python what 'QAbstractItemViewPrivate
    *QAbstractItemView::d_func()' takes.

  What has no ritual
  ------------------

  6 of the 151 functions Qt declares: 2 not a gap; 2 the class is abstract,
  so C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractItemView is created at the first use, not by
    'QAbstractItemView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractItemView.
  - Qt tells when it has removed the C++ QAbstractItemView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractItemView that has no cute function yet,
    '__init__', 'dataChanged', 'dropIndicatorPosition', 'moveCursor',
    'setState', 'state', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QAbstractItemView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DragDropMode(CuteNum):
    """
    The enum 'QAbstractItemView::DragDropMode' of Qt, with the 5 names Qt
    gives in it.
    """

    NoDragDrop = Kee[int](0)
    DragOnly = Kee[int](1)
    DropOnly = Kee[int](2)
    DragDrop = Kee[int](3)
    InternalMove = Kee[int](4)

  class EditTrigger(CuteFlags):
    """
    The flags enum 'QAbstractItemView::EditTrigger' of Qt, with the 7 names
    Qt gives in it. Qt names the type of its combinations
    'QAbstractItemView::EditTriggers'.
    """

    NoEditTriggers = 0x0
    CurrentChanged = 0x1
    DoubleClicked = 0x2
    SelectedClicked = 0x4
    EditKeyPressed = 0x8
    AnyKeyPressed = 0x10
    AllEditTriggers = 0x1f

  EditTriggers = EditTrigger

  class ScrollHint(CuteNum):
    """
    The enum 'QAbstractItemView::ScrollHint' of Qt, with the 4 names Qt gives
    in it.
    """

    EnsureVisible = Kee[int](0)
    PositionAtTop = Kee[int](1)
    PositionAtBottom = Kee[int](2)
    PositionAtCenter = Kee[int](3)

  class ScrollMode(CuteNum):
    """
    The enum 'QAbstractItemView::ScrollMode' of Qt, with the 2 names Qt gives
    in it.
    """

    ScrollPerItem = Kee[int](0)
    ScrollPerPixel = Kee[int](1)

  class SelectionBehavior(CuteNum):
    """
    The enum 'QAbstractItemView::SelectionBehavior' of Qt, with the 3 names
    Qt gives in it.
    """

    SelectItems = Kee[int](0)
    SelectRows = Kee[int](1)
    SelectColumns = Kee[int](2)

  class SelectionMode(CuteNum):
    """
    The enum 'QAbstractItemView::SelectionMode' of Qt, with the 5 names Qt
    gives in it.
    """

    NoSelection = Kee[int](0)
    SingleSelection = Kee[int](1)
    MultiSelection = Kee[int](2)
    ExtendedSelection = Kee[int](3)
    ContiguousSelection = Kee[int](4)

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
    Calls Qt's 'QString QAbstractItemView::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#tr

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
    #  QString QAbstractItemView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QAbstractItemView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractItemView'

  #  A C++ QAbstractItemView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractItemView'

  #  The functions Qt calls itself that QAbstractItemView is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dataChanged': (
          'void QAbstractItemView::dataChanged(const QModelIndex &, const '
          'QModelIndex &, const QList<int> &)',
      ),
      'moveCursor': (
          'QModelIndex QAbstractItemView::moveCursor(CursorAction, '
          'Qt::KeyboardModifiers)',
      ),
      'selectedIndexes': (
          'QModelIndexList QAbstractItemView::selectedIndexes() const',
      ),
  }

  #  The functions Qt calls itself that QAbstractItemView is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setModel': (
          ('_ZN17QAbstractItemView8setModelEP18QAbstractItemModel',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QAbstractItemModel'),
           )),
      ),
      'setSelectionModel': (
          ('_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionMode'
           'l',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QItemSelectionModel'),
           )),
      ),
      'keyboardSearch': (
          ('_ZN17QAbstractItemView14keyboardSearchERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'visualRect': (
          ('_ZNK17QAbstractItemView10visualRectERK11QModelIndex',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'scrollTo': (
          ('_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHintE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'enum', 'QtWidgets:QAbstractItemView.ScrollHint'),
           )),
      ),
      'indexAt': (
          ('_ZNK17QAbstractItemView7indexAtERK6QPoint',
           ('address', 'value', 'QtCore:QModelIndex'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'sizeHintForRow': (
          ('_ZNK17QAbstractItemView14sizeHintForRowEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'sizeHintForColumn': (
          ('_ZNK17QAbstractItemView17sizeHintForColumnEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'itemDelegateForIndex': (
          ('_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelIndex',
           ('address', 'address', 'QtWidgets:QAbstractItemDelegate'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'reset': (
          ('_ZN17QAbstractItemView5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setRootIndex': (
          ('_ZN17QAbstractItemView12setRootIndexERK11QModelIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'doItemsLayout': (
          ('_ZN17QAbstractItemView13doItemsLayoutEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'selectAll': (
          ('_ZN17QAbstractItemView9selectAllEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'rowsInserted': (
          ('_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'rowsAboutToBeRemoved': (
          ('_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndexii',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'selectionChanged': (
          ('_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QItemSelection'),
               ('address', 'value', 'QtCore:QItemSelection'),
           )),
      ),
      'currentChanged': (
          ('_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'updateEditorData': (
          ('_ZN17QAbstractItemView16updateEditorDataEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateEditorGeometries': (
          ('_ZN17QAbstractItemView22updateEditorGeometriesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateGeometries': (
          ('_ZN17QAbstractItemView16updateGeometriesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'verticalScrollbarAction': (
          ('_ZN17QAbstractItemView23verticalScrollbarActionEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'horizontalScrollbarAction': (
          ('_ZN17QAbstractItemView25horizontalScrollbarActionEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'verticalScrollbarValueChanged': (
          ('_ZN17QAbstractItemView29verticalScrollbarValueChangedEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'horizontalScrollbarValueChanged': (
          ('_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'closeEditor': (
          ('_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractItemDe'
           'legate11EndEditHintE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
               ('int', 'enum',
                'QtWidgets:QAbstractItemDelegate.EndEditHint'),
           )),
      ),
      'commitData': (
          ('_ZN17QAbstractItemView10commitDataEP7QWidget',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QWidget'),
           )),
      ),
      'editorDestroyed': (
          ('_ZN17QAbstractItemView15editorDestroyedEP7QObject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'horizontalOffset': (
          ('_ZNK17QAbstractItemView16horizontalOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'verticalOffset': (
          ('_ZNK17QAbstractItemView14verticalOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'isIndexHidden': (
          ('_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'setSelection': (
          ('_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QItemSe'
           'lectionModel13SelectionFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
               ('int', 'flags', 'QtCore:QItemSelectionModel.SelectionFlag'),
           )),
      ),
      'visualRegionForSelection': (
          ('_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemSele'
           'ction',
           ('address', 'value', 'QtGui:QRegion'),
           (
               ('address', 'value', 'QtCore:QItemSelection'),
           )),
      ),
      'edit': (
          ('_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerEP6Q'
           'Event',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('int', 'enum', 'QtWidgets:QAbstractItemView.EditTrigger'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'selectionCommand': (
          ('_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6QEv'
           'ent',
           ('int', 'flags', 'QtCore:QItemSelectionModel.SelectionFlag'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'address', 'QtCore:QEvent'),
           )),
      ),
      'startDrag': (
          ('_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'flags', 'QtCore:Qt.DropAction'),
           )),
      ),
      'initViewItemOption': (
          ('_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionView'
           'Item',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionViewItem'),
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
    Calls Qt's 'const QMetaObject *QAbstractItemView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractItemView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> Optional[QAbstractItemModel]:
    """
    Calls Qt's 'QAbstractItemModel *QAbstractItemView::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#model

    Returns
    -------

    Optional[QAbstractItemModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemModel *QAbstractItemView::model() const
    address = self.uglySide.call('ritual_ZNK17QAbstractItemView5modelEv')
    from ..QtCore import QAbstractItemModel
    return QAbstractItemModel._cuteAt(address)

  def selectionModel(self) -> Optional[QItemSelectionModel]:
    """
    Calls Qt's 'QItemSelectionModel *QAbstractItemView::selectionModel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#selectionModel

    Returns
    -------

    Optional[QItemSelectionModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemSelectionModel *QAbstractItemView::selectionModel() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView14selectionModelEv',
    )
    return QItemSelectionModel._cuteAt(address)

  @overload()
  def itemDelegate(self) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate *QAbstractItemView::itemDelegate()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#itemDelegate

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QAbstractItemView::itemDelegate() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView12itemDelegateEv',
    )
    return QAbstractItemDelegate._cuteAt(address)

  @overload(QModelIndex)
  def itemDelegate(
      self,
      index: QModelIndex,
  ) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate *QAbstractItemView::itemDelegate(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#itemDelegate

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
    #  QAbstractItemDelegate *QAbstractItemView::itemDelegate(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView12itemDelegateERK11QModelIndex',
        self._valueOf(index),
    )
    return QAbstractItemDelegate._cuteAt(address)

  def selectionMode(self) -> SelectionMode:
    """
    Calls Qt's 'QAbstractItemView::SelectionMode
    QAbstractItemView::selectionMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#selectionMode

    Returns
    -------

    SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SelectionMode(number)'
      gives.
    """
    #  QAbstractItemView::SelectionMode QAbstractItemView::selectionMode()
    #      const
    return QAbstractItemView.SelectionMode(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView13selectionModeEv',
    ))

  def selectionBehavior(self) -> SelectionBehavior:
    """
    Calls Qt's 'QAbstractItemView::SelectionBehavior
    QAbstractItemView::selectionBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#selectionBehavior

    Returns
    -------

    SelectionBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'SelectionBehavior(number)' gives.
    """
    #  QAbstractItemView::SelectionBehavior
    #      QAbstractItemView::selectionBehavior() const
    return QAbstractItemView.SelectionBehavior(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView17selectionBehaviorEv',
    ))

  def currentIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemView::currentIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#currentIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemView::currentIndex() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView12currentIndexEv',
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def rootIndex(self) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemView::rootIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#rootIndex

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemView::rootIndex() const
    address = self.uglySide.call('ritual_ZNK17QAbstractItemView9rootIndexEv')
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def editTriggers(self) -> EditTriggers:
    """
    Calls Qt's 'EditTriggers QAbstractItemView::editTriggers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#editTriggers

    Returns
    -------

    EditTriggers
      The value standing for the combination Qt gave back.
    """
    #  EditTriggers QAbstractItemView::editTriggers() const
    return QAbstractItemView.EditTriggers(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView12editTriggersEv',
    ))

  def verticalScrollMode(self) -> ScrollMode:
    """
    Calls Qt's 'ScrollMode QAbstractItemView::verticalScrollMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#verticalScrollMode

    Returns
    -------

    ScrollMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ScrollMode(number)'
      gives.
    """
    #  ScrollMode QAbstractItemView::verticalScrollMode() const
    return QAbstractItemView.ScrollMode(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView18verticalScrollModeEv',
    ))

  def horizontalScrollMode(self) -> ScrollMode:
    """
    Calls Qt's 'ScrollMode QAbstractItemView::horizontalScrollMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#horizontalScrollMode

    Returns
    -------

    ScrollMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ScrollMode(number)'
      gives.
    """
    #  ScrollMode QAbstractItemView::horizontalScrollMode() const
    return QAbstractItemView.ScrollMode(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView20horizontalScrollModeEv',
    ))

  def hasAutoScroll(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::hasAutoScroll() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#hasAutoScroll
    """
    #  bool QAbstractItemView::hasAutoScroll() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView13hasAutoScrollEv',
    )

  def autoScrollMargin(self) -> int:
    """
    Calls Qt's 'int QAbstractItemView::autoScrollMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#autoScrollMargin
    """
    #  int QAbstractItemView::autoScrollMargin() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView16autoScrollMarginEv',
    )

  def tabKeyNavigation(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::tabKeyNavigation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#tabKeyNavigation
    """
    #  bool QAbstractItemView::tabKeyNavigation() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView16tabKeyNavigationEv',
    )

  def showDropIndicator(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::showDropIndicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#showDropIndicator
    """
    #  bool QAbstractItemView::showDropIndicator() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView17showDropIndicatorEv',
    )

  def dragEnabled(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::dragEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#dragEnabled
    """
    #  bool QAbstractItemView::dragEnabled() const
    return self.uglySide.call('ritual_ZNK17QAbstractItemView11dragEnabledEv')

  def dragDropOverwriteMode(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::dragDropOverwriteMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#dragDropOverwriteMode
    """
    #  bool QAbstractItemView::dragDropOverwriteMode() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView21dragDropOverwriteModeEv',
    )

  def dragDropMode(self) -> DragDropMode:
    """
    Calls Qt's 'DragDropMode QAbstractItemView::dragDropMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#dragDropMode

    Returns
    -------

    DragDropMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DragDropMode(number)'
      gives.
    """
    #  DragDropMode QAbstractItemView::dragDropMode() const
    return QAbstractItemView.DragDropMode(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView12dragDropModeEv',
    ))

  def defaultDropAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QAbstractItemView::defaultDropAction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#defaultDropAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QAbstractItemView::defaultDropAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView17defaultDropActionEv',
    ))

  def alternatingRowColors(self) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::alternatingRowColors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#alternatingRowColors
    """
    #  bool QAbstractItemView::alternatingRowColors() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView20alternatingRowColorsEv',
    )

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractItemView::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractItemView::iconSize() const
    address = self.uglySide.call('ritual_ZNK17QAbstractItemView8iconSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def textElideMode(self) -> Qt.TextElideMode:
    """
    Calls Qt's 'Qt::TextElideMode QAbstractItemView::textElideMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#textElideMode

    Returns
    -------

    Qt.TextElideMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextElideMode(number)'
      gives.
    """
    #  Qt::TextElideMode QAbstractItemView::textElideMode() const
    return Qt.TextElideMode(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView13textElideModeEv',
    ))

  @overload(QModelIndex)
  def visualRect(self, index: QModelIndex) -> QRect:
    """
    Calls Qt's 'QRect QAbstractItemView::visualRect(const QModelIndex &index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#visualRect

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
    #  QRect QAbstractItemView::visualRect(const QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView10visualRectERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def indexAt(self, point: QPoint) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QAbstractItemView::indexAt(const QPoint &point)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#indexAt

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QAbstractItemView::indexAt(const QPoint &point) const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView7indexAtERK6QPoint',
        self._valueOf(point),
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  @overload(QModelIndex)
  def sizeHintForIndex(self, index: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QAbstractItemView::sizeHintForIndex(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#sizeHintForIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractItemView::sizeHintForIndex(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView16sizeHintForIndexERK11QModelIndex',
        self._valueOf(index),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def sizeHintForRow(self, row: int) -> int:
    """
    Calls Qt's 'int QAbstractItemView::sizeHintForRow(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#sizeHintForRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  int QAbstractItemView::sizeHintForRow(int row) const
    ritual = 'ritual_ZNK17QAbstractItemView14sizeHintForRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAbstractItemView14sizeHintForRowEi'
    return self.uglySide.call(ritual, row)

  @overload(int)
  def sizeHintForColumn(self, column: int) -> int:
    """
    Calls Qt's 'int QAbstractItemView::sizeHintForColumn(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#sizeHintForColumn

    Parameters
    ----------

    column : int
      Passed on as it is.
    """
    #  int QAbstractItemView::sizeHintForColumn(int column) const
    ritual = 'ritual_ZNK17QAbstractItemView17sizeHintForColumnEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAbstractItemView17sizeHintForColumnEi'
    return self.uglySide.call(ritual, column)

  def updateThreshold(self) -> int:
    """
    Calls Qt's 'int QAbstractItemView::updateThreshold() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#updateThreshold
    """
    #  int QAbstractItemView::updateThreshold() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView15updateThresholdEv',
    )

  def keyboardSearchFlags(self) -> Qt.MatchFlags:
    """
    Calls Qt's 'Qt::MatchFlags QAbstractItemView::keyboardSearchFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#keyboardSearchFlags

    Returns
    -------

    Qt.MatchFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::MatchFlags QAbstractItemView::keyboardSearchFlags() const
    return Qt.MatchFlags(self.uglySide.call(
        'ritual_ZNK17QAbstractItemView19keyboardSearchFlagsEv',
    ))

  @overload(QModelIndex)
  def isPersistentEditorOpen(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::isPersistentEditorOpen(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#isPersistentEditorOpen

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemView::isPersistentEditorOpen(const QModelIndex
    #      &index) const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView22isPersistentEditorOpenERK11QModelIn'
        'dex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def indexWidget(self, index: QModelIndex) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QAbstractItemView::indexWidget(const QModelIndex
    &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#indexWidget

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QAbstractItemView::indexWidget(const QModelIndex &index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView11indexWidgetERK11QModelIndex',
        self._valueOf(index),
    )
    return QWidget._cuteAt(address)

  @overload(int)
  def itemDelegateForRow(self, row: int) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate
    *QAbstractItemView::itemDelegateForRow(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#itemDelegateForRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QAbstractItemView::itemDelegateForRow(int row)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView18itemDelegateForRowEi', row,
    )
    return QAbstractItemDelegate._cuteAt(address)

  @overload(int)
  def itemDelegateForColumn(
      self,
      column: int,
  ) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate
    *QAbstractItemView::itemDelegateForColumn(int column) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#itemDelegateForColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QAbstractItemView::itemDelegateForColumn(int
    #      column) const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView21itemDelegateForColumnEi', column,
    )
    return QAbstractItemDelegate._cuteAt(address)

  @overload(QModelIndex)
  def itemDelegateForIndex(
      self,
      index: QModelIndex,
  ) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate
    *QAbstractItemView::itemDelegateForIndex(const QModelIndex &index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#itemDelegateForIndex

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
    #  QAbstractItemDelegate *QAbstractItemView::itemDelegateForIndex(const
    #      QModelIndex &index) const
    ritual = (
        'ritual_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelInde'
        'x')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QAbstractItemView20itemDelegateForIndexERK11QMod'
          'elIndex')
    address = self.uglySide.call(ritual, self._valueOf(index))
    return QAbstractItemDelegate._cuteAt(address)

  @overload(Qt.InputMethodQuery)
  def inputMethodQuery(self, query: Qt.InputMethodQuery) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery query) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#inputMethodQuery

    Parameters
    ----------

    query : Qt.InputMethodQuery
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QAbstractItemView::inputMethodQuery(Qt::InputMethodQuery
    #      query) const
    ritual = (
        'ritual_ZNK17QAbstractItemView16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QAbstractItemView16inputMethodQueryEN2Qt16InputM'
          'ethodQueryE')
    address = self.uglySide.call(ritual, query.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QAbstractItemView::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#horizontalOffset
    """
    #  int QAbstractItemView::horizontalOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView16horizontalOffsetEv',
    )

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QAbstractItemView::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#verticalOffset
    """
    #  int QAbstractItemView::verticalOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView14verticalOffsetEv',
    )

  @overload(QModelIndex)
  def isIndexHidden(self, index: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::isIndexHidden(const QModelIndex
    &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#isIndexHidden

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QAbstractItemView::isIndexHidden(const QModelIndex &index) const
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView13isIndexHiddenERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QItemSelection)
  def visualRegionForSelection(self, selection: QItemSelection) -> QRegion:
    """
    Calls Qt's 'QRegion QAbstractItemView::visualRegionForSelection(const
    QItemSelection &selection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#visualRegionForSelection

    Parameters
    ----------

    selection : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QAbstractItemView::visualRegionForSelection(const
    #      QItemSelection &selection) const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView24visualRegionForSelectionERK14QItemS'
        'election',
        self._valueOf(selection),
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def selectedIndexes(self) -> QList[QModelIndex]:
    """
    Calls Qt's 'QModelIndexList QAbstractItemView::selectedIndexes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#selectedIndexes

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QModelIndexList QAbstractItemView::selectedIndexes() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView15selectedIndexesEv',
    )
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, QEvent)
  @overload(QModelIndex, NoneType)
  def selectionCommand(
      self,
      index: QModelIndex,
      event: Optional[QEvent] = None,
  ) -> QItemSelectionModel.SelectionFlags:
    """
    Calls Qt's 'QItemSelectionModel::SelectionFlags
    QAbstractItemView::selectionCommand(const QModelIndex &index, const
    QEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#selectionCommand

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QItemSelectionModel.SelectionFlags
      The value standing for the combination Qt gave back.
    """
    #  QItemSelectionModel::SelectionFlags
    #      QAbstractItemView::selectionCommand(const QModelIndex &index,
    #      const QEvent *event) const
    ritual = (
        'ritual_ZNK17QAbstractItemView16selectionCommandERK11QModelIndexPK6'
        'QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QAbstractItemView16selectionCommandERK11QModelIn'
          'dexPK6QEvent')
    return QItemSelectionModel.SelectionFlags(self.uglySide.call(
        ritual, self._valueOf(index), self._addressOf(event),
    ))

  def dirtyRegionOffset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QAbstractItemView::dirtyRegionOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#dirtyRegionOffset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QAbstractItemView::dirtyRegionOffset() const
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView17dirtyRegionOffsetEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def viewportSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QAbstractItemView::viewportSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#viewportSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QAbstractItemView::viewportSizeHint() const
    ritual = 'ritual_ZNK17QAbstractItemView16viewportSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QAbstractItemView16viewportSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractItemModel)
  @overload(NoneType)
  def setModel(self, model: Optional[QAbstractItemModel]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setModel(QAbstractItemModel *model)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#setModel

    Parameters
    ----------

    model : Optional[QAbstractItemModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::setModel(QAbstractItemModel *model)
    ritual = 'ritual_ZN17QAbstractItemView8setModelEP18QAbstractItemModel'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView8setModelEP18QAbstractItemModel')
    self.uglySide.call(ritual, self._addressOf(model))

  @overload(QItemSelectionModel)
  @overload(NoneType)
  def setSelectionModel(
      self,
      selectionModel: Optional[QItemSelectionModel],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setSelectionModel(QItemSelectionModel
    *selectionModel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setSelectionModel

    Parameters
    ----------

    selectionModel : Optional[QItemSelectionModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::setSelectionModel(QItemSelectionModel
    #      *selectionModel)
    ritual = (
        'ritual_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionM'
        'odel')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView17setSelectionModelEP19QItemSele'
          'ctionModel')
    self.uglySide.call(ritual, self._addressOf(selectionModel))

  @overload(QAbstractItemDelegate)
  @overload(NoneType)
  def setItemDelegate(
      self,
      delegate: Optional[QAbstractItemDelegate],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setItemDelegate(QAbstractItemDelegate
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setItemDelegate

    Parameters
    ----------

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::setItemDelegate(QAbstractItemDelegate
    #      *delegate)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView15setItemDelegateEP21QAbstractItemDele'
        'gate',
        self._addressOf(delegate),
    )

  @overload(SelectionMode)
  def setSelectionMode(self, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void
    QAbstractItemView::setSelectionMode(QAbstractItemView::SelectionMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setSelectionMode

    Parameters
    ----------

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QAbstractItemView::setSelectionMode(QAbstractItemView::
    #      SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView16setSelectionModeENS_13SelectionModeE',
        mode.value,
    )

  @overload(SelectionBehavior)
  def setSelectionBehavior(self, behavior: SelectionBehavior) -> None:
    """
    Calls Qt's 'void
    QAbstractItemView::setSelectionBehavior(QAbstractItemView::
    SelectionBehavior behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setSelectionBehavior

    Parameters
    ----------

    behavior : SelectionBehavior
      Passed on as its number.
    """
    #  void QAbstractItemView::setSelectionBehavior(QAbstractItemView::
    #      SelectionBehavior behavior)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView20setSelectionBehaviorENS_17SelectionB'
        'ehaviorE',
        behavior.value,
    )

  @overload(EditTriggers)
  def setEditTriggers(self, triggers: EditTriggers) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setEditTriggers(EditTriggers
    triggers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setEditTriggers

    Parameters
    ----------

    triggers : EditTriggers
      Passed on as its number.
    """
    #  void QAbstractItemView::setEditTriggers(EditTriggers triggers)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView15setEditTriggersE6QFlagsINS_11EditTri'
        'ggerEE',
        triggers.value,
    )

  @overload(ScrollMode)
  def setVerticalScrollMode(self, mode: ScrollMode) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setVerticalScrollMode(ScrollMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setVerticalScrollMode

    Parameters
    ----------

    mode : ScrollMode
      Passed on as its number.
    """
    #  void QAbstractItemView::setVerticalScrollMode(ScrollMode mode)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView21setVerticalScrollModeENS_10ScrollMod'
        'eE',
        mode.value,
    )

  @overload(ScrollMode)
  def setHorizontalScrollMode(self, mode: ScrollMode) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setHorizontalScrollMode(ScrollMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setHorizontalScrollMode

    Parameters
    ----------

    mode : ScrollMode
      Passed on as its number.
    """
    #  void QAbstractItemView::setHorizontalScrollMode(ScrollMode mode)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView23setHorizontalScrollModeENS_10ScrollM'
        'odeE',
        mode.value,
    )

  @overload(bool)
  def setAutoScroll(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setAutoScroll(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setAutoScroll

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractItemView::setAutoScroll(bool enable)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView13setAutoScrollEb', enable,
    )

  @overload(int)
  def setAutoScrollMargin(self, margin: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setAutoScrollMargin(int margin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setAutoScrollMargin

    Parameters
    ----------

    margin : int
      Passed on as it is.
    """
    #  void QAbstractItemView::setAutoScrollMargin(int margin)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView19setAutoScrollMarginEi', margin,
    )

  @overload(bool)
  def setTabKeyNavigation(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setTabKeyNavigation(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setTabKeyNavigation

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractItemView::setTabKeyNavigation(bool enable)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView19setTabKeyNavigationEb', enable,
    )

  @overload(bool)
  def setDropIndicatorShown(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setDropIndicatorShown(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setDropIndicatorShown

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractItemView::setDropIndicatorShown(bool enable)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView21setDropIndicatorShownEb', enable,
    )

  @overload(bool)
  def setDragEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setDragEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setDragEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractItemView::setDragEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView14setDragEnabledEb', enable,
    )

  @overload(bool)
  def setDragDropOverwriteMode(self, overwrite: bool) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setDragDropOverwriteMode(bool
    overwrite)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setDragDropOverwriteMode

    Parameters
    ----------

    overwrite : bool
      Passed on as it is.
    """
    #  void QAbstractItemView::setDragDropOverwriteMode(bool overwrite)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView24setDragDropOverwriteModeEb',
        overwrite,
    )

  @overload(DragDropMode)
  def setDragDropMode(self, behavior: DragDropMode) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setDragDropMode(DragDropMode
    behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setDragDropMode

    Parameters
    ----------

    behavior : DragDropMode
      Passed on as its number.
    """
    #  void QAbstractItemView::setDragDropMode(DragDropMode behavior)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView15setDragDropModeENS_12DragDropModeE',
        behavior.value,
    )

  @overload(Qt.DropAction)
  def setDefaultDropAction(self, dropAction: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setDefaultDropAction(Qt::DropAction
    dropAction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setDefaultDropAction

    Parameters
    ----------

    dropAction : Qt.DropAction
      Passed on as its number.
    """
    #  void QAbstractItemView::setDefaultDropAction(Qt::DropAction
    #      dropAction)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView20setDefaultDropActionEN2Qt10DropActio'
        'nE',
        dropAction.value,
    )

  @overload(bool)
  def setAlternatingRowColors(self, enable: bool) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setAlternatingRowColors(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setAlternatingRowColors

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QAbstractItemView::setAlternatingRowColors(bool enable)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView23setAlternatingRowColorsEb', enable,
    )

  @overload(QSize)
  def setIconSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setIconSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#setIconSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QAbstractItemView::setIconSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView11setIconSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(Qt.TextElideMode)
  def setTextElideMode(self, mode: Qt.TextElideMode) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setTextElideMode(Qt::TextElideMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setTextElideMode

    Parameters
    ----------

    mode : Qt.TextElideMode
      Passed on as its number.
    """
    #  void QAbstractItemView::setTextElideMode(Qt::TextElideMode mode)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView16setTextElideModeEN2Qt13TextElideMode'
        'E',
        mode.value,
    )

  @overload(int)
  def setUpdateThreshold(self, threshold: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setUpdateThreshold(int threshold)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setUpdateThreshold

    Parameters
    ----------

    threshold : int
      Passed on as it is.
    """
    #  void QAbstractItemView::setUpdateThreshold(int threshold)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView18setUpdateThresholdEi', threshold,
    )

  @overload(Qt.MatchFlags)
  def setKeyboardSearchFlags(self, searchFlags: Qt.MatchFlags) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setKeyboardSearchFlags(Qt::MatchFlags
    searchFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setKeyboardSearchFlags

    Parameters
    ----------

    searchFlags : Qt.MatchFlags
      Passed on as its number.
    """
    #  void QAbstractItemView::setKeyboardSearchFlags(Qt::MatchFlags
    #      searchFlags)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView22setKeyboardSearchFlagsE6QFlagsIN2Qt9'
        'MatchFlagEE',
        searchFlags.value,
    )

  @overload(QModelIndex, QWidget)
  @overload(QModelIndex, NoneType)
  def setIndexWidget(
      self,
      index: QModelIndex,
      widget: Optional[QWidget],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setIndexWidget(const QModelIndex
    &index, QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setIndexWidget

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::setIndexWidget(const QModelIndex &index,
    #      QWidget *widget)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView14setIndexWidgetERK11QModelIndexP7QWid'
        'get',
        self._valueOf(index), self._addressOf(widget),
    )

  @overload(int, QAbstractItemDelegate)
  @overload(int, NoneType)
  def setItemDelegateForRow(
      self,
      row: int,
      delegate: Optional[QAbstractItemDelegate],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setItemDelegateForRow(int row,
    QAbstractItemDelegate *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setItemDelegateForRow

    Parameters
    ----------

    row : int
      Passed on as it is.

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::setItemDelegateForRow(int row,
    #      QAbstractItemDelegate *delegate)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView21setItemDelegateForRowEiP21QAbstractI'
        'temDelegate',
        row, self._addressOf(delegate),
    )

  @overload(int, QAbstractItemDelegate)
  @overload(int, NoneType)
  def setItemDelegateForColumn(
      self,
      column: int,
      delegate: Optional[QAbstractItemDelegate],
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setItemDelegateForColumn(int column,
    QAbstractItemDelegate *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setItemDelegateForColumn

    Parameters
    ----------

    column : int
      Passed on as it is.

    delegate : Optional[QAbstractItemDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::setItemDelegateForColumn(int column,
    #      QAbstractItemDelegate *delegate)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView24setItemDelegateForColumnEiP21QAbstra'
        'ctItemDelegate',
        column, self._addressOf(delegate),
    )

  @overload(QModelIndex)
  def setRootIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setRootIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setRootIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::setRootIndex(const QModelIndex &index)
    ritual = 'ritual_ZN17QAbstractItemView12setRootIndexERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView12setRootIndexERK11QModelIndex')
    self.uglySide.call(ritual, self._valueOf(index))

  @overload(QModelIndex)
  def setCurrentIndex(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setCurrentIndex(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setCurrentIndex

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::setCurrentIndex(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView15setCurrentIndexERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QRect, QItemSelectionModel.SelectionFlags)
  def setSelection(
      self,
      rect: QRect,
      command: QItemSelectionModel.SelectionFlags,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setSelection(const QRect &rect,
    QItemSelectionModel::SelectionFlags command)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setSelection

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    command : QItemSelectionModel.SelectionFlags
      Passed on as its number.
    """
    #  void QAbstractItemView::setSelection(const QRect &rect,
    #      QItemSelectionModel::SelectionFlags command)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView12setSelectionERK5QRect6QFlagsIN19QIte'
        'mSelectionModel13SelectionFlagEE',
        self._valueOf(rect), command.value,
    )

  @overload(QRegion)
  def setDirtyRegion(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QAbstractItemView::setDirtyRegion(const QRegion
    &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#setDirtyRegion

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QAbstractItemView::setDirtyRegion(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView14setDirtyRegionERK7QRegion',
        self._valueOf(region),
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
    - Qt's 'QAbstractItemView::QAbstractItemView(QWidget *parent)': the class
      is abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    - Qt's 'QAbstractItemView::QAbstractItemView(QAbstractItemViewPrivate
      &a0, QWidget *parent)': the class is abstract, so C++ cannot make one,
      and the C++ class of ours does not fill in every function it leaves
      open.
    """
    raise NotImplementedError(
        "'QAbstractItemView.__init__' has no cute function yet. Qt's "
        "'QAbstractItemView::QAbstractItemView(QWidget *parent)': the class "
        "is abstract, so C++ cannot make one, and the C++ class of ours "
        "does not fill in every function it leaves open. Qt's "
        "'QAbstractItemView::QAbstractItemView(QAbstractItemViewPrivate "
        "&a0, QWidget *parent)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  def resetVerticalScrollMode(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::resetVerticalScrollMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#resetVerticalScrollMode
    """
    #  void QAbstractItemView::resetVerticalScrollMode()
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView23resetVerticalScrollModeEv',
    )

  def resetHorizontalScrollMode(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::resetHorizontalScrollMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#resetHorizontalScrollMode
    """
    #  void QAbstractItemView::resetHorizontalScrollMode()
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView25resetHorizontalScrollModeEv',
    )

  @overload(str)
  def keyboardSearch(self, search: str) -> None:
    """
    Calls Qt's 'void QAbstractItemView::keyboardSearch(const QString
    &search)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#keyboardSearch

    Parameters
    ----------

    search : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractItemView::keyboardSearch(const QString &search)
    ritual = 'ritual_ZN17QAbstractItemView14keyboardSearchERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView14keyboardSearchERK7QString'
    self.uglySide.call(ritual, search)

  @overload(QModelIndex)
  @overload(QModelIndex, ScrollHint)
  def scrollTo(
      self,
      index: QModelIndex,
      hint: ScrollHint = ScrollHint.EnsureVisible,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::scrollTo(const QModelIndex &index,
    ScrollHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#scrollTo

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    hint : ScrollHint
      Passed on as its number. May be left out, as in Qt: it is then
      ScrollHint.EnsureVisible.
    """
    #  void QAbstractItemView::scrollTo(const QModelIndex &index, ScrollHint
    #      hint)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView8scrollToERK11QModelIndexNS_10ScrollHi'
        'ntE',
        self._valueOf(index), hint.value,
    )

  @overload(QModelIndex)
  def openPersistentEditor(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::openPersistentEditor(const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#openPersistentEditor

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::openPersistentEditor(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView20openPersistentEditorERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def closePersistentEditor(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::closePersistentEditor(const
    QModelIndex &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#closePersistentEditor

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::closePersistentEditor(const QModelIndex
    #      &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView21closePersistentEditorERK11QModelInde'
        'x',
        self._valueOf(index),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#reset
    """
    #  void QAbstractItemView::reset()
    ritual = 'ritual_ZN17QAbstractItemView5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView5resetEv'
    self.uglySide.call(ritual)

  def doItemsLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::doItemsLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#doItemsLayout
    """
    #  void QAbstractItemView::doItemsLayout()
    ritual = 'ritual_ZN17QAbstractItemView13doItemsLayoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView13doItemsLayoutEv'
    self.uglySide.call(ritual)

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#selectAll
    """
    #  void QAbstractItemView::selectAll()
    ritual = 'ritual_ZN17QAbstractItemView9selectAllEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView9selectAllEv'
    self.uglySide.call(ritual)

  @overload(QModelIndex)
  def edit(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::edit(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#edit

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::edit(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView4editERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex, EditTrigger, QEvent)
  @overload(QModelIndex, EditTrigger, NoneType)
  def edit(
      self,
      index: QModelIndex,
      trigger: EditTrigger,
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::edit(const QModelIndex &index,
    EditTrigger trigger, QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#edit

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    trigger : EditTrigger
      Passed on as its number.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemView::edit(const QModelIndex &index, EditTrigger
    #      trigger, QEvent *event)
    ritual = (
        'ritual_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTriggerE'
        'P6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView4editERK11QModelIndexNS_11EditTr'
          'iggerEP6QEvent')
    return self.uglySide.call(
        ritual, self._valueOf(index), trigger.value, self._addressOf(event),
    )

  def clearSelection(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::clearSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#clearSelection
    """
    #  void QAbstractItemView::clearSelection()
    self.uglySide.call('ritual_ZN17QAbstractItemView14clearSelectionEv')

  def scrollToTop(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::scrollToTop()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#scrollToTop
    """
    #  void QAbstractItemView::scrollToTop()
    self.uglySide.call('ritual_ZN17QAbstractItemView11scrollToTopEv')

  def scrollToBottom(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::scrollToBottom()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#scrollToBottom
    """
    #  void QAbstractItemView::scrollToBottom()
    self.uglySide.call('ritual_ZN17QAbstractItemView14scrollToBottomEv')

  @overload(QModelIndex)
  def update(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::update(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#update

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::update(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView6updateERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex, int, int)
  def rowsInserted(self, parent: QModelIndex, start: int, end: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::rowsInserted(const QModelIndex
    &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#rowsInserted

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
    #  void QAbstractItemView::rowsInserted(const QModelIndex &parent, int
    #      start, int end)
    ritual = 'ritual_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView12rowsInsertedERK11QModelIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QModelIndex, int, int)
  def rowsAboutToBeRemoved(
      self,
      parent: QModelIndex,
      start: int,
      end: int,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::rowsAboutToBeRemoved(const
    QModelIndex &parent, int start, int end)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#rowsAboutToBeRemoved

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
    #  void QAbstractItemView::rowsAboutToBeRemoved(const QModelIndex
    #      &parent, int start, int end)
    ritual = (
        'ritual_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QModelIndex'
        'ii')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView20rowsAboutToBeRemovedERK11QMode'
          'lIndexii')
    self.uglySide.call(ritual, self._valueOf(parent), start, end)

  @overload(QItemSelection, QItemSelection)
  def selectionChanged(
      self,
      selected: QItemSelection,
      deselected: QItemSelection,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::selectionChanged(const QItemSelection
    &selected, const QItemSelection &deselected)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#selectionChanged

    Parameters
    ----------

    selected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.

    deselected : QItemSelection
      Passed on as a value: Qt reads the C++ QItemSelection, which stays
      Python's own.
    """
    #  void QAbstractItemView::selectionChanged(const QItemSelection
    #      &selected, const QItemSelection &deselected)
    ritual = (
        'ritual_ZN17QAbstractItemView16selectionChangedERK14QItemSelectionS'
        '2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView16selectionChangedERK14QItemSele'
          'ctionS2_')
    self.uglySide.call(
        ritual, self._valueOf(selected), self._valueOf(deselected),
    )

  @overload(QModelIndex, QModelIndex)
  def currentChanged(
      self,
      current: QModelIndex,
      previous: QModelIndex,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::currentChanged(const QModelIndex
    &current, const QModelIndex &previous)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#currentChanged

    Parameters
    ----------

    current : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    previous : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::currentChanged(const QModelIndex &current,
    #      const QModelIndex &previous)
    ritual = (
        'ritual_ZN17QAbstractItemView14currentChangedERK11QModelIndexS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView14currentChangedERK11QModelIndex'
          'S2_')
    self.uglySide.call(
        ritual, self._valueOf(current), self._valueOf(previous),
    )

  def updateEditorData(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::updateEditorData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#updateEditorData
    """
    #  void QAbstractItemView::updateEditorData()
    ritual = 'ritual_ZN17QAbstractItemView16updateEditorDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView16updateEditorDataEv'
    self.uglySide.call(ritual)

  def updateEditorGeometries(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::updateEditorGeometries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#updateEditorGeometries
    """
    #  void QAbstractItemView::updateEditorGeometries()
    ritual = 'ritual_ZN17QAbstractItemView22updateEditorGeometriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView22updateEditorGeometriesEv'
    self.uglySide.call(ritual)

  def updateGeometries(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::updateGeometries()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#updateGeometries
    """
    #  void QAbstractItemView::updateGeometries()
    ritual = 'ritual_ZN17QAbstractItemView16updateGeometriesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView16updateGeometriesEv'
    self.uglySide.call(ritual)

  @overload(int)
  def verticalScrollbarAction(self, action: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::verticalScrollbarAction(int action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#verticalScrollbarAction

    Parameters
    ----------

    action : int
      Passed on as it is.
    """
    #  void QAbstractItemView::verticalScrollbarAction(int action)
    ritual = 'ritual_ZN17QAbstractItemView23verticalScrollbarActionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView23verticalScrollbarActionEi'
    self.uglySide.call(ritual, action)

  @overload(int)
  def horizontalScrollbarAction(self, action: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::horizontalScrollbarAction(int
    action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#horizontalScrollbarAction

    Parameters
    ----------

    action : int
      Passed on as it is.
    """
    #  void QAbstractItemView::horizontalScrollbarAction(int action)
    ritual = 'ritual_ZN17QAbstractItemView25horizontalScrollbarActionEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView25horizontalScrollbarActionEi')
    self.uglySide.call(ritual, action)

  @overload(int)
  def verticalScrollbarValueChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::verticalScrollbarValueChanged(int
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QAbstractItemView::verticalScrollbarValueChanged(int value)
    ritual = 'ritual_ZN17QAbstractItemView29verticalScrollbarValueChangedEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView29verticalScrollbarValueChangedE'
          'i')
    self.uglySide.call(ritual, value)

  @overload(int)
  def horizontalScrollbarValueChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::horizontalScrollbarValueChanged(int
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QAbstractItemView::horizontalScrollbarValueChanged(int value)
    ritual = (
        'ritual_ZN17QAbstractItemView31horizontalScrollbarValueChangedEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView31horizontalScrollbarValueChange'
          'dEi')
    self.uglySide.call(ritual, value)

  @overload(QWidget, QAbstractItemDelegate.EndEditHint)
  @overload(NoneType, QAbstractItemDelegate.EndEditHint)
  def closeEditor(
      self,
      editor: Optional[QWidget],
      hint: QAbstractItemDelegate.EndEditHint,
  ) -> None:
    """
    Calls Qt's 'void QAbstractItemView::closeEditor(QWidget *editor,
    QAbstractItemDelegate::EndEditHint hint)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#closeEditor

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hint : QAbstractItemDelegate.EndEditHint
      Passed on as its number.
    """
    #  void QAbstractItemView::closeEditor(QWidget *editor,
    #      QAbstractItemDelegate::EndEditHint hint)
    ritual = (
        'ritual_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstractIte'
        'mDelegate11EndEditHintE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView11closeEditorEP7QWidgetN21QAbstr'
          'actItemDelegate11EndEditHintE')
    self.uglySide.call(ritual, self._addressOf(editor), hint.value)

  @overload(QWidget)
  @overload(NoneType)
  def commitData(self, editor: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::commitData(QWidget *editor)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#commitData

    Parameters
    ----------

    editor : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::commitData(QWidget *editor)
    ritual = 'ritual_ZN17QAbstractItemView10commitDataEP7QWidget'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView10commitDataEP7QWidget'
    self.uglySide.call(ritual, self._addressOf(editor))

  @overload(QObject)
  @overload(NoneType)
  def editorDestroyed(self, editor: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::editorDestroyed(QObject *editor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#editorDestroyed

    Parameters
    ----------

    editor : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::editorDestroyed(QObject *editor)
    ritual = 'ritual_ZN17QAbstractItemView15editorDestroyedEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView15editorDestroyedEP7QObject'
    self.uglySide.call(ritual, self._addressOf(editor, 'QObject'))

  @overload(QModelIndex)
  def pressed(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::pressed(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#pressed

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::pressed(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView7pressedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def clicked(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::clicked(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#clicked

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::clicked(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView7clickedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def doubleClicked(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::doubleClicked(const QModelIndex
    &index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#doubleClicked

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::doubleClicked(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView13doubleClickedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def activated(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::activated(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#activated

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::activated(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView9activatedERK11QModelIndex',
        self._valueOf(index),
    )

  @overload(QModelIndex)
  def entered(self, index: QModelIndex) -> None:
    """
    Calls Qt's 'void QAbstractItemView::entered(const QModelIndex &index)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#entered

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QAbstractItemView::entered(const QModelIndex &index)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView7enteredERK11QModelIndex',
        self._valueOf(index),
    )

  def viewportEntered(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::viewportEntered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#viewportEntered
    """
    #  void QAbstractItemView::viewportEntered()
    self.uglySide.call('ritual_ZN17QAbstractItemView15viewportEnteredEv')

  @overload(QSize)
  def iconSizeChanged(self, size: QSize) -> None:
    """
    Calls Qt's 'void QAbstractItemView::iconSizeChanged(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#iconSizeChanged

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QAbstractItemView::iconSizeChanged(const QSize &size)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView15iconSizeChangedERK5QSize',
        self._valueOf(size),
    )

  @overload(Qt.DropActions)
  def startDrag(self, supportedActions: Qt.DropActions) -> None:
    """
    Calls Qt's 'void QAbstractItemView::startDrag(Qt::DropActions
    supportedActions)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#startDrag

    Parameters
    ----------

    supportedActions : Qt.DropActions
      Passed on as its number.
    """
    #  void QAbstractItemView::startDrag(Qt::DropActions supportedActions)
    ritual = (
        'ritual_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropActionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView9startDragE6QFlagsIN2Qt10DropAct'
          'ionEE')
    self.uglySide.call(ritual, supportedActions.value)

  @overload(QStyleOptionViewItem)
  @overload(NoneType)
  def initViewItemOption(
      self,
      option: Optional[QStyleOptionViewItem],
  ) -> None:
    """
    Calls Qt's 'void
    QAbstractItemView::initViewItemOption(QStyleOptionViewItem *option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#initViewItemOption

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::initViewItemOption(QStyleOptionViewItem
    #      *option) const
    ritual = (
        'ritual_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleOptionV'
        'iewItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QAbstractItemView18initViewItemOptionEP20QStyleO'
          'ptionViewItem')
    self.uglySide.call(ritual, self._addressOf(option))

  def scheduleDelayedItemsLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::scheduleDelayedItemsLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#scheduleDelayedItemsLayout
    """
    #  void QAbstractItemView::scheduleDelayedItemsLayout()
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView26scheduleDelayedItemsLayoutEv',
    )

  def executeDelayedItemsLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::executeDelayedItemsLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#executeDelayedItemsLayout
    """
    #  void QAbstractItemView::executeDelayedItemsLayout()
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView25executeDelayedItemsLayoutEv',
    )

  @overload(int, int)
  def scrollDirtyRegion(self, dx: int, dy: int) -> None:
    """
    Calls Qt's 'void QAbstractItemView::scrollDirtyRegion(int dx, int dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#scrollDirtyRegion

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.
    """
    #  void QAbstractItemView::scrollDirtyRegion(int dx, int dy)
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView17scrollDirtyRegionEii', dx, dy,
    )

  def startAutoScroll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::startAutoScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#startAutoScroll
    """
    #  void QAbstractItemView::startAutoScroll()
    self.uglySide.call('ritual_ZN17QAbstractItemView15startAutoScrollEv')

  def stopAutoScroll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::stopAutoScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#stopAutoScroll
    """
    #  void QAbstractItemView::stopAutoScroll()
    self.uglySide.call('ritual_ZN17QAbstractItemView14stopAutoScrollEv')

  def doAutoScroll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::doAutoScroll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#doAutoScroll
    """
    #  void QAbstractItemView::doAutoScroll()
    self.uglySide.call('ritual_ZN17QAbstractItemView12doAutoScrollEv')

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QAbstractItemView::focusNextPrevChild(bool next)
    ritual = 'ritual_ZN17QAbstractItemView18focusNextPrevChildEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView18focusNextPrevChildEb'
    return self.uglySide.call(ritual, next)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemView::event(QEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def viewportEvent(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::viewportEvent(QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#viewportEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemView::viewportEvent(QEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView13viewportEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView13viewportEventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::mouseMoveEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView14mouseMoveEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::mouseReleaseEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView17mouseReleaseEventEP11QMouseEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::mouseDoubleClickEvent(QMouseEvent *event)
    ritual = (
        'ritual_ZN17QAbstractItemView21mouseDoubleClickEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView21mouseDoubleClickEventEP11QMous'
          'eEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::dragEnterEvent(QDragEnterEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::dragEnterEvent(QDragEnterEvent *event)
    ritual = (
        'ritual_ZN17QAbstractItemView14dragEnterEventEP15QDragEnterEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView14dragEnterEventEP15QDragEnterEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def dragMoveEvent(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::dragMoveEvent(QDragMoveEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#dragMoveEvent

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::dragMoveEvent(QDragMoveEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView13dragMoveEventEP14QDragMoveEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView13dragMoveEventEP14QDragMoveEven'
          't')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def dragLeaveEvent(self, event: Optional[QDragLeaveEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#dragLeaveEvent

    Parameters
    ----------

    event : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::dragLeaveEvent(QDragLeaveEvent *event)
    ritual = (
        'ritual_ZN17QAbstractItemView14dragLeaveEventEP15QDragLeaveEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView14dragLeaveEventEP15QDragLeaveEv'
          'ent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDropEvent)
  @overload(NoneType)
  def dropEvent(self, event: Optional[QDropEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::dropEvent(QDropEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#dropEvent

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::dropEvent(QDropEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView9dropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView9dropEventEP10QDropEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::focusInEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView12focusInEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::focusOutEvent(QFocusEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#focusOutEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::focusOutEvent(QFocusEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView13focusOutEventEP11QFocusEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView11resizeEventEP12QResizeEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QAbstractItemView10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QInputMethodEvent)
  @overload(NoneType)
  def inputMethodEvent(self, event: Optional[QInputMethodEvent]) -> None:
    """
    Calls Qt's 'void QAbstractItemView::inputMethodEvent(QInputMethodEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#inputMethodEvent

    Parameters
    ----------

    event : Optional[QInputMethodEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractItemView::inputMethodEvent(QInputMethodEvent *event)
    ritual = (
        'ritual_ZN17QAbstractItemView16inputMethodEventEP17QInputMethodEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView16inputMethodEventEP17QInputMeth'
          'odEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QAbstractItemView::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractItemView::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN17QAbstractItemView11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QAbstractItemView11eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  def d_func(self) -> Optional[QAbstractItemViewPrivate]:
    """
    Calls Qt's 'QAbstractItemViewPrivate *QAbstractItemView::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#d_func

    Returns
    -------

    Optional[QAbstractItemViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemViewPrivate *QAbstractItemView::d_func()
    address = self.uglySide.call('ritual_ZN17QAbstractItemView6d_funcEv')
    from . import QAbstractItemViewPrivate
    return QAbstractItemViewPrivate._cuteAt(address)

  @staticmethod
  def dataChanged(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemView::dataChanged(const QModelIndex &topLeft,
    const QModelIndex &bottomRight, const QList<int> &roles)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractItemView.dataChanged' has no cute function yet. Qt's "
        "'void QAbstractItemView::dataChanged(const QModelIndex &topLeft, "
        "const QModelIndex &bottomRight, const QList<int> &roles)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def dropIndicatorPosition(*__, **_) -> Never:
    """
    Qt's 'DropIndicatorPosition QAbstractItemView::dropIndicatorPosition()
    const': gives the enum 'QAbstractItemView::DropIndicatorPosition', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractItemView.dropIndicatorPosition' has no cute function "
        "yet. Qt's 'DropIndicatorPosition "
        "QAbstractItemView::dropIndicatorPosition() const': gives the enum "
        "'QAbstractItemView::DropIndicatorPosition', whose class cannot be "
        "named here.")

  @staticmethod
  def moveCursor(*__, **_) -> Never:
    """
    Qt's 'QModelIndex QAbstractItemView::moveCursor(CursorAction
    cursorAction, Qt::KeyboardModifiers modifiers)': names the enum
    'QAbstractItemView::CursorAction', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractItemView.moveCursor' has no cute function yet. Qt's "
        "'QModelIndex QAbstractItemView::moveCursor(CursorAction "
        "cursorAction, Qt::KeyboardModifiers modifiers)': names the enum "
        "'QAbstractItemView::CursorAction', whose class cannot be named "
        "here.")

  @staticmethod
  def setState(*__, **_) -> Never:
    """
    Qt's 'void QAbstractItemView::setState(State state)': names the enum
    'QAbstractItemView::State', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractItemView.setState' has no cute function yet. Qt's 'void "
        "QAbstractItemView::setState(State state)': names the enum "
        "'QAbstractItemView::State', whose class cannot be named here.")

  @staticmethod
  def state(*__, **_) -> Never:
    """
    Qt's 'State QAbstractItemView::state() const': gives the enum
    'QAbstractItemView::State', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QAbstractItemView.state' has no cute function yet. Qt's 'State "
        "QAbstractItemView::state() const': gives the enum "
        "'QAbstractItemView::State', whose class cannot be named here.")
