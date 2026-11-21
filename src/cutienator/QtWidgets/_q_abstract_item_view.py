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
from ..QtCore import Qt
from . import QAbstractScrollArea, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QAbstractItemModel, QItemSelectionModel, QMetaObject
  from ..QtCore import QModelIndex, QPoint, QRect, QSize, QVariant
  from . import QAbstractItemDelegate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractItemDelegate = WAIT['QAbstractItemDelegate']
  QAbstractItemModel = WAIT['QAbstractItemModel']
  QItemSelectionModel = WAIT['QItemSelectionModel']
  QModelIndex = WAIT['QModelIndex']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']

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
  can call so far, 76 names in all: 'metaObject', 'tr', 'setModel', 'model',
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
  'scrollToTop', 'scrollToBottom', 'update'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAbstractItemView::~QAbstractItemView()': the destructor: Python
    never removes a C++ QAbstractItemView.

  What has no ritual
  ------------------

  73 of the 151 functions Qt declares: 57 protected; 7 a signal; 3 private; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template;
  1 the class is abstract, so C++ cannot make one.

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
    from ..QtCore import QItemSelectionModel
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
    from . import QAbstractItemDelegate
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
    from . import QAbstractItemDelegate
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
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView14sizeHintForRowEi', row,
    )

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
    return self.uglySide.call(
        'ritual_ZNK17QAbstractItemView17sizeHintForColumnEi', column,
    )

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
    from . import QAbstractItemDelegate
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
    from . import QAbstractItemDelegate
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
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView20itemDelegateForIndexERK11QModelInde'
        'x',
        self._valueOf(index),
    )
    from . import QAbstractItemDelegate
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
    address = self.uglySide.call(
        'ritual_ZNK17QAbstractItemView16inputMethodQueryEN2Qt16InputMethodQ'
        'ueryE',
        query.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView8setModelEP18QAbstractItemModel',
        self._addressOf(model),
    )

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
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView17setSelectionModelEP19QItemSelectionM'
        'odel',
        self._addressOf(selectionModel),
    )

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
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView12setRootIndexERK11QModelIndex',
        self._valueOf(index),
    )

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
    self.uglySide.call(
        'ritual_ZN17QAbstractItemView14keyboardSearchERK7QString', search,
    )

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
    self.uglySide.call('ritual_ZN17QAbstractItemView5resetEv')

  def doItemsLayout(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::doItemsLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractitemview.html#doItemsLayout
    """
    #  void QAbstractItemView::doItemsLayout()
    self.uglySide.call('ritual_ZN17QAbstractItemView13doItemsLayoutEv')

  def selectAll(self) -> None:
    """
    Calls Qt's 'void QAbstractItemView::selectAll()'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractitemview.html#selectAll
    """
    #  void QAbstractItemView::selectAll()
    self.uglySide.call('ritual_ZN17QAbstractItemView9selectAllEv')

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
