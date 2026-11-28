"""
QCommonListViewBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCommonListViewBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import Qt, QList
from . import QListView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QModelIndex, QPoint, QRect, QSize
  from ..QtGui import QDragLeaveEvent, QDragMoveEvent, QDropEvent, QPainter
  from . import QAbstractItemDelegate, QListViewItem, QListViewLayoutInfo
  from . import QScrollBar, QStyleOptionViewItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QListViewItem = WAIT['QListViewItem']
  QListViewLayoutInfo = WAIT['QListViewLayoutInfo']
  QModelIndex = WAIT['QModelIndex']
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QStyleOptionViewItem = WAIT['QStyleOptionViewItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCommonListViewBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCommonListViewBase: a plain Python object standing
  in front of one C++ QCommonListViewBase.

  What exists
  -----------

  Every function of Qt's QCommonListViewBase that has a ritual and that
  Python can call so far, 44 names in all: 'itemIndex',
  'indexToListViewItem', 'doBatchedItemLayout', 'clear', 'setRowCount',
  'intersectingSet', 'dataChanged', 'scrollContentsBy', 'mapToViewport',
  'horizontalOffset', 'verticalOffset', 'updateHorizontalScrollBar',
  'updateVerticalScrollBar', 'appendHiddenRow', 'removeHiddenRow',
  'setPositionForIndex', 'paintDragDrop', 'filterDragMoveEvent',
  'filterDragLeaveEvent', 'filterDropEvent', 'filterStartDrag', 'spacing',
  'isWrapping', 'gridSize', 'flow', 'movement', 'offset', 'pressedPosition',
  'uniformItemSizes', 'column', 'verticalScrollBar', 'horizontalScrollBar',
  'modelIndex', 'rowCount', 'initViewItemOption', 'viewport', 'clipRect',
  'cachedItemSize', 'viewItemRect', 'itemSize', 'delegate', 'isHidden',
  'hiddenCount', 'isRightToLeft'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCommonListViewBase::~QCommonListViewBase()': the destructor:
    Python never removes a C++ QCommonListViewBase.
  - Qt's 'int QCommonListViewBase::horizontalScrollToValue(int index,
    QListView::ScrollHint hint, bool leftOf, bool rightOf, const QRect &area,
    const QRect &rect) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'int QCommonListViewBase::verticalScrollToValue(int index,
    QListView::ScrollHint hint, bool above, bool below, const QRect &area,
    const QRect &rect) const': takes a type Python has no way to hand over
    yet.
  - Qt's 'QListView::ScrollMode QCommonListViewBase::verticalScrollMode()
    const': gives a type Python has no way to take yet.
  - Qt's 'QListView::ScrollMode QCommonListViewBase::horizontalScrollMode()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 50 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QCommonListViewBase is created at the first use, not by
    'QCommonListViewBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCommonListViewBase.
  - Each name of Qt's QCommonListViewBase that has no cute function yet,
    '__init__', 'horizontalScrollMode', 'horizontalScrollToValue',
    'verticalScrollMode', 'verticalScrollToValue', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCommonListViewBase'

  #  A C++ QCommonListViewBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCommonListViewBase'

  #  The functions Qt calls itself that QCommonListViewBase is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'intersectingSet': (
          'QList<QModelIndex> QCommonListViewBase::intersectingSet(const '
          'QRect &) const',
      ),
      'horizontalScrollToValue': (
          'int QCommonListViewBase::horizontalScrollToValue(int, '
          'QListView::ScrollHint, bool, bool, const QRect &, const QRect '
          '&) const',
      ),
      'verticalScrollToValue': (
          'int QCommonListViewBase::verticalScrollToValue(int, '
          'QListView::ScrollHint, bool, bool, const QRect &, const QRect '
          '&) const',
      ),
  }

  #  The functions Qt calls itself that QCommonListViewBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemIndex': (
          ('_ZNK19QCommonListViewBase9itemIndexERK13QListViewItem',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtWidgets:QListViewItem'),
           )),
      ),
      'indexToListViewItem': (
          ('_ZNK19QCommonListViewBase19indexToListViewItemERK11QModelIndex',
           ('address', 'value', 'QtWidgets:QListViewItem'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'doBatchedItemLayout': (
          ('_ZN19QCommonListViewBase19doBatchedItemLayoutERK19QListViewLayo'
           'utInfoi',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtWidgets:QListViewLayoutInfo'),
               ('int', 'number', ''),
           )),
      ),
      'clear': (
          ('_ZN19QCommonListViewBase5clearEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setRowCount': (
          ('_ZN19QCommonListViewBase11setRowCountEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'dataChanged': (
          ('_ZN19QCommonListViewBase11dataChangedERK11QModelIndexS2_',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'scrollContentsBy': (
          ('_ZN19QCommonListViewBase16scrollContentsByEiib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'mapToViewport': (
          ('_ZNK19QCommonListViewBase13mapToViewportERK5QRect',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
      ),
      'horizontalOffset': (
          ('_ZNK19QCommonListViewBase16horizontalOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'verticalOffset': (
          ('_ZNK19QCommonListViewBase14verticalOffsetEv',
           ('int', 'number', ''),
           ()),
      ),
      'updateHorizontalScrollBar': (
          ('_ZN19QCommonListViewBase25updateHorizontalScrollBarERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'updateVerticalScrollBar': (
          ('_ZN19QCommonListViewBase23updateVerticalScrollBarERK5QSize',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSize'),
           )),
      ),
      'appendHiddenRow': (
          ('_ZN19QCommonListViewBase15appendHiddenRowEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'removeHiddenRow': (
          ('_ZN19QCommonListViewBase15removeHiddenRowEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'setPositionForIndex': (
          ('_ZN19QCommonListViewBase19setPositionForIndexERK6QPointRK11QMod'
           'elIndex',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
               ('address', 'value', 'QtCore:QModelIndex'),
           )),
      ),
      'paintDragDrop': (
          ('_ZN19QCommonListViewBase13paintDragDropEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'filterDragMoveEvent': (
          ('_ZN19QCommonListViewBase19filterDragMoveEventEP14QDragMoveEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QDragMoveEvent'),
           )),
      ),
      'filterDragLeaveEvent': (
          ('_ZN19QCommonListViewBase20filterDragLeaveEventEP15QDragLeaveEve'
           'nt',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QDragLeaveEvent'),
           )),
      ),
      'filterDropEvent': (
          ('_ZN19QCommonListViewBase15filterDropEventEP10QDropEvent',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtGui:QDropEvent'),
           )),
      ),
      'filterStartDrag': (
          ('_ZN19QCommonListViewBase15filterStartDragE6QFlagsIN2Qt10DropAct'
           'ionEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:Qt.DropAction'),
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

  @overload(QListViewItem)
  def itemIndex(self, item: QListViewItem) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::itemIndex(const QListViewItem &item)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#itemIndex

    Parameters
    ----------

    item : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.
    """
    #  int QCommonListViewBase::itemIndex(const QListViewItem &item) const
    return self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase9itemIndexERK13QListViewItem',
        self._valueOf(item),
    )

  @overload(QModelIndex)
  def indexToListViewItem(self, index: QModelIndex) -> QListViewItem:
    """
    Calls Qt's 'QListViewItem QCommonListViewBase::indexToListViewItem(const
    QModelIndex &index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#indexToListViewItem

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QListViewItem
      A new cute QListViewItem around the copy Qt gave back. Python owns it.
    """
    #  QListViewItem QCommonListViewBase::indexToListViewItem(const
    #      QModelIndex &index) const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase19indexToListViewItemERK11QModelInd'
        'ex',
        self._valueOf(index),
    )
    from . import QListViewItem
    return QListViewItem._cuteOwning(address)

  @overload(QRect)
  def intersectingSet(self, area: QRect) -> QList[QModelIndex]:
    """
    Calls Qt's 'QList<QModelIndex> QCommonListViewBase::intersectingSet(const
    QRect &area) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#intersectingSet

    Parameters
    ----------

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QList[QModelIndex]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QModelIndex> QCommonListViewBase::intersectingSet(const QRect
    #      &area) const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase15intersectingSetERK5QRect',
        self._valueOf(area),
    )
    from ..QtCore import QModelIndex
    return QList[QModelIndex]._cuteOwning(address)

  @overload(QRect)
  def mapToViewport(self, rect: QRect) -> QRect:
    """
    Calls Qt's 'QRect QCommonListViewBase::mapToViewport(const QRect &rect)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#mapToViewport

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCommonListViewBase::mapToViewport(const QRect &rect) const
    ritual = 'ritual_ZNK19QCommonListViewBase13mapToViewportERK5QRect'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QCommonListViewBase13mapToViewportERK5QRect'
    address = self.uglySide.call(ritual, self._valueOf(rect))
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def horizontalOffset(self) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::horizontalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#horizontalOffset
    """
    #  int QCommonListViewBase::horizontalOffset() const
    ritual = 'ritual_ZNK19QCommonListViewBase16horizontalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QCommonListViewBase16horizontalOffsetEv'
    return self.uglySide.call(ritual)

  def verticalOffset(self) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::verticalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#verticalOffset
    """
    #  int QCommonListViewBase::verticalOffset() const
    ritual = 'ritual_ZNK19QCommonListViewBase14verticalOffsetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QCommonListViewBase14verticalOffsetEv'
    return self.uglySide.call(ritual)

  def spacing(self) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#spacing
    """
    #  int QCommonListViewBase::spacing() const
    return self.uglySide.call('ritual_ZNK19QCommonListViewBase7spacingEv')

  def isWrapping(self) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::isWrapping() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#isWrapping
    """
    #  bool QCommonListViewBase::isWrapping() const
    return self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase10isWrappingEv',
    )

  def gridSize(self) -> QSize:
    """
    Calls Qt's 'QSize QCommonListViewBase::gridSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#gridSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCommonListViewBase::gridSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8gridSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def flow(self) -> QListView.Flow:
    """
    Calls Qt's 'QListView::Flow QCommonListViewBase::flow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#flow

    Returns
    -------

    QListView.Flow
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QListView.Flow(number)'
      gives.
    """
    #  QListView::Flow QCommonListViewBase::flow() const
    return QListView.Flow(self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase4flowEv',
    ))

  def movement(self) -> QListView.Movement:
    """
    Calls Qt's 'QListView::Movement QCommonListViewBase::movement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#movement

    Returns
    -------

    QListView.Movement
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QListView.Movement(number)' gives.
    """
    #  QListView::Movement QCommonListViewBase::movement() const
    return QListView.Movement(self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8movementEv',
    ))

  def offset(self) -> QPoint:
    """
    Calls Qt's 'QPoint QCommonListViewBase::offset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#offset

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QCommonListViewBase::offset() const
    address = self.uglySide.call('ritual_ZNK19QCommonListViewBase6offsetEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def pressedPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QCommonListViewBase::pressedPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#pressedPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QCommonListViewBase::pressedPosition() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase15pressedPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def uniformItemSizes(self) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::uniformItemSizes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#uniformItemSizes
    """
    #  bool QCommonListViewBase::uniformItemSizes() const
    return self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase16uniformItemSizesEv',
    )

  def column(self) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#column
    """
    #  int QCommonListViewBase::column() const
    return self.uglySide.call('ritual_ZNK19QCommonListViewBase6columnEv')

  def verticalScrollBar(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QCommonListViewBase::verticalScrollBar() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#verticalScrollBar

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QCommonListViewBase::verticalScrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase17verticalScrollBarEv',
    )
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  def horizontalScrollBar(self) -> Optional[QScrollBar]:
    """
    Calls Qt's 'QScrollBar *QCommonListViewBase::horizontalScrollBar()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#horizontalScrollBar

    Returns
    -------

    Optional[QScrollBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScrollBar *QCommonListViewBase::horizontalScrollBar() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase19horizontalScrollBarEv',
    )
    from . import QScrollBar
    return QScrollBar._cuteAt(address)

  @overload(int)
  def modelIndex(self, row: int) -> QModelIndex:
    """
    Calls Qt's 'QModelIndex QCommonListViewBase::modelIndex(int row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#modelIndex

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    QModelIndex
      A new cute QModelIndex around the copy Qt gave back. Python owns it.
    """
    #  QModelIndex QCommonListViewBase::modelIndex(int row) const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase10modelIndexEi', row,
    )
    from ..QtCore import QModelIndex
    return QModelIndex._cuteOwning(address)

  def rowCount(self) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#rowCount
    """
    #  int QCommonListViewBase::rowCount() const
    return self.uglySide.call('ritual_ZNK19QCommonListViewBase8rowCountEv')

  def viewport(self) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QCommonListViewBase::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#viewport

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QCommonListViewBase::viewport() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8viewportEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def clipRect(self) -> QRect:
    """
    Calls Qt's 'QRect QCommonListViewBase::clipRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#clipRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCommonListViewBase::clipRect() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8clipRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def cachedItemSize(self) -> QSize:
    """
    Calls Qt's 'QSize QCommonListViewBase::cachedItemSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#cachedItemSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCommonListViewBase::cachedItemSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase14cachedItemSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QListViewItem)
  def viewItemRect(self, item: QListViewItem) -> QRect:
    """
    Calls Qt's 'QRect QCommonListViewBase::viewItemRect(const QListViewItem
    &item) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#viewItemRect

    Parameters
    ----------

    item : QListViewItem
      Passed on as a value: Qt reads the C++ QListViewItem, which stays
      Python's own.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QCommonListViewBase::viewItemRect(const QListViewItem &item)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase12viewItemRectERK13QListViewItem',
        self._valueOf(item),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QStyleOptionViewItem, QModelIndex)
  def itemSize(self, opt: QStyleOptionViewItem, idx: QModelIndex) -> QSize:
    """
    Calls Qt's 'QSize QCommonListViewBase::itemSize(const
    QStyleOptionViewItem &opt, const QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#itemSize

    Parameters
    ----------

    opt : QStyleOptionViewItem
      Passed on as a value: Qt reads the C++ QStyleOptionViewItem, which
      stays Python's own.

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCommonListViewBase::itemSize(const QStyleOptionViewItem &opt,
    #      const QModelIndex &idx) const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8itemSizeERK20QStyleOptionViewItemR'
        'K11QModelIndex',
        self._valueOf(opt), self._valueOf(idx),
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QModelIndex)
  def delegate(self, idx: QModelIndex) -> Optional[QAbstractItemDelegate]:
    """
    Calls Qt's 'QAbstractItemDelegate *QCommonListViewBase::delegate(const
    QModelIndex &idx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#delegate

    Parameters
    ----------

    idx : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QAbstractItemDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractItemDelegate *QCommonListViewBase::delegate(const QModelIndex
    #      &idx) const
    address = self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8delegateERK11QModelIndex',
        self._valueOf(idx),
    )
    from . import QAbstractItemDelegate
    return QAbstractItemDelegate._cuteAt(address)

  @overload(int)
  def isHidden(self, row: int) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::isHidden(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#isHidden

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  bool QCommonListViewBase::isHidden(int row) const
    return self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase8isHiddenEi', row,
    )

  def hiddenCount(self) -> int:
    """
    Calls Qt's 'int QCommonListViewBase::hiddenCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#hiddenCount
    """
    #  int QCommonListViewBase::hiddenCount() const
    return self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase11hiddenCountEv',
    )

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::isRightToLeft() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#isRightToLeft
    """
    #  bool QCommonListViewBase::isRightToLeft() const
    return self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase13isRightToLeftEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setRowCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::setRowCount(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#setRowCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QCommonListViewBase::setRowCount(int a0)
    self.uglySide.call('ritual_ZN19QCommonListViewBase11setRowCountEi', a0)

  @overload(QPoint, QModelIndex)
  def setPositionForIndex(self, a0: QPoint, a1: QModelIndex) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::setPositionForIndex(const QPoint
    &a0, const QModelIndex &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#setPositionForIndex

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QCommonListViewBase::setPositionForIndex(const QPoint &a0, const
    #      QModelIndex &a1)
    ritual = (
        'ritual_ZN19QCommonListViewBase19setPositionForIndexERK6QPointRK11Q'
        'ModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase19setPositionForIndexERK6QPoin'
          'tRK11QModelIndex')
    self.uglySide.call(ritual, self._valueOf(a0), self._valueOf(a1))

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
    Qt's 'QCommonListViewBase::QCommonListViewBase(QListView *q,
    QListViewPrivate *d)': the class is abstract, so C++ cannot make one, and
    the C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QCommonListViewBase.__init__' has no cute function yet. Qt's "
        "'QCommonListViewBase::QCommonListViewBase(QListView *q, "
        "QListViewPrivate *d)': the class is abstract, so C++ cannot make "
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

  @overload(QListViewLayoutInfo, int)
  def doBatchedItemLayout(self, info: QListViewLayoutInfo, max: int) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::doBatchedItemLayout(const
    QListViewLayoutInfo &info, int max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#doBatchedItemLayout

    Parameters
    ----------

    info : QListViewLayoutInfo
      Passed on as a value: Qt reads the C++ QListViewLayoutInfo, which stays
      Python's own.

    max : int
      Passed on as it is.
    """
    #  bool QCommonListViewBase::doBatchedItemLayout(const
    #      QListViewLayoutInfo &info, int max)
    return self.uglySide.call(
        'ritual_ZN19QCommonListViewBase19doBatchedItemLayoutERK19QListViewL'
        'ayoutInfoi',
        self._valueOf(info), max,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcommonlistviewbase.html#clear
    """
    #  void QCommonListViewBase::clear()
    self.uglySide.call('ritual_ZN19QCommonListViewBase5clearEv')

  @overload(QModelIndex, QModelIndex)
  def dataChanged(self, a0: QModelIndex, a1: QModelIndex) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::dataChanged(const QModelIndex &a0,
    const QModelIndex &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#dataChanged

    Parameters
    ----------

    a0 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    a1 : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QCommonListViewBase::dataChanged(const QModelIndex &a0, const
    #      QModelIndex &a1)
    self.uglySide.call(
        'ritual_ZN19QCommonListViewBase11dataChangedERK11QModelIndexS2_',
        self._valueOf(a0), self._valueOf(a1),
    )

  @overload(int, int, bool)
  def scrollContentsBy(
      self,
      dx: int,
      dy: int,
      scrollElasticBand: bool,
  ) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::scrollContentsBy(int dx, int dy,
    bool scrollElasticBand)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#scrollContentsBy

    Parameters
    ----------

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    scrollElasticBand : bool
      Passed on as it is.
    """
    #  void QCommonListViewBase::scrollContentsBy(int dx, int dy, bool
    #      scrollElasticBand)
    ritual = 'ritual_ZN19QCommonListViewBase16scrollContentsByEiib'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QCommonListViewBase16scrollContentsByEiib'
    self.uglySide.call(ritual, dx, dy, scrollElasticBand)

  @overload(QSize)
  def updateHorizontalScrollBar(self, step: QSize) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::updateHorizontalScrollBar(const
    QSize &step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#updateHorizontalScrollBar

    Parameters
    ----------

    step : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QCommonListViewBase::updateHorizontalScrollBar(const QSize &step)
    ritual = (
        'ritual_ZN19QCommonListViewBase25updateHorizontalScrollBarERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase25updateHorizontalScrollBarERK'
          '5QSize')
    self.uglySide.call(ritual, self._valueOf(step))

  @overload(QSize)
  def updateVerticalScrollBar(self, step: QSize) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::updateVerticalScrollBar(const QSize
    &step)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#updateVerticalScrollBar

    Parameters
    ----------

    step : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QCommonListViewBase::updateVerticalScrollBar(const QSize &step)
    ritual = (
        'ritual_ZN19QCommonListViewBase23updateVerticalScrollBarERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase23updateVerticalScrollBarERK5Q'
          'Size')
    self.uglySide.call(ritual, self._valueOf(step))

  @overload(int)
  def appendHiddenRow(self, row: int) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::appendHiddenRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#appendHiddenRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QCommonListViewBase::appendHiddenRow(int row)
    ritual = 'ritual_ZN19QCommonListViewBase15appendHiddenRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QCommonListViewBase15appendHiddenRowEi'
    self.uglySide.call(ritual, row)

  @overload(int)
  def removeHiddenRow(self, row: int) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::removeHiddenRow(int row)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#removeHiddenRow

    Parameters
    ----------

    row : int
      Passed on as it is.
    """
    #  void QCommonListViewBase::removeHiddenRow(int row)
    ritual = 'ritual_ZN19QCommonListViewBase15removeHiddenRowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QCommonListViewBase15removeHiddenRowEi'
    self.uglySide.call(ritual, row)

  @overload(QPainter)
  @overload(NoneType)
  def paintDragDrop(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QCommonListViewBase::paintDragDrop(QPainter *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#paintDragDrop

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonListViewBase::paintDragDrop(QPainter *painter)
    ritual = 'ritual_ZN19QCommonListViewBase13paintDragDropEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QCommonListViewBase13paintDragDropEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def filterDragMoveEvent(self, a0: Optional[QDragMoveEvent]) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::filterDragMoveEvent(QDragMoveEvent
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#filterDragMoveEvent

    Parameters
    ----------

    a0 : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCommonListViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
    ritual = (
        'ritual_ZN19QCommonListViewBase19filterDragMoveEventEP14QDragMoveEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase19filterDragMoveEventEP14QDrag'
          'MoveEvent')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def filterDragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> bool:
    """
    Calls Qt's 'bool
    QCommonListViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#filterDragLeaveEvent

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCommonListViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
    ritual = (
        'ritual_ZN19QCommonListViewBase20filterDragLeaveEventEP15QDragLeave'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase20filterDragLeaveEventEP15QDra'
          'gLeaveEvent')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QDropEvent)
  @overload(NoneType)
  def filterDropEvent(self, a0: Optional[QDropEvent]) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::filterDropEvent(QDropEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#filterDropEvent

    Parameters
    ----------

    a0 : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCommonListViewBase::filterDropEvent(QDropEvent *a0)
    ritual = 'ritual_ZN19QCommonListViewBase15filterDropEventEP10QDropEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase15filterDropEventEP10QDropEven'
          't')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(Qt.DropActions)
  def filterStartDrag(self, a0: Qt.DropActions) -> bool:
    """
    Calls Qt's 'bool QCommonListViewBase::filterStartDrag(Qt::DropActions
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#filterStartDrag

    Parameters
    ----------

    a0 : Qt.DropActions
      Passed on as its number.
    """
    #  bool QCommonListViewBase::filterStartDrag(Qt::DropActions a0)
    ritual = (
        'ritual_ZN19QCommonListViewBase15filterStartDragE6QFlagsIN2Qt10Drop'
        'ActionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QCommonListViewBase15filterStartDragE6QFlagsIN2Qt'
          '10DropActionEE')
    return self.uglySide.call(ritual, a0.value)

  @overload(QStyleOptionViewItem)
  @overload(NoneType)
  def initViewItemOption(
      self,
      option: Optional[QStyleOptionViewItem],
  ) -> None:
    """
    Calls Qt's 'void
    QCommonListViewBase::initViewItemOption(QStyleOptionViewItem *option)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcommonlistviewbase.html#initViewItemOption

    Parameters
    ----------

    option : Optional[QStyleOptionViewItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCommonListViewBase::initViewItemOption(QStyleOptionViewItem
    #      *option) const
    self.uglySide.call(
        'ritual_ZNK19QCommonListViewBase18initViewItemOptionEP20QStyleOptio'
        'nViewItem',
        self._addressOf(option),
    )

  @staticmethod
  def horizontalScrollMode(*__, **_) -> Never:
    """
    Qt's 'QListView::ScrollMode QCommonListViewBase::horizontalScrollMode()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCommonListViewBase.horizontalScrollMode' has no cute function "
        "yet. Qt's 'QListView::ScrollMode "
        "QCommonListViewBase::horizontalScrollMode() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def horizontalScrollToValue(*__, **_) -> Never:
    """
    Qt's 'int QCommonListViewBase::horizontalScrollToValue(int index,
    QListView::ScrollHint hint, bool leftOf, bool rightOf, const QRect &area,
    const QRect &rect) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QCommonListViewBase.horizontalScrollToValue' has no cute function "
        "yet. Qt's 'int QCommonListViewBase::horizontalScrollToValue(int "
        "index, QListView::ScrollHint hint, bool leftOf, bool rightOf, "
        "const QRect &area, const QRect &rect) const': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def verticalScrollMode(*__, **_) -> Never:
    """
    Qt's 'QListView::ScrollMode QCommonListViewBase::verticalScrollMode()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCommonListViewBase.verticalScrollMode' has no cute function yet. "
        "Qt's 'QListView::ScrollMode "
        "QCommonListViewBase::verticalScrollMode() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def verticalScrollToValue(*__, **_) -> Never:
    """
    Qt's 'int QCommonListViewBase::verticalScrollToValue(int index,
    QListView::ScrollHint hint, bool above, bool below, const QRect &area,
    const QRect &rect) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QCommonListViewBase.verticalScrollToValue' has no cute function "
        "yet. Qt's 'int QCommonListViewBase::verticalScrollToValue(int "
        "index, QListView::ScrollHint hint, bool above, bool below, const "
        "QRect &area, const QRect &rect) const': takes a type Python has no "
        "way to hand over yet.")
